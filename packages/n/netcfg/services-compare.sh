cat services | egrep -v "^#" | sed "s:#.*::" | sed "s:^\([^ \t]\+\)[ \t]\+\([^ \t]\+\)[ \t]*$:\1 \2:g" | sort > services.stripped
cat services.new | egrep -v "^#" | sed "s:#.*::" | sed "s:^\([^ \t]\+\)[ \t]\+\([^ \t]\+\)[ \y]*$:\1 \2:g" | sort > services.new.stripped
diff -u services.stripped services.new.stripped | egrep "^[+-]"
rm services.stripped services.new.stripped
