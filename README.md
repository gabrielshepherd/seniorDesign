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
        mode=2
        frequency=2437
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
```bash
cd Documents
```
```bash
sudo git clone https://github.com/gabrielshepherd/seniorDesign.git
```
```bash
cd ..
```
```bash
sudo nano /lib/systemd/system/ledcontroller.service
```
```bash
[Unit]
Description=LED Controller
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/pi/seniorDesign/app.py
RemainAfterExit=yes
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable ledcontroller.service
```
```bash
sudo reboot now
```
```bash
sudo cp /media/pi/Samsung\ USB/StorageRoomData.xls /home/pi/seniorDesign/MainGUICode
```
```bash
#! /bin/bash
sudo python3 /home/pi/seniorDesign/MainGUICode/AdditionalPages.py
```
```bash
cd Desktop
```
```bash
chmod u+x StartGUI.sh
```
```bash
sudo apt-get update
```
```bash
sudo apt-get install git
```
```bash
sudo apt-get install python3-pip
```
