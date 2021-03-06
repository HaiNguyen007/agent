# -*- coding: utf-8 -*-

'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
import utils
import os

PRJNAME="lib_gdi"

CONF = {}
CONF["pathsrc"]=".." + os.sep + PRJNAME + os.sep + "src"
CONF["pathdst"]=utils.PATHTMP + os.sep + PRJNAME

CONF_WINDOWS={}
CONF_WINDOWS["outname"]="dwaggdi.dll" 
CONF_WINDOWS["cpp_include_paths"]=[] 
CONF_WINDOWS["cpp_library_paths"]=CONF_WINDOWS["cpp_include_paths"]
CONF_WINDOWS["libraries"]=["gdi32", "shell32", "user32", "userenv"]
CONF["windows"]=CONF_WINDOWS

CONF_LINUX={}
CONF_LINUX["outname"]="dwaggdi.so" 
CONF_LINUX["cpp_include_paths"]=[] 
CONF_LINUX["cpp_library_paths"]=CONF_LINUX["cpp_include_paths"]
CONF_LINUX["libraries"]=["X11", "Xpm"]
CONF["linux"]=CONF_LINUX

'''
CONF_MAC={}
CONF_MAC["outname"]="dwaggdi.so" 
CONF_MAC["cpp_include_paths"]=[] 
CONF_MAC["cpp_library_paths"]=CONF_MAC["cpp_include_paths"]
CONF_MAC["libraries"]=[] 
CONF["mac"]=CONF_MAC
'''

class Compile():
    
    def get_name(self):
        return PRJNAME;
    
    def run(self):
        utils.info("BEGIN " + self.get_name())       
        utils.make_tmppath() 
        utils.remove_from_native(CONF)        
        confos=utils.compile_lib(CONF)
        if confos is not None:        
            utils.copy_to_native(CONF)
        utils.info("END " + self.get_name())
        
if __name__ == "__main__":
    m = Compile()
    m.run()
    
    
    
    
    
    
    