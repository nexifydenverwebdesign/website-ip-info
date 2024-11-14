import socket
import requests

def get_ip_info(website):
    try:
        # Get the IP address of the website
        ip_address = socket.gethostbyname(website)
        print(f"IP Address of {website}: {ip_address}")
        
        # Use a free API to get geolocation info about the IP
        api_url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'fail':
                print("Could not fetch geolocation information.")
            else:
                print(f"Location: {data['city']}, {data['regionName']}, {data['country']}")
                print(f"Latitude: {data['lat']}, Longitude: {data['lon']}")
                print(f"ISP: {data['isp']}")
                print(f"Organisation: {data['org']}")
                print(f"AS (Autonomous System): {data['as']}")
        else:
            print("Error fetching location data.")

    except socket.gaierror:
        print(f"Could not resolve the domain name for {website}. Please check the URL.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    website = input("Enter a website URL (e.g., www.google.com): ")
    get_ip_info(website)
