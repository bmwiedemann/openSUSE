#! /bin/sh

echo -e "\nPreparing data...\n"
bzcat $1 >book.pgn
#head -30000 book.pgn >smallbook.pgn
echo -e "\nDone."

#echo -e "\nGenerating smallbook...\n"
#src/gnuchess <<EOF
#book add smallbook.pgn
#quit
#EOF
#mv book.dat smallbook.dat
#echo -e "\nDone.\n"

echo -e "\nGenerating book...\n"
expect <<EOF
set timeout 360
spawn src/gnuchess
expect "White" { send "book add book.pgn\n" }
expect "all done!" { send "quit\n" }
EOF
mv -v book.bin src/book.bin
echo -e "\nDone.\n"

echo "Books are ready!"
