#!/bin/bash
set -e
prov_req_name="ocamlfind"
td=`mktemp --directory`

test -n "${td}"
_x() {
 rm -rf "${td}"
}
trap _x EXIT

cmd=
test "$1" = "-prov" && cmd=prov
test "$1" = "-req"  && cmd=req
do_work() {
  local f=$1
  local pkg_name
  local pkg_prov_req
  local pkg_prov
  local pkg_req
  local elem req
  pkg_name="${f##*/}"
  if test "${pkg_name}" = "META"
  then
    pkg_name="${f%/*}"
    pkg_name="${pkg_name##*/}"
  else
    pkg_name="${pkg_name#META.}"
  fi
  pkg_prov_req="`
    env \
      pkg_name="${pkg_name}" \
      cmd="${cmd}" \
    awk '
      BEGIN {
        dbg=0;
        count=1;
        depth=0;
        pkg_name=ENVIRON["pkg_name"];
        cmd=ENVIRON["cmd"];
        
        if(dbg) printf "bEGIN \\"%s\\" cmd: %s\n", pkg_name, cmd > "/dev/stderr" ;
        requires[pkg_name]=""
        ppx_runtime_deps[pkg_name]=""
        pkg_names[depth]=pkg_name
      }
      
      {
        if(dbg) printf "line: %s\n", $0  > "/dev/stderr"
      }
      
      /^[[:blank:]]*directory[[:blank:]]*=/ {
        if(dbg) printf "GOT: %s\n", $0 > "/dev/stderr" ;
        if (depth == 0) {
          x = split($0, a, "\\"");
          if ( a[2] ) {
            candidate = a[2];
            if(dbg) printf "dir: %s %s\n", x, candidate > "/dev/stderr" ;
            if (candidate ~ /^\^/) {
              next
            }
            if (candidate ~ /^\+/) {
              candidate = substr(candidate, 2);
            }
            if (candidate ~ /^\//) {
              x = split(candidate, a, "/");
              if ( x )
                candidate = a[x];
            }
            if (candidate ~ /^\.\.\//) {
              x = split(candidate, a, "/");
              if ( x )
                candidate = a[x];
            }
            if(dbg) printf "dir: %s %s\n", x, candidate > "/dev/stderr" ;
            if (candidate != pkg_name) {
              requires[candidate] = requires[pkg_name];
              delete requires[pkg_name];
              pkg_name = candidate;
              if(dbg) printf "new pkg_name %s %s\n", x, pkg_name > "/dev/stderr" ;
              pkg_names[depth]=pkg_name
            } else {
              if(dbg) printf "pkg_name remains %s\n", pkg_name > "/dev/stderr" ;
            }
          }
        }
        next
      }

      /^[[:blank:]]*requires(|\([^-][^)]+\))[[:blank:]]*(+=|=)/ {
        if(dbg) printf "GOT: %s\n", $0 > "/dev/stderr" ;
        done=0
        requires_line = ""
        do {
          need_next_line = 1
          line = $0
          requires_line = sprintf("%s%s", requires_line, line)
          l = length(requires_line)
          qm = index(requires_line, "\\"")
          if (l > qm) {
            line = substr(requires_line, qm + 1)
            qm = index(line, "\\"")
            need_next_line = qm == 0
          }

          if (need_next_line) {
            done = getline == 0
          } else {
            done = 1
          }
        } while (done == 0)

        x = split(requires_line, a, "\\"");
        if ( a[2] ) {
          if(dbg) printf "req2 %s %s\n", x, a[2] > "/dev/stderr" ;
          x = gsub("[[:blank:]]+", ",", a[2]);
          if(dbg) printf "req2 %s %s\n", x, a[2] > "/dev/stderr" ;
          if (requires[pkg_name] == "") {
            requires[pkg_name] = a[2]
          } else {
            requires[pkg_name] = sprintf("%s,%s", requires[pkg_name],a[2])
          }
        }
        next
      }

      /^[[:blank:]]*ppx_runtime_deps[[:blank:]]*(+=|=)/ {
        if(dbg) printf "GOT: %s\n", $0 > "/dev/stderr" ;
        done=0
        ppx_runtime_deps_line = ""
        do {
          need_next_line = 1
          line = $0
          ppx_runtime_deps_line = sprintf("%s%s", ppx_runtime_deps_line, line)
          l = length(ppx_runtime_deps_line)
          qm = index(ppx_runtime_deps_line, "\\"")
          if (l > qm) {
            line = substr(ppx_runtime_deps_line, qm + 1)
            qm = index(line, "\\"")
            need_next_line = qm == 0
          }

          if (need_next_line) {
            done = getline == 0
          } else {
            done = 1
          }
        } while (done == 0)

        x = split(ppx_runtime_deps_line, a, "\\"");
        if ( a[2] ) {
          if(dbg) printf "req2 %s %s\n", x, a[2] > "/dev/stderr" ;
          x = gsub("[[:blank:]]+", ",", a[2]);
          if(dbg) printf "req2 %s %s\n", x, a[2] > "/dev/stderr" ;
          if (ppx_runtime_deps[pkg_name] == "") {
            ppx_runtime_deps[pkg_name] = a[2]
          } else {
            requires[pkg_name] = sprintf("%s,%s", requires[pkg_name],a[2])
          }
        }
        next
      }
      
      /^[[:blank:]]*package[[:blank:]]/ {
        if(dbg) printf "GOT: %s\n", $0 > "/dev/stderr" ;
        depth = depth + 1;
        if(dbg) printf "depth %s\n", depth > "/dev/stderr" ;
        x = split($0, a, "\\"");
        if ( a[2] ) {
          if(dbg) printf "req2 %s %s\n", x, a[2] > "/dev/stderr" ;
          pkg_name = pkg_name"."a[2];
          requires[pkg_name]=""
          pkg_names[depth]=pkg_name
          if(dbg) printf "new pkg_name %s %s\n", x, pkg_name > "/dev/stderr" ;
        }
        next
      }
      
      /^[[:blank:]]*)/ {
        if(dbg) printf "GOT: %s\n", $0 > "/dev/stderr" ;
        depth = depth -1;
        if(dbg) printf "depth %s\n", depth > "/dev/stderr" ;
        pkg_name=pkg_names[depth]
        if(dbg) printf "old pkg_name %s %s\n", x, pkg_name > "/dev/stderr" ;
        next
      }
      
      END {
        if(dbg) printf "eND \\"%s\\"\n", pkg_name > "/dev/stderr" ;
        for (req in requires) {
          if(dbg)printf "eNd \\"%s\\"\n", req > "/dev/stderr";
          # format: provides:requires
          printf "%s:%s\n", req, requires[req];
        }
        for (req in ppx_runtime_deps) {
          if(dbg)printf "eNd \\"%s\\"\n", req > "/dev/stderr";
          # format: provides:requires
          printf "%s:%s\n", req, ppx_runtime_deps[req];
        }
        if(dbg) printf "ENd \\"%s\\"\n", pkg_name > "/dev/stderr" ;
      }
    ' \"${f}\"
  `"
  for elem in ${pkg_prov_req}
  do
    pkg_prov="${elem%%:*}"
    pkg_req="${elem#*:}"
    pkg_req="${pkg_req//,/ }"
    if test -n "${pkg_prov}" && test "${cmd}" = "prov"
    then
      echo "${prov_req_name}($pkg_prov)"
    fi
    if test "${cmd}" = "req"
    then
      for i in ${pkg_req}
      do
        echo "${prov_req_name}(${i})"
      done
    fi
  done
}
while read filename
do
  case "${filename}" in
    */META*) do_work "${filename}" ;;
    *) ;;
  esac
done
# vim: tw=666 ts=2 shiftwidth=2 et
