#!/bin/sh
cd ~/.themes
for d in $(ls -1A); do if [ ! -f $d/metadata.json ]; then echo -n '{"last-edited": 1573734795}' > $d/metadata.json; fi ; done
