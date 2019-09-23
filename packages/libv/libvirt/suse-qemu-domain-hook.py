#!/usr/bin/python3
# libvirt hook script for QEMU/KVM domains. See the libvirt hooks
# documenation for more details
#
#  https://www.libvirt.org/hooks.html
#
# Currently this hook looks for domains with <metadata> containing
# configuration for dmmd <disk> devices.  All <metadata> sub-elements
# must have a matching <disk> under <devices>. Those without a matching
# <disk> will be ignored.
#
# The dmmd device syntax is similar to Xen's block-dmmd. E.g.
#   md;/dev/md0(/etc/mdadm/mdadm.conf);lvm;/dev/vg/lv
#
# Device pairs (type;dev) are processed in order. The last device
# should match a <source dev=> attribute of a <disk>. The following
# configuration illustrates a domain with two dmmd devices
#
# <domain>
#   ...
#   <metadata>
#     <hook:dmmd xmlns:hook='https://libvirt.org/schemas/domain/hooks/1.0'>
#       <disk>md;/dev/md0(/etc/mdadm.conf);lvm;/dev/vg1/lv1</disk>
#       <disk>md;/dev/md1(/etc/mdadm.conf);lvm;/dev/vg1/lv2</disk>
#     </hook:dmmd>
#   </metadata>
#   <devices>
#     ...
#     <disk type='block' device='disk'>
#       <driver name='qemu' type='raw'/>
#       <source dev='/dev/vg1/lv1'/>
#       <target dev='vdb' bus='virtio'/>
#     </disk>
#     <disk type='block' device='disk'>
#       <driver name='qemu' type='raw'/>
#       <source dev='/dev/vg1/lv2'/>
#       <target dev='vdc' bus='virtio'/>
#     </disk>
#   </devices>
# </domain>
#
#
#  md devices can optionally:
#   specify a config file through:
#      md;/dev/md100(/var/opt/config/mdadm.conf)
#   use an array name (mdadm -N option):
#      md;My-MD-name;lvm;/dev/vg1/lv1

import os
import sys
import time
import subprocess
from lxml import etree
from subprocess import check_output
from subprocess import CalledProcessError

COMMAND_TIMEOUT = 60
MDADM_BIN = "/sbin/mdadm"
PVSCAN_BIN = "/sbin/pvscan"
LVCHANGE_BIN = "/sbin/lvchange"
HOOK_NAMESPACE = "https://libvirt.org/schemas/domain/hooks/1.0"
HOOK_NS_TAG = "{%s}" % HOOK_NAMESPACE

DEBUG = False

def write_debug(msg):
    if DEBUG:
        with open("/var/log/libvirt/qemu/suse-qemu-hook-output.log", "a") as f:
            f.write(msg + "\n")


def run_cmd(cmd):
    cmd_output = ""
    rc = 0

    msg = ""
    for m in cmd:
        msg += m + " "
    write_debug("run_cmd executing: " + msg)
        
    try:
        cmd_output = check_output(cmd, stderr=subprocess.STDOUT)
    except CalledProcessError as err:
        write_debug("run_cmd: caught CalledProcessError with output: " + err.output)
        rc = err.returncode

    if rc != 0:
       write_debug("run_cmd failed: " + msg)

    return [rc, cmd_output]


def prepare_md(dev):
    conf = []
    mdadmopts = []
    devpath = ""
    startcfg = dev.find("(")

    # check if MD config specifies a conf file for mdadm
    if startcfg != -1:
        endcfg = dev.find(")")
        conf = ["-c"]
        conf.append(dev[startcfg + 1:endcfg])
        dev = dev[:startcfg]

    # check if MD config contains a device or array name
    if not dev.startswith("/"):
        mdadmopts = ["-s"]
        mdadmopts.append("-N")
        devpath = "/dev/md/" + dev
    else:
        devpath = dev

    # check if MD device is already active
    cmd = [MDADM_BIN, "-Q"]
    cmd.append(devpath)
    write_debug("prepare_md: calling mdadm -Q for device " + devpath)
    ret, cmd_output = run_cmd(cmd)
    if ret == 0:
        write_debug("prepare_md: mdadm -Q succeeded for device " + devpath + ". Already activated")
        return 0

    cmd = [MDADM_BIN, "-A"]
    cmd.extend(mdadmopts)
    cmd.extend(conf)
    cmd.append(devpath)

    write_debug("prepare_md: calling mdadm -A for device " + devpath)
    ret, cmd_output = run_cmd(cmd)

    if ret != 0:
        write_debug("prepare_md: mdadm -A failed for device " + devpath)
    else:
        write_debug("prepare_md: mdadm -A succeeded for device " + devpath)
    return ret


def release_md(dev):
    conf = []
    devpath = ""
    startcfg = dev.find("(")

    if startcfg != -1:
        endcfg = dev.find(")")
        conf = ["-c"]
        conf.append(dev[startcfg + 1:endcfg])
        dev = dev[:startcfg]

    # check if MD config contains a device or array name. For
    # querying and deactivating a device name is required
    if not dev.startswith("/"):
        devpath = "/dev/md/" + dev
    else:
        devpath = dev

    # check if device exists
    cmd = [MDADM_BIN, "-Q"]
    cmd.extend(conf)
    cmd.append(devpath)

    write_debug("release_md: calling mdadm -Q for device " + devpath)
    ret, cmd_output = run_cmd(cmd)
    if ret != 0:
        write_debug("release_md: mdadm -Q failed for device " + devpath + ". Already deactivated")
        return 0

    cmd = [MDADM_BIN, "-S"]
    cmd.extend(conf)
    cmd.append(devpath)
    write_debug("release_md: calling mdadm -S for device " + devpath)
    ret, cmd_output = run_cmd(cmd)
    if ret == 0:
        write_debug("release_md: mdadm -S succeeded for device " + devpath)
    else:
        write_debug("release_md: mdadm -S failed for device " + devpath)

    return ret


def prepare_lvm(dev):
    cmd = [LVCHANGE_BIN]
    cmd.append("-aey")
    cmd.append(dev)

    endtime = time.time() + COMMAND_TIMEOUT;
    while time.time() < endtime:
        # When using MD devices for LVM PV, it is best to rescan for PV and VG
        run_cmd([PVSCAN_BIN])
        ret, cmd_output = run_cmd(cmd)
        if ret == 0 and os.path.exists(dev):
            write_debug("prepare_lvm: lvchange -aey succeeded on device " + dev)
            return 0
        else:
            write_debug("prepare_lvm: lvchange -aey failed on device " + dev)
        time.sleep(0.1)

    write_debug("prepare_lvm: lvchange -aey never succeeded for device " + dev)
    return 1


def release_lvm(dev):
    # Nothing to do if the device doesn't exist or is already deactivated
    if not os.path.exists(dev):
        write_debug("release_lvm: dev " + dev + " does not exist. Nothing to do!")
        return 0

    cmd = [LVCHANGE_BIN]
    cmd.append("-aen")
    cmd.append(dev)

    endtime = time.time() + COMMAND_TIMEOUT;
    while time.time() < endtime:
        ret, cmd_output = run_cmd(cmd)
        if ret == 0:
            write_debug("release_lvm: lvchange -aen succeeded for device " + dev)
            return 0
        else:
            write_debug("release_lvm: lvchange -aen failed for device " + dev + ". Trying again...")
            
        time.sleep(0.1)

    write_debug("release_lvm: lvchange -aen never succeeded for device " + dev)
    return 1


def prepare_config(params):
    write_debug("prepare_config: called with params " + params)
    conf = params.split(";")
    i = 0

    while i < len(conf):
        t = conf[i]
        d = conf[i+1]
        write_debug("prepare_config: got t = " + t + " and d = " + d)
        if t == "md":
            if prepare_md(d):
                write_debug("prepare_config: failed to prepare MD device " + d)
                return 1
        if t == "lvm":
            if prepare_lvm(d):
                write_debug("prepare_config: failed to prepare LVM device " + d)
                return 1
        i += 2

    return 0


def release_config(params):
    write_debug("release_config: called with params " + params)
    conf = params.split(";")
    i = len(conf) - 1
    ret = 0

    # work backwards through the list when releasing, cleaning
    # up LVM first, then MD
    while i >= 0:
        t = conf[i-1]
        d = conf[i]
        write_debug("release_config: got t = " + t + " and d = " + d)
        if t == "md":
            if release_md(d):
                write_debug("release_config: failed to release MD device " + d)
                ret = 1
        if t == "lvm":
            if release_lvm(d):
                write_debug("release_config: failed to release LVM device " + d)
                ret = 1
        i -= 2

    return ret


if len(sys.argv) < 3:
    sys.exit(1)

exit_code = 0
disk_devs = []
phase = sys.argv[2]
vmxml = sys.stdin.read()

tree = etree.fromstring(vmxml.encode("utf-8", "ignore"))
devs = tree.xpath("/domain/devices/disk")
dmmd_configs = tree.xpath("/domain/metadata/hook:dmmd/disk", namespaces={'hook': HOOK_NAMESPACE})

if len(dmmd_configs) == 0:
    write_debug("No dmmd configurations found in <metadata>")
    sys.exit(0)

write_debug("got phase: " + phase)

# build a list of <disk type='block'> source device names to check against
# dmmd configurations
for d in devs:
    val = d.get("type")
    if val is None or val != "block":
        continue

    for child in d:
        if child.tag == "source":
            disk_devs.append(child.get("dev"))

# For each dmmd configuration in <metadata>, check there is a corresponding
# disk
for config in dmmd_configs:
    # check that a disk exists for this config. <disk> devices may have
    # been added or removed without a corresponding update to <metadata>
    index = config.text.rfind(";")
    if index == -1:
        continue

    disk = config.text[index + 1:]
    # remove config file specfied with '(/path/to/conf)'
    if disk.endswith(")"):
        index = disk.rfind("(")
        if index == -1:
            continue
        disk = disk[:index]

    if disk not in disk_devs:
        write_debug("Ignoring config '" + config.text + "' with no matching <disk> device")
        continue

    # TODO: check that migration can be handled by the 'prepare' phase on
    # destination and 'release' phase on source
    if phase == "prepare":
        exit_code = prepare_config(config.text)

    if phase == "release":
        exit_code = release_config(config.text)

sys.exit(exit_code)
