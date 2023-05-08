
# lib
import platform
import os

# get info
system_info = platform.uname()
os_name = platform.system()

# for windows
if os_name == "Windows":

      string = '\033[34m' + f"""\n

                                    ..,
                        ....,,:;+ccllll
            ...,,+:;  cllllllllllllllllll
      ,cclllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll             os_name: {os_name}
      llllllllllllll  lllllllllllllllllll             node_name: {system_info.node}
                                                      processor: {system_info.processor}
      llllllllllllll  lllllllllllllllllll             release: {system_info.release}
      llllllllllllll  lllllllllllllllllll             version: {system_info.version}
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      `'ccllllllllll  lllllllllllllllllll
            `' \\*::  :ccllllllllllllllll
                        ````''*::cll
                                    ``

      """ + '\033[34m'

      print(string)