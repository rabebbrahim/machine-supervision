"""Module Project Supervision of a machine
IO-network / CPU / Virtual Memory/ Disk
ALL RIGHTS RESERVED
"""
import time
import datetime
import psutil
import mysql.connector
import controllers
import writer
import database


def main():
    """
    The main function
    Writing informations received by CPU , VM, Disk an IO-network and put it in file txt
    and sending the Jauge of their infos to the database to get statistics of
    eich evolution with the time

    """
    while True:
        try:
            time.sleep(10)

            #############################
            # get cpu percent &
            # Write to file: "data_cpu.txt"
            ##############################

            cpu_percent = controllers.get_cpu_analyser()
            file_line = f"{datetime.datetime.now()}| CPU percent: {cpu_percent} %"
            writer.write_to_file_cpu(file_line)
            print("cpu data sent to file ...")

            ###############################
            # get disk usage &
            # write to file: "data_disk.txt"
            ################################

            disk_datas = controllers.get_disk_usage()
            file_line = f"{datetime.datetime.now()}|  my_disk : {disk_datas}"
            writer.write_to_file_disk(file_line)
            print("disk data sent to file ...")

            ############################
            # get virtual_memory &
            # write to file: "data_vm.txt
            #############################

            virtual_memory = controllers.get_virtual_memory()
            file_line = f"{datetime.datetime.now()} | memory_stats : {virtual_memory}"
            writer.write_to_file_vm(file_line)
            print("virtual memory data sent to file ...")

            ###############################
            # get network IO &
            # write to file : "data_io.txt"
            ###############################

            net_io = controllers.get_net_io_counters()
            file_line = f"{datetime.datetime.now()} | io_net_stats : {net_io}"
            writer.write_to_file_io_net(file_line)
            print("io_net data sent to file ...")
            print("******")
            print("************")
            print("*********************")

            ###############################
            # write cpu_percent to database
            ###############################

            sql_statement = f"INSERT INTO cpu_percent " \
                            f"(counter) " \
                            f"VALUES " \
                            f"({cpu_percent})"
            database.write_to_db(sql_statement)


            ##########################################
            # write the sent and received byte to database
            #############################################
            io_bytes_sent = controllers.get_net_io_counters().bytes_sent
            io_bytes_recv = controllers.get_net_io_counters().bytes_recv

            sql_io_net = f"INSERT INTO io_net" \
                         f"(bytes_sent, bytes_recv) " \
                         f"VALUES " \
                         f"({io_bytes_sent},{io_bytes_recv})"
            database.write_to_db(sql_io_net)

            #####################################################
            # send the virtual memory informations to the database
            ######################################################

            sql_virtual_memory = f"INSERT INTO virtual_memory " \
                                 f"(total, available, percent, used, free, active) " \
                                 f"VALUES " \
                                 f"({controllers.get_vm_values().total},{controllers.get_vm_values().available},{controllers.get_vm_values().percent},{controllers.get_vm_values().used},{controllers.get_vm_values().free},{controllers.get_vm_values().active})"

            database.write_to_db(sql_virtual_memory)

            ###########################################
            # send the disk information to the database
            ############################################

            sql_disk = f"INSERT INTO disk_usage " \
                       f"(total, used, free, percent) " \
                       f"VALUES " \
                       f"({controllers.get_disk_values().total},{controllers.get_disk_values().used}, {controllers.get_disk_values().free},{controllers.get_disk_values().percent})"
            database.write_to_db(sql_disk)


        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
