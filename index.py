import os
from src.colors import *

current_user = str.strip(os.popen("whoami").read())

def menu():
    log("**AutoConfigure**\n", "aqua")
    white()
    print("1. Instalar requerimientos inciales")
    print("2. Configurar Kitty")
    print("3. Configurar bspwm y sxhkd")
    print("4. Configurar Polybar")
    print("5. Configurar Picom")
    print("6. Configurar Zsh y P10k")
    print("7. Install NvChat with neovim")
    print("8. Install Fzf")
    green()
    option = input("> ")

    if option == "1":
        installInit()

    if option == "2":
        installKitty()

    if option == "3":
        installBspwm()
    
    if option == "4":
        installPolybar()

    if option == "5":
        installPicom()
    
    if option == "6":
        installZshAndP10k()
        
    if option == "7":
        installNvim()
        
    if option == "8":
        installFzF()

def installInit():
    log(">>  Iniciando instalacion de Dependencias...", "purple")
    white()
    os.system("sudo apt-get update -y")
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libuv1-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev libpcre3-dev -y")


    os.system("sudo apt install rofi bspwm locate npm feh -y")
    log(">>  Configurando fuentes iniciales..", "purple")
    # install initial fonts
    os.system("sudo cp resources/fonts.zip /usr/local/share/fonts/")
    os.system("cd /usr/local/share/fonts && sudo unzip -o fonts.zip && sudo rm fonts.zip")
    log(">>  Configuracion inicial finalizada", "purple")
    # install batcat and lsd
    os.system("sudo dpkg -i resources/bat_amd64.deb")
    os.system("sudo dpkg -i resources/lsd_amd64.deb")

def installKitty():
    log(">>  Configurando Kitty...", "blue")
    # instalando la kitty
    os.system("7z x -y ./resources/last-kitty.txz -o./kitty")
    os.system("cd kitty && 7z x -y ./last-kitty.tar && rm last-kitty.tar")
    os.system("sudo apt remove kitty -y && sudo apt autoremove -y")
    os.system("sudo mv ./kitty /opt")
    os.system("sudo chmod +x /opt/kitty/bin/kitty")
    os.system("sudo chmod +x /opt/kitty/bin/kitten")
    # configurando la Kitty
    os.system("mkdir ~/.config/kitty/")
    os.system("cp ./resources/kitty.conf ~/.config/kitty/")
    os.system("cp ./resources/color.ini ~/.config/kitty/")
    log(">>  Config Kitty Exitosa", "blue")

def installBspwm():
    log(">>  Clonando repo Bspwm y sxhkd...", "yellow")
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    log(">>  Iniciando instalacion Bspwm y sxhkd...", "yellow")
    os.system("cd bspwm/ && make && sudo make install && cd ..")
    os.system("cd sxhkd/ && make && sudo make install && cd ..")
    log(">>  Configurando archivos Bspwm y sxhkd...", "yellow")
    # Crea las carpetas de bspwm y sxhkd en ~/.config
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")

    os.system("cp bspwm/examples/bspwmrc ~/.config/bspwm/")
    os.system("cp bspwm/examples/sxhkdrc ~/.config/sxhkd/")

    os.system("chmod +x ~/.config/bspwm/bspwmrc")

    # Pendiente configurar el sxhkd seccion 2.2
    os.system("cp resources/sxhkdrc ~/.config/sxhkd") 
    os.system("cp resources/bspwm-resize ~/.config/bspwm/")

    # CLipboard Bidireccional para VMWare
    bswpm_content = os.popen("cat ~/.config/bspwm/bspwmrc").read()
    if ("vmware-user-suid-wrapper" in bswpm_content ) == False :
        os.system("echo 'vmware-user-suid-wrapper &' >> ~/.config/bspwm/bspwmrc")

    # configurar fondo de pantalla
    if ("feh --bg-fill ~/.wallpapers/wallpaper.jpg" in bswpm_content) == False :
        os.system("mkdir ~/.wallpapers")
        os.system("cp resources/wallpaper.jpg ~/.wallpapers")
        os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg &' >> ~/.config/bspwm/bspwmrc")
        os.system("echo 'xsetroot -cursor_name left_ptr &' >> ~/.config/bspwm/bspwmrc")
        os.system("echo 'wmname LG3D &' >> ~/.config/bspwm/bspwmrc")
        
    os.system("rm -rf sxhkd/ && rm -rf bspwm/")
    log(">>  Config Bspwm y sxhkd finalizada exitosamente", "yellow")

def installPolybar():
    log(">>  Instalando Librerias...", "orange")
    
    # instalacion de la polybar
    log(">>  Clonando repo y configurando polybar...", "orange")
    os.system("mkdir ~/.config/polybar/")
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("mkdir -p polybar/build && cd polybar/build && cmake .. && make -j$(nproc)")
    os.system("cd ./polybar/build/ && sudo make install" )

    # instalando blue-sky
    log(">>  Clonando repo y configurando blueSky...", "orange")
    os.system("git clone https://github.com/VaughnValle/blue-sky.git")
    os.system("cp -r blue-sky/polybar/* ~/.config/polybar")
    os.system("sudo cp -r blue-sky/polybar/fonts/* /usr/share/fonts/truetype/")
    bswpm_content = os.popen("cat ~/.config/bspwm/bspwmrc").read()
    if ("./launch.sh" in bswpm_content ) == False :
        os.system("echo '~/.config/polybar/./launch.sh &' >> ~/.config/bspwm/bspwmrc")

    os.system("fc-cache -v")
    
    # Migrando theme para Rofi
    os.system("mkdir -p ~/.config/rofi/themes")
    os.system("cp blue-sky/nord.rasi ~/.config/rofi/themes")
    os.system('echo "@theme \"~/.config/rofi/themes/nord.rasi\"" > ~/.config/rofi/config.rasi')
    
    # instalando modulos personalizados
    log(">>  Instalando modulos personalizados polybar...", "orange")
    os.system("cp resources/polybar/current.ini ~/.config/polybar/")
    os.system("cp resources/polybar/workspace.ini ~/.config/polybar/")
    os.system("cp resources/polybar/launch.sh ~/.config/polybar/")
    
    os.system("mkdir ~/.config/bin/")
    os.system("cp -r resources/polybar/bin/* ~/.config/bin/")
    os.system("chmod +x ~/.config/bin/*.sh")
    
    os.system("rm -rf polybar/")
    os.system("rm -rf blue-sky/")
    
def installPicom():
    # instalando picom
    log(">>  Instalando librerias necesarias...", "aqua")
    log(">>  Clonando y configurando picom...", "aqua")
    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.system("cd picom/ && git submodule update --init --recursive")
    os.system("cd picom/ && meson --buildtype=release . build && ninja -C build && sudo ninja -C build install")

    # Generando los difuminados con picom
    os.system("mkdir ~/.config/picom/")
    os.system("cp resources/picom.conf ~/.config/picom/")
    bswpm_content = os.popen("cat ~/.config/bspwm/bspwmrc").read()
    if ("picom" in bswpm_content ) == False :
        os.system("echo 'picom &' >> ~/.config/bspwm/bspwmrc")
        os.system("echo 'bspc config border_width 0 &' >> ~/.config/bspwm/bspwmrc")
    log(">>  Picom configurado exitosamente", "aqua")
    
    os.system("rm -rf picom/")

def installZshAndP10k():
    log(">> Iniciando instalacion de ZSH", "yellow")
    os.system("sudo apt install zsh -y")
    exists = os.system("wc ~/.zshrc")
    if exists != 0 :
        log("No existe el fichero ~/.zshrc, creando...")
        defaultConfig = os.system("cat /etc/zsh/newuser.zshrc.recommended")
        if defaultConfig == 0:
            os.system("cat /etc/zsh/newuser.zshrc.recommended > ~/.zshrc")
        
    os.system("sudo apt install zsh-autosuggestions zsh-syntax-highlighting -y")

    # instala la powerLevel 10k
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")
    os.system("cp resources/.zshrc ~/")
    os.system("cp resources/.p10k.zsh ~/")

    # Instalacion de powerlevel10k para root
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/powerlevel10k")
    os.system("sudo cp resources/.zshrc /root/")
    os.system("sudo chown root:root /usr/local/share/zsh/site-functions/_bspc")
    os.system("sudo cp resources/.p10k-root.zsh /root/.p10k.zsh")

    if (current_user):
        zsh_dir = os.popen("which zsh").read()
        if zsh_dir :
            os.system(f'sudo usermod --shell {str.strip(zsh_dir)} {str.strip(current_user)}')
            os.system(f'sudo usermod --shell {str.strip(zsh_dir)} root')
        os.system(f'sudo ln -s -f /home/{str.strip(current_user)}/.zshrc /root/.zshrc')
    
    _installZshPlugin()

def _installZshPlugin(): 
    os.system("sudo rm -rf /usr/share/zsh-sudo")
    os.system(f"sudo mkdir /usr/share/zsh-sudo && sudo chown {current_user}:{current_user} /usr/share/zsh-sudo")
    os.system("cd /usr/share/zsh-sudo && sudo wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh")
    os.system("sudo chmod +x /usr/share/zsh-sudo/*.zsh")
    
def installNvim():
    os.system("sudo apt remove neovim -y")
    os.system("rm -rf ~/.config/nvim")
    os.system("git clone https://github.com/NvChad/starter ~/.config/nvim --depth 1")
    os.system("tar -xf resources/neovim/nvim*.gz")
    os.system("sudo mkdir /opt/nvim")
    os.system("sudo mv nvim-linux64/* /opt/nvim")
    os.system("rm -rf nvim-linux64")
    
def installFzF():
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    os.system("~/.fzf/install")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        log("[!] No ejecutes esta herramienta como root", "red")
    else:
        menu()


""" 
if (os.uname().nodename) == "kali":
    log("Kali", "blue") """