import argparse
import grpc
import restaurant_pb2_grpc
import restaurant_pb2

DEF_PORT = 8008

class Cliente:
    def __init__(self, stub):
        self.stub = stub
    
    def RequestReservation(self, reservation_file):
        reserve_req_list = []
        with open(reservation_file, "r", encoding="utf8") as file:
            for i in file:
                reserve_req_list.append(i.replace("\n", ""))
        reserve_message = restaurant_pb2.ReservationRequest(reserva = restaurant_pb2.Reservation(date = reserve_req_list[0], time=reserve_req_list[1], diners=int(reserve_req_list[2]), client_name=reserve_req_list[3], contact_phone_number=reserve_req_list[4]))
        response = self.stub.request(reserve_message)
        match (response.response):
            case 0:
                id_res = restaurant_pb2.ReservationID()
                id_res.CopyFrom(response.res_id)
                print(f'El id de la reserva efectuada es {id_res.reserve_id}')
            case 1:
                print(response.description)
    
    def CheckReservation(self, resid):
        check_message = restaurant_pb2.ReservationID(reserve_id=int(resid))
        retval = self.stub.check(check_message)
        match (retval.response):
            case 0:
                id_res = restaurant_pb2.ReservationID()
                id_res.CopyFrom(retval.my_reserva.res_id)
                print(
                    f'Detalles de la reserva:\n\tID de reserva: {id_res.reserve_id}\n\tFecha: {retval.my_reserva.date}\n\tHora: {retval.my_reserva.time}\n\tComensales: {retval.my_reserva.diners}\n\tEstá a nombre de {retval.my_reserva.client_name}\n\tTeléfono: {retval.my_reserva.contact_phone_number}')
            case 1:
                print(retval.description)
    
    def CancelReservation(self, resid):
        cancel_message = restaurant_pb2.ReservationID(reserve_id=int(resid))
        servres = self.stub.cancel(cancel_message)
        match (servres.response):
            case 0:
                print('Se eliminó la reserva correctamente')
            case 1:
                print(servres.description)

    def ListAllReservations(self):
        print(self.stub.list(restaurant_pb2.ListReq()))


# Parseador de argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", type=str, default='localhost', dest="ip", help="IP a usar")
parser.add_argument("-p", "--port", type=int, default=DEF_PORT, dest="port", help="Puerto a usar")

# COMANDO DEL CLIENTE. ES OBLIGATORIO. UNA OPCION DE LAS 4
command_subparsers = parser.add_subparsers(dest='command', help='Commands', required=True, metavar='COMMAND')
    # RESERVAR:
request_parser = command_subparsers.add_parser('request', help='Reserva')
request_parser.add_argument('-fr', '--file-reserve', type=str, dest='file', required=True)
    # CHECK:
check_parser = command_subparsers.add_parser('check', help='Chequea')
check_parser.add_argument('-id', '--reserve-id', type=int, dest='resid', required=True)
    # CANCELAR:
cancel_parser = command_subparsers.add_parser('cancel', help='Cancela reserva')
cancel_parser.add_argument('-id', '--reserve-id', type=int, dest='resid', required=True)
    # LISTAR:
list_parser = command_subparsers.add_parser('listall', help='Lista')

if __name__ == '__main__':
    args = parser.parse_args()
    cliente = Cliente(restaurant_pb2_grpc.RestaurantStub(  grpc.insecure_channel(f'{args.ip}:{args.port}')  ))
    match(args.command):
        case 'request':
            cliente.ReqReservation(args.file)
        case 'check':
            cliente.CheckReservation(args.resid)
        case 'cancel':
            cliente.CancelReservation(args.resid)
        case 'listall':
            cliente.ListAllReservations()