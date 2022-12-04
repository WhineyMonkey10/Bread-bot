echo "Script started at $(date)"
# Save the bash script's PID to a file
echo $$ > $HOME/bread-bot/startuppid.txt

while true; do
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
    sleep 1
done



