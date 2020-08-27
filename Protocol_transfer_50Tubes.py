# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:06:25 2020

@author: jingwui
"""

from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Transfer competent cells from Falcon Tube to 48 Eppendorf tubes',
    'author': 'yeohjingwui@gmail.com',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.0'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):
    
    Falcon = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical',3)
    #plate1 = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', 5)
    plate2 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 1)
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_300])
    
#    p300.pick_up_tip()
#    
#    for c in range(6):
#        for r in range(4):     
#            p300.transfer(100, Falcon['B2'], plate1.columns()[c][r], 
#                          new_tip = 'never')
#            p300.blow_out()
#            
#            p300.transfer(100, Falcon['B2'], plate2.columns()[c][r],
#                          new_tip = 'never')
#            p300.blow_out()
#            
#    p300.drop_tip()
    
    
    ### Possibly the simpler approach but distribute may have some volume 
    # left inside or not enough 
    p300.pick_up_tip()

    
#    p300.distribute(90, Falcon['B1'], plate1.wells(), new_tip='never') #, disposal_volume = 0)
    
#        p300.distribute(100, Falcon['B2'], plate1.wells(), new_tip='never', 
#                disposal_volume = 0)
#    
#        p300.blow_out()

    p300.distribute(90, Falcon['B1'], plate2.wells(), new_tip='never') #,disposal_volume = 0)
    
        
    p300.drop_tip()
            
    