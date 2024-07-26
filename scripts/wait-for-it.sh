#!/usr/bin/env bash
should_run=true

after_boot() {
    if [ ! -z "$AFTER_BOOT" ]; then
        chmod +x $AFTER_BOOT
        "$AFTER_BOOT"
        echo "After boot exited with code $?"
    fi
}

before_shutdown() {
    should_run=false
    if [ ! -z "$BEFORE_SHUTDOWN" ]; then
        chmod +x $BEFORE_SHUTDOWN
        "$BEFORE_SHUTDOWN"
        echo "Before shutdown exited with code $?"
        exit $?
    fi
}

wait_for() {
    echo ""
    echo "..."
    echo -e "\e[1;35m============================================\e[0m"
    echo -e "\e[1;35m|        Dependency service check          |\e[0m"
    echo -e "\e[1;35m============================================\e[0m"
    if [ ! -z "$WAIT_FOR" ]; then
        for i in $(echo $WAIT_FOR | tr "," "\n")
        do
          array=$(echo $i | tr ":" "\n")
          host="${array[0]}"
          port="${array[1]}"
          code=1
          while [ "$code" != "0" ] && [ $should_run ]
          do
              echo -e "\e[1;36mWaiting for $i to come up... \e[0m"
              nc -z -v -w5 $host $port
              code=$?
              echo -e "\e[1;33mCheck exited with code $code. \e[0m"
              if [ "$code" != "0" ]; then
                sleep 5
              fi
          done
          echo -e "\e[1;32m$i is up. Continuing.\e[0m"
          sleep 5
        done
    fi;
}

trap before_shutdown HUP INT TERM KILL

wait_for;
echo "..."
echo -e "\e[1;35m============================================\e[0m"
echo -e "\e[1;35m|            Command Execution             |\e[0m"
echo -e "\e[1;35m============================================\e[0m"
echo -e "\e[1;36mStarting command $@...\e[0m"
"$@" &
PID=$!
echo -e "\e[1;32mCommand $@ is running with PID $PID\e[0m"
echo "..."
echo -e "\e[1;36mStarting after boot...\e[0m"
echo "..."
after_boot;
echo -e "\e[1;36mAfter boot completed.\e[0m"
echo -e "\e[1;32mReady.\e[0m"
wait $PID
exit $?
