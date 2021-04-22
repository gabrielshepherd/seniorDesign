```bash
sudo raspi-config
```
```bash
sudo nano /etc/network/interfaces
```
```bash
# interfaces(5) file used by ifup(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d
source-directory /etc/network/interfaces.d
```
```bash
# interfaces(5) file used by ifup(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d
source-directory /etc/network/interfaces.d

auto wlan0
iface wlan0 inet manual
  wpa-driver nl80211
  wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
```
```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
```bash
ctrl_interface-DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
```
```bash
ctrl_interface-DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
        ssid="PartsInventory"
        psk="sd4032017"
        key_mgmt=WPA-PSK
}
```
```bash
sudo nano /etc/dhcpcd.conf
```
```bash
# Example static IP configuration:
interface wlan0
static ip_address=172.16.0.1/24
...
static routers=172.16.0.1
```
```bash
sudo pip3 install Flask
```
```bash
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
```
```bash
sudo pip3 install --force-reinstall adafruit-blinka
```
```bash
# Example static IP configuration:
interface wlan0
static ip_address=172.16.0.2/24
...
static routers=172.16.0.1
```
```bash
sudo pip3 install requests
```
```bash
sudo pip3 install tk
```
```bash
sudo pip3 install xlrd
```
```bash
sudo pip3 install xlwt
```
