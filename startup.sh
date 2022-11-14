if [ ps -p $(cat $HOME/bread-bot/pid.txt) ]; then
    echo "Bot is running"
    echo "Bot is running at $(date)" >> $HOME/bread-bot/restart.log
else
    echo "Bot is not running"
    echo "Restarting bot..."
    cd $HOME/bread-bot
    nohup python index.py &
    echo $! > $HOME/bread-bot/pid.txt
    echo "Bot restarted at $(date)" >> $HOME/bread-bot/restart.log
fi


