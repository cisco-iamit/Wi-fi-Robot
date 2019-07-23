sudo apt-get update
sudo apt-get upgrade
sudo dist-upgrade
#sudo reboot
sudo apt install dnsmasq hostapd
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
sudo rm /etc/dhcpcd.conf
sudo cp dhcpcd.conf /etc/dhcpcd.conf
sudo service dhcpcd restart
sudo systemctl start dnsmasq

# sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo rm /etc/dnsmasq.conf
sudo cp dnsmasq.conf /etc/dnsmasq.conf
sudo systemctl reload dnsmasq
sudo systemctl start dnsmasq

sudo rm /etc/hostapd.conf
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo rm /etc/hostapd
sudo cp hostapd /etc/default/hostapd

sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd

sudo systemctl status hostapd
sudo systemctl status dnsmasq

sudo rm /etc/sysctl.conf
sudo cp hostapd /etc/default/sysctl.conf
# sudo nano /etc/sysctl.conf
# net.ipv4.ip_forward=1

sudo iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
sudo rm /etc/rc.local
sudo cp hostapd /etc/default/rc.local
# sudo nano /etc/rc.local
# iptables-restore < /etc/iptables.ipv4.nat

sudo reboot

sudo systemctl start dhcpcd
sudo systemctl start dnsmasq
sudo systemctl start hostapd

sudo systemctl reload dhcpcd
sudo systemctl reload dnsmasq
sudo systemctl reload hostapd
