#!/usr/bin/perl

use strict;
use integer;
use bytes;
eval 'use File::Copy qw(copy move)';
eval 'use File::Temp qw(mkstemp mktemp)';
eval 'use POSIX qw(uname)';
eval 'use Cwd qw(realpath)';

my $device;
my $diskboot;
my $instdev;
my $diskboot_start;
my $default_backup;
my $default = "/etc/default/grub_installdevice";
my $debug = 0;

$debug = 1 if ($ARGV[0] =~ m/^(--debug|-d)$/);

sub is_part ($) {
  my ($dev) = @_;
  my $ret;

  $dev = realpath($dev);
  if ($dev =~ qr{/dev/(.+)}) {
    $ret = 1 if (-e "/sys/class/block/$1/partition");
  }
  $ret;
}

sub is_abstraction ($) {
  my ($path) = @_;
  my @abs;

  chomp( @abs = qx{grub2-probe --target=abstraction $path} );
  die "Failed to probe $path for target abstraction\n" if ($? != 0);
  @abs;
}

sub default_installdevice () {
  my $ret;

  if ( -w $default ) {
    open( IN, "< $default") || return;
    while ( <IN> ) {
      chomp;
      (m{^/dev}) && ($ret = $_, last);
    }
    close ( IN );
  }
  $ret;
}

sub new_installdevice ($) {
  my ($dev) = @_;
  my $cfg;

  die unless (open( IN, "< $default"));

  while ( <IN> ) {
    if (m{^/dev}) {
      $cfg .= "${dev}\n";
    } else {
      $cfg .= $_;
    }
  }
  close ( IN );

  my ($out, $newf) = mkstemp('/tmp/grub.installdevice.XXXXX');
  die unless (print ( $out $cfg));
  close ( $out );

  $default_backup = mktemp("${default}.old.XXXXX");
  copy($default, $default_backup);
  move($newf, $default);
}

sub is_grub_drive ($$$) {
  my ( $prefix, $path, $isdev ) = @_;
  my $tgt;
  my ($td, $tp);
  my ($pd, $pp);
  my $pattern = qr{\((hd[0-9]+)?,?((?:gpt|msdos)[0-9]+)?\)};

  if ($isdev) {
    chomp( $tgt = qx{grub2-probe --target=drive -d $path} );
  } else {
    chomp( $tgt = qx{grub2-probe --target=drive $path} );
  }

  die "Failed to probe $path for target drive\n" if ($? != 0);
  ( $tgt =~ $pattern ) && (($td, $tp) = ($1, $2)) || return ;
  ( $prefix =~ $pattern ) && (($pd, $pp) = ($1, $2)) || return ;
  return if ($pd && $pd ne $td);
  return 1 unless ($tp);
  ($pp eq $tp) ? 1 : 0;
}

sub embed_part_start ($){
  my ($dev) = @_;
  my @blk;
  my $ret;

  chomp (@blk = qx{lsblk --list --ascii --noheadings --output PATH,PTTYPE,PARTTYPE $dev});
  die "Failed to get block device information for $dev\n" if ($? != 0);
  foreach (@blk) {
    my ($path, $pttype, $parttype) = split /\s+/;
    if ($pttype eq 'dos') {
      $ret = 1;
      last;
    } elsif ($pttype eq 'gpt' && $parttype eq '21686148-6449-6e6f-744e-656564454649') {
      if ($path =~ qr{/dev/(.+)}) {
	if ( -r "/sys/class/block/$1/start" ) {
	  chomp ($ret = qx{cat /sys/class/block/$1/start});
	  last;
	}
      }
    }
  }

  $ret;
}

sub check_mbr ($) {
  my ($dev) = @_;
  my $devh;
  my $mbr;

  open( $devh, "< $dev" ) or die "$0: cannot open $dev: $!\n";
  sysread( $devh, $mbr, 512 ) == 512 or die "$0: $dev: read error\n";
  close( $devh );
  my( $magic ) = unpack('H4', $mbr);
  return if ($magic ne 'eb63');

  my( $version ) = unpack('x128H4', $mbr);
  return if ($version ne '0020');

  my( $sector_nr ) = unpack('x92L<', $mbr);
  return if ($sector_nr ne embed_part_start($dev));

  my( $drive_nr ) = unpack('x100H2', $mbr);
  return if ($drive_nr ne 'ff');

  $sector_nr;
}

sub check_diskboot ($$) {
  my ($dev, $sector_nr) = @_;
  my $devh;
  my $diskboot;
  my @ret;

  open($devh, "< $dev" ) or die "$0: cannot open $dev: $!\n";
  # print "looks at sector $sector_nr of the same hard drive for core.img\n";
  sysseek($devh, $sector_nr*512, 0) or die "$0: $dev: $!\n";
  # grub-core/boot/i386/pc/diskboot.S
  sysread($devh, $diskboot, 512 ) == 512 or die "$0: $dev: read error\n";
  close($devh);

  my( $magic ) = unpack('H8', $diskboot);
  # print $magic , "\n";

  # 5256be1b - upstream diskboot.S
  # 5256be63 - trustedgrub2 1.4
  # 5256be56 - diskboot.S with mjg TPM patches (e.g. in openSUSE Tumbleweed)
  return if ($magic !~ m/(5256be1b|5256be63|5256be56)/);

  for (1..3) {
    my $nr;
    my $s = 512 - 12 * $_;
    my( $nr_low, $nr_high, $size ) = unpack("x${s}L<L<S<", $diskboot);

    last unless ($nr = ($nr_high << 32) + $nr_low);
    last unless ($size);
    push @ret, $nr;
    push @ret, $size;
  }

  @ret;
}

sub lzma_start ($$) {
  my ($core, $size) = @_;
  my $off;
  my $r;

  $r = ($size > 8192) ? 8192 : $size;
  # Find the last 6 bytes of lzma_decode to find the offset of the lzma_stream:
  $off = index( unpack( "H".($r<<1), $core ), 'd1e9dffeffff' );
  if ($off != -1) {
    $off >>= 1;
    $off += 8;
    $off = (($off + 0b1111) >> 4) << 4;
  }
}

sub decomp_lzma ($$) {
  my ($core, $off) = @_;
  my $comp_size;
  my $decomp_size;
  my $lzma;
  my $lzmah;
  my $unlzma;

  # grub-core/boot/i386/pc/startup_raw.S
  my $tmpf = "/tmp/lzma_grub.lzma";
  ($comp_size, $decomp_size) = unpack ("x8VV", $core);
  $lzma = pack( "CVVx4", 0x5d, 0x00010000, $decomp_size );
  $lzma .= substr( $core, $off, $comp_size );

  open($lzmah, "> $tmpf") or die "$0: cannot open $tmpf : $!\n";
  binmode $lzmah;
  print $lzmah $lzma;
  close($lzmah);

  $unlzma = qx{lzcat $tmpf};
  die if ($? != 0);
  die "decompressed size mismatch\n" if (length($unlzma) != $decomp_size);

  ($unlzma, $decomp_size);
}

sub search_prefix (@) {
  my ($unlzma, $decomp_size) = @_;

  my ($mod_base) = unpack("x19V", $unlzma);
  my ($mod_magic, $mod_off, $mod_sz) = unpack("x$mod_base A4 L< L<", $unlzma);
  die "module magic mismatch\n" if ( $mod_magic ne "mimg" );
  die "module out of bound" if ($mod_base + $mod_sz > $decomp_size);
  my $mod_start = $mod_base + $mod_off;
  my $mod_end = $mod_base + $mod_sz;
  my $embed;
  my $prefix;
  while ($mod_start < ($mod_end - 8)) {
    my ($type, $sz) = unpack("x${mod_start} L< L<", $unlzma);
    last if ($mod_start + $sz > $mod_end);
    last if ($sz < 8);
    if ($type == 2) {
      ($embed) = unpack(join('', 'x', $mod_start + 8, 'A', $sz - 8), $unlzma);
    } elsif ($type == 3) {
      ($prefix) = unpack(join('', 'x', $mod_start + 8, 'A', $sz - 8), $unlzma);
    }
    $sz = (($sz + 0b11) >> 2) << 2;
    $mod_start += $sz;
  }

  $prefix;
}

sub part_to_disk ($) {
  my ($dev) = @_;
  my $ret;

  if ($dev =~ m{/dev/disk/by-uuid/}) {
     $dev = realpath($dev);
  }

  my @regexp = (
    qr{(/dev/disk/(?:by-id|by-path)/.+)-part[0-9]+},
    qr{(/dev/[a-z]+d[a-z])[0-9]+},
    qr{(/dev/nvme[0-9]+n[0-9]+)p[0-9]+}
  );

  foreach (@regexp) {
    if ($dev =~ $_) {
      $ret = $1;
      last;
    }
  }

  $ret;
}

sub get_prefix ($@) {
  my ($dev, ($sector_nr, $size)) = @_;
  my $devh;
  my $core;
  my $off;
  my $prefix;

  $size <<= 9;
  $sector_nr <<= 9;

  open( $devh, "< $dev" ) or die "$0: cannot open $dev: $!\n";
  sysseek( $devh, $sector_nr, 0) or die "$0: $dev: $!\n";
  sysread( $devh, $core, $size ) == $size or die "$0: $dev: read error\n";
  close( $devh );

  $off = lzma_start($core, $size);
  return if ($off == -1);

  $prefix = search_prefix( decomp_lzma($core, $off) );
}

eval {

my @uname = uname();
die "machine hardware is not x86_64\n" if ($uname[4] ne 'x86_64');

die "no install device config or no permission to alter it\n" unless ($instdev = default_installdevice());
die "/boot is abstraction\n" if (is_abstraction("/boot"));
die "$instdev is NOT partition\n" unless (is_part($instdev));

chomp ( $device = qx{grub2-probe --target=disk /boot} );
die "no disk for /boot\n" unless ( $device );

my $sector_nr = check_mbr($device);

die "$device mbr is not used for suse grub embedding\n" unless ($sector_nr);

my @core_sectors = check_diskboot($device, $sector_nr);

die "core image is not single continuous chunk\n" if (@core_sectors != 2);

die "starting sector of startup_raw $core_sectors[0]" .
" did not follow diskboot $sector_nr\n" if ($core_sectors[0] != $sector_nr + 1);

my $prefix = get_prefix($device, @core_sectors);

die "$prefix is not pointing to /boot" unless ($prefix && is_grub_drive ($prefix, '/boot', 0));

my $instdisk = part_to_disk($instdev);

die "cannot determine disk device for $instdev" unless ($instdisk);
die "$instdisk is not grub disk" unless (is_grub_drive($prefix, $instdisk, 1));

new_installdevice($instdisk);

print "The system has been detected using grub in master boot record for booting this updated system with \$prefix=$prefix. However the $default has the install device set to the partition, $instdev. To avoid potential breakage in the application binary interface between grub image and modules, the install device of grub has been changed to use the disk device, $instdisk, to update the master boot record with new grub in order to keep up with the new binary.\n";

print "The backup of the original file is $default_backup\n";

};

print "No fixup required: $@" if ($debug && $@);
