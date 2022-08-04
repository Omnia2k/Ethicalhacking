import shodan
SHODAN_API_KEY = "6xiabWVLsnib9ky4f0AMxc039O08DMHK" 
#Api object
api = shodan.Shodan(SHODAN_API_KEY)
try:
    #searching with target "google" on shodan using api
    res = api.search('google')
    print(f"Results found: {res['total']}")
    #get the total number of the results
    for item in res['matches']:
        # loop over the matching items to get the ip, hostname, post,and the location.
        print(f"IP: {item['ip_str']}")
        print(f"Host: {item['hostnames']}")
        print(f"Open ports: {item['port']}")
        print(f"Country: {item['location']['country_name']}")
        print(f"City: {item['location']['city']}")
except:
    print('An error occured')