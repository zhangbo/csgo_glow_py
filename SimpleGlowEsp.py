import pymem

import pymem.process



dwEntityList = (0x4CE44EC)

dwLocalPlayer = (0xCD3764)

dwGlowObjectManager = (0x5224748)

m_iGlowIndex = (0xA3F8)

m_iTeamNum = (0xF4)



pm = pymem.Pymem("csgo.exe")

client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll



def main():

    print("Glow is launched.")

    while True:

        glow_manager = pm.read_int(client + dwGlowObjectManager)


        for i in range(1, 32):  # Entities 1-32 are reserved for players. 

            entity = pm.read_uint(client + (dwEntityList + i * 0x10))

            
            if entity:

                entity_team_id = pm.read_uint(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                
                if entity_team_id == 2:  # Terrorist

                    pm.write_float(glow_manager + ((entity_glow * 0x38) + 0x4), float(1))   # R 

                    pm.write_float(glow_manager + ((entity_glow * 0x38) + 0x8), float(0))   # G

                    pm.write_float(glow_manager + ((entity_glow * 0x38) + 0xC), float(0))   # B

                    pm.write_float(glow_manager + ((entity_glow * 0x38) + 0x10), float(1))  # Alpha


                
                elif entity_team_id == 3:  # Counter-terrorist

                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   # R

                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # G

                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B

                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                
                pm.write_int(glow_manager + ((entity_glow * 0x38) + 0x24), 1)           # Enable glow
                pm.write_int(glow_manager + ((entity_glow * 0x38) + 0x25), 0)          




if __name__ == '__main__':

    main()
