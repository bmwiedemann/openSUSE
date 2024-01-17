#!/bin/bash
# Script to fix the crc of openldap slapd.d ldifs.

do_update_crc () {
    if [ -z ${1} ]; then
        echo "Invalid call to do_update_crc() - no filename provided"
        exit 1
    fi
    
    tgt_ldif=$1
    
    if [ ! -f "${tgt_ldif}" ]; then
        echo "invalid call to do_update_crc() - file ${tgt_ldif} does not exist?"
        exit 1
    fi
    
    rm -f "${tgt_ldif}.crcbak"
    mv "${tgt_ldif}" "${tgt_ldif}.crcbak"
    
    /usr/bin/awk '
BEGIN {
    # CRC-32 ZIP polynomial in reversed bit order.
    POLY = 0xedb88320

    # 8-bit character -> ordinal table.
    for (i = 0; i < 256; i++)
        ORD[sprintf("%c", i)] = i
}

{
    # Remember each input line.
    input[NR] = $0

    # Verify the file header.
    if (NR == 1 && $0 != "# AUTO-GENERATED FILE - DO NOT EDIT!! Use ldapmodify.")
        exit 1
    if (NR == 2 && $0 !~ /# CRC32 ......../)
        exit 1
}

# Calculate CRC-32.
function crc32(crc, string,    i, j, c) {
    crc = and(compl(crc), 0xffffffff)
    for (i = 1; i <= length(string); i++) {
        c = substr(string, i, 1)
        crc = xor(crc, ORD[c])
        for (j = 0; j < 8; j++)
            crc = and(crc, 1) ? xor(rshift(crc, 1), POLY) : rshift(crc, 1)
    }
    crc = and(compl(crc), 0xffffffff)
    return crc
}

END {
    # Calculate CRC-32 of the file and update it in the header.
    crc = 0
    for (i = 3; i <= length(input); i++)
        crc = crc32(crc, input[i] "\n")
    input[2] = "# CRC32 " sprintf("%08x", crc)

    # Print the output.
    for (i = 1; i <= length(input); i++)
        print input[i]
}' "${tgt_ldif}.crcbak" > "${tgt_ldif}"

}

