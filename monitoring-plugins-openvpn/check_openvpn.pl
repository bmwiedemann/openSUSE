#!/usr/bin/perl -w

#######################################################################
#
# Copyright (c) 2007 Jaime Gascon Romero <jgascon@gmail.com>
#
# License Information:
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# $Id: check_openvpn.pl,v 1.0 2007/07/15 16:07:20 jgr Exp jgr $
# $Revision: 1.0 $
# Home Site: http://emergeworld.blogspot.com/
# #####################################################################

use diagnostics;
use strict;
use Net::Telnet ();
use Getopt::Long qw(:config no_ignore_case);
use vars qw($PROGNAME $VERSION);
use lib "/usr/nagios/libexec";
use utils qw(%ERRORS);

$PROGNAME = "check_openvpn";
$VERSION = '$Revision: 1.0 $';

$ENV{'PATH'}='';
$ENV{'BASH_ENV'}=''; 
$ENV{'ENV'}='';

my ($opt_h, $opt_H, $opt_p, $opt_P, $opt_t, $opt_i, $opt_n, $opt_c, $opt_w, $opt_C, $opt_r);

sub print_help ();
sub print_usage ();

GetOptions
  ("h"  =>  \$opt_h, "help" => \$opt_h,
   "H=s" => \$opt_H, "host=s"  => \$opt_H,
   "p=i" => \$opt_p, "port=i" => \$opt_p,
   "P=s" => \$opt_P, "password=s" => \$opt_P,
   "t=i" => \$opt_t, "timeout=i" => \$opt_t,
   "i"  =>  \$opt_i, "ip" => \$opt_i,
   "n" => \$opt_n, "numeric" => \$opt_n,
   "c" => \$opt_c, "critical" => \$opt_c,
   "w" => \$opt_w, "warning" => \$opt_w,
   "C=s" => \$opt_C, "common_name=s" => \$opt_C,
   "r=s" => \$opt_r, "remote_ip=s" => \$opt_r,
  ) or exit $ERRORS{'UNKNOWN'};

# default values
unless ( defined $opt_t ) {
   $opt_t = 10;
}

if ($opt_h) {print_help(); exit $ERRORS{'OK'};}

if ( ! defined($opt_H) || ! defined($opt_p) ) {
  print_usage();
  exit $ERRORS{'UNKNOWN'}
}

my @lines;
my @clients;
my @clients_ip;
my $t;

eval { 
$t = new Net::Telnet (Timeout => $opt_t,
                      Port => $opt_p,
                      Prompt => '/END$/'
                    );
$t->open($opt_H);
if ( defined $opt_P ) {
  $t->waitfor('/ENTER PASSWORD:$/');
  $t->print($opt_P);
}
$t->waitfor('/^$/');
@lines = $t->cmd("status 2");
$t->close;
};

if ($@) {
 print "OpenVPN Critical: Can't connect to server\n";
 exit $ERRORS{'CRITICAL'};
}


if (defined $opt_i || defined $opt_r) {
  foreach (@lines) {
    if ($_ =~ /CLIENT_LIST,.*,(\d+\.\d+\.\d+\.\d+):\d+,/) {
      push @clients_ip, $1;
    }
}
  if (defined $opt_i) {
    print "OpenVPN OK: "."@clients_ip ";
    exit $ERRORS{'OK'};
  } elsif (defined $opt_r) {
    if ( ! grep /\b$opt_r\b/, @clients_ip) {
      if (defined $opt_c) {
        print "OpenVPN CRITICAL: $opt_r don't found";
        exit $ERRORS{'CRITICAL'};
      } else {
        print "OpenVPN WARNING: $opt_r don't found";
        exit $ERRORS{'WARNING'};
      }
    }
    print "OpenVPN OK: "."@clients_ip ";
    exit $ERRORS{'OK'};
  }
}

foreach (@lines) {
  if ($_ =~ /CLIENT_LIST,(.*),\d+\.\d+\.\d+\.\d+:\d+,/) {
    push @clients, $1;
  }
}

if (defined $opt_C) {
  if ( ! grep /\b$opt_C\b/, @clients) {
    if (defined $opt_c) {
      print "OpenVPN CRITICAL: $opt_C don't found";
      exit $ERRORS{'CRITICAL'};
    } else {
      print "OpenVPN WARNING: $opt_C don't found";
      exit $ERRORS{'WARNING'};
    }
  }
}


if (defined $opt_n) {
print "OpenVPN OK: ".@clients." connected clients.";
exit $ERRORS{'OK'};
}

print "OpenVPN OK: "."@clients ";
exit $ERRORS{'OK'};

#######################################################################
###### Subroutines ####################################################

sub print_usage() {
  print "Usage: $PROGNAME -H | --host <IP or hostname> -p | --port <port number> [-P | --password] <password> [-t | --timeout] <timeout in seconds> 
                    [-i | --ip] [-n | --numeric] [-C | --common_name] <common_name> [-r | --remote_ip] <remote_ip> [-c | --critical] [-w | --warning]\n\n";
  print "       $PROGNAME [-h | --help]\n";
}

sub print_help() {
  print "$PROGNAME $VERSION\n\n";
  print "Copyright (c) 2007 Jaime Gascon Romero

Nagios plugin to check the clients connected to a openvpn server.

";
 print_usage();
  print "
-H | --host
  IP address or hostname of the openvpn server.

-p | --port
  Management port interface of the openvpn server.

-P | --password
  Password for the management interface of the openvpn server.

-t | --timeout
  Timeout for the connection attempt. Optional, default 10 seconds.


        Optional parameters
        ===================

-i | --ip
  Prints the IP address of the remote client instead of the common name.

-n | --numeric
  Prints the number of clients connected to the openvpn server.


        Matching Parameters
        ===================

-C | --common_name
  The common name, as it is specified in the client certificate, who is wanted to check.

-r | --remote_ip
  The client remote ip address who is wanted to check.

-c | --critical
  Exits with CRITICAL status if the client specified by the common name or the remote ip address is not connected.

-w | --warning
  Exits with WARNING status if the client specified by the common name or the remote ip address is not connected.


       Other Parameters
       ================

-h | --help
  Show this help.
";

}

# vim:sts=2:sw=2:ts=2:et
