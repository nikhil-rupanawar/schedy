import os
import sys
import logging
import grpc
from concurrent import futures
from functools import partial
from messaging.rpc.rpcserver import ClockNodeRpcServer, InMemoryApSchedulerTickerMixin
from messaging.rpc.providers.grpc.interfaces.messages_pb2 import (
    ReplaceSchedulesResponse,
    AddScheduleResponse,
    RemoveScheduleResponse,
    HealthPingResponse,
    RegisterClockNodeRequest,
)
from messaging.rpc.providers.grpc.interfaces.clocknode_service_pb2_grpc import (
        ClockNodeServiceServicer,
        add_ClockNodeServiceServicer_to_server
)

from messaging.rpc.providers.grpc.interfaces.registry_service_pb2_grpc import RegistryServiceStub

logger = logging.getLogger(__name__)


class ClockNodeServer(ClockNodeServiceServicer,
        ClockNodeRpcServer,
        InMemoryApSchedulerTickerMixin
    ):

    @property
    def server_config(self):
        return {
            'schedule_director_registery_service_uri': os.environ.get(
                'SCHEDULE_DIRECTOR_REGISTERY_URI',
                'grpc://localhost:50000'
            ),
            'director_access_uri':  os.environ.get(
                'DIRECTOR_ACCESS_URI',
                'grpc://localhost:10000' # tell external world where to communicate
            ),
            'port': os.environ.get('PORT', 10000),
            'network_interface': os.environ.get('NETWORK_INTERFACE', '[::]')
        }


    def start(self):
        self.init_ticker()
        self.start_ticker()
        self.register_to_director()
        self._start_and_block()

    def register_to_director(self):
        channel = grpc.insecure_channel('localhost:50001')
        stub = RegistryServiceStub(channel)
        request = RegisterClockNodeRequest()
        stub.register_clock_node(request)

    def _start_and_block(self):
        config = self.server_config
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_ClockNodeServiceServicer_to_server(self, server)
        server.add_insecure_port(f'{config["network_interface"]}:{int(config["port"])}')
        server.start()
        server.wait_for_termination()

    def stop(self):
        self.stop_ticker()

    def replace_schedules(self, request, context):
        self.ticker.remove_all_jobs()
        for job_definition in request.sch:
            self._add_job(job_definition)
        return ReplaceSchedulesResponse()

    def add_schedule(self, request, context):
        logger.info('Adding job {}'.format(request.job_definition.id))
        self._schedule_job(request.job_definition)
        return AddScheduleResponse()

    def remove_schedule(self, request, context):
        self.ticker.remove_job(request.id)

    def _add_job(self, schedule_details):
        print("Triggered {schedule_details}")

    def health_ping(self, request, context):
        return HealthPingResponse()


if __name__ == '__main__':
    service = ClockNodeService()
    service.start()
