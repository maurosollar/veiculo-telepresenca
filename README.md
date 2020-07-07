# Veículo de Tele-Presença

Este veículo de tele presença tem como objetivo de possibilitar uma pessoa caminhar e interagir virtualmente com outro ambiente via áudio e vídeo se locomovendo pelo ambiente. O veículo utiliza o próprio navegador nativo da Raspbian para acessar um servidor de vídeo conferência "Jitsi" qual podemos utilizar ele público ou privado caso tenha instalado.

Este veículo necessita de acesso a uma rede WiFi para acessar o servidor de vídeo conferência e receber os comandos para se locomover.

## Materiais necessários:

- 1 - Display 7" 1024x600 touch
- 1 - Raspberry PI 4 B
- 1 - WebCam Logitech C920
- 1 - Caixa de som
- 1 - Conjunto de rodas Mecanum, comprado na China já com arduino e placa de controle que recebe via serial os comandos de movimentos.
- 1 - Bateria 12V 7Ah chumbo ácido
- 1 - Adaptador USB TP-Link WiFi com antena de 4dB, não foi utilizado o WiFi da própria Raspberry em função do baixo ganho de recepção.
- 1 - Carregador de baterias
- 1 - Conversor DC-DC
- 1 - Cartão Micro-SD 8GB Classe 10
- 1 - Teclado sem fio

## Passos para instalação:

Utilizado um 2020-02-13-raspbian-buster 

Como utilizei adaptador USB WiFi, tive que desativar a WiFi On-Board e configurar a externa:

```
sudo vi /boot/config.txt
dtoverlay=pi3-disable-wifi

sudo vi /etc/modprobe.d/raspi-blacklist.conf
#wifi
blacklist brcmfmac
blacklist brcmutil

sudo vi interfaces
source-directory /etc/network/interfaces.d
auto lo
iface lo inet loopback
iface eth0 inet manual
allow-hotplug wlan0
iface wlan0 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

sudo raspi-config
Opção 5 - Interfacing Options / P2 SSH - Enable / P5 I2C - Enable / P6 Serial - Disable Shell and Enable Serial
```

## Atualize o Raspbian
```
sudo apt-get update
sudo apt-get upgrade
```

## Continue...



