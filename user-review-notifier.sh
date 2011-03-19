#!/bin/sh
dir="/home/yasulab/user-review-notifier/"
package="org.sorarier.whistle"
mail="yasulab@gmail.com"

python ${dir}user-review-getter.py ${package} > ${dir}latest.data
diff ${dir}latest.data ${dir}last.data > ${dir}diff.data
mv ${dir}latest.data ${dir}last.data
python ${dir}sendmail.py ${dir}diff.data ${mail}
