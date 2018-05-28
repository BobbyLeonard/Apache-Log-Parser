import os

def ReadFromFile(location):
        path = open(location, 'r')
        file = path.read()
        path.close()
        return file

def WriteToFile(item, location):
        writepath = open(location, 'w')
        for value in item:
            writepath.write(str(value) + "\n")
        writepath.close()

def IPsforWhois():

		# Function to take the Ip Addresses parsed from Apache logs
		# Perform a whois on each Ip and output to file
		
        deleteOld = "sudo rm /home/bobby/WhoisList"
        os.system(deleteOld)
        path = open("/home/bobby/ApacheLogParserOutput", 'r')
        file = path.read()
        for IP in file.split("\n"):
            cmd = "whois %s >> /home/bobby/WhoisList" % (IP)
            os.system(cmd)
        path.close()
        os.system("clear")

def CIDRtoBan():

		# Function which takes the data from the whois file
		# Searches for and returns lines relating to CIDR 
		
        deleteOld = "sudo rm /home/bobby/CIDRtoBan"
        os.system(deleteOld)
        firstcat = "cat /home/bobby/WhoisList | grep route: > /home/bobby/CIDRtoBan"
        secondcat = "cat /home/bobby/WhoisList | grep CIDR: >> /home/bobby/CIDRtoBan"
        os.system(firstcat)
        os.system(secondcat)
        path = open("/home/bobby/CIDRtoBan", 'r')
        file = path.read()
        todayList = []
        for item in file.split():
            if item[0].isdigit():
                todayList.append(item)
        return todayList

IpSet = set() # Declare a set, to remove multiples from log files
file = ReadFromFile("/var/log/apache2/other_vhosts_access.log")
for sentence in file.split("\n"):
                words = list(sentence.split())
                if(len(words) > 5):
                        IpSet.add(words[1])
file = ReadFromFile("/var/log/apache2/other_vhosts_access.log.1")
for sentence in file.split("\n"):
                words = list(sentence.split())
                if(len(words) > 5):
                        IpSet.add(words[1])

WriteToFile(IpSet, "/home/bobby/ApacheLogParserOutput")
print("\nFiles Read, Parsing ...\n")
IPsforWhois()
todayList = CIDRtoBan()
yesterdayString = (ReadFromFile("/home/bobby/CIDRtoBanYesterday"))
yesterdayList = []
for sentence in yesterdayString.split("\n"):
                yesterdayList.append(sentence)
				
finalList = []
for IP in todayList:
                if not IP in yesterdayList:
                        finalList.append(IP)
						# If the IP isnt in the list from yesterday
						# add to the final list


WriteToFile(finalList, "/home/bobby/CIDRtoBanYesterday")
# Finished, save todays list for use tomorrow

for item in finalList:
                print(item)
