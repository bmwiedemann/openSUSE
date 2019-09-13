#!/usr/bin/perl -w
# nagios: -epn
#
# check_zypper - nagios plugin
#
# Copyright (C) 2008-2010, Novell, Inc.
# Copyright (C) 2011-2014, SUSE Linux Products GmbH
# Copyright (C) 2015-2018, SUSE Linux GmbH
# Author: Lars Vogdt
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the Novell nor the names of its contributors may be
#   used to endorse or promote products derived from this software without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# perltidy -pbp check_zypper.pl
# 

use strict;
use warnings;
use Getopt::Long;
use vars qw($PROGNAME $VERSION $DEBUG);

# cleanup the environment
$ENV{'PATH'}     = '/bin:/usr/bin:/sbin:/usr/sbin:';
$ENV{'BASH_ENV'} = '';
$ENV{'ENV'}      = '';

# constants
$PROGNAME = "check_zypper";
$VERSION  = '1.97';
$DEBUG    = 0;

# variables
our (
    $opt_V, $opt_h, $opt_i, $opt_w, $opt_c, $opt_f, $opt_l,
    $opt_o, $opt_p, $opt_r, $opt_s, $opt_t, $opt_u, $opt_v
);
our $zypper           = '/usr/bin/zypper';
our $zypperopt        = '--non-interactive --no-gpg-checks list-updates';
our $sudo             = '/usr/bin/sudo';
our $zypp_refresh     = '/usr/sbin/zypp-refresh ""';
our $refresh_wrapper  = '/usr/sbin/zypp-refresh-wrapper';
our $use_sudo         = 'unset LANG; ';
our $releasefile      = '/etc/SuSE-release';
our $alt_releasefile  = '/etc/os-release';
our $productfile      = '/etc/products.d/baseproduct';
our $rpm              = '/bin/rpm';
our $awk              = '/bin/awk';
our $grep             = '/bin/grep';
our $TIMEOUT          = 120;
our @patchignore      = ();
our @packageignore    = ();
our @packagewhitelist = ();
our @localwhitelist   = ();
our $patchlevel       = 0;
our $exitcode         = 0;
our %ERRORS           = (
    'OK'        => 0,
    'WARNING'   => 1,
    'CRITICAL'  => 2,
    'UNKNOWN'   => 3,
    'DEPENDENT' => 4,
);
our %REVERSE = (
    4 => 'DEPENDENT',
    3 => 'UNKNOWN',
    2 => 'CRITICAL',
    1 => 'WARNING',
    0 => 'OK',
);
our %supported_release = (
    'openSUSE'   => [ '42.3', '15.0', '15.1' ],
    'SLE'        => [ '11.4', '12.3', '12.4', '15.0', '15.1' ],
    'Tumbleweed' => [ '2019*'],
);
$opt_w = 'recommended,optional,unsupported,local_package';
$opt_c = 'security';
$opt_f = "$releasefile";
$opt_f = "$alt_releasefile" if ( -r "$alt_releasefile" );
$opt_t = '120';
$opt_v = 0;
$opt_o = 0;
$opt_p = 1;
$opt_s = 0;

#######################################################################
# Functions
#######################################################################

sub print_myrevision ($$) {
    my $commandName    = shift;
    my $pluginRevision = shift;
    print "$commandName v$pluginRevision\n";
}

sub mysupport () {
    print "Please use https://bugzilla.suse.com to submit patches or ";
    print "suggest improvements.\n";
    print "Please include version information with all correspondence ";
    print "(when possible,\n";
    print "use output from the --version option of the plugin itself).\n";
}

sub usage ($) {
    my $format = shift;
    printf( $format, @_ );
    exit $ERRORS{'UNKNOWN'};
}

sub get_distribution_from_os_release($) {
    my ($file) = @_;
    my %dist = (
        'name'    => '',
        'version' => '',
        'release' => '0',
    );
    open( RELEASE, "<$file" ) || warn("Could not open $file\n");
    while (<RELEASE>) {
        if (/^PRETTY_NAME=\"SUSE Linux Enterprise.*/) {
            $dist{'name'} = 'SLE';
        }
        elsif (/^PRETTY_NAME=\".*Tumbleweed.*/) {
            $dist{'name'} = 'Tumbleweed';
        }
        elsif (/^PRETTY_NAME=\"openSUSE.*/) {
            $dist{'name'} = 'openSUSE';
        }
    }
    close(RELEASE);
    open( RELEASE, "<$file" ) || warn("Could not open $file\n");
    while (<RELEASE>) {
        if (/^VERSION_ID/) {
            my ($version) = $_ =~ m/VERSION_ID=\"(.*)\"/;
            if (( $dist{'name'} eq 'SLE' ) || ( $dist{'name'} eq '' )) {
                if ( $version =~ m/(\d+)\.(\d+).*/ ) {
                    $dist{'version'} = trim($1);
                    $dist{'release'} = trim($2);
                }
		else {
		    $dist{'version'} = trim($version);
		}
            }
            else {
                $dist{'version'} = trim($version);
            }
        }
    }
    close(RELEASE);
    return ( \%dist );
}

sub get_distribution($) {
    my ($file) = @_;
    my %dist = (
        'name'    => '',
        'version' => '',
        'release' => '0',
    );
    open( RELEASE, "<$file" ) || warn("Could not open $file\n");
    while (<RELEASE>) {
        if (/^SUSE Linux Enterprise/) {
            $dist{'name'} = 'SLE';
        }
        elsif (/^openSUSE/) {
            $dist{'name'} = 'openSUSE';
        }
        elsif (/^CODENAME\s+=\s+Tumbleweed/) {
            $dist{'name'} = 'Tumbleweed';
        }
        if (/^VERSION/) {
            my ($version) = $_ =~ m/VERSION = (.*)/;
            $dist{'version'} = trim($version);
        }
        if (/^PATCHLEVEL/) {
            my ($release) = $_ =~ m/PATCHLEVEL = (.*)/;
            $dist{'release'} = trim($release);
        }
    }
    close(RELEASE);
    return ( \%dist );
}

sub endoflife($) {
    my ($file) = @_;
    my $eol = '1970-01-01';
    if ( -r "$file" ) {
        open( PRODFILE, "<$file" ) || warn("Could not open $file\n");
        while (<PRODFILE>) {
            chomp;
            if (/<endoflife>(.*)<\/endoflife>/) {
                $eol = $1;
            }
        }
    }
    my ( $d, $m, $y ) = ( localtime( time() ) )[ 3, 4, 5 ];
    my $year = 1900 + $y;
    print STDERR "INFO: Current: $year-$m-$d; End of life: $eol\n"
        if ($DEBUG);
}

sub print_usage () {
    print "This plugin checks for software updates on systems that \n";
    print "use package management systems based on the zypper command \n";
	print "found in (open)SUSE.\n\n";
    print "It checks for security, recommended and optional patches \n";
    print "and also for optional package updates.\n\n";
    print "You can define the status by patch category. Use a commata to\n";
    print "list more than one category to a state. Possible values are: \n";
    print "   recommended,optional,security and packages\n\n";
    print "If you like to know the names of available patches and packages, \n";
    print "use the \"-v\" option.\n\n";
    print "Usage:\n";
    print "  $PROGNAME [-w <category>] [-c <category>] [-t <timeout>] [-v]\n";
    print "  $PROGNAME [-h | --help]\n";
    print "  $PROGNAME [-V | --version]\n";
    print "\n\nOptions:\n";
    print "  -c, --critical\n";
    print "      A patch with this category result in critical status.\n";
    print "      Default: $opt_c\n";
    print "  -f, --releasefile\n";
    print "      Use the given file to get informations about the distribution.\n";
    print "      Default: $alt_releasefile (fallback: $releasefile)\n";
    print "  -h, --help\n";
    print "      Print detailed help screen\n";
    print "  -i, --ignore <file>\n";
    print "      Ignore patches/packages that are mentioned in <file>\n";
    print "      Place the file in /etc/nagios/ or /etc/monitoring-plugins/ \n";
    print "      and/or adapt the apparmor profile before using this feature!\n";
    print "      Just list one patch/package per line - example:\n\n";
    print "      patch:libtiff-devel\n";
    print "      # comment\n";
    print "      package:libtiff3\n";
    print "      package:libtiff-devel\n";
    print "      # comment\n";
    print "      whitelist:aaa_base\n";
    print "      # comment\n";
    print "      local_package:mypackage\n\n";
    print "  -o, --ignore_outdated\n";
    print "      Don't warn if a repository is outdated.\n";
    print "  -p, --no_perfdata\n";
    print "      Print no perfdata\n";
    print "  -r, --refresh_repos\n";
    print "      Tries to refresh the repositories before checking for updates.\n";
    print "      Note: this maybe needs an entry in /etc/sudoers like:\n";
    print "            nagios ALL = NOPASSWD: /usr/bin/zypper ref\n";
    print "            (and additional lines for the \'-s\' Option) if no \n";
    print "             check-zypp-wrapper is available.\n";
    print "  -s, --use_sudo\n";
    print "      Zypper needs root privileges on some distributions \n";
    print "      known: 10.1, SLE10, SLE12 and beyond).\n";
    print "      You can enable the script to use $sudo to start zypper.\n";
    print "      But don't forget to enable nopasswd sudo for the user \n";
    print "      starting $PROGNAME\n";
    print "      Via lines like the two below on in /etc/sudoers:\n";
    print "          nagios ALL = NOPASSWD: /usr/bin/zypper services, \\ \n";
    print "                       /usr/bin/zypper $zypperopt\n";
    print "  -t, --timeout\n";
    print "      Just in case of problems, let's not hang Nagios and define a timeout.\n";
    print "      Default value is: $opt_t seconds\n";
    print "  -u, --check-vendor\n";
    print "      Check if installed packages are not from a supported vendor.\n";
    print "  -l, --check-local\n";
    print "      Check for local packages that are not in any \n";
    print "      repository. NOTE: zypper just searches for\n";
    print "      exact the same version-release in the repositories, \n";
    print "      so if the repositories do not contain\n";
    print "      old versions of the packages, this check may always \n";
    print "      produce a warning.\n";
    print "      This check does not work on SLE-10\n";
    print "  -v, --verbose_output\n";
    print "      Print more information (useful only with Nagios v3.x).\n";
    print "  -w, --warning\n";
    print "      A patch with this category result in warning status.\n";
    print "      Default: $opt_w\n";
    print "\n";
    print "  -V, --version\n";
    print "      Print version information\n";
    print "\n";
    print "  -d, --debug\n";
    print "      Print debug output to STDERR\n";
    print "\n";
    print " The lines below contain all entries for your sudoers ";
    print " file, if needed:\n";
    print "    nagios ALL = NOPASSWD: /usr/sbin/zypp-refresh \"\",\\ \n";
	print "                           /usr/bin/zypper refresh,\\ \n";
	print "                           /usr/bin/zypper services,\\ \n";
    print "                           /usr/bin/zypper $zypperopt\n";
}

sub print_help {
    my $exit = shift || undef;
    print "Copyright (c) 2009-2018, SUSE Linux GmbH\n\n";
    print_usage();
    print "\n";
    mysupport();
    exit $exit if ( defined($exit) );
}

sub check_zypper() {
    if ( -x "$zypper" ) {
        print STDERR "INFO: Trying $use_sudo $zypper services 2>/dev/null 1>&2\n"
            if ($DEBUG);
        return ( system("$use_sudo $zypper services 2>/dev/null 1>&2") );
    }
    else {
        return 1;
    }
}

sub refresh_zypper($) {
    my ($dist) = @_;
    if ( -x "$refresh_wrapper" ) {
        print STDERR "INFO: Trying $refresh_wrapper 2>/dev/null 1>&2\n"
            if ($DEBUG);
        if ( open( WRAPPER, "$refresh_wrapper 2>&1 |" ) ) {
            my @wrapper_out = <WRAPPER>;
            close(WRAPPER);
            foreach my $line (@wrapper_out) {
                chomp $line;
                print STDERR "LINE: $line\n" if ($DEBUG);
                # error handling
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Could not refresh repository.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if (
                    $line =~ /There are no enabled repositories defined.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Digest verification failed.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /refusing file.*wrong digest.*/ );
            }
            return ( "Refresh OK", $ERRORS{'OK'} );
        }
    }
    elsif ( -x "$zypp_refresh" ) {
        print STDERR "INFO: Trying $zypp_refresh 2>&1\n" if ($DEBUG);
        if ( open( WRAPPER, "$refresh_wrapper 2>&1 |" ) ) {
            my @wrapper_out = <WRAPPER>;
            close(WRAPPER);
            foreach my $line (@wrapper_out) {
                chomp $line;
                print STDERR "LINE: $line\n" if ($DEBUG);

                # error handling
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line
                    =~ /Could not access the package manager engine.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Could not refresh repository.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if (
                    $line =~ /There are no enabled repositories defined.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Digest verification failed.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /refusing file.*wrong digest.*/ );
            }
            return ( "Refresh OK", $ERRORS{'OK'} );
        }
    }
    elsif ( -x "$zypper" ) {
        print STDERR "INFO: Trying $sudo $zypper refresh 2>/dev/null 1>&2\n"
            if ($DEBUG);
        if ((      ( "$dist->{'name'}" eq "openSUSE" )
                && ( "$dist->{'version'}" eq "10.2" )
            )
            || (   ( "$dist->{'name'}" eq "SLE" )
                && ( "$dist->{'version'}" eq "10" ) )
            )
        {
            my $res = system("$sudo $zypper refresh 2>/dev/null 1>&2");
            return ( "ERROR: Unable to refresh the repositories",
                $ERRORS{'CRITICAL'} )
                if !($res);
        }
        elsif ( open( ZYPPER, "$sudo $zypper refresh 2>&1 |" ) ) {
            my @wrapper_out = <ZYPPER>;
            close(ZYPPER);
            foreach my $line (@wrapper_out) {
                chomp $line;
                print STDERR "LINE: $line\n" if ($DEBUG);
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Could not refresh repository.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if (
                    $line =~ /There are no enabled repositories defined.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /Digest verification failed.*/ );
                return ( "ERROR: " . xml_re_escape($line),
                    $ERRORS{'CRITICAL'} )
                    if ( $line =~ /refusing file.*wrong digest.*/ );
            }
            return ( "Refresh OK", $ERRORS{'OK'} );
        }
    }
    else {
        return (
            "ERROR: Could not refresh the repositories - binary not found",
            $ERRORS{'CRITICAL'} );
    }
}

sub check_errorcode($) {
    my $status      = shift;
    my $level       = 0;
    my $returnvalue = 'OK';
    $returnvalue = 'WARNING'  if ( "$opt_w" =~ /$status/ );
    $returnvalue = 'CRITICAL' if ( "$opt_c" =~ /$status/ );
    $level       = $ERRORS{"$returnvalue"};
    $exitcode    = $level     if ( $level gt $exitcode );
    $returnvalue = $REVERSE{"$exitcode"};
    return "$returnvalue";
}

sub xml_re_escape($) {
    my ($text) = @_;
    $text =~ s/&amp;/&/sg;
    $text =~ s/&lt;/</sg;
    $text =~ s/&gt;/>/sg;
    $text =~ s/&quot;/"/sg;
    $text =~ s/&apos;/'/sg;
    return $text;
}

sub trim($) {
    my ($text) = @_;
    $text =~ s/^\s+//;
    $text =~ s/\s+$//;
    return $text;
}

sub check($) {
    my ($dist) = @_;
    my ( $status, $ret_str, $error );
    my $secstr       = '';
    my $recstr       = '';
    my $optstr       = '';
    my $pacstr       = '';
    my $warnstr      = '';
    my $unsupstr     = '';
    my $local_pacstr = '';
    my $update_avail = 0;
    my %packagelist;
    my @unsup_packagelist = ();
    my @loc_packagelist   = ();

    if ($opt_u) {
        print STDERR
            "INFO: checking for unsupported packages installed on the system\n"
            if ($DEBUG);
        @unsup_packagelist
            = `$rpm -qa --qf "%{NAME} %{VENDOR}\n" | $grep -v 'SUSE LINUX Products GmbH, Nuernberg, Germany' | $grep -v 'openSUSE' | $grep -v 'SUSE LLC <https://www.suse.com/>' | $grep -v gpg-pubkey | $awk '" " { print \$1 }'`;
        my $category = 'unsupported';
        my $status   = 'new';
        foreach my $name ( sort(@unsup_packagelist) ) {
            chomp($name);
            if ( grep { $_ eq $name } @packagewhitelist ) {
                print STDERR
                    "WARINING: ignoring $name as it is in \@packagewhitelist\n"
                    if ($DEBUG);
                next;
            }
            $packagelist{"$category"}{"$name"}{'category'} = "$category";
            $packagelist{"$category"}{"$name"}{'name'}     = "$name";
            $packagelist{"$category"}{"$name"}{'status'}   = "$status";
        }
    }

    if ( ($opt_l) && ( $dist->{'version'} gt 10.4 ) ) {
        print STDERR "INFO: checking for local packages not referenced in repositories\n"
            if ($DEBUG);
        @loc_packagelist = `$zypper search --details --installed-only | $grep '(System Packages)' | $awk '" " { print \$3 }'`;
        my $category = 'local_package';
        my $status   = 'new';
        foreach my $name ( sort(@loc_packagelist) ) {
            chomp($name);
            if ( grep { $_ eq $name } @localwhitelist ) {
                print STDERR
                    "WARINING: ignoring $name as it is in \@localwhitelist\n"
                    if ($DEBUG);
                next;
            }
            $packagelist{"$category"}{"$name"}{'category'} = "$category";
            $packagelist{"$category"}{"$name"}{'name'}     = "$name";
            $packagelist{"$category"}{"$name"}{'status'}   = "$status";
        }
    }

    print STDERR "INFO: Trying $use_sudo $zypper $zypperopt\n" if ($DEBUG);

    if ( open( FH, "$use_sudo $zypper $zypperopt 2>&1 |" ) ) {
        while (<FH>) {
            chomp;
            my $category = 'unknown';
            print STDERR "LINE: $_\n" if ($DEBUG);
            # error handling
            return (
                'There is a pending update of the update-stack itself. This plugin can not check if there are more updates pending.',
                'CRITICAL'
            ) if (/softwaremgmt/);
            return (
                'There is a pending update of the update-stack itself. This plugin can not check if there are more updates pending.',
                'CRITICAL'
            ) if (/Softwarestack/);
            return ( 'UNKNOWN: ' . xml_re_escape($_), 'UNKNOWN' )
                if (/not found on medium/);
            return ( 'UNKNOWN: ' . xml_re_escape($_), 'UNKNOWN' )
                if (/I\/O error: Can't provide/);
            return ( 'UNKNOWN: ' . xml_re_escape($_), 'UNKNOWN' )
                if (/Error message:/);
            return ( 'UNKNOWN: ' . xml_re_escape($_), 'UNKNOWN' )
                if (/A ZYpp transaction is already in progress./);
            return ( 'UNKNOWN: ' . xml_re_escape($_), 'UNKNOWN' )
                if (/System management is locked/);

            if ( (/Repository.*is out-of-date/) || (/Repository.*outdated/) )
            {
                print STDERR "WARNING: possibly outdated repository found\n"
                    if ($DEBUG);
                if ( !$opt_o ) {
                    $error = check_errorcode('security');
                    $warnstr = "At least one of your Repositories might be out of date. Please run \"zypper refresh\" as root to update it. ";
                    $warnstr .= "\n" if ($opt_v);
                    next;
                }
            }
            if (/<message type=\"warning\">(.*)<\/message>/) {
                $update_avail = 1;
                $error        = check_errorcode('security');
                $warnstr      = xml_re_escape($1) . ' ';
                $warnstr .= "\n" if ($opt_v);
            }
            if ((      ( "$dist->{'name'}" eq "SLE" )
                    && ( "$dist->{'version'}" eq "10.2" )
                )
                || (   ( "$dist->{'name'}" eq "SLE" )
                    && ( "$dist->{'version'}" eq "10" ) )
                )
            {
                my ( $url, $name, $version, $category, $status )
                    = split( '\s*\|\s*', $_, 5 )
                    ; # just for reference - perhaps we need the variables later
                if ( defined($name) ) {
                    if ( grep { $_ eq $name } @patchignore ) {
                        print STDERR "WARNING: ignoring $name as it is in \@patchignore\n"
                            if ($DEBUG);
                        next;
                    }
                }
                $category = 'optional' if (/\|\s*optional\s*\|\s*Needed/);
                $category = 'recommended'
                    if (/\|\s*recommended\s*\|\s*Needed/);
                $category = 'security' if (/\|\s*security\s*\|\s*Needed/);
                $packagelist{"$category"}{"$name"}{'category'} = "$category"
                    if defined($category);
                $packagelist{"$category"}{"$name"}{'status'} = "$status"
                    if defined($status);
                $packagelist{"$category"}{"$name"}{'name'} = "$name"
                    if defined($name);
            }
            else {
                if (/<update /) {
                    my ($name)    = $_ =~ /name="(.*?)"/;
                    my ($edition) = $_ =~ /edition="(.*?)"/;
                    if (/kind="patch"/) {    # line contains patch
                        if ( grep { $_ eq $name } @patchignore ) {
                            print STDERR "WARNING: ignoring $name as it is in \@patchignore\n"
                                if ($DEBUG);
                            next;
                        }
                        if ( grep { $_ eq "$name-$edition" } @patchignore ) {
                            print STDERR "WARNING: ignoring $name-$edition as it is in \@patchignore\n"
                                if ($DEBUG);
                            next;
                        }
                        $category = 'optional' if (/category="optional"/);
                        $category = 'recommended' if (/category="recommended"/);
                        $category = 'security' if (/category="security"/);
                    }
                    elsif (/kind="package"/) {
                        if ( grep { $_ eq $name } @packageignore ) {
                            print STDERR "WARNING: ignoring $name as it is in \@packageignore\n"
                                if ($DEBUG);
                            next;
                        }
                        if ( grep { $_ eq "$name-$edition" } @packageignore )
                        {
                            print STDERR "WARNING: ignoring $name-$edition as it is in \@packageignore\n"
                                if ($DEBUG);
                            next;
                        }
                        $category = 'package';
                    }
                    $packagelist{"$category"}{"$name"}{'category'} = "$category";
                    $packagelist{"$category"}{"$name"}{'name'}   = "$name";
                    $packagelist{"$category"}{"$name"}{'status'} = "Needed";
                }
            }
        }
        if ($DEBUG) {
            print STDERR 'INFO: Packages     (paccount): '
                . scalar( keys %{ ( $packagelist{'package'} ) } ) . "\n";
            print STDERR 'INFO: Optional     (optcount): '
                . scalar( keys %{ ( $packagelist{'optional'} ) } ) . "\n";
            print STDERR 'INFO: Recommended  (reccount): '
                . scalar( keys %{ ( $packagelist{'recommended'} ) } ) . "\n";
            print STDERR 'INFO: Security     (seccount): '
                . scalar( keys %{ ( $packagelist{'security'} ) } ) . "\n";
            print STDERR 'INFO: Unsupported  (uspcount): '
                . scalar( keys %{ ( $packagelist{'unsupported'} ) } ) . "\n";
            print STDERR 'INFO: Local Package(lspcount): '
                . scalar( keys %{ ( $packagelist{'local_package'} ) } )
                . "\n";
            use Data::Dumper;
            print STDERR Data::Dumper->Dump( [ \%packagelist ] );
        }
        if ( defined( $packagelist{'package'} )
            && ( scalar( keys %{ ( $packagelist{'package'} ) } ) ne 0 ) )
        {
            $update_avail = 1;
            $error        = check_errorcode('packages');
            $pacstr       = scalar( keys %{ ( $packagelist{'package'} ) } )
                . " package update(s);";
        }
        if ( defined( $packagelist{'optional'} )
            && ( scalar( keys %{ ( $packagelist{'optional'} ) } ) ne 0 ) )
        {
            $update_avail = 1;
            $error        = check_errorcode('optional');
            $optstr       = scalar( keys %{ ( $packagelist{'optional'} ) } )
                . " optional update(s);";
        }
        if ( defined( $packagelist{'recommended'} )
            && ( scalar( keys %{ ( $packagelist{'recommended'} ) } ) ne 0 ) )
        {
            $update_avail = 1;
            $error        = check_errorcode('recommended');
            $recstr = scalar( keys %{ ( $packagelist{'recommended'} ) } )
                . " recommended update(s);";
        }
        if ( defined( $packagelist{'security'} )
            && ( scalar( keys %{ ( $packagelist{'security'} ) } ) ne 0 ) )
        {
            $update_avail = 1;
            $error        = check_errorcode('security');
            $secstr       = scalar( keys %{ ( $packagelist{'security'} ) } )
                . " security update(s);";
        }
        if ( defined( $packagelist{'unsupported'} )
            && ( scalar( keys %{ ( $packagelist{'unsupported'} ) } ) ne 0 ) )
        {
            $update_avail = 1;
            $error        = check_errorcode('unsupported');
            $unsupstr = scalar( keys %{ ( $packagelist{'unsupported'} ) } )
                . " unsupported package(s);";
        }
        if ( defined( $packagelist{'local_package'} )
            && ( scalar( keys %{ ( $packagelist{'local_package'} ) } ) ne 0 )
            )
        {
            $update_avail = 1;
            $error        = check_errorcode('local_package');
            $local_pacstr
                = scalar( keys %{ ( $packagelist{'local_package'} ) } )
                . " local package(s);";

        }
        if ($update_avail) {
            $ret_str .= trim("$warnstr $secstr $recstr $optstr $pacstr $unsupstr $local_pacstr")." ";
            my @packagelist             = ();
            my @unsupported_packagelist = ();
            @loc_packagelist = ();
            if ($opt_v) {
                foreach my $cat (
                    'security',    'recommended',
                    'optional',    'package',
                    'unsupported', 'local_package'
                    )
                {
                    for my $key ( sort( keys %packagelist ) ) {
                        if ( "$key" eq "$cat" ) {
                            for my $name (
                                sort( keys %{ $packagelist{$cat} } ) )
                            {
                                if ( "$cat" eq "package" ) {
                                    push @packagelist,
                                        $packagelist{$cat}{$name}{'name'};
                                }
                                elsif ( "$cat" eq "unsupported" ) {
                                    push @unsupported_packagelist,
                                        $packagelist{$cat}{$name}{'name'};
                                }
                                elsif ( "$cat" eq "local_package" ) {
                                    push @loc_packagelist,
                                        $packagelist{$cat}{$name}{'name'};
                                }
                                else {
                                    $ret_str .= "\n$cat patch: "
                                        . $packagelist{$cat}{$name}{'name'};
                                }
                            }
                        }
                    }
                }
                $ret_str .= "\nPackages: " . join( ' ', sort(@packagelist) )
                    if @packagelist;
                $ret_str
                    .= "\nunsupported Packages: "
                    . join( ' ', sort(@unsupported_packagelist) )
                    if @unsupported_packagelist;
                $ret_str
                    .= "\nlocal Packages  : "
                    . join( ' ', sort(@loc_packagelist) )
                    if @loc_packagelist;
                $ret_str
                    .= "\nIgnored Patches : "
                    . join( ' ', @patchignore ) . " "
                    if @patchignore;
                $ret_str
                    .= "\nIgnored Packages: "
                    . join( ' ', @packageignore ) . " "
                    if @packageignore;
                if ( $#packagewhitelist lt 11 ) {
                    $ret_str
                        .= "\nUnsupported, ignored Packages: "
                        . join( ' ', sort(@packagewhitelist) ) . " "
                        if @packagewhitelist;
                }
                else {
                    $ret_str
                        .= "\nUnsupported, ignored Packages: $#packagewhitelist ";
                }
                if ( $#localwhitelist lt 11 ) {
                    $ret_str
                        .= "\nLocal, ignored Packages: "
                        . join( ' ', sort(@localwhitelist) ) . " "
                        if @localwhitelist;
                }
                else {
                    $ret_str
                        .= "\nLocal, ignored Packages: $#localwhitelist ";
                }

            }
        }
        else {
            $error   = "OK";
            $ret_str = "no updates available ";
            if ($opt_v) {
                $ret_str
                    .= "\nIgnored Patches : "
                    . join( ' ', @patchignore ) . " "
                    if @patchignore;
                $ret_str
                    .= "\nIgnored Packages: "
                    . join( ' ', @packageignore ) . " "
                    if @packageignore;
                if ( $#packagewhitelist lt 11 ) {
                    $ret_str
                        .= "\nUnsupported, ignored Packages: "
                        . join( ' ', @packagewhitelist ) . " "
                        if @packagewhitelist;
                }
                else {
                    $ret_str
                        .= "\nUnsupported, ignored Packages: $#packagewhitelist ";
                }
                if ( $#localwhitelist lt 11 ) {
                    $ret_str
                        .= "\nLocal, ignored Packages: "
                        . join( ' ', @localwhitelist ) . " "
                        if @localwhitelist;
                }
                else {
                    $ret_str
                        .= "\nLocal, ignored Packages: $#localwhitelist ";
                }
            }
        }
        $ret_str
            .= "| security="
            . scalar( keys %{ ( $packagelist{'security'} ) } )
            . ";;;; recommended="
            . scalar( keys %{ ( $packagelist{'recommended'} ) } )
            . ";;;; optional="
            . scalar( keys %{ ( $packagelist{'optional'} ) } )
            . ";;;; packages="
            . scalar( keys %{ ( $packagelist{'package'} ) } )
            . ";;;;\n"
            if ($opt_p);
    }
    close(FH);
    return ( "$ret_str", "$error" );
}

#######################################################################
# Main
#######################################################################

Getopt::Long::Configure('bundling');
GetOptions(
    "V"               => \$opt_V,
    "version"         => \$opt_V,
    "h"               => \$opt_h,
    "help"            => \$opt_h,
    "d"               => \$DEBUG,
    "debug"           => \$DEBUG,
    "i=s"             => \$opt_i,
    "ignore=s"        => \$opt_i,
    "w=s"             => \$opt_w,
    "warning=s"       => \$opt_w,
    "c=s"             => \$opt_c,
    "critical=s"      => \$opt_c,
    "f=s"             => \$opt_f,
    "releasefile=s"   => \$opt_f,
    "o"               => \$opt_o,
    "ignore_outdated" => \$opt_o,
    "p:0"             => \$opt_p,
    "no_perfdata:0"   => \$opt_p,
    "r"               => \$opt_r,
    "refresh_repos"   => \$opt_r,
    "t=i"             => \$opt_t,
    "timeout=i"       => \$opt_t,
    "l"               => \$opt_l,
    "check-local"     => \$opt_l,
    "u"               => \$opt_u,
    "check-vendor"    => \$opt_u,
    "v"               => \$opt_v,
    "verbose_output"  => \$opt_v,
    "s"               => \$opt_s,
    "use_sudo"        => \$opt_s,
) or print_help(2);

$TIMEOUT = $opt_t if ($opt_t);

# Just in case of problems, let's not hang Nagios
$SIG{'ALRM'} = sub {
    print "UNKNOWN - Plugin timed out\n";
    exit $ERRORS{'UNKNOWN'};
};
alarm($TIMEOUT);

if ($opt_V) {
    print_myrevision( $PROGNAME, "$VERSION" );
    exit $ERRORS{'OK'};
}

my $dist;

if ( "$opt_f" eq "$alt_releasefile" ) {
    $dist = get_distribution_from_os_release("$opt_f");
}
else {
    $dist = get_distribution("$opt_f");
}

if ($DEBUG) {
    use English;
    use Data::Dumper;
    print STDERR "INFO: check_zypper version: $VERSION\n";
    print STDERR "INFO: userid : " . getlogin() . "\n";
    foreach my $gid ( split( / /, "$GID" ) ) {
        print STDERR "INFO: groupid: " . getgrgid("$gid") . "\n";
    }
    print STDERR "INFO: got distname: $dist->{'name'}, distversion: ";
	print STDERR "$dist->{'version'}, distrelease: $dist->{'release'}";
    print STDERR " from $opt_f\n";
    print STDERR "INFO: " . Data::Dumper->Dump( [ \%supported_release ] );
}

my $version_release = $dist->{'version'};

$zypperopt = '--non-interactive --no-gpg-checks list-updates'
    if ( "$dist->{'version'}" eq "10.2" );
$zypperopt = '--xmlout --non-interactive list-updates --type package --type patch'
    if ( $dist->{'version'} gt 11.0 );

if ( "$dist->{'name'}" eq "SLE" ) {
    $version_release = "$dist->{'version'}.$dist->{'release'}";
    if ( ( "$dist->{'version'}" eq "10" ) && ( $dist->{'release'} gt 0 ) ) {
        $zypperopt = '--non-interactive --no-gpg-checks --terse list-updates';
    }
    else {
        $zypperopt
            = '--xmlout --non-interactive list-updates --type package --type patch';
    }
}

$use_sudo .= "$sudo" if ($opt_s);

if ($opt_h) {
    print_help();
    exit $ERRORS{'OK'};
}

if ($opt_i) {
    if ( !-r "$opt_i" ) {
        print "Updates CRITICAL - can't find file '$opt_i' - perhaps ";
		print "you should not use option '-i'?\n";
        exit $ERRORS{'CRITICAL'};
    }
    else {
        open( IGNORES, "<$opt_i" ) or die "Could not open $opt_i: $!\n";
        print "INFO: Ignoring the following patches/packages:\n" if ($DEBUG);
        while (<IGNORES>) {
            next if /^#/;
            next if /^\s*$/;
            chomp;
            if ( (/^patch:/) || (/^Patch:/) ) {
                my ( $foo, $toadd ) = split( ':', $_, 2 );
                $toadd =~ s/\s*//g;    # Patch names have no whitespaces
                print "INFO: + Patch  : $toadd\n" if ($DEBUG);
                push @patchignore, "$toadd";
            }
            elsif ( (/^package:/) || (/^Package:/) ) {
                my ( $foo, $toadd ) = split( ':', $_, 2 );
                $toadd =~ s/\s*//g;    # Package names have no whitespaces
                print "INFO: + Package: $toadd\n" if ($DEBUG);
                push @packageignore, "$toadd";
            }
            elsif ( (/^whitelist:/) || (/^Whitelist:/) ) {
                my ( $foo, $toadd ) = split( ':', $_, 2 );
                $toadd =~ s/\s*//g;    # Package names have no whitespaces
                print "INFO: + Whitelisting Package: $toadd\n" if ($DEBUG);
                push @packagewhitelist, "$toadd";
            }
            elsif ( (/^local_package:/) || (/^local package:/) ) {
                my ( $foo, $toadd ) = split( ':', $_, 2 );
                $toadd =~ s/\s*//g;    # Package names have no whitespaces
                print "INFO: + Whitelisting local Package: $toadd\n"
                    if ($DEBUG);
                push @localwhitelist, "$toadd";
            }
        }
        close(IGNORES);
    }
}

if ($opt_r) {
    my ( $ret_str, $error ) = refresh_zypper($dist);
    if ($error) {
        print "$ret_str\n";
        exit $ERRORS{'UNKNOWN'};
    }
}

alarm(0);

if ( check_zypper() ) {
    print "Updates UNKNOWN - system does not allow to execute zypper\n";
    exit $ERRORS{'UNKNOWN'};
}
else {
    my ( $ret_str, $error ) = check($dist);
    if ( $dist->{'name'} eq "Tumbleweed" ) {
        print STDERR "INFO: found Tumbleweed $version_release in ";
		print STDERR "\%supported_release\n";
        print STDERR "INFO: without parsing ";
		print STDERR "http://download.opensuse.org/tumbleweed/repo/oss/media.1/media ";
		print STDERR "I can not say more\n";
        print STDERR "INFO: at the moment. So a FIXME for the script - ";
		print STDERR "but until then, I don't be evil and say OK.\n";
    }
    elsif ( grep {/\Q$dist->{'name'}\E/} keys %supported_release ) {
        print STDERR "INFO: found $dist->{'name'} - checking supportstatus\n"
            if ($DEBUG);
        if (grep( { "$_" eq "$version_release" }
                @{ $supported_release{ $dist->{'name'} } } ) )
        {
            print STDERR
                "INFO: found $version_release for $dist->{'name'} in \%supported_release - OK\n"
                if ($DEBUG);
        }
        else {
            $ret_str
                = "discontinued OS Release $dist->{'name'} $version_release; "
                . $ret_str;
            $error = 'CRITICAL';
        }
    }
    else {
        $ret_str = "unknown OS Release $dist->{'name'}-$version_release; "
            . $ret_str;
        $error = 'UNKNOWN';
    }
    print "Updates $error : $ret_str";
    $exitcode = $ERRORS{$error};
    print STDERR "INFO: Exit-Code: " . $exitcode . "\n" if ($DEBUG);
    exit $exitcode;
}
