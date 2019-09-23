#!/usr/bin/perl -w
#
#	convert tool for pam_mount.conf 
#
#	Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
#	This file is under the same license as pam_mount itself.
#
#	Please submit bugfixes or comments via http://bugs.opensuse.org/
#
use Data::Dumper;
use Getopt::Long;
use IO::File;
use XML::Writer;
use strict;

my $OLD_CONF = "-";
my $NEW_CONF = "-";
my $debug = 0;

Getopt::Long::Configure(qw(bundling));
GetOptions(
	"i=s" => \$OLD_CONF,
	"o=s" => \$NEW_CONF,
	"d"   => \$debug,
);

my %callbacks = (
	"debug"           => \&callback_debug,
        "logout"          => \&callback_logout,
	"mkmountpoint"    => \&callback_mkmountpoint,
	"fsckloop"        => \&callback_fsckloop,
	"luserconf"       => \&callback_luserconf,
	"options_allow"   => \&callback_options_allow,
	"options_deny"    => \&callback_options_deny,
	"options_require" => \&callback_options_require,
	"lsof"            => \&callback_lsof,
	"fsck"            => \&callback_fsck,
	"losetup"         => \&callback_losetup,
	"unlosetup"       => \&callback_unlosetup,
	"cifsmount"       => \&callback_cifsmount,
	"smbmount"        => \&callback_smbmount,
	"ncpmount"        => \&callback_ncpmount,
	"smbumount"       => \&callback_smbumount,
	"ncpumount"       => \&callback_ncpumount,
	"fusemount"       => \&callback_fusemount,
	"fuseumount"      => \&callback_fuseumount,
	"umount"          => \&callback_umount,
	"lclmount"        => \&callback_lclmount,
	"cryptmount"      => \&callback_cryptmount,
	"nfsmount"        => \&callback_nfsmount,
	"mntagain"        => \&callback_mntagain,
	"mntcheck"        => \&callback_mntcheck,
	"pmvarrun"        => \&callback_pmvarrun,
	"volume"          => \&callback_volume,
);

my $output = new IO::File("> $NEW_CONF");
my $writer = new XML::Writer(OUTPUT => $output, UNSAFE => 1);

$writer->xmlDecl("UTF-8");
$writer->startTag("pam_mount");
$writer->raw("\n\n");

sub callback_debug
{
	my @fields = @_;

	$writer->emptyTag("debug", "enable" => $fields[1]);
}

sub callback_logout
{
	my @fields = @_;

        # we create a default entry here, fields are not evaluated
	$writer->emptyTag("logout", "wait" => "2000", "hup" => "0", "term" => "1", "kill" => "1");
}

sub callback_mkmountpoint
{
	my @fields = @_;

	$writer->emptyTag("mkmountpoint", "enable" => $fields[1]);
}

sub callback_fsckloop
{
	my @fields = @_;

	$writer->emptyTag("fsckloop", "device" => $fields[1]);
}

sub callback_luserconf
{
	my @fields = @_;

	$writer->emptyTag("luserconf", "name" => $fields[1].".xml");
	print STDERR "Please note that you will also probably have to convert",
	      $fields[1], "\n";
}

sub callback_options_allow
{
	my @fields = @_;

	$writer->emptyTag("mntoptions", "allow" => $fields[1]);
}

sub callback_options_deny
{
	my @fields = @_;

	$writer->emptyTag("mntoptions", "deny" => $fields[1]);
}

sub callback_options_require
{
	my @fields = @_;

	$writer->emptyTag("mntoptions", "require" => $fields[1]);
}

sub callback_fsck
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("fsck");
	$writer->characters(join(" ", @fields));
	$writer->endTag("fsck");
}

sub callback_losetup
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("losetup");
	$writer->characters(join(" ", @fields));
	$writer->endTag("losetup");
}

sub callback_unlosetup
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("unlosetup");
	$writer->characters(join(" ", @fields));
	$writer->endTag("unlosetup");
}

sub callback_cifsmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("cifsmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("cifsmount");
}

sub callback_smbmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("smbmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("smbmount");
}

sub callback_ncpmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("ncpmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("ncpmount");
}

sub callback_smbumount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("smbumount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("smbumount");
}

sub callback_ncpumount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("ncpumount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("ncpumount");
}

sub callback_fusemount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("fusemount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("fusemount");
}

sub callback_fuseumount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("fuseumount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("fuseumount");
}

sub callback_umount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("umount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("umount");
}

sub callback_lclmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("lclmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("lclmount");
}

sub callback_cryptmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("cryptmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("cryptmount");
}

sub callback_nfsmount
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("nfsmount");
	$writer->characters(join(" ", @fields));
	$writer->endTag("nfsmount");
}

sub callback_mntagain
{
	# not translated - removed in pam_mount 0.32
}

sub callback_lsof
{
    # not translated - removed
}

sub callback_mntcheck
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("mntcheck");
	$writer->characters(join(" ", @fields));
	$writer->endTag("mntcheck");
}

sub callback_pmvarrun
{
	my @fields = @_;

	shift @fields;
	$writer->startTag("pmvarrun");
	$writer->characters(join(" ", @fields));
	$writer->endTag("pmvarrun");
}

sub callback_volume
{
	my @fields = @_;

	shift @fields;

	my %attr = (
		"fstype" => "auto",
	);
	
	# search for wrong splits 
	# happens at 'a value' or "a value"
	# and remove quotes around a single value. "value" or 'value'
	my @new_fields;
	my($nf, $char);
	
	foreach my $f (@fields) {
		if (!defined($nf) && $f =~ /^'(.+)'$/) {
			push(@new_fields, $1);
		} elsif (!defined($nf) && $f =~ /^"(.+)"$/) {
			push(@new_fields, $1);
		} elsif (!defined($nf) && $f =~ /^'([^']+)$/) {
			$nf   = $1;
			$char = "'";
		} elsif (!defined($nf) && $f =~ /^"([^"]+)$/) {
			$nf   = $1;
			$char = "\"";
		} elsif (defined($nf) && $f =~ /^([^$char]+)$char$/) {
			$nf  .= " $1";
			push(@new_fields, $nf);
			$nf   = undef;
			$char = undef;
		} elsif(defined($nf)) {
			$nf .= " $f";
		} else {
			push(@new_fields, $f);
		}
	}
	@fields = @new_fields;
	if ($debug) {
		print STDERR Data::Dumper->Dump([@new_fields])
	}
	
	foreach my $i (2..7) {
		$fields[$i] =~ s/&/\%(USER)/g;
		$fields[$i] =~ s/\\\s/ /g;
	}

	if ($fields[0] =~ /^\@\@(.*)/) {
		$attr{sgrp} = "$1";
	} elsif ($fields[0] =~ /^\@(.*)/) {
		$attr{pgrp} = "$1";
	} else {
		$attr{user} = "$fields[0]";
	}
	
	if (defined($fields[1]) && $fields[1] ne "local") {
		$attr{fstype}     = $fields[1];
	}
	if (defined($fields[2]) && $fields[2] ne "-") {
		$attr{server}     = $fields[2];
	}
	if (defined($fields[3])) {
		$attr{path}       = $fields[3];
	}
	if (defined($fields[4]) && $fields[4] ne "-") {
		$attr{mountpoint} = $fields[4];
	}
	if (defined($fields[5]) && $fields[5] ne "-") {
		$attr{options}    = $fields[5];
	}
	if (defined($fields[6]) && $fields[6] ne "-") {
		$attr{fskeycipher}= $fields[6];
	}
	if (defined($fields[7]) && $fields[7] ne "-") {
		$attr{fskeypath}  = $fields[7];
	}

	$writer->emptyTag("volume", %attr );
}

sub parse_conf
{
	my @file;
	open(OUT, "< $OLD_CONF") || die "Cannot open $OLD_CONF: $!\n";
	@file = <OUT>;
	close OUT;
	
	foreach my $line (@file) {
		++$.;
		chomp $line;
		$line =~ s/^\s+//s;

		if (length($line) == 0 || substr($line, 0, 1) eq "#") {
			next;
		}

		my @fields = split(/(?<!\\)\s+/, $line);
		for (my $i = 0; $i <= $#fields; ++$i) {
			if ($fields[$i] eq "#") {
				#
				# Old-style config file had this oddity in
				# one spot, so need to trim it.
				#
				splice(@fields, $i);
				last;
			}
		}

		if (exists $callbacks{$fields[0]}) {
			if ($debug) {
				print STDERR "callback_$fields[0] called: ",
				      join(" ", @fields), "\n";
			}

			$callbacks{$fields[0]}->(@fields);
			$writer->raw("\n\n");
		} else {
			print STDERR "-" x 40, "\n",
			      "Unknown command: \"$fields[0]\" near ",
			      "line $.:\n",
			      $line, "\n",
			      "-" x 40, "\n";
			return 1;
		}

                # insert new <logout> field after debug

                if( $fields[0] eq "debug" )
                {
                       if ($debug) {
                                print STDERR "callback_logout called: (default)\n";
                        }

                        $callbacks{"logout"}->();
                        $writer->raw("\n\n");
                }
	}

	return 0;
}

my $ret = parse_conf();

$writer->endTag("pam_mount");
$writer->end();
$output->close();

exit $ret;
