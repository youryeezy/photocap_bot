import grpc

from bot import external_bot
from grpc_python import photocap_pb2_grpc, photocap_pb2



class GRPCServer(photocap_pb2_grpc.MsTelegramBotServicer):
    async def SendMessage(self, request: photocap_pb2.Message, context: grpc.ServicerContext) -> photocap_pb2.IsSuccessfully:

        try:
            await external_bot.send_message(
                phone=phone,
                url=url,
                abonent=abonent,
                lac=lac,
                cell=cell,
                azimut=azimut)
            return IsSuccessfully(is_successfully=True)
        except Exception:
            return IsSuccessfully(is_successfully=False)


async def telegram_bot_server() -> None:
    server = grpc.aio.server()
    add_MsTelegramBorServicer_to_server(GRPCServer(), server)
    server.add_insecure_port(f'[::]:{settings.grpc_server_port}')
    await server.start()
    await server.wait_for_termination()