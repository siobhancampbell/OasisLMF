#!/bin/bash
SCRIPT=$(readlink -f "$0") && cd $(dirname "$SCRIPT")

# --- Script Init ---
set -euET -o pipefail
shopt -s inherit_errexit 2>/dev/null || echo "WARNING: Unable to set inherit_errexit. Possibly unsupported by this shell, Subprocess failures may not be detected."

LOG_DIR=log
mkdir -p $LOG_DIR
rm -R -f $LOG_DIR/*


touch $LOG_DIR/stderror.err
ktools_monitor.sh $$ $LOG_DIR & pid0=$!

exit_handler(){
   exit_code=$?

   # disable handler
   trap - QUIT HUP INT KILL TERM ERR EXIT

   kill -9 $pid0 2> /dev/null
   if [ "$exit_code" -gt 0 ]; then
       # Error - run process clean up
       echo 'Ktools Run Error - exitcode='$exit_code

       set +x
       group_pid=$(ps -p $$ -o pgid --no-headers)
       sess_pid=$(ps -p $$ -o sess --no-headers)
       script_pid=$$
       printf "Script PID:%d, GPID:%s, SPID:%d
" $script_pid $group_pid $sess_pid >> $LOG_DIR/killout.txt

       ps -jf f -g $sess_pid > $LOG_DIR/subprocess_list
       PIDS_KILL=$(pgrep -a --pgroup $group_pid | awk 'BEGIN { FS = "[ \t\n]+" }{ if ($1 >= '$script_pid') print}' | grep -v celery | egrep -v *\\.log$  | egrep -v *startup.sh$ | sort -n -r)
       echo "$PIDS_KILL" >> $LOG_DIR/killout.txt
       kill -9 $(echo "$PIDS_KILL" | awk 'BEGIN { FS = "[ \t\n]+" }{ print $1 }') 2>/dev/null
       exit $exit_code
   else
       # script successful
       exit 0
   fi
}
trap exit_handler QUIT HUP INT KILL TERM ERR EXIT

check_complete(){
    set +e
    proc_list="eve getmodel gulcalc fmcalc summarycalc eltcalc aalcalc aalcalcmeanonly leccalc pltcalc ordleccalc modelpy gulpy fmpy gulmc summarypy eltpy pltpy aalpy lecpy"
    has_error=0
    for p in $proc_list; do
        started=$(find log -name "${p}_[0-9]*.log" | wc -l)
        finished=$(find log -name "${p}_[0-9]*.log" -exec grep -l "finish" {} + | wc -l)
        if [ "$finished" -lt "$started" ]; then
            echo "[ERROR] $p - $((started-finished)) processes lost"
            has_error=1
        elif [ "$started" -gt 0 ]; then
            echo "[OK] $p"
        fi
    done
    if [ "$has_error" -ne 0 ]; then
        false # raise non-zero exit code
    else
        echo 'Run Completed'
    fi
}
# --- Setup run dirs ---

find output -type f -not -name '*summary-info*' -not -name '*.json' -exec rm -R -f {} +

rm -R -f fifo/*
rm -R -f work/*
mkdir -p work/kat/


mkfifo fifo/gul_P1
mkfifo fifo/gul_P2
mkfifo fifo/gul_P3
mkfifo fifo/gul_P4
mkfifo fifo/gul_P5
mkfifo fifo/gul_P6
mkfifo fifo/gul_P7
mkfifo fifo/gul_P8
mkfifo fifo/gul_P9
mkfifo fifo/gul_P10
mkfifo fifo/gul_P11
mkfifo fifo/gul_P12
mkfifo fifo/gul_P13
mkfifo fifo/gul_P14
mkfifo fifo/gul_P15
mkfifo fifo/gul_P16
mkfifo fifo/gul_P17
mkfifo fifo/gul_P18
mkfifo fifo/gul_P19
mkfifo fifo/gul_P20

mkfifo fifo/gul_S1_summary_P1
mkfifo fifo/gul_S1_pltcalc_P1

mkfifo fifo/gul_S1_summary_P2
mkfifo fifo/gul_S1_pltcalc_P2

mkfifo fifo/gul_S1_summary_P3
mkfifo fifo/gul_S1_pltcalc_P3

mkfifo fifo/gul_S1_summary_P4
mkfifo fifo/gul_S1_pltcalc_P4

mkfifo fifo/gul_S1_summary_P5
mkfifo fifo/gul_S1_pltcalc_P5

mkfifo fifo/gul_S1_summary_P6
mkfifo fifo/gul_S1_pltcalc_P6

mkfifo fifo/gul_S1_summary_P7
mkfifo fifo/gul_S1_pltcalc_P7

mkfifo fifo/gul_S1_summary_P8
mkfifo fifo/gul_S1_pltcalc_P8

mkfifo fifo/gul_S1_summary_P9
mkfifo fifo/gul_S1_pltcalc_P9

mkfifo fifo/gul_S1_summary_P10
mkfifo fifo/gul_S1_pltcalc_P10

mkfifo fifo/gul_S1_summary_P11
mkfifo fifo/gul_S1_pltcalc_P11

mkfifo fifo/gul_S1_summary_P12
mkfifo fifo/gul_S1_pltcalc_P12

mkfifo fifo/gul_S1_summary_P13
mkfifo fifo/gul_S1_pltcalc_P13

mkfifo fifo/gul_S1_summary_P14
mkfifo fifo/gul_S1_pltcalc_P14

mkfifo fifo/gul_S1_summary_P15
mkfifo fifo/gul_S1_pltcalc_P15

mkfifo fifo/gul_S1_summary_P16
mkfifo fifo/gul_S1_pltcalc_P16

mkfifo fifo/gul_S1_summary_P17
mkfifo fifo/gul_S1_pltcalc_P17

mkfifo fifo/gul_S1_summary_P18
mkfifo fifo/gul_S1_pltcalc_P18

mkfifo fifo/gul_S1_summary_P19
mkfifo fifo/gul_S1_pltcalc_P19

mkfifo fifo/gul_S1_summary_P20
mkfifo fifo/gul_S1_pltcalc_P20



# --- Do ground up loss computes ---

( pltcalc < fifo/gul_S1_pltcalc_P1 > work/kat/gul_S1_pltcalc_P1 ) 2>> $LOG_DIR/stderror.err & pid1=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P2 > work/kat/gul_S1_pltcalc_P2 ) 2>> $LOG_DIR/stderror.err & pid2=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P3 > work/kat/gul_S1_pltcalc_P3 ) 2>> $LOG_DIR/stderror.err & pid3=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P4 > work/kat/gul_S1_pltcalc_P4 ) 2>> $LOG_DIR/stderror.err & pid4=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P5 > work/kat/gul_S1_pltcalc_P5 ) 2>> $LOG_DIR/stderror.err & pid5=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P6 > work/kat/gul_S1_pltcalc_P6 ) 2>> $LOG_DIR/stderror.err & pid6=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P7 > work/kat/gul_S1_pltcalc_P7 ) 2>> $LOG_DIR/stderror.err & pid7=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P8 > work/kat/gul_S1_pltcalc_P8 ) 2>> $LOG_DIR/stderror.err & pid8=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P9 > work/kat/gul_S1_pltcalc_P9 ) 2>> $LOG_DIR/stderror.err & pid9=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P10 > work/kat/gul_S1_pltcalc_P10 ) 2>> $LOG_DIR/stderror.err & pid10=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P11 > work/kat/gul_S1_pltcalc_P11 ) 2>> $LOG_DIR/stderror.err & pid11=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P12 > work/kat/gul_S1_pltcalc_P12 ) 2>> $LOG_DIR/stderror.err & pid12=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P13 > work/kat/gul_S1_pltcalc_P13 ) 2>> $LOG_DIR/stderror.err & pid13=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P14 > work/kat/gul_S1_pltcalc_P14 ) 2>> $LOG_DIR/stderror.err & pid14=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P15 > work/kat/gul_S1_pltcalc_P15 ) 2>> $LOG_DIR/stderror.err & pid15=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P16 > work/kat/gul_S1_pltcalc_P16 ) 2>> $LOG_DIR/stderror.err & pid16=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P17 > work/kat/gul_S1_pltcalc_P17 ) 2>> $LOG_DIR/stderror.err & pid17=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P18 > work/kat/gul_S1_pltcalc_P18 ) 2>> $LOG_DIR/stderror.err & pid18=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P19 > work/kat/gul_S1_pltcalc_P19 ) 2>> $LOG_DIR/stderror.err & pid19=$!
( pltcalc -H < fifo/gul_S1_pltcalc_P20 > work/kat/gul_S1_pltcalc_P20 ) 2>> $LOG_DIR/stderror.err & pid20=$!


tee < fifo/gul_S1_summary_P1 fifo/gul_S1_pltcalc_P1 > /dev/null & pid21=$!
tee < fifo/gul_S1_summary_P2 fifo/gul_S1_pltcalc_P2 > /dev/null & pid22=$!
tee < fifo/gul_S1_summary_P3 fifo/gul_S1_pltcalc_P3 > /dev/null & pid23=$!
tee < fifo/gul_S1_summary_P4 fifo/gul_S1_pltcalc_P4 > /dev/null & pid24=$!
tee < fifo/gul_S1_summary_P5 fifo/gul_S1_pltcalc_P5 > /dev/null & pid25=$!
tee < fifo/gul_S1_summary_P6 fifo/gul_S1_pltcalc_P6 > /dev/null & pid26=$!
tee < fifo/gul_S1_summary_P7 fifo/gul_S1_pltcalc_P7 > /dev/null & pid27=$!
tee < fifo/gul_S1_summary_P8 fifo/gul_S1_pltcalc_P8 > /dev/null & pid28=$!
tee < fifo/gul_S1_summary_P9 fifo/gul_S1_pltcalc_P9 > /dev/null & pid29=$!
tee < fifo/gul_S1_summary_P10 fifo/gul_S1_pltcalc_P10 > /dev/null & pid30=$!
tee < fifo/gul_S1_summary_P11 fifo/gul_S1_pltcalc_P11 > /dev/null & pid31=$!
tee < fifo/gul_S1_summary_P12 fifo/gul_S1_pltcalc_P12 > /dev/null & pid32=$!
tee < fifo/gul_S1_summary_P13 fifo/gul_S1_pltcalc_P13 > /dev/null & pid33=$!
tee < fifo/gul_S1_summary_P14 fifo/gul_S1_pltcalc_P14 > /dev/null & pid34=$!
tee < fifo/gul_S1_summary_P15 fifo/gul_S1_pltcalc_P15 > /dev/null & pid35=$!
tee < fifo/gul_S1_summary_P16 fifo/gul_S1_pltcalc_P16 > /dev/null & pid36=$!
tee < fifo/gul_S1_summary_P17 fifo/gul_S1_pltcalc_P17 > /dev/null & pid37=$!
tee < fifo/gul_S1_summary_P18 fifo/gul_S1_pltcalc_P18 > /dev/null & pid38=$!
tee < fifo/gul_S1_summary_P19 fifo/gul_S1_pltcalc_P19 > /dev/null & pid39=$!
tee < fifo/gul_S1_summary_P20 fifo/gul_S1_pltcalc_P20 > /dev/null & pid40=$!

( summarycalc -m -i  -1 fifo/gul_S1_summary_P1 < fifo/gul_P1 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P2 < fifo/gul_P2 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P3 < fifo/gul_P3 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P4 < fifo/gul_P4 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P5 < fifo/gul_P5 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P6 < fifo/gul_P6 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P7 < fifo/gul_P7 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P8 < fifo/gul_P8 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P9 < fifo/gul_P9 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P10 < fifo/gul_P10 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P11 < fifo/gul_P11 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P12 < fifo/gul_P12 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P13 < fifo/gul_P13 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P14 < fifo/gul_P14 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P15 < fifo/gul_P15 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P16 < fifo/gul_P16 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P17 < fifo/gul_P17 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P18 < fifo/gul_P18 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P19 < fifo/gul_P19 ) 2>> $LOG_DIR/stderror.err  &
( summarycalc -m -i  -1 fifo/gul_S1_summary_P20 < fifo/gul_P20 ) 2>> $LOG_DIR/stderror.err  &

( ( eve 1 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P1  ) 2>> $LOG_DIR/stderror.err ) &  pid41=$!
( ( eve 2 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P2  ) 2>> $LOG_DIR/stderror.err ) &  pid42=$!
( ( eve 3 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P3  ) 2>> $LOG_DIR/stderror.err ) &  pid43=$!
( ( eve 4 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P4  ) 2>> $LOG_DIR/stderror.err ) &  pid44=$!
( ( eve 5 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P5  ) 2>> $LOG_DIR/stderror.err ) &  pid45=$!
( ( eve 6 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P6  ) 2>> $LOG_DIR/stderror.err ) &  pid46=$!
( ( eve 7 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P7  ) 2>> $LOG_DIR/stderror.err ) &  pid47=$!
( ( eve 8 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P8  ) 2>> $LOG_DIR/stderror.err ) &  pid48=$!
( ( eve 9 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P9  ) 2>> $LOG_DIR/stderror.err ) &  pid49=$!
( ( eve 10 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P10  ) 2>> $LOG_DIR/stderror.err ) &  pid50=$!
( ( eve 11 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P11  ) 2>> $LOG_DIR/stderror.err ) &  pid51=$!
( ( eve 12 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P12  ) 2>> $LOG_DIR/stderror.err ) &  pid52=$!
( ( eve 13 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P13  ) 2>> $LOG_DIR/stderror.err ) &  pid53=$!
( ( eve 14 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P14  ) 2>> $LOG_DIR/stderror.err ) &  pid54=$!
( ( eve 15 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P15  ) 2>> $LOG_DIR/stderror.err ) &  pid55=$!
( ( eve 16 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P16  ) 2>> $LOG_DIR/stderror.err ) &  pid56=$!
( ( eve 17 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P17  ) 2>> $LOG_DIR/stderror.err ) &  pid57=$!
( ( eve 18 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P18  ) 2>> $LOG_DIR/stderror.err ) &  pid58=$!
( ( eve 19 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P19  ) 2>> $LOG_DIR/stderror.err ) &  pid59=$!
( ( eve 20 20 | getmodel | gulcalc -S100 -L100 -r -a1 -i - > fifo/gul_P20  ) 2>> $LOG_DIR/stderror.err ) &  pid60=$!

wait $pid1 $pid2 $pid3 $pid4 $pid5 $pid6 $pid7 $pid8 $pid9 $pid10 $pid11 $pid12 $pid13 $pid14 $pid15 $pid16 $pid17 $pid18 $pid19 $pid20 $pid21 $pid22 $pid23 $pid24 $pid25 $pid26 $pid27 $pid28 $pid29 $pid30 $pid31 $pid32 $pid33 $pid34 $pid35 $pid36 $pid37 $pid38 $pid39 $pid40 $pid41 $pid42 $pid43 $pid44 $pid45 $pid46 $pid47 $pid48 $pid49 $pid50 $pid51 $pid52 $pid53 $pid54 $pid55 $pid56 $pid57 $pid58 $pid59 $pid60


# --- Do ground up loss kats ---

kat work/kat/gul_S1_pltcalc_P1 work/kat/gul_S1_pltcalc_P2 work/kat/gul_S1_pltcalc_P3 work/kat/gul_S1_pltcalc_P4 work/kat/gul_S1_pltcalc_P5 work/kat/gul_S1_pltcalc_P6 work/kat/gul_S1_pltcalc_P7 work/kat/gul_S1_pltcalc_P8 work/kat/gul_S1_pltcalc_P9 work/kat/gul_S1_pltcalc_P10 work/kat/gul_S1_pltcalc_P11 work/kat/gul_S1_pltcalc_P12 work/kat/gul_S1_pltcalc_P13 work/kat/gul_S1_pltcalc_P14 work/kat/gul_S1_pltcalc_P15 work/kat/gul_S1_pltcalc_P16 work/kat/gul_S1_pltcalc_P17 work/kat/gul_S1_pltcalc_P18 work/kat/gul_S1_pltcalc_P19 work/kat/gul_S1_pltcalc_P20 > output/gul_S1_pltcalc.csv & kpid1=$!
wait $kpid1


rm -R -f work/*
rm -R -f fifo/*

check_complete
