#! /usr/bin/zsh

RUN_PFETCH=/home/paulo/automation/miband_automation_tool/shell-scripts/mi_band/run_pfetch.sh

tilix -a session-add-right -x $RUN_PFETCH
sleep .6
tilix -a session-add-down -x "htop"
sleep .6    
tilix -a session-switch-to-previous-terminal && tilix -a session-switch-to-previous-terminal

cat /home/paulo/automation/miband_automation_tool/shell-scripts/mi_band/welcome.txt



$SHELL
