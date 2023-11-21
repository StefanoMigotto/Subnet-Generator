import json

#get the primary data


array_of_networks = []
arrayTable = []

ip_address = [int(input("IP-D1: ")),int(input("IP-D2: ")),int(input("IP-D3: ")),int(input("IP-D4: "))]
ip_subnet = int(input("IP.Subnet: "))
total_of_networks = int(input("Total of Network: "))

print("TIP: Per il correto funzionamento inserisci in ordine decrescente le reti con più HOST.")
for i in range(total_of_networks):
    array_of_networks.append([int(input("N.Network: ")),int(input("N.Host: "))])

#read json file

# for print the corrent subnetting is data['subnet_'+str(i)]['subnet']

lnh = open('list_of_number_host.json');
data = json.load(lnh)
for j in range(len(array_of_networks)):
    for i in range(31):
        #Controlla il numero di host e assegna ad una subnet
        if array_of_networks[j][1] > data['subnet_'+str(i+1)]['host']:
            if array_of_networks[j][0] == 1: #SUBNET                        MASK                        HOST                       IP ADDRESS      IP ADDRESS D1          BROADCAST
                arrayTable.append([data['subnet_'+str(i)]['subnet'],data['subnet_'+str(i)]['mask'],data['subnet_'+str(i)]['host'], ip_address,str(ip_address[0]), str(data['subnet_'+str(i)]['broadcast']),data['subnet_'+str(i)]['subnet']])
            else:
                BR_MOD = data['subnet_'+str(i)]['broadcast']['B3']+1
                BROADCAST_MODIFICATO = str(ip_address[0]) + "." + str(data['subnet_'+str(i)]['broadcast']['B2'])+ "." + str(BR_MOD) + ".0"


                arrayTable.append([data['subnet_'+str(i)]['subnet'],data['subnet_'+str(i)]['mask'],data['subnet_'+str(i)]['host'],BROADCAST_MODIFICATO, str(ip_address[0]),str(data['subnet_'+str(i)]['broadcast']), data['subnet_'+str(i)]['subnet']])
        
            break

for i in range(len(array_of_networks)):
    print("Network: " + str(array_of_networks[i][0]) + " Host Richiesti: " + str(array_of_networks[i][1]) + " Host Ricevuti: " + str(arrayTable[i][2]) + " IP Rete: " + str(arrayTable[i][3]) + "/" + str(arrayTable[i][6]) + " SubnetMask: " + str(arrayTable[i][1]) + " Broadcast: " + str(arrayTable[i][4] + arrayTable[i][5]))

input()