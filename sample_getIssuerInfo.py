#! /usr/bin/env python
"""
Sample script that tries to execute a SELECT FILE command in a FTCOS PKI.

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
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString, toBytes
from getIssuerInfo import *

# apdu testing
Correcto_APDU_issuer_info = [0x80, 0xFC, 0x12, 0x00, 0x10]
error1_APDU_issuer_info = [0x80, 0xFC, 0x12, 0x00, 0x50]
error2_APDU_issuer_info = [0x35, 0xFC, 0x12, 0x00, 0x10]
error3_APDU_issuer_info = [0x80, 0xFC, 0x22, 0x33, 0x10]
error4_APDU_issuer_info = [0x80, 0x99, 0x12, 0x00, 0x10]
error5_APDU_issuer_info = [0x80, 0xFC, 0x12, 0x00, 0x10]

# request any card type
cardtype = AnyCardType()


try:
    # request card insertion
    print 'insert a card (SIM card if possible) within 10s'
    cardrequest = CardRequest(timeout=10, cardType=cardtype)
    cardservice = cardrequest.waitforcard()

    # attach the console tracer
    observer = ConsoleCardConnectionObserver()
    cardservice.connection.addObserver(observer)

    # connect to the card and perform a few transmits
    cardservice.connection.connect()

    # Select file test
    response, sw1, sw2 = test_apdu(Correcto_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    response, sw1, sw2 = test_apdu(error1_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    response, sw1, sw2 = test_apdu(error2_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    response, sw1, sw2 = test_apdu(error3_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    response, sw1, sw2 = test_apdu(error4_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    response, sw1, sw2 = test_apdu(error5_APDU_issuer_info, cardservice)
    entersafe_manage_select_file(response, sw1, sw2)
    

except CardRequestTimeoutException:
    print 'time-out: no card inserted during last 10s'

except:
    import sys
    print sys.exc_info()[1]

import sys
if 'win32' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)
