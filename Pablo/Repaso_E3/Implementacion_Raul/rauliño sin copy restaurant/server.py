import grpc
import restaurant_pb2
import restaurant_pb2_grpc
from concurrent import futures

class Restaurant(restaurant_pb2_grpc.Restaurant):
    reserves = {}
    def request(self, reserve_request, context):
        if int(reserve_request.reserva.date.replace('/', '')) in self.reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='Ya existe una reserva en la fecha indicada'
            )
        else:
            reserve_request.reserva.res_id.id = int(reserve_request.reserva.date.replace('/', ''))
            self.reserves.update({reserve_request.reserva.res_id.id:reserve_request.reserva})
            return restaurant_pb2.ServerResponse(
                res_id=restaurant_pb2.ReservationID(id=reserve_request.reserva.res_id.id)
            )
            

    def check(self, reservation_id, context):
        if reservation_id.id not in self.reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='ID No encontrado, posiblemente no exista reserva en esa fecha'
            )
        else:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ACK,
                my_reserva=self.reserves.get(reservation_id.id)
            )
        

    def cancel(self, reservation_id, context):
        if reservation_id.id not in self.reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='ID No encontrado, posiblemente no exista reserva en esa fecha'
            )
        else:
            self.reserves.pop(reservation_id.id)
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ACK,
            )
            
    def list(self, list_request, context):
        return restaurant_pb2.ServerResponse(
            reserve_list=list(self.reserves.values())
        )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
server.add_insecure_port('0.0.0.0:8008')
server.start()

try:
    server.wait_for_termination()

except KeyboardInterrupt:
    server.stop(0)
