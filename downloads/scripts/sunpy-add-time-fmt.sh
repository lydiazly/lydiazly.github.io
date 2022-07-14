#!/bin/bash
# ~/lib
# Add time format to .../lib/pythonX.X/site-packages/sunpy/time/time.py
# 2018-07-11 written by Lydia
# 2018-07-11 modified by Lydia

# User defined
timefmt='%Y-%m-%dT%H:%M:%SZ'
timecmt='Example 2007-05-04T21:08:12Z'

fname=$(dirname $(python -c 'import sunpy.time; print(sunpy.time.__file__)'))/time.py
addstr='    "'"${timefmt}"'",      # '"${timecmt}"
if [ -f ${fname} ] && ! grep -q '"'"${timefmt}"'"' ${fname}; then
    sed -i '/TIME_FORMAT_LIST = /a\'"${addstr}" ${fname}
    echo -e "Added this format to\n${fname}:\n"
else
    echo -e 'Already have this format:\n'
fi
grep --color '"'"${timefmt}"'"' ${fname}
echo -e '\n=== Done!('$(basename $0)') ==='
exit 0
