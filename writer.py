"""
Module contains functions to
create a files to stock datas of
CPU , RAM, disk , IO network

ALL RIGHTS RESERVED
copyright 2021
BRAHIM RABEB
"""


##################################
# functions to write to file datas
##################################

def write_to_file_io_net(text):
    """ write string into a file
    text(str) : the text to insert into the file
    returns non
    """
    with open("data_io_net.txt", "a+") as file:
        file.write(text + "\n")


def write_to_file_cpu(text):
    """ write string into a file
    text(str) : the text to insert into the file
    returns non
    """
    with open("data_cpu.txt", "a+") as file:
        file.write(text + "\n")


def write_to_file_vm(text):
    """ write string into a file
    text(str) : the text to insert into the file
    returns non
    """
    with open("data_vm.txt", "a+") as file:
        file.write(text + "\n")

######################
# write disk data
######################
def write_to_file_disk(text):
    """ write string into a file
    text(str) : the text to insert into the file
    returns non
    """
    with open("data_disk.txt", "a+") as file:
        file.write(text + "\n")

