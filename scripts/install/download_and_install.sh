set -e
apt update && apt install vim sudo git curl -y
git clone https://github.com/robocomp/robocomp_libs
cd robocomp_libs/
bash scripts/install/resources/robocomp_prerequisites_install.sh
mkdir build
cd build/
cmake ..
make -j 10
sudo make install
sudo ldconfig
