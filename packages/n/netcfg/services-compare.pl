#!/usr/bin/perl -w

use strict;

my $sfile = 'services';
my $snewfile = 'services.new';

my %s;
my %snew;

parse_services_file($sfile, \%s);
parse_services_file($snewfile, \%snew);

my @preserved_pairs;
my @services_changing_port;
my @services_renamed;
my @removed_pairs;
my @new_pairs;

BEGINLOOP: foreach my $port (keys %s)
{
  if (exists($snew{$port}) and $snew{$port} eq $s{$port})
  {
    # service port pair preserved
    push(@preserved_pairs, "$snew{$port} $port");
    next BEGINLOOP;
  }

  foreach my $portnew (keys %snew)
  {
    if ($snew{$portnew} eq $s{$port} and protocol($portnew) eq protocol($port))
    {
      push(@services_changing_port, "$snew{$portnew} $port -> $portnew");
      next BEGINLOOP;
    }
  }

  if (exists($snew{$port})) # and $snew{$port} ne $s{$port} and service don't use another port
  {
    push(@services_renamed, "$s{$port} -> $snew{$port} ($port)");
  }
  else
  {
    push(@removed_pairs, "$s{$port} $port");
  }
}

my $string_scp = join(" ", @services_changing_port);

foreach my $portnew (keys %snew)
{
  if (not exists($s{$portnew}))
  {
    if (index($string_scp, $snew{$portnew}) == -1)
    {
      push(@new_pairs, "$snew{$portnew} $portnew");
    }
  }
}

print_pairs("Removed pairs", sort (@removed_pairs));
print_pairs("Renamed or replaced services", sort (@services_renamed));
print_pairs("Services, that changed port", sort (@services_changing_port));
print_pairs("New pairs", sort (@new_pairs));
print_pairs("Preserved pairs", sort (@preserved_pairs));

sub print_pairs
{
  my $heading = shift;
  my @pairs = @_;
  print "\n";
  print "$heading\n";
  my $underline = ('-' x length($heading));
  print $underline, "\n";
  foreach my $pair (@pairs)
  { print $pair,"\n"; }
}

sub protocol
{
  my $port = shift;
  $port =~ s/.*\///;
  return $port;
}

sub parse_services_file
{
  my $filename = shift;
  my $hashref = shift;

  open(FILE, $filename) or die "cannot read $filename\n";
  while (<FILE>)
  {
    chomp;
    $_ =~ s/#.*//;
    if ($_)
    { 
      # my ($service, $port) = split(/[ \t]+/, $_); is not sufficient because of errors in xml like 
      #       Apple Remote Desktop (Net Assistant) 3283/tcp     # Net Assistant (updated 2011-11-09) [Michael_Stein]
      my $service = my $port = $_;
      $service =~ s:[ \t]+[0-9]+/[a-z]+.*$::;
      $port =~ s:^.*[ \t]+([0-9]+/[a-z]+).*$:$1:;
      $hashref->{$port} = $service;
#      printf "[%s] [%s]\n", ($service, $port);
    }
  }

  close(FILE);
}


