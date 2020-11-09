import nmap 
   
# range check interface
begin = 22
end = 80
  
# adress ip
target = '192.168.1.1'
   

scanner = nmap.PortScanner() 
   
for i in range(begin,end+1):  
    res = scanner.scan(target,str(i)) 
    res = res['scan'][target]['tcp'][i]['state'] 
    print(f'port {i} is {res}.') 