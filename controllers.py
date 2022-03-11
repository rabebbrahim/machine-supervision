"""
Module contains  functions calling
psutil to get informations from
CPU, RAM , IO network and Disk

"""

import psutil


######################################
# functions to get infos from io network
######################################

def get_net_io_counters():
    """Get the net I/O counters
    to send it to db
    """
    return psutil.net_io_counters()


#################################################################
# this function we need it to send infos to the file text clearly
# in form of string separated with pipes between values
#################################################################
def get_net_io_values():
    """
    to send information to the file
    """
    stats = psutil.net_io_counters()
    my_stats = [
        " bytes_sent = " + str(stats.bytes_sent),
        "| bytes_recv = " + str(stats.bytes_recv),
        "| packet_sent = " + str(stats.packets_sent),
        "| packet_recv = " + str(stats.packets_recv),
        "| errin = " + str(stats.errin),
        "| errout =" + str(stats.errout),
        "| dropin =" + str(stats.dropin),
        "| dropout =" + str(stats.dropout),
    ]
    return "".join(my_stats)


###############################
# function to get cpu informations
#################################

def get_cpu_analyser():
    """cpu percent

    """
    return psutil.cpu_percent(
        interval=None,
        percpu=False
    )


def get_virtual_memory():
    """ RAM connect
    returns vm stats
    (total, available, percent, used, free, active)
    """
    stats = psutil.virtual_memory()
    my_stats = [
        "total:" + str(stats.total),
        "| available:" + str(stats.available),
        "| percent:" + str(stats.percent),
        "| used:" + str(stats.used),
        "| free:" + str(stats.free),
        "| active:" + str(stats.active),
    ]
    return "".join(my_stats)


##########################
# function to get vm values
###########################
def get_vm_values():
    """
   get virtual memory statistics
   return (total, available , used, free, percent and active )
    """
    return psutil.virtual_memory()

######################################
# disk usage to stock in the file txt
#######################################
def get_disk_usage():
    """
    disk usage
    returns : sdisk usage( total , used, free,percent)
    """
    disk = psutil.disk_usage('/')
    my_disk = [
        "total:" + str(disk.total),
        "| used:" + str(disk.used),
        "| free:" + str(disk.free),
        "| percent:" + str(disk.percent),
    ]
    return "".join(my_disk)

#######################################
# get disk data
########################################

def get_disk_values():
    """
    convert disk stats to values to send to the badatase
    """
    return psutil.disk_usage('/')
