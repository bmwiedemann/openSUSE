#!/usr/bin/perl
########################################################################
#
# mkdump.pl - Preparing disks for use as S/390 dump device
#
# Copyright (c) 2011 Tim Hardeck, SUSE LINUX Products GmbH
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Based on mkdump.sh (c) 2004 Hannes Reinecke, SuSE AG
#
# License:
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
########################################################################

use strict;
use warnings;
use Fcntl;
use Getopt::Long;

my $VERSION = "2.0.3";

my $BLKID = "/sbin/blkid";
my $PARTED = "/usr/sbin/parted";
my $FDASD = "/sbin/fdasd";
my $DASDVIEW = "/sbin/dasdview";
my $DASDFMT = "/sbin/dasdfmt";
my $ZIPL = "/sbin/zipl";
my $UDEVADM = "/sbin/udevadm";
my $ZGETDUMP = "/sbin/zgetdump";

# temporary DASD device configuration file for Zipl
my $MDPATH = "/tmp/mvdump.conf.".`mcookie`;
# zFCP dump dir, without a leading '/'
my $ZFCP_DUMP_DIR = "mydumps";

my $OPT_DEBUG = 0;
my $OPT_FORCE = 0;
my $OPT_VERBOSE = 0;

sub cleanup
{
	# DASD
	if (-e $MDPATH) {
		system("rm -f $MDPATH");
	}
}

sub exit_with
{
	my $message = shift();
	my $exitcode = shift();
	
	print STDERR "$message Exiting...\n";
	cleanup();

	# fdasd isn't able to create volume label interactively
	# could be fixed with a reformat
	if ($exitcode == 65280) {
		$exitcode = 12;
	}
	
	# bigger exit codes are not supported
	if ($exitcode > 255) {
		$exitcode = 255;
	}
	
	exit($exitcode);
}

sub run_cmd
{
	my $cmd = shift();

	my $output = "";
	if (! $OPT_DEBUG) {
		my ($app) = $cmd =~ /\/(\w+) /;

		# run command
		$output = `$cmd`;
		my $exit_code = $?;
		# wait for udev to finish processing
		system("$UDEVADM settle");

		# only print output in case of an error or in verbose mode
		if ($output and ($exit_code != 0 or $OPT_VERBOSE)) {
			print("$output\n");
		}

		if ($exit_code != 0) {
			exit_with("$app failed with exit code $exit_code", $exit_code);
		}
	} else {
		# only print the command in debug mode
		print("\`$cmd\`\n");
	}
	return($output);
}

sub check_paths
{
	for my $path ($BLKID, $PARTED, $FDASD, $DASDVIEW, $DASDFMT, $ZIPL, $UDEVADM, $ZGETDUMP) {
		unless ( -x $path) {
			exit_with("Command $path is not available.", 13);
		}
	}
}

sub read_file
{
	my $path = shift();

	open(my $file, "<", "$path") or exit_with("Unable to access $path: $!.", 15);
	my @content = <$file>;
	close($file);

	# no need for arrays in case of single lines
	if (@content > 1) {
		return @content;
	} else {
		chomp($content[0]);
		return($content[0]);
	}
}

sub is_dasd
{
	# remove leading /dev/
	my $device = substr(shift(), 5);

	if (-r "/sys/block/$device/device/discipline") {
		return(1);
	} else {
		return(0);
	}
}

sub is_zfcp
{
	# remove leading /dev/
	my $device = substr(shift(), 5);
	my $devpath = "/sys/block/$device/device";

	unless (-r "$devpath/hba_id" or -r "$devpath/type") {
		return(0);
	}

	my $devtype = read_file("$devpath/type");

	# SCSI type '0' means disk
	if ($devtype == 0) {
		return(1);
	} else {
		return(0);
	}
}

sub get_partition_num
{
	# remove leading /dev/
	my $device = substr(shift, 5);
	
	my $part_num = grep(/\s+$device\d+/, read_file("/proc/partitions"));
	
	return($part_num);
}

sub print_device
{
	my $device = shift();
	my $only_dump_disks = shift();
	
	my $devpath = "/sys/block/" . substr($device, 5);
	my $output = $device;
	my $dump_device = 0;
	
	my $size = int(read_file("$devpath/size") / 2048);	# 512 Byte blocks
	# size can't be read this way in case of unformatted devices
	if ($size != 0) {
		$output .= "\t${size}MB";
	} else {
		$output .= "\tunknown";
	}

	if (is_dasd($device)) {
		my ($busid) = readlink("$devpath/device") =~ /(\w\.\w\.\w{4})/;
		$output .=  "\t$busid";

		# check for dump record and list multi volumes
		my $zgetdump_output = `$ZGETDUMP -d $device 2>&1`;
		my @dump_devs = $zgetdump_output =~ /(\w\.\w\.\w{4})/g;
		if (@dump_devs) {
			$dump_device = 1;
			$output .= "\tdumpdevice";
			# no need to output the dump ids for a single device
			if (@dump_devs > 1) {
				for my $id (@dump_devs) {
					$output .= "|$id";
				}
			}
		} else {
			# check for single volume dump devices
			if ($zgetdump_output =~ /Single-volume DASD dump tool/) {
				$dump_device = 1;
				$output .= "\tdumpdevice";
			}
		}
	} else {
		my $adapter = read_file("$devpath/device/hba_id");
		my $wwpn = read_file("$devpath/device/wwpn");
		my $lun = read_file("$devpath/device/fcp_lun");
		$output .= "\t$adapter\t$wwpn\t$lun";

		# check for dump record
		my $zgetdump = `$ZGETDUMP -d $device 2>&1`;
		if ($? == 0) {
			my ($dsize) = ($zgetdump =~ /Maximum dump size\.:\s+([0-9]+) MB/m);
			$dsize = $size unless (defined($dsize));
			$output = "$device\t${dsize}MB\t$adapter\t$wwpn\t$lun\tdumpdevice";
			$dump_device = 1;
		}
	}
	if ($only_dump_disks) {
		if ($dump_device) {
			print("$output\n");
		}
	} else {
		print("$output\n");
	}
}

sub list_free_disks
{
	my $devices_ref = shift();
	my $type = shift();

	if (@$devices_ref) {
		for my $device (@$devices_ref) {
			print_device($device);
		}
	} else {
		print STDERR "No free $type devices available!\n";
	}
}

sub list_dump_disks
{
	my @devices = @_;

	if (@devices) {
		for my $device (@devices) {
			print_device($device, 1);
		}
	} else {
		print STDERR "No dump devices available!\n";
	}
}

sub determine_free_disks
{
	my @dasd;
	my @zfcp;
	my @devices;
	
	# gather block devices
	my $path="/sys/block/";
	opendir(DIR, $path) or exit_with("Unable to find $path: $!", 15);
	while (defined(my $file = readdir(DIR))) {
		# no need to add other devices then dasd* or sd*
		if ($file =~ /^dasd[a-z]+$/ or $file =~ /^sd[a-z]+$/) {
			push(@devices, $file);
		}
	}
	closedir(DIR);

	for my $entry (@devices) {
		# only allow disks, no partitions
		my ($device) = $entry =~  /^([a-z]+)$/;
		next unless ($device);

		$device = "/dev/$device";

		# determine if the block device could be accessed exclusively
		if(-b $device and sysopen(my $blockdev, $device, O_RDWR|O_EXCL)) {
			close($blockdev);
			if (is_dasd($device)) {
				push(@dasd, $device);
			}
			if (is_zfcp($device)) {
				push(@zfcp, $device);
			}
		}
		# wait for udev to process all events triggered by sysopen(,O_EXCL)
		system("$UDEVADM settle");
	}

	return(\@dasd, \@zfcp);
}

sub prepare_dasd
{
	my @devices = @_;

	my $format_disks = "";

	# check formatting
	for my $device (@devices) {
		# determine  disk layout
		my ($fmtstr) = `$DASDVIEW -x $device`  =~ /(\w\w\w) formatted/;
		
		SWITCH:
		for($fmtstr) {
			if (/NOT/) {
				print("Unformatted disk, formatting $device.\n");
				$format_disks .= " $device";
				last SWITCH;
			}
			if (/LDL/) {
				if ($OPT_FORCE) {
					print("Linux disk layout, reformatting $device.\n");
					$format_disks .= " $device";
				} else {
					print("$device was formatted with the Linux disk layout.\n");
					print("Unable to use it without reformatting.\n");
					exit_with("Re-issue the mkdump command with the --force option.", 12);
				}
				last SWITCH;
			}
			if (/CDL/) {
				# allow reformatting  with force, since fdasd isn't able to create volume label interactively
				if ($OPT_FORCE) {
					print("Compatible disk layout, force reformatting $device.\n");
					$format_disks .= " $device";
				} else {
					print("$device: Compatible disk layout, Ok to use.\n");
				}
				last SWITCH;
			}
			exit_with("Unknown layout ($fmtstr), cannot use disk.", 11);
		}
	}

	# format devices
	if ($format_disks) {
		#up to eight devices in parallel
		run_cmd("$DASDFMT -P 8 -b 4096 -y -f $format_disks");
	}

	# check partitioning and partition
	for my $device (@devices) {
		my $part_num = get_partition_num($device);
		if ($part_num == 0 or $OPT_FORCE) {
			print("Re-partitioning disk $device.\n");
			run_cmd("$FDASD -a $device");
		} else {
			# allow disk with one partition if it don't consist a file system
			if ($part_num == 1) {
				my ($fstype) = `$BLKID ${device}1` =~ /TYPE=\"(\w+)\"/;
				if ($fstype) {
					exit_with("Device ${device}1 already contains a filesystem of type $fstype.", 12);
				}
			} else {
				exit_with("$part_num partitions detected, cannot use disk $device.", 12);
			}
		}
	}
}

sub setup_dasddump
{
	my @devices = @_;

	prepare_dasd(@devices);

	# create zipl device configuration file
	# don't create files in debug mode
	unless ($OPT_DEBUG) {
		open(my $file, ">", $MDPATH) or exit_with("Unable to access $MDPATH: $!.", 15);
		for my $device (@devices) {
			print{$file}("${device}1\n");
		}
		close($file);
	}

	print("Creating dump record.\n");
	run_cmd("${ZIPL} -V -n -M $MDPATH");

	cleanup();
}

sub setup_zfcpdump
{
	my $device = shift();

	# check partitioning
	my $part_num = get_partition_num($device);
	if ($part_num == 0 or $OPT_FORCE) {
		print("Re-partitioning disk $device.\n");
		run_cmd("$PARTED -s -- $device  mklabel gpt mkpart primary 0 -1");
	} else {
		if ($part_num > 1) {
			exit_with("$part_num partitions detected, cannot use disk $device.", 12);
		}
	}

	# install bootloader
	print("Creating dump record.\n");
	run_cmd("${ZIPL} -V -d ${device}1");

	cleanup();
}

sub print_version
{
	print << "EOF";
mkdump $VERSION

Copyright (c) 2011 SUSE LINUX Products GmbH
License GPLv2 or (at your option) any later version.
<http://www.gnu.org/licenses/gpl-2.0.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Tim Hardeck <thardeck\@suse.de>.
EOF
	exit(0);
}

sub print_usage
{
	my $exitcode = shift();
	
        print << "EOF";
Usage: mkdump [OPTIONS] [DEVICE]...
mkdump $VERSION

Prepare one or more volumes for use as S/390 dump device. Supported devices
are ECKD DASD and SCSI over zFCP disks, while multi-volumes are limited to DASD.

Only whole disks can be used, no partitions! If the device is incompatible
formatted/partioned, the script will refuse to install the dump record
unless the --force switch is given.

Disks which are in use or have mounted partitions will not be listed and can't be used.
The mentioning of "dumpdevice" after a disk indicates that it is an already usable dump device. Additionally multi-volume dump devices are indicated by the list of including DASD ids.

Options:
    -h, --help		display this help and exit
    -V, --version	display version information and exit

    -d, --debug		debug mode, do not run programs which commit changes
    -v, --verbose	be verbose and show command outputs
    -f, --force		force overwrite of the disk

    -l, --list-dump	display dump disks
    -D, --list-dasd	display usable DASD disks (Device, Size, ID, Dump)
    -Z, --list-zfcp	display usable SCSI over zFCP disks (Device, Size, ID, WWPN, LUN, Dump)

Report bugs on https://bugzilla.novell.com/
EOF

	exit($exitcode);
}

sub analyze_cmd_parameters
{
	#verbose, debug and force are global
	my $opt_help = 0;
	my $opt_version = 0;
	my $opt_dump = 0;
	my $opt_dasd = 0;
	my $opt_zfcp = 0;

	if (@ARGV == 0) {
		print_usage(14);
	}
	
	Getopt::Long::Configure('bundling');
	GetOptions(
		'h|help'	=> \$opt_help,
		'V|version'	=> \$opt_version,
		'd|debug'	=> \$OPT_DEBUG,
		'v|verbose'	=> \$OPT_VERBOSE,
		'f|force'	=> \$OPT_FORCE,
		'l|list-dump'	=> \$opt_dump,
		'D|list-dasd'	=> \$opt_dasd,
		'Z|list-zfcp'	=> \$opt_zfcp,
	) or print_usage(14);
	
	if ($opt_help) {
		print_usage(0);
	}

	if ($opt_version) {
		print_version();
	}

	# determine free dasd and zfcp devices
	my ($dasd_ref, $zfcp_ref) = determine_free_disks();

	if ($opt_dump) {
		list_dump_disks(@$dasd_ref, @$zfcp_ref);
		exit 0;
	}
	
	if ($opt_dasd) {
		list_free_disks(\@$dasd_ref, "dasd");
	}

	if ($opt_zfcp) {
		list_free_disks(\@$zfcp_ref, "zfcp");
	}

	# allow listing of both device types at the same time
	if ($opt_dasd or $opt_zfcp) {
		exit 0;
	}

	# check provided devices and be strict
	my @devices;
	for my $device (@ARGV) {
		if (grep(/$device/, @devices)) {
			exit_with("$device is mentioned more than once.", 14);
		}
		if ( $device =~ /^\/dev\/[a-z]+$/ == 0) {
			exit_with("The device parameter $device is inaccurate. Only whole disks are allowed.", 14);
		}
		if (grep(/$device/, (@$dasd_ref, @$zfcp_ref))) {
			if (is_zfcp($device) and @ARGV > 1) {
				exit_with("Multi-volume dumps aren't supported with zFCP.", 14);
			}
			push(@devices, $device);
		} else {
			if (-b $device) {
				exit_with("$device is in use or not a DASD/zFCP disk!", 14);
			} else {
				exit_with("$device does not exist!", 14);
			}
		}
	}

	if (@devices == 0) {
		exit_with("No usable devices where provided.", 14);
	}

	return(@devices);
}

sub main
{
	check_paths();
	my @devices = analyze_cmd_parameters();

	# only one dump device is possible with zFCP which is enforced in analyze_cmd_parameters
	if (is_zfcp($devices[0])) {
		setup_zfcpdump($devices[0]);
	} else {
		setup_dasddump(@devices);
	}

	print("Creating the dump device was successful.\n");
}

main();
