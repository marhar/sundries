package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
)

/*
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
*/

var (
	hasMerge = regexp.MustCompile("(?m)^<<<<<<< ")
)

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func patch(theirs string, yours string, filename string, contents []byte) {
	fmt.Println("patch")
}

func main() {
	pid := os.Getpid()
	theirs := "/tmp/vfix." + strconv.Itoa(pid) + ".THEIRS"
	yours := "/tmp/vfix." + strconv.Itoa(pid) + ".YOURS"

	_ = os.RemoveAll(theirs)
	_ = os.RemoveAll(yours)
	err := os.Mkdir(theirs, 0755)
	check(err)
	err = os.Mkdir(yours, 0755)
	check(err)

	defer func() {
		_ = os.RemoveAll(theirs)
		_ = os.RemoveAll(yours)
	}()

	filenames, err := filepath.Glob("*")
	check(err)

	for _, filename := range filenames {
		info, err := os.Stat(filename)
		if info.IsDir() {
			continue
		}
		fmt.Println(filename)
		contents, err := os.ReadFile(filename)
		check(err)

		if hasMerge.FindIndex([]byte(contents)) != nil {
			patch(theirs, yours, filename, contents)
		}
		/*
			if hasMerge.FindIndex(contents) != nil {
				fmt.Println("HAS", file)
			}
		*/
	}
}
