#!/usr/bin/perl
# 
# PreBoot Authentication Image Creator for
# Unlocking Self Encrypting Drive
#

use strict;
use warnings;

use File::Path qw(make_path remove_tree);
use File::Temp qw(tempdir);
use File::Copy qw(copy);

die "no sedutil module for dracut, stopped" unless (`dracut --list-modules 2>/dev/null` =~ /\bsedutil\b/);

my $kver = `uname -r`;
chomp $kver;
my $scratch = tempdir('mkpba-XXXXX') or die "$!, stopped";
my $bdir = "boot";
my $gdir = "$bdir/grub";
my $initrd = "initrd-$kver";
my $kern = "vmlinuz-$kver";
my $cfg = "grub.cfg";
my $iso = "linuxpba-$kver.iso";
my $rescue = "sedutil-rescue-$kver.iso";
my $keep = 0;

make_path("$scratch/$bdir", "$scratch/$gdir", {verbose => 1}) == 2
  or die "$!, stopped";

system ("dracut", "--force", "-m", "sedutil base", "$scratch/$bdir/$initrd") == 0
  or die "stopped";

copy("/$bdir/$kern", "$scratch/$bdir")
  or die "$!, stopped";

open(CFG, ">", "$scratch/$gdir/$cfg")
  or die "$!, stopped";

print CFG <<"END";
set gfxpayload=keep

ext=""
if [ x\$grub_platform = xefi ]; then
  ext=efi
fi

echo 'Loading Linux $kver ...'
linux\$ext /$bdir/$kern libata.allow_tpm=1 quiet rd.hostonly=0 linuxpba
echo 'Loading sedutilpba-$kver.img ...'
initrd\$ext /$bdir/$initrd
echo 'Boot ...'
boot
END

close(CFG);

system ("grub2-script-check", "--verbose", "$scratch/$gdir/$cfg") == 0
  or die "stopped";

system ("grub2-mkrescue", "-o", $iso, $scratch) == 0
  or die "stopped";

system ("dracut", "--force", "-m", "sedutil base", "--include", "./$iso", "/$iso", "$scratch/$bdir/$initrd") == 0
  or die "stopped";

open(CFG, ">", "$scratch/$gdir/$cfg")
  or die "$!, stopped";

print CFG <<"END";
set gfxpayload=keep

ext=""
if [ x\$grub_platform = xefi ]; then
  ext=efi
fi

echo 'Loading Linux $kver ...'
linux\$ext /$bdir/$kern libata.allow_tpm=1 quiet rd.hostonly=0 rd.break=cmdline
echo 'Loading sedutilpba-$kver.img ...'
initrd\$ext /$bdir/$initrd
echo 'Boot ...'
boot
END

close(CFG);

system ("grub2-script-check", "--verbose", "$scratch/$gdir/$cfg") == 0
  or die "stopped";

system ("grub2-mkrescue", "-o", $rescue, $scratch) == 0
  or die "stopped";

remove_tree($scratch, {verbose => 1}) unless ($keep);
