import ssdd
#import cristian_ice
import sys
import datetime
import Ice
Ice.loadSlice('cristian.ice')

class Cliente(Ice.Application):
    def run(self, argv):
        #proxy = self.communicator().stringToProxy(argv[1])
        #print(proxy)
        timeprinter = ssdd.CristianPrx.checkedCast(self.communicator().stringToProxy("Cristian -t -e 1.1:tcp -h 192.168.8.224 -p 4080 -t 60000"))

        if not timeprinter:
            raise RuntimeError("Invalid proxy")
        
        time_client_1 = 1000*datetime.datetime.now().timestamp()
        print("Tiempo del cliente 1: ",time_client_1)
        time_server = float(timeprinter.getServerTime("02338460G", float(time_client_1)))
        print("Tiempo del servidor: ",time_server)

        time_client_2 = 1000*datetime.datetime.now().timestamp()
        print("Tiempo del cliente 2: ", time_client_2)

        delta_timeClient = time_client_2 - time_client_1

        cristian = time_server + 0.5*(delta_timeClient)

        reporter = ssdd.SyncReportPrx.checkedCast(self.communicator().stringToProxy("SyncReport -t -e 1.1:tcp -h 192.168.8.224 -p 4080 -t 60000"))
        reporter.notifyTime("02338460G", "Pablo Blázquez Sánchez", time_client_2, cristian, delta_timeClient/2)


sys.exit(Cliente().main(sys.argv))