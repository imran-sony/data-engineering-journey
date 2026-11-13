cd ~/de-bootcamp/ostad-de-bootcamp-main

pwd

wc -l module-01/data/orders_oct2026.csv

wc -l module-01/data/app_2026-10.log

grep -c "| WARN" module-01/data/app_2026-10.log

grep -c "DEBUG" module-01/data/app_2026-10.log

grep "^2026-10-10" module-01/data/app_2026-10.log | grep -c "| ERROR |"

grep "| WARN" module-01/data/app_2026-10.log | cut -c1-10 | uniq -c | sort -rn

grep -c "bKash" module-01/data/orders_oct2026.csv

grep "| ERROR |" module-01/data/app_2026-10.log | grep -c "auth"

grep "| ERROR |" module-01/data/app_2026-10.log | cut -c1-10 | uniq -c | sort -n
