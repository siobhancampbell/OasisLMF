#!/bin/bash
SCRIPT=$(readlink -f "$0") && cd $(dirname "$SCRIPT")

# --- Script Init ---
set -euET -o pipefail
shopt -s inherit_errexit 2>/dev/null || echo "WARNING: Unable to set inherit_errexit. Possibly unsupported by this shell, Subprocess failures may not be detected."

LOG_DIR=log
mkdir -p $LOG_DIR
rm -R -f $LOG_DIR/*

# --- Setup run dirs ---

find output -type f -not -name '*summary-info*' -not -name '*.json' -exec rm -R -f {} +

find fifo/ \( -name '*P13[^0-9]*' -o -name '*P13' \) -exec rm -R -f {} +
rm -R -f work/*
mkdir -p work/kat/


mkfifo fifo/gul_P13

mkfifo fifo/gul_S1_summary_P13
mkfifo fifo/gul_S1_summarycalc_P13



# --- Do ground up loss computes ---
summarycalctocsv -s < fifo/gul_S1_summarycalc_P13 > work/kat/gul_S1_summarycalc_P13 & pid1=$!
tee < fifo/gul_S1_summary_P13 fifo/gul_S1_summarycalc_P13 > /dev/null & pid2=$!
summarycalc -m -i  -1 fifo/gul_S1_summary_P13 < fifo/gul_P13 &

( eve -R 13 20 | getmodel | gulcalc -S100 -L100 -r -a0 -i - > fifo/gul_P13  ) &  pid3=$!

wait $pid1 $pid2 $pid3

