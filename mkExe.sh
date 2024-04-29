cd $HOME/.config/progressBar-clt-main/
chmod +x hack.py
cd

if ! grep -qxF "export PATH="$PATH:$HOME/.config/progressBar-clt-main/"" ~/.bashrc; then
    echo "export PATH="$PATH:$HOME/.config/progressBar-clt-main/"" >> ~/.bashrc
    echo "PATH added to .bashrc"
echo "all Done"
fi
