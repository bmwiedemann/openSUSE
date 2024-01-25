#!/bin/sh
# Configure warewulf with the primary network of the host
WW4CONF=/etc/warewulf/warewulf.conf

# Get the mask from prefix
cdr2mask()
{
   # Number of args to shift, 255..255, first non-255 byte, zeroes
   set -- $(( 5 - ($1 / 8) )) 255 255 255 255 $(( (255 << (8 - ($1 % 8))) & 255 )) 0 0 0
   [ $1 -gt 1 ] && shift $1 || shift
   echo ${1-0}.${2-0}.${3-0}.${4-0}
}

# Get the ip4 address of the netork
network_address() {
    declare address prefix_length
    IFS=/ read address prefix_length <<< "$1"

    declare -a octets
    IFS=. read -a octets <<< "$address"

    declare mask
    mask=$( printf "%08x" $(( (1 << 32) - (1 << (32 - prefix_length)) )) )

    declare -i i
    for i in {0..3}; do octets[$i]=$(( octets[i] & 16#${mask:2*i:2} )); done

    echo $( IFS=.; echo "${octets[*]}" )
}
# Check if last Octed is in range
function is_ip_in_range() {
  # split the ip addresses into their octets.
  local ip_start_octets=($(echo $DYNSTART | tr "." " "))
  local ip_end_octets=($(echo $DYNEND | tr "." " "))
  local ip_address_octets=($(echo $1 | tr "." " "))

  # compare the octets one at a time to see if the ip address is within the range.
    if [[ ${ip_address_octets[3]} -lt ${ip_start_octets[3]} || ${ip_address_octets[3]} -gt ${ip_end_octets[3]} ]]; then
      return 1
    fi 
  # if we reach this point, the ip address is in the range.
  return 0
}

echo "-- WW4 CONFIGURAION $* --"

# Make sure that a ip address was defined for out network so that 
# we can configure dhcpd correctly
IP4CIDR=`ip addr | awk '/scope global/ {print $2;exit}'`
IP4=${IP4CIDR%/*}
IP4PREFIX=${IP4CIDR#*/}
IP4MASK=$(cdr2mask $IP4PREFIX)
IP4NET=$(network_address "$IP4/$IP4PREFIX")

if [ "$IP4PREFIX" -gt 25 ] ; then
  echo "ERROR: warewulf does at least a /25 network for dynamic addresses"
  cat << EOF
ipaddr: $IP4
netmask: $IP4MASK
network: $IP4NET
  range start: $DYNSTART
  range end: $DYNEND
EOF
  exit 0
fi

DYNSIZE=20
DYNSTART=${IP4#*.*.*.}
DYNSTART=$(( $DYNSTART + 2))
DYNPRE=${IP4%.*}
DYNEND=$(( $DYNSTART + $DYNSIZE + 1 ))
if [ $DYNEND -gt 254 ] ; then
  DYNEND=$(( $IPNET + 2 + $DYNSIZE ))
  DYNSTART=$(( $IPNET + 2 ))
fi
DYNSTART="${DYNPRE}.${DYNSTART}"
DYNEND="${DYNPRE}.${DYNEND}"

if is_ip_in_range $IP4 ; then
   echo "ERROR: ip address is in range for dynamic address, please set this manually"
   exit 0
fi


if [ -e $WW4CONF ] ; then
  test -n $IP4 && sed -i 's/^ipaddr:.*/ipaddr: '$IP4'/' $WW4CONF
  test -n $IP4MASK && sed -i 's/^netmask:.*/netmask: '$IP4MASK'/' $WW4CONF
  test -n $IP4NET && sed -i 's/^network:.*/network: '$IP4NET'/' $WW4CONF 
  test -n $DYNSTART && sed -i 's/^  range start:.*/  range start: '$DYNSTART'/' $WW4CONF 
  test -n $DYNEND && sed -i 's/^  range end:.*/  range end: '$DYNEND'/' $WW4CONF 
  cat << EOF
ipaddr: $IP4
netmask: $IP4MASK
network: $IP4NET
  range start: $DYNSTART
  range end: $DYNEND
EOF
fi

