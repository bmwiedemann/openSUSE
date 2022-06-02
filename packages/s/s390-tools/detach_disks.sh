#!/bin/sh

DASDFILE=/tmp/dasd.list.$(mcookie)
DETFILE=/tmp/detach.disks.$(mcookie)
KEEPFILE=/tmp/keep.disks.$(mcookie)
NICFILE=/tmp/nic.list.$(mcookie)
FAILFILE=/tmp/error.$(mcookie)

function expand_RANGE(){
local RANGE=${1}
local RANGE_SAVE=${RANGE}
local DEVNO
local BEGIN=0
local END=0

RANGE=$(IFS=":-"; echo ${RANGE} | cut -f1-2 -d" " )
set -- ${RANGE}
let BEGIN=0x$1 2>/dev/null
let END=0x$2 2>/dev/null

if [ ${BEGIN} -eq 0 ] || [ ${END} -eq 0 ]; then
  ${msg} "An invalid device number range was specified: ${RANGE_SAVE}" >&2
  touch ${FAILFILE}
  return
fi

for DEVNO in $(eval echo {${BEGIN}..${END}})
  do printf "%d\n"  ${DEVNO}
  done
}

function usage(){
  echo "Usage: ${0} [ -F ] [ -q ] [ -h ]"
  echo "        -F      Exit with failure if any invalid parms are detected."
  echo "        -q      Don't generate any output."
  echo "        -h      Display this help message."
}

msg="echo"
let FORCE_FAIL=0

############################################################
# Parse the parameters from the command line
#
ARGS=$(getopt -a --options Fhq -n "detach_devices" -- "$@")
if [ $? -ne 0 ]; then
  usage
  exit 3
fi

eval set -- "${ARGS}"
for ARG; do
        case "${ARG}" in
                -F) let FORCE_FAIL=1
                    shift 1
                    ;;
                -h) usage;
                    exit 0
                    ;;
                -q) msg="/bin/true"
                    shift 1
                    ;;
                --) shift 1
                    ;;
                *) ${msg} "Extraneous input detected: ${1}"
                   shift 1
                   ;;
        esac
done

if [ -r /etc/sysconfig/virtsetup ]; then
  . /etc/sysconfig/virtsetup
else ${msg} "No /etc/sysconfig/virtsetup file was found."
     exit 1
fi

# First, get a list of all the DASD devices we have for this guest, in decimal.
# (Trying to handle things in hex gets complicated.)
/usr/sbin/vmcp -b1048576 q v dasd | cut -f2 -d" "  |\
  while read HEXNO
    do let DECNO=0x${HEXNO}
       echo ${DECNO}
    done > ${DASDFILE} 2>/dev/null

# If the system administrator specified certain devices to be detached
# let's put those device numbers in a file, one per line.
touch ${DETFILE}
for ADDR in $(IFS=", " ; echo ${ZVM_DISKS_TO_DETACH})
  do if $(echo ${ADDR} | grep -iqE ":|-" 2>/dev/null)
       then expand_RANGE ${ADDR} >> ${DETFILE}
       else let DEVNO=0
            let DEVNO=0x${ADDR} 2>/dev/null
            if [ ${DEVNO} -eq 0 ]; then
              ${msg} "An invalid device number was specified: ${ADDR}" >&2
              touch ${FAILFILE}
            else printf "%d\n" ${DEVNO}
            fi
     fi
  done > ${DETFILE}

# If the system administrator specified certain devices that should _not_
# be detached, let's put those in another file, one per line.
touch ${KEEPFILE}
for ADDR in $(IFS=", " ; echo ${ZVM_DISKS_TO_NOT_DETACH})
  do if $(echo ${ADDR} | grep -iqE ":|-" 2>/dev/null)
       then expand_RANGE ${ADDR} >> ${KEEPFILE}
       else let DEVNO=0
            let DEVNO=0x${ADDR} 2>/dev/null
            if [ ${DEVNO} -eq 0 ]; then
              ${msg} "An invalid device number was specified: ${ADDR}" >&2
              touch ${FAILFILE}
            else printf "%d\n" ${DEVNO}
            fi
     fi
  done > ${KEEPFILE}

if [ ${FORCE_FAIL} -eq 1 ] && [ -e ${FAILFILE} ]; then
  let RETURN_CODE=1
  ${msg} "Terminating detach_disk because of input errors."
else 
# If the system administrator specified that all "unused" disks should be
# detached, compare the disks lsdasd show as activated to the complete
# list of disks we have currently, and add the inactive ones to the
# file containing devices to be detached
     if [ "${ZVM_DETACH_ALL_UNUSED}" == "yes" ]; then
       lsdasd -s | sed -e 1,2d | cut -f1 -d" " | \
         while read ADDR
           do let DEVNO=0x${ADDR}
              sed -i -e "/^${DEVNO}$/d" ${DASDFILE}
          done
       cat ${DASDFILE} >> ${DETFILE}
     fi

# Now remove any "to be kept" disks from the detach file
     while read DEVNO
       do sed -i -e "/^${DEVNO}/d" ${DETFILE}
       done < ${KEEPFILE}

# Get a list of all the virtual NICs since they require an
# extra keyword to detach. Contrary to what we've done before
# these will be hex values
     /usr/sbin/vmcp -b1048576 q nic | grep Adapter | cut -f2 -d" "  | cut -f1 -d. > ${NICFILE}

# Now we sort the device numbers and detach them.
     sort -un ${DETFILE} | \
       while read DEVNO
         do HEXNO=$(printf %04X ${DEVNO})
            if grep -q ^${HEXNO}$ ${NICFILE} 2>/dev/null ; then
              vmcp detach nic ${HEXNO} 2>/dev/null
            else vmcp detach ${HEXNO} 2>/dev/null
            fi
         done
     let RETURN_CODE=0 
fi

rm -f ${DASDFILE} ${DETFILE} ${KEEPFILE} ${NICFILE} ${FAILFILE}
exit ${RETURN_CODE}
