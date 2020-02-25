#!/usr/bin/python3

#  Xen Mask Calculator - Calculate CPU masking information based on cpuid(1)
#  Copyright (C) 2017 Armando Vega
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import sys
import os


EAX1_MATCH = '0x00000001 0x00:'
EAX7_MATCH = '0x00000007 0x00:'
EXP_LINELN = 76

libxl_names_ecx1 = []
libxl_names_edx1 = []
libvirt_names_ecx1 = []
libvirt_names_edx1 = []

libxl_names_ebx7 = []
libxl_names_ecx7 = []
libvirt_names_ebx7 = []
libvirt_names_ecx7 = []

def fill_ecx1(bit, libxl, libvirt):
    if libxl_names_ecx1[bit]:
       print("ecx bit %s already set: libxl %s libvirt %s. Ignoring %s/%s\n" % (bit, libxl_names_ecx1[bit], libvirt_names_ecx1[bit], libxl, libvirt))
       return
    libxl_names_ecx1[bit] = libxl
    libvirt_names_ecx1[bit] = libvirt

def fill_edx1(bit, libxl, libvirt):
    if libxl_names_edx1[bit]:
       print("edx bit %s already set: libxl %s libvirt %s. Ignoring %s/%s\n" % (bit, libxl_names_edx1[bit], libvirt_names_edx1[bit], libxl, libvirt))
       return
    libxl_names_edx1[bit] = libxl
    libvirt_names_edx1[bit] = libvirt

def fill_ebx7(bit, libxl, libvirt):
    if libxl_names_ebx7[bit]:
       print("edx bit %s already set: libxl %s libvirt %s. Ignoring %s/%s\n" % (bit, libxl_names_ebx7[bit], libvirt_names_ebx7[bit], libxl, libvirt))
       return
    libxl_names_ebx7[bit] = libxl
    libvirt_names_ebx7[bit] = libvirt

def fill_ecx7(bit, libxl, libvirt):
    if libxl_names_ecx7[bit]:
       print("ecx bit %s already set: libxl %s libvirt %s. Ignoring %s/%s\n" % (bit, libxl_names_ecx7[bit], libvirt_names_ecx7[bit], libxl, libvirt))
       return
    libxl_names_ecx7[bit] = libxl
    libvirt_names_ecx7[bit] = libvirt

def fill_bit_names():
    for i in range(0,32):
        libxl_names_ecx1.append(None)
        libxl_names_edx1.append(None)
        libxl_names_ebx7.append(None)
        libxl_names_ecx7.append(None)
        libvirt_names_ecx1.append(None)
        libvirt_names_edx1.append(None)
        libvirt_names_ebx7.append(None)
        libvirt_names_ecx7.append(None)

    fill_ecx1(0, "sse3", "pni")
    fill_ecx1(1, "pclmulqdq", "pclmuldq")
    fill_ecx1(2, "dtes64", "dtes64")
    fill_ecx1(3, "monitor", "monitor")
    fill_ecx1(4, "dscpl", "ds_cpl")
    fill_ecx1(5, "vmx", "vmx")
    fill_ecx1(6, "smx", "smx")
    fill_ecx1(7, "est", "est")
    fill_ecx1(8, "tm2", "tm2")
    fill_ecx1(9, "ssse3", "ssse3")
    fill_ecx1(10, "cntxid", "cid")
    fill_ecx1(12, "fma", "fma")
    fill_ecx1(13, "cmpxchg16", "cx16")
    fill_ecx1(14, "xtpr", "xtpr")
    fill_ecx1(15, "pdcm", "pdcm")
    fill_ecx1(17, "pcid", "pcid")
    fill_ecx1(18, "dca", "dca")
    fill_ecx1(19, "sse4_1", "sse4.1")
    fill_ecx1(20, "sse4_2", "sse4.2")
    fill_ecx1(21, "x2apic", "x2apic")
    fill_ecx1(22, "movbe", "movbe")
    fill_ecx1(23, "popcnt", "popcnt")
    fill_ecx1(24, "tsc-deadline", "tsc-deadline")
    fill_ecx1(25, "aes", "aes")
    fill_ecx1(26, "xsave", "xsave")
    fill_ecx1(27, "osxsave", "osxsave")
    fill_ecx1(28, "avx", "avx")
    fill_ecx1(29, "f16c", "f16c")
    fill_ecx1(30, "rdrand", "rdrand")
    fill_ecx1(31, "hypervisor", "hypervisor")

    fill_edx1(0, "fpu", "fpu")
    fill_edx1(1, "vme", "vme")
    fill_edx1(2, "de", "de")
    fill_edx1(3, "pse", "pse")
    fill_edx1(4, "tsc", "tsc")
    fill_edx1(5, "msr", "msr")
    fill_edx1(6, "pae", "pae")
    fill_edx1(7, "mce", "mce")
    fill_edx1(8, "cmpxchg8", "cx8")
    fill_edx1(9, "apic", "apic")
    fill_edx1(11, "sysenter", "sep")
    fill_edx1(12, "mtrr", "mtrr")
    fill_edx1(13, "pge", "pge")
    fill_edx1(14, "mca", "mca")
    fill_edx1(15, "cmov", "cmov")
    fill_edx1(16, "pat", "pat")
    fill_edx1(17, "pse36", "pse36")
    fill_edx1(18, "psn", "pn")
    fill_edx1(19, "clfsh", "clflush")
    fill_edx1(21, "ds", "ds")
    fill_edx1(22, "acpi", "acpi")
    fill_edx1(23, "mmx", "mmx")
    fill_edx1(24, "fxsr", "fxsr")
    fill_edx1(25, "sse", "sse")
    fill_edx1(26, "sse2", "sse2")
    fill_edx1(27, "ss", "ss")
    fill_edx1(28, "htt", "ht")
    fill_edx1(29, "tm", "tm")
    fill_edx1(30, "ia64", "ia64")
    fill_edx1(31, "pbe", "pbe")

    fill_ebx7(0, "fsgsbase", "fsgsbase")
    fill_ebx7(1, "tsc_adjust", "tsc_adjust")
    fill_ebx7(3, "bmi1", "bmi1")
    fill_ebx7(4, "hle", "hle")
    fill_ebx7(5, "avx2", "avx2")
    fill_ebx7(7, "smep", "smep")
    fill_ebx7(8, "bmi2", "bmi2")
    fill_ebx7(9, "erms", "erms")
    fill_ebx7(10, "invpcid", "invpcid")
    fill_ebx7(11, "rtm", "rtm")
    fill_ebx7(12, "cmt", "cmt")
    fill_ebx7(14, "mpx", "mpx")
    fill_ebx7(16, "avx512f", "avx512f")
    fill_ebx7(17, "avx512dq", "avx512dq")
    fill_ebx7(18, "rdseed", "rdseed")
    fill_ebx7(19, "adx", "adx")
    fill_ebx7(20, "smap", "smap")
    fill_ebx7(21, "avx512-ifma", "avx512-ifma")
    fill_ebx7(23, "clflushopt", "clflushopt")
    fill_ebx7(24, "clwb", "clwb")
    fill_ebx7(26, "avx512pf", "avx512pf")
    fill_ebx7(27, "avx512er", "avx512er")
    fill_ebx7(28, "avx512cd", "avx512cd")
    fill_ebx7(29, "sha", "sha")
    fill_ebx7(30, "avx512bw", "avx512bw")
    fill_ebx7(31, "avx512vl", "avx512vl")

    fill_ecx7(0, "prefetchwt1", "prefetchwt1")
    fill_ecx7(1, "avx512-vbmi", "avx512-vbmi")
    fill_ecx7(2, "umip", "umip")
    fill_ecx7(3, "pku", "pku")
    fill_ecx7(4, "ospke", "ospke")
    fill_ecx7(6, "avx512-vbmi2", "avx512-vbmi2")
    fill_ecx7(8, "gfni", "gfni")
    fill_ecx7(9, "vaes", "vaes")
    fill_ecx7(10, "vpclmulqdq", "vpclmulqdq")
    fill_ecx7(11, "avx512-vnni", "avx512-vnni")
    fill_ecx7(12, "avx512-bitalg", "avx512-bitalg")
    fill_ecx7(14, "avx512-vpopcntdq", "avx512-vpopcntdq")
    fill_ecx7(22, "rdpid", "rdpid")
    fill_ecx7(25, "cldemote", "cldemote")


def get_register_mask(regs):
    """ Take a list of register values and return the calculated mask """
    reg_n = len(regs)
    mask = ''
    for idx in range(32):
        counter = 0
        for reg in regs:
            counter += 1 if (reg & (1 << idx) > 0) else 0
        # if we have all 1s or all 0s we don't mask the bit
        if counter == reg_n or counter == 0:
            mask = mask + 'x'
        else:
            mask = mask + '0'
    # we calculated the mask in reverse, so we reverse it again
    return mask[::-1]


def print_xl_masking_config(nodes):
    """ Take a dictionary of nodes containing their registers and print out CPUID masking configuration for xl """
    nomasking = 'x' * 32
    libxl = []
    libvirt = []
    eax1_ecx_regs = []
    eax1_edx_regs = []
    eax7_ebx_regs = []
    eax7_ecx_regs = []
    for node in nodes:
        eax1_ecx_regs.append(nodes[node]['eax1_ecx'])
        eax1_edx_regs.append(nodes[node]['eax1_edx'])
        eax7_ebx_regs.append(nodes[node]['eax7_ebx'])
        eax7_ecx_regs.append(nodes[node]['eax7_ecx'])
    # Get masks for the EAX1 and EAX7 registers
    eax1_ecx_mask = get_register_mask(eax1_ecx_regs)
    eax1_edx_mask = get_register_mask(eax1_edx_regs)
    eax7_ebx_mask = get_register_mask(eax7_ebx_regs)
    eax7_ecx_mask = get_register_mask(eax7_ecx_regs)
    # Build the xl CPUID config
    cpuid_config = 'cpuid = [\n    "0x00000001:ecx=' + eax1_ecx_mask
    if eax1_edx_mask != nomasking:
        cpuid_config += ',edx=' + eax1_edx_mask
    cpuid_config += '",\n'
    cpuid_config += '    "0x00000007,0x00:ebx=' + eax7_ebx_mask
    if eax7_ecx_mask != nomasking:
        cpuid_config += ',ecx=' + eax7_ecx_mask
    cpuid_config += '"\n'
    cpuid_config += ']'
    print(cpuid_config)

    bitnum = len(eax1_ecx_mask)
    while bitnum > 0:
       bitnum -= 1
       bitval = eax1_ecx_mask[len(eax1_ecx_mask) - 1 - bitnum]
       if bitval == "0" and libxl_names_ecx1[bitnum]:
           libxl.append(libxl_names_ecx1[bitnum] + "=0")
           libvirt.append(libvirt_names_ecx1[bitnum])

    bitnum = len(eax1_edx_mask)
    while bitnum > 0:
       bitnum -= 1
       bitval = eax1_edx_mask[len(eax1_edx_mask) - 1 - bitnum]
       if bitval == "0" and libxl_names_edx1[bitnum]:
           libxl.append(libxl_names_edx1[bitnum] + "=0")
           libvirt.append(libvirt_names_edx1[bitnum])

    bitnum = len(eax7_ebx_mask)
    while bitnum > 0:
       bitnum -= 1
       bitval = eax7_ebx_mask[len(eax7_ebx_mask) - 1 - bitnum]
       if bitval == "0" and libxl_names_ebx7[bitnum]:
           libxl.append(libxl_names_ebx7[bitnum] + "=0")
           libvirt.append(libvirt_names_ebx7[bitnum])

    bitnum = len(eax7_ecx_mask)
    while bitnum > 0:
       bitnum -= 1
       bitval = eax7_ecx_mask[len(eax7_ecx_mask) - 1 - bitnum]
       if bitval == "0" and libxl_names_ecx7[bitnum]:
           libxl.append(libxl_names_ecx7[bitnum] + "=0")
           libvirt.append(libvirt_names_ecx7[bitnum])

    if len(libxl) > 0:
       output = "cpuid = [ host"
       for i in libxl:
           output += "," + i
       output += " ]"
       print(output)

       print("<domain>")
       print("  <cpu>")
       for i in libvirt:
           print("    <feature policy='optional' name='%s' />" % i)
       print("  </cpu>")
       print("</domain>")


def print_verbose_masking_info(nodes):
    """ Take a dictionary of nodes containing their registers and print out verbose mask derivation information """
    eax1_ecx_regs = []
    eax1_edx_regs = []
    eax7_ebx_regs = []
    eax7_ecx_regs = []
    for node in nodes:
        eax1_ecx_regs.append(nodes[node]['eax1_ecx'])
        eax1_edx_regs.append(nodes[node]['eax1_edx'])
        eax7_ebx_regs.append(nodes[node]['eax7_ebx'])
        eax7_ecx_regs.append(nodes[node]['eax7_ecx'])

    print("")
    print('== Detailed mask derivation info ==')
    print("")

    print('EAX1 ECX registers:')
    for reg in eax1_ecx_regs:
        print('{0:032b}'.format(reg))
    print('================================')
    print(get_register_mask(eax1_ecx_regs))

    print("")
    print('EAX1 EDX registers:')
    for reg in eax1_edx_regs:
        print('{0:032b}'.format(reg))
    print('================================')
    print(get_register_mask(eax1_edx_regs))

    print("")
    print('EAX7,0 EBX registers:')
    for reg in eax7_ebx_regs:
        print('{0:032b}'.format(reg))
    print('================================')
    print(get_register_mask(eax7_ebx_regs))

    print("")
    print('EAX7,0 ECX registers:')
    for reg in eax7_ecx_regs:
        print('{0:032b}'.format(reg))
    print('================================')
    print(get_register_mask(eax7_ecx_regs))


if __name__ == '__main__':
    epilog = """The individual 'node_files' are generated with 'cpuid -1r':
    server1~$ cpuid -1r > node1
    server2~$ cpuid -1r > node2
    server3~$ cpuid -1r > node3

    ~$ {0} node1 node2 node3

    Use 'zypper install cpuid' to install the cpuid.rpm.

Note: Run 'cpuid' with NATIVE boot instead of dom0 to get the complete cpid value.
Xen hides some bits from dom0!
    """.format(sys.argv[0])
    parser = argparse.ArgumentParser(
             formatter_class=argparse.RawDescriptionHelpFormatter,
             description='A utility that calculates a XEN CPUID difference mask',
             epilog=epilog
             )
    parser.add_argument('node_files', nargs='*', help='Filenames of XEN node CPUID outputs')
    parser.add_argument('-v', '--verbose', action='store_true', help='Get detailed mask derivation information')
    args = parser.parse_args()
    if len(args.node_files) < 2:
        print('Need at least 2 files to do the comparison!')
        parser.print_help()
        sys.exit(1)
    
    fill_bit_names()
    nodes = dict()
    for node in args.node_files:
        if os.path.isfile(node):
            try:
                f = open(node)
            except IOError as e:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
                sys.exit(1)
            else:
                lines = [line.strip() for line in f]
                eax1 = ''
                eax7 = ''
                # try to match the lines containing interesting registers
                # EAX1 - Processor Info and Feature Bits
                # EAX7 - Extended features
                for line in lines:
                    if line.startswith(EAX1_MATCH):
                        eax1 = line
                    elif line.startswith(EAX7_MATCH):
                        eax7 = line
                # if we get garbled data we should probably just give up
                if len(eax1) < EXP_LINELN or len(eax7) < EXP_LINELN:
                    print('ERROR: invalid data format in file : ' + node)
                    sys.exit(1)

                # check if we can actually parse the strings into integers
                try:
                    eax1_ecx = int(eax1.split()[4].split('=')[1], 0)
                    eax1_edx = int(eax1.split()[5].split('=')[1], 0)
                    eax7_ebx = int(eax7.split()[3].split('=')[1], 0)
                    eax7_ecx = int(eax7.split()[4].split('=')[1], 0)
                except ValueError:
                    print('ERROR: invalid data format in file: ' + node)
                    sys.exit(1)

                nodes[node] = dict()
                nodes[node]['eax1_ecx'] = eax1_ecx
                nodes[node]['eax1_edx'] = eax1_edx
                nodes[node]['eax7_ebx'] = eax7_ebx
                nodes[node]['eax7_ecx'] = eax7_ecx
                f.close()
        else:
            print('File not found: ' + node)
            sys.exit(1)

    print_xl_masking_config(nodes)
    if args.verbose:
        print_verbose_masking_info(nodes)
