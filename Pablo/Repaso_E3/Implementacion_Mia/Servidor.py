import grpc
import restaurant_pb2
import restaurant_pb2_grpc
from concurrent import futures

class Restaurant(restaurant_pb2_grpc.Restaurant):
    d_reserves = {}
    def request(self, reserve_request, context):
        my_resv = restaurant_pb2.Reservation()
        my_resv.CopyFrom(reserve_request.reserva)
        my_identifier = restaurant_pb2.ReservationID()
        my_identifier.CopyFrom(my_resv.res_id)
        if int(my_resv.date.replace('/', '')) in self.d_reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='Ya existe una reserva en la fecha indicada'
            )
        else:
            my_identifier.reserve_id = int(my_resv.date.replace('/', ''))
            my_resv.res_id.CopyFrom(my_identifier)
            self.d_reserves.update({my_identifier.reserve_id:my_resv})
            # print(self.d_reserves.items())
            return restaurant_pb2.ServerResponse(
                res_id=restaurant_pb2.ReservationID(reserve_id=my_identifier.reserve_id)
            )

    def check(self, reservation_id, context):
        my_identifier = restaurant_pb2.ReservationID()
        my_identifier.CopyFrom(reservation_id)
        
        if my_identifier.reserve_id not in self.d_reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='ID No encontrado, posiblemente no exista reserva en esa fecha'
            )
        else:
            obtain_resv = restaurant_pb2.Reservation()
            obtain_resv.CopyFrom(self.d_reserves.get(my_identifier.reserve_id))
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ACK,
                my_reserva=obtain_resv
            )

    def cancel(self, reservation_id, context):
        my_identifier = restaurant_pb2.ReservationID()
        my_identifier.CopyFrom(reservation_id)
        
        if my_identifier.reserve_id not in self.d_reserves:
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ERR,
                description='ID No encontrado, posiblemente no exista reserva en esa fecha'
            )
        else:
            self.d_reserves.pop(my_identifier.reserve_id)
            return restaurant_pb2.ServerResponse(
                response=restaurant_pb2.ServerResponse.Response.ACK
            )
            
    def list(self, list_request, context):
        lr = restaurant_pb2.ListReq()
        lr.CopyFrom(list_request)
        return restaurant_pb2.ServerResponse(
            reserve_list=list(self.d_reserves.values())
        )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
server.add_insecure_port('0.0.0.0:8008')
server.start()

try:
    server.wait_for_termination()

except KeyboardInterrupt:
    server.stop(0)
