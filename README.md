# website-ip-info
This Python script allows users to retrieve the IP address of a given website and gather additional information about the server.

# Website IP Info

### Overview
`website-ip-info` is a simple Python script that allows you to retrieve the **IP address** and **geolocation information** (city, country, ISP, organization, etc.) of a given website. This tool is useful for network diagnostics, troubleshooting, and general information gathering about websites and their hosting infrastructure.

By resolving the domain name to an IP address and utilizing a free public API, this script provides a detailed breakdown of the server hosting the website. It can be used by network administrators, developers, or anyone curious about a website's server location.

### Features
- **IP Address Lookup**: Resolves the domain name to the associated IP address using Python's `socket` library.
- **Geolocation Information**: Fetches geolocation data such as the city, country, latitude, and longitude of the server hosting the website.
- **ISP and Organization Info**: Provides details about the Internet Service Provider (ISP) and the organization responsible for the server.
- **Autonomous System (AS) Info**: Displays the Autonomous System number related to the hosting server, useful for identifying large networks or cloud providers.
- **Error Handling**: Handles issues like invalid domains, failed API requests, or network connection problems gracefully.

### Installation

To use the `website-ip-info` script, you need to have Python installed on your machine. The script also relies on the `requests` library to fetch geolocation data from an external API.

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/website-ip-info.git
   cd website-ip-info

    Install the required dependencies:

    pip install requests

Usage

    Navigate to the directory where the script is located.

    Run the script by executing the following command:

python get_ip_info.py

When prompted, enter the domain name of the website you want to look up (e.g., google.com or example.com).

Enter a website URL (e.g., www.google.com): google.com

The script will output the IP address of the website and additional information such as its location, ISP, and organization.

Example output:

Enter a website URL (e.g., www.google.com): google.com
IP Address of google.com: 142.250.72.14
Location: Mountain View, California, United States
Latitude: 37.4056, Longitude: -122.0775
ISP: Google LLC
Organisation: Google LLC
AS (Autonomous System): AS15169
