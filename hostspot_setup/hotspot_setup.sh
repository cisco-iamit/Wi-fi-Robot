sudo apt-get update
sudo apt-get upgrade
sudo apt install hostapd
sudo apt install dnsmasq


sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

sudo cp dhcpcd.conf /etc/dhcpcd.conf
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp dnsmasq.conf /etc/dnsmasq.conf
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo cp hostapd /etc/default/hostapd
