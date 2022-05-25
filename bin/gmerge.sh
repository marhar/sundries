#!/bin/bash

THEIRS=/tmp/gmerge.$$.THEIRS
YOURS=/tmp/gmerge.$$.YOURS
trap 'rm -rf $THEIRS $YOURS' 0

rm -rf $THEIRS $YOURS
mkdir  $THEIRS $YOURS

for i in $(grep -l '<<<<<<<' "$@"); do
    awk '
    BEGIN                               { state = "in_both" }
    state == "in_both" &&   /^<<<<<<< / { state = "in_first";  next }
    state == "in_first" &&  /^=======/  { state = "in_second"; next }
    state == "in_second" && /^>>>>>>> / { state = "in_both"  ; next }
    { if (state == "in_both" || state == "in_first") print }
    ' <"$i" >"$THEIRS/$i"
    awk '
    BEGIN                               { state = "in_both" }
    state == "in_both" &&   /^<<<<<<< / { state = "in_first";  next }
    state == "in_first" &&  /^=======/  { state = "in_second"; next }
    state == "in_second" && /^>>>>>>> / { state = "in_both"  ; next }
    { if (state == "in_both" || state == "in_second") print }
    ' <"$i" >"$YOURS/$i"
done

meld --auto-compare -output=. $THEIRS . $YOURS

