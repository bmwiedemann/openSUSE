#!/usr/bin/perl
use warnings;
use strict;
use Getopt::Long;
my $VERSION = '0.002';

my $options = {
	'procnet' => '/proc/net',
	};

sub version {
	print "$VERSION\n";
}
sub help {
	my $name = $1 if $0 =~ /\/([^\/]+)$/;
	print <<FOO;
$name [ --procnet <dir> ] [ --hel p ] [ --version ]

  --procnet <dir> 	- Direcotry where proc/net lives, normally /proc/net
  --help		- help (this screen)
  --version		- get version information

This script attempts to read the proc interface to the Linux kernel bonding driver, and 
determine if the bonded interfaces are optimal. It will wanr if any of the enslaved devices 
are not 'up' (exit 1), and if any bonded interfaces are not active at all (exit 2). This 
script is suitable for feeding to NRPE for Nagios (or similar) to check.

This script is distributed under the Artistic and Gnu Public Licences.
 
Version: $VERSION.
(c) 2004 Fotango Limited. http://opensource.fotango.com/.
Written by James Bromberger <jbromberger_AT_fotango.com>
FOO
}

sub read_proc_bond {
	my $file = shift;
	return unless -r $file;
	open F, $file or die "Cannot read $file";
	my $data;
	while (<F>) {
		$data->{'version'} = $1 if /^Ethernet Channel Bonding Driver: (.+)$/;
		$data->{'mode'} = $1 if /^Bonding Mode: (.+)$/;
		$data->{'primary'} = $1 if /^Primary Slave: (.+)$/;
		$data->{'active'} = $1 if /^Currently Active Slave: (.+)$/;
		$data->{'status'} = $1 if /^MII Status: (\S+)$/;
		$data->{'polling'} = $1 if /^MII Polling Interval \(ms\): (\S+)$/;
		$data->{'up-delay'} = $1 if /^Up Delay \(ms\): (\S+)$/;
		$data->{'down-delay'} = $1 if /^Down Delay \(ms\): (\S+)$/;
		if (/^Slave Interface: (.+)$/) {
			my $slave = $1;
			while (($_ = <F>||"") !~ /^$/) {
				$data->{'slaves'}->{$slave}->{'mii'} = $1 if /^MII Status: (.+)$/;
				$data->{'slaves'}->{$slave}->{'failure-count'} = $1 if /^Link Failure Count: (.+)$/;
				$data->{'slaves'}->{$slave}->{'actor-churn'} = $1 if /^Actor Churn State: (.+)$/;
				$data->{'slaves'}->{$slave}->{'partner-churn'} = $1 if /^Partner Churn State: (.+)$/;
				}
			}
		}
	close F;
	return $data;
	}


sub check_bond {
	my $file = shift;
	my $interface_name = shift;
	my $data = read_proc_bond($file);
	return (0, "Unable to read bond information") unless $data;
	my $error = 0;
	my $config_str;
	my $status = $data->{'status'};
	if (defined $data->{'slaves'}) {
		foreach (keys %{$data->{'slaves'}}) {
			$status = "warn" if $data->{'slaves'}->{$_}->{'actor-churn'}
						&& $data->{'slaves'}->{$_}->{'actor-churn'} eq "churned";
			$status = "warn" if $data->{'slaves'}->{$_}->{'partner-churn'}
						&& $data->{'slaves'}->{$_}->{'partner-churn'} eq "churned";
		}
	}
	if (defined $data->{'active'}) {
		$config_str = sprintf "$interface_name %s on %s: members =", $data->{'status'}, $data->{'active'} ;
	} elsif (defined $data->{'slaves'}) {
		$config_str = sprintf "$interface_name %s: members =", $status;
	} else {
		$config_str = sprintf "$interface_name %s has no physical devices", $data->{'status'};
		$error = 1;
	}
	foreach (keys %{$data->{'slaves'}}) {
		my $result = $data->{'slaves'}->{$_}->{'mii'};
		$result = "churned" if $data->{'slaves'}->{$_}->{'actor-churn'}
	       				&& $data->{'slaves'}->{$_}->{'actor-churn'} ne 'none';
		$result = "churned" if $data->{'slaves'}->{$_}->{'partner-churn'}
	       				&& $data->{'slaves'}->{$_}->{'partner-churn'} ne 'none';
		$config_str.= " $_ (" . $result . ")";
		$error = 1 unless $data->{'slaves'}->{$_}->{'mii'} eq 'up';
		$error = 1 if $data->{'slaves'}->{$_}->{'actor-churn'}
	       			&& $data->{'slaves'}->{$_}->{'actor-churn'} ne 'none';
		$error = 1 if $data->{'slaves'}->{$_}->{'partner-churn'}
	       			&& $data->{'slaves'}->{$_}->{'partner-churn'} ne 'none';
		$error = 2 if ($data->{'status'} ne 'up');
	}
	return $error, $config_str;
	}


sub find_bonds {
	my $dir = shift;
	return unless -r $dir;
	# $dir = '/proc/net';
	my $bonds;
	if (-r "$dir/bonding") {
		opendir D, "$dir/bonding" or die "Cannot open dir: $dir/bonding";
		map {$bonds->{$_} = "$dir/bonding/$_"} grep /^bond/, readdir D;
		closedir D;
		}
	opendir D, "$dir" or die "Cannot open dir: $dir";
	map {$bonds->{$_} = "$dir/$_/info" if -r "$dir/$_/info"} grep /^bond/, readdir D;
	closedir D;
	my $err = 0;
	my $message;
	foreach (keys %{$bonds}) {
		my ($this_error, $this_message) = check_bond($bonds->{$_}, $_);
		$err = $this_error if $this_error;
		$message.= $this_message . " ";
		}
	if (not $message) {
		$message = "No bond information found";
		$err = 1;
		}
	print "$message\n";
	exit $err;
	}


GetOptions($options, "procnet=s", "help", "version");
if(defined $options->{'help'}) {
	help();
	exit;
	}
elsif (defined $options->{'version'}) {
	version();
	exit;
}
find_bonds($options->{'procnet'});
