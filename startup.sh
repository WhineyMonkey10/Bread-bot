wait 5
cd /bread-bot
nohup python index.py &
echo $! > $HOME/bread-bot/pid.txt
