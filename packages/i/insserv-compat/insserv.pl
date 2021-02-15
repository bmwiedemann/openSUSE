#!/usr/bin/perl -w
# Copyright (c) 2012,2013 SUSE Linux Products GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

=head1 insserv

insserv - Enable an installed system init script

=head1 SYNOPSIS

insserv [[-r] <script>]

=head1 OPTIONS

=over 4

=item B<--remove, -r>

Remove the listed scripts from all runlevels

=back

=head1 DESCRIPTION

This version of insserv is just a stub for compatibility. It only reads the
'Default-Start' property of LSB init script headers to enable init scripts.
Anything else is handled by systemd.

### BEGIN INIT INFO
# Provides:          boot_facility_1 [ boot_facility_2 ...]
# Required-Start:    boot_facility_1 [ boot_facility_2 ...]
# Required-Stop:     boot_facility_1 [ boot_facility_2 ...]
# Should-Start:      boot_facility_1 [ boot_facility_2 ...]
# Should-Stop:       boot_facility_1 [ boot_facility_2 ...]
# X-Start-Before:    boot_facility_1 [ boot_facility_2 ...]
# X-Stop-After:      boot_facility_1 [ boot_facility_2 ...]
# Default-Start:     run_level_1 [ run_level_2 ...]
# Default-Stop:      run_level_1 [ run_level_2 ...]
# X-Interactive:     true
# Short-Description: single_line_description
# Description:       multiline_description
### END INIT INFO

=head1 SEE ALSO

systemd(1)

=cut

use strict;
use File::Basename qw/basename dirname/;
use Getopt::Long;
Getopt::Long::Configure("no_ignore_case");

my $init_d = "/etc/init.d";

my %options;

sub parse($)
{
	my $name = shift;
	my $fh;
	unless (open($fh, '<', "$init_d/$name")) {
		warn "can't open $name: $!";
		return undef;
	}
	my $r = {};
	my $header = 0;
	while(<$fh>) {
		if ($header == 0 && /^### BEGIN INIT INFO/) {
			$header = 1;
			next;
		}
		next unless $header;
		last if ($header == 1 && /^### END INIT INFO/);
		unless (s/^#\s//) {
			warn "$name: parse error";
			$r = undef;
			last;
		}
		if (/^(Default-(?:Start|Stop)):\s*(.*)/i) {
			$r->{lc $1} = $2;
		}
	}
	close $fh;
	return $r;
}

sub do_unlink($)
{
	my $file = shift;
	print "rm $file\n" if $options{'verbose'};
	unlink($file);
}

sub do_symlink($$)
{
	my ($old, $new) = @_;
	print "ln -s $old $new\n" if $options{'verbose'};
	return 1 if ($options{'dryrun'});
	symlink($old, $new);
}

sub getlinks(;$)
{
	my $name = shift;
	my $links;
	for my $d (qw/rc0 rc1 rc2 rc3 rc4 rc5 rc6 rcS boot/) {
		my $dir = "$init_d/$d.d";
		opendir(my $dh, $dir) || next;
		for my $n (readdir $dh) {
			next unless $n =~ /^[KS]\d\d/;
			my $fn = "$dir/$n";
			next unless -l $fn;
			if ($name) {
				my $n = readlink $fn;
				$n =~ s/.*\///;
				next unless ($n eq $name);
			}
			push @$links, $fn;
		}
		closedir $dh;
	}
	return $links;
}

sub cleanup()
{
	for my $link (@{getlinks()||[]}) {
		next if -e $link;
		do_unlink($link);
	}
}


sub get_systemd_service($)
{
	my $name = shift;
	for my $file ("/usr/lib/systemd/system/$name.service",
		"/run/systemd/system/$name.service",
		"/etc/systemd/system/$name.service") {
		return $file if -e $file;
	}
	return undef;
}
sub warn_systemd_masked($$)
{
	return unless -t STDERR;
	my $name = shift;
	my $state = shift;
	my $file = get_systemd_service($name);
	return unless $file;
	print STDERR "Warning: $init_d/$name is masked by $file.\nTry 'chkconfig $name $state' instead\n";
}

sub disable($)
{
	my $name = shift;
	warn_systemd_masked($name, "off");
	for my $link (@{getlinks($name)||[]}) {
		do_unlink($link);
	}
}

sub createlinks($$$)
{
	my $type = shift;
	my $name = shift;
	my @lvl = split(' ', shift);
	my $num = '50';
	for my $l (@lvl) {
		my $d = "rc$l.d";
		$d = 'boot.d' if ($l eq 'B');
		do_symlink("../$name", "$init_d/$d/$type$num$name");
	}
}

sub enable($)
{
	my $name = shift;
	($name, my $override) = split(/,/, $name, 2);
	if ($override && $override =~ s/.*start=([^s]+).*/$1/) {
		$override =~ s/,/ /g;
	} else {
		$override = undef;
	}
	my $links = getlinks($name);
	return 0 if $links; # already enabled
	warn_systemd_masked($name, "on");
	my $h = parse($name);
	return unless defined $h;
	createlinks('S', $name, $override || $h->{'default-start'} || '2 3 5');
	# default stop is actually ignored in SUSE ... o_O
	createlinks('K', $name, $override || $h->{'default-start'} || '2 3 5');
}

sub usage($) {
	my $r = shift;
	eval "use Pod::Usage; pod2usage($r);";
	if ($@) {
		die "Pod::Usage missing\n";
	}
}

if ($0 =~ /install_initd$/) {
} elsif ($0 =~ /remove_initd$/) {
	$options{'remove'} = 1;
} else {
	GetOptions(
		\%options,
		"verbose|v",
		"config|c=s", # ignored
		"override|o=s", # ignored
		"path|p=s",
		"dryrun|n",
		"remove|r",
		"default|d", # ignored
		"force|f", # meaningless
		"upstart-job|u=s", # ignored
		"help|h",
	) or usage(1);
}

$init_d = $options{'path'} if $options{'path'};

if (@ARGV) {
	my $p = $ARGV[0] =~ /\// ? $ARGV[0] : "$init_d/$ARGV[0]";
	# need to strip off potential extra parameters
	my $script = $1 if $p =~ /([^,]+)/;
	if (!-e $script) {
		warn "$p doesn't exist";
		usage(1) if @ARGV;
		cleanup();
	}
	if (-d _) {
		$init_d = shift @ARGV;
	} else {
		$init_d = dirname($p);
		$ARGV[0] = basename($p);
	}
}

usage(1) if ($options{'remove'} && !@ARGV);
usage(0) if ($options{'help'});

if (@ARGV) {
	for my $name (@ARGV) {
		if ($name =~ s/^(\/.*)\/(.+)/$2/) {
			$init_d = $1 if $1;
		}
		if ($options{'remove'}) {
			disable($name);
		} else {
			enable($name);
		}
	}
} else {
	cleanup();
}
