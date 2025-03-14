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
mkdir -p output/full_correlation/

rm -R -f work/*
mkdir -p work/kat/
mkdir -p work/full_correlation/
mkdir -p work/full_correlation/kat/

rm -R -f /tmp/%FIFO_DIR%/
mkdir -p /tmp/%FIFO_DIR%/fifo/
mkdir -p /tmp/%FIFO_DIR%/fifo/full_correlation/
mkdir -p work/gul_S1_summaryaalcalc
mkdir -p work/full_correlation/gul_S1_summaryaalcalc
mkdir -p work/il_S1_summaryleccalc
mkdir -p work/full_correlation/il_S1_summaryleccalc
mkdir -p work/ri_S1_summaryleccalc
mkdir -p work/full_correlation/ri_S1_summaryleccalc

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_fc_P1

mkfifo /tmp/%FIFO_DIR%/fifo/gul_P1

mkfifo /tmp/%FIFO_DIR%/fifo/gul_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/gul_S1_summary_P1.idx
mkfifo /tmp/%FIFO_DIR%/fifo/gul_S1_eltcalc_P1
mkfifo /tmp/%FIFO_DIR%/fifo/gul_S1_summarycalc_P1
mkfifo /tmp/%FIFO_DIR%/fifo/gul_S1_pltcalc_P1

mkfifo /tmp/%FIFO_DIR%/fifo/il_P1

mkfifo /tmp/%FIFO_DIR%/fifo/il_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/il_S1_summary_P1.idx

mkfifo /tmp/%FIFO_DIR%/fifo/ri_P1

mkfifo /tmp/%FIFO_DIR%/fifo/ri_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/ri_S1_summary_P1.idx

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_P1

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summary_P1.idx
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_eltcalc_P1
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summarycalc_P1
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_pltcalc_P1

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/il_P1

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/il_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/il_S1_summary_P1.idx

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/ri_P1

mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/ri_S1_summary_P1
mkfifo /tmp/%FIFO_DIR%/fifo/full_correlation/ri_S1_summary_P1.idx



# --- Do reinsurance loss computes ---



tee < /tmp/%FIFO_DIR%/fifo/ri_S1_summary_P1 work/ri_S1_summaryleccalc/P1.bin > /dev/null & pid1=$!
tee < /tmp/%FIFO_DIR%/fifo/ri_S1_summary_P1.idx work/ri_S1_summaryleccalc/P1.idx > /dev/null & pid2=$!

summarycalc -m -f -p input/RI_1 -1 /tmp/%FIFO_DIR%/fifo/ri_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/ri_P1 &

# --- Do insured loss computes ---



tee < /tmp/%FIFO_DIR%/fifo/il_S1_summary_P1 work/il_S1_summaryleccalc/P1.bin > /dev/null & pid3=$!
tee < /tmp/%FIFO_DIR%/fifo/il_S1_summary_P1.idx work/il_S1_summaryleccalc/P1.idx > /dev/null & pid4=$!

summarycalc -m -f  -1 /tmp/%FIFO_DIR%/fifo/il_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/il_P1 &

# --- Do ground up loss computes ---

eltcalc < /tmp/%FIFO_DIR%/fifo/gul_S1_eltcalc_P1 > work/kat/gul_S1_eltcalc_P1 & pid5=$!
summarycalctocsv < /tmp/%FIFO_DIR%/fifo/gul_S1_summarycalc_P1 > work/kat/gul_S1_summarycalc_P1 & pid6=$!
pltcalc < /tmp/%FIFO_DIR%/fifo/gul_S1_pltcalc_P1 > work/kat/gul_S1_pltcalc_P1 & pid7=$!


tee < /tmp/%FIFO_DIR%/fifo/gul_S1_summary_P1 /tmp/%FIFO_DIR%/fifo/gul_S1_eltcalc_P1 /tmp/%FIFO_DIR%/fifo/gul_S1_summarycalc_P1 /tmp/%FIFO_DIR%/fifo/gul_S1_pltcalc_P1 work/gul_S1_summaryaalcalc/P1.bin > /dev/null & pid8=$!
tee < /tmp/%FIFO_DIR%/fifo/gul_S1_summary_P1.idx work/gul_S1_summaryaalcalc/P1.idx > /dev/null & pid9=$!

summarycalc -m -i  -1 /tmp/%FIFO_DIR%/fifo/gul_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/gul_P1 &

# --- Do reinsurance loss computes ---



tee < /tmp/%FIFO_DIR%/fifo/full_correlation/ri_S1_summary_P1 work/full_correlation/ri_S1_summaryleccalc/P1.bin > /dev/null & pid10=$!
tee < /tmp/%FIFO_DIR%/fifo/full_correlation/ri_S1_summary_P1.idx work/full_correlation/ri_S1_summaryleccalc/P1.idx > /dev/null & pid11=$!

summarycalc -m -f -p input/RI_1 -1 /tmp/%FIFO_DIR%/fifo/full_correlation/ri_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/full_correlation/ri_P1 &

# --- Do insured loss computes ---



tee < /tmp/%FIFO_DIR%/fifo/full_correlation/il_S1_summary_P1 work/full_correlation/il_S1_summaryleccalc/P1.bin > /dev/null & pid12=$!
tee < /tmp/%FIFO_DIR%/fifo/full_correlation/il_S1_summary_P1.idx work/full_correlation/il_S1_summaryleccalc/P1.idx > /dev/null & pid13=$!

summarycalc -m -f  -1 /tmp/%FIFO_DIR%/fifo/full_correlation/il_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/full_correlation/il_P1 &

# --- Do ground up loss computes ---

eltcalc < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_eltcalc_P1 > work/full_correlation/kat/gul_S1_eltcalc_P1 & pid14=$!
summarycalctocsv < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summarycalc_P1 > work/full_correlation/kat/gul_S1_summarycalc_P1 & pid15=$!
pltcalc < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_pltcalc_P1 > work/full_correlation/kat/gul_S1_pltcalc_P1 & pid16=$!


tee < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summary_P1 /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_eltcalc_P1 /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summarycalc_P1 /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_pltcalc_P1 work/full_correlation/gul_S1_summaryaalcalc/P1.bin > /dev/null & pid17=$!
tee < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summary_P1.idx work/full_correlation/gul_S1_summaryaalcalc/P1.idx > /dev/null & pid18=$!

summarycalc -m -i  -1 /tmp/%FIFO_DIR%/fifo/full_correlation/gul_S1_summary_P1 < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_P1 &

( tee < /tmp/%FIFO_DIR%/fifo/full_correlation/gul_fc_P1 /tmp/%FIFO_DIR%/fifo/full_correlation/gul_P1  | fmcalc -a2 | tee /tmp/%FIFO_DIR%/fifo/full_correlation/il_P1 | fmcalc -a3 -p input/RI_1 -n - > /tmp/%FIFO_DIR%/fifo/full_correlation/ri_P1 ) & pid19=$!
( eve 1 1 | getmodel | gulcalc -S0 -L0 -r -j /tmp/%FIFO_DIR%/fifo/full_correlation/gul_fc_P1 -a1 -i - | tee /tmp/%FIFO_DIR%/fifo/gul_P1 | fmcalc -a2 | tee /tmp/%FIFO_DIR%/fifo/il_P1 | fmcalc -a3 -p input/RI_1 -n - > /tmp/%FIFO_DIR%/fifo/ri_P1 ) & pid20=$!

wait $pid1 $pid2 $pid3 $pid4 $pid5 $pid6 $pid7 $pid8 $pid9 $pid10 $pid11 $pid12 $pid13 $pid14 $pid15 $pid16 $pid17 $pid18 $pid19 $pid20


# --- Do reinsurance loss kats ---


# --- Do reinsurance loss kats for fully correlated output ---


# --- Do insured loss kats ---


# --- Do insured loss kats for fully correlated output ---


# --- Do ground up loss kats ---

kat work/kat/gul_S1_eltcalc_P1 > output/gul_S1_eltcalc.csv & kpid1=$!
kat work/kat/gul_S1_pltcalc_P1 > output/gul_S1_pltcalc.csv & kpid2=$!
kat work/kat/gul_S1_summarycalc_P1 > output/gul_S1_summarycalc.csv & kpid3=$!

# --- Do ground up loss kats for fully correlated output ---

kat work/full_correlation/kat/gul_S1_eltcalc_P1 > output/full_correlation/gul_S1_eltcalc.csv & kpid4=$!
kat work/full_correlation/kat/gul_S1_pltcalc_P1 > output/full_correlation/gul_S1_pltcalc.csv & kpid5=$!
kat work/full_correlation/kat/gul_S1_summarycalc_P1 > output/full_correlation/gul_S1_summarycalc.csv & kpid6=$!
wait $kpid1 $kpid2 $kpid3 $kpid4 $kpid5 $kpid6


ordleccalc -r -Kri_S1_summaryleccalc -F -f -S -s -M -m -W -w -O output/ri_S1_ept.csv -o output/ri_S1_psept.csv & lpid1=$!
ordleccalc  -Kil_S1_summaryleccalc -F -S -s -M -m -O output/il_S1_ept.csv & lpid2=$!
aalcalc -Kgul_S1_summaryaalcalc > output/gul_S1_aalcalc.csv & lpid3=$!
ordleccalc -r -Kfull_correlation/ri_S1_summaryleccalc -F -f -S -s -M -m -W -w -O output/full_correlation/ri_S1_ept.csv -o output/full_correlation/ri_S1_psept.csv & lpid4=$!
ordleccalc  -Kfull_correlation/il_S1_summaryleccalc -F -S -s -M -m -O output/full_correlation/il_S1_ept.csv & lpid5=$!
aalcalc -Kfull_correlation/gul_S1_summaryaalcalc > output/full_correlation/gul_S1_aalcalc.csv & lpid6=$!
wait $lpid1 $lpid2 $lpid3 $lpid4 $lpid5 $lpid6

rm -R -f work/*
rm -R -f /tmp/%FIFO_DIR%/
