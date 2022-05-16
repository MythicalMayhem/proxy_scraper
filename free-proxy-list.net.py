import requests
#pip install requests 

proxies = []

r = requests.get('https://free-proxy-list.net/').text
r = r.split('<tbody>')[1].split('</tbody>')[0].split('<tr>')
r.remove(r[0])

for i in range(len(r)):
    ip = r[i].split('<td>')[1].split('</td>')[0]
    port = r[i].split('<td>')[2].split('</td>')[0]
    proxies.append(ip + ':' + port )
print(proxies)

