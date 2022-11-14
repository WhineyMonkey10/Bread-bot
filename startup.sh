echo "Restarting Bread Bot..."
cd $HOME/bread-bot
sleep 1
nohup python index.py &
echo $! > $HOME/bread-bot/pid.txt
echo "Bot restarted at $(date)" >> $HOME/bread-bot/restart.log
