# !/bin/bash
echo "Hello world"
sleep 2
echo "Подождали"
sudo apt-get upgrade -y 
sudo apt install git -y 
apt-get install -y python3 python3-pip 
sudo apt install -y libsodium-dev cmake g++ git
sleep 3
# Второй этап-----------------------------------------------
sudo apt install curl
sudo apt-get install screen git 
curl https://rclone.org/install.sh | sudo bash
sleep 2
# Третий этап -----------------------------------------------------
cd 
mkdir AutoRclone
git clone https://github.com/azaz111/linode1.git
cd linode1
unzip AutoRclone.zip -d /root/AutoRclone
sleep 7
cd
chmod 777 awsstat.py
screen -dmS otchet python3 awsstat.py
chmod 777 trans.sh
mkdir /aws32 
screen -dmS mount rclone mount --daemon aws32: /aws32 
# Четвкртый --------------------------------------------------
cd
mkdir /disk1
mkdir /disk3
# Создаем дериктории на дисках
cd /disk1
mkdir vid1 
cd /disk3
mkdir video
cd /root
# Качаем плоттер и устанавливаем 
cd
git clone https://github.com/madMAx43v3r/chia-plotter.git 
sleep 3
cd chia-plotter
git submodule update --init
sleep 3
./make_devel.sh
sleep 5
cd
# ЗАпуск Плотера ------------------------------
screen -dmS videorender1 ./chia-plotter/build/chia_plot -n -1 -r 16 -u 256 -t /disk1/vid1/ -d /disk3/video/ -f b8e1d57e3e2dbb40ac8f2b257b762d05fcfc5b79c32a22255424644b7d183daa7c454624783f2d959c02eb1d2a4ba3a3 -p 91ea997633345082b15f83b957449180037030b6b7485f07ed4ee7558d08d3efbccf2c3d68ba724f5b3a8281a0055e27
screen -dmS otchet python3 awsstat.py
screen -dmS trans ./trans.sh
screen -r trans
