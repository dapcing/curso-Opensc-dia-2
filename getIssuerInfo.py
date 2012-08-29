#! /usr/bin/env python
"""
Sample script that tries to execute a SELECT FILE command in a FTCOS PKI Card.

__author__ = "http:www.emergya.es"

Copyright 2012 Emergya
Author: Alejandro Diaz Torres, mailto:adiaz@emergya.com

This file is part of pyscard-entersafe-exaples.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from smartcard.util import toHexString
from entersafeBase import *


def entersafe_manage_select_file(response, sw1, sw2):

    # there is a OK
    if sw1 == SW1_EXPECTED:
	print 'Selected file is', toHexString(response)
	print 'Archivo Correcto...'
    else:
        if sw1 == 0x6C:
           if sw2 == 0x10:
             print 'Error de longitud LE (se esperaba 10) (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
           if sw2 != 0x10:
	     print 'Error desconocido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
        if sw1 == 0x69:
           if sw2 == 0x85:
             print 'Condicion insuficiente para uso del comando (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
           else:
             print 'Error desconocido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
        if sw1 == 0x6A:
           if sw2 == 0x81:
             print 'Funcion no soportada (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
           if sw2 == 0x82:
             print 'Archivo no encontrado (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
           if sw2 == 0x86:
             print 'P1 y/o P2 invalidos (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
           if sw2 != 0x82 and sw2 != 0x81 and sw2 != 0x86:
             print 'Error desconocido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'    
        if sw1 == 0x6E:
           if sw2 == 0x00:
             print 'CLA invalido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'  
           if sw2 != 0x00:
             print 'Error desconocido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')' 
	if sw1 != 0x6C and sw1 != 0x69 and sw1 != 0x6A and sw1 !=0x6E:
           print 'Error desconocido (sw1,sw2)=(', hex(sw1), ',', hex(sw2), ')'
    # TODO:
    # 62 83 Invalid selected file
    # 69 85 Insufficient condition for using the command
    # 6A 81 Not supported function
    # 6A 82 File not found
    # 6A 86 Invalid P1/P2
    # 6E 00 Invalid CLA
