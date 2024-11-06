#!/usr/bin/perl
#

use strict;
sub is_prerelease($) {
  my $gem_version = shift;
  return ($gem_version =~ /[a-zA-Z]/);
}

sub get_release($) {
  my $gem_version = shift;
  my @release;

  my @splitted_version = split(/\./, $gem_version);
  push (@release, shift(@splitted_version));
  for my $element (@splitted_version) {
    last if $element !~ /\A\d+\z/;
    push(@release, $element);
  }
  return (\@release);
}

sub get_version_str($$) {
  my ($gem_version, $release_ref) = @_;

  my $release_str = join('.', @$release_ref);

  if (is_prerelease($gem_version)) {
    $gem_version =~ s/$release_str\./$release_str~/;
  };
  return ($gem_version);
}

sub handle_line($$$$$$) {
   my ($line, $ruby_abi, $ruby_abi_version, $gem_name, $gem_version, $mode) = @_;

   my $release_ref      = get_release($gem_version);
   my @release          = @$release_ref;
   my $gem_version_str  = get_version_str($gem_version, $release_ref);
   my @gem_sub_version;

   print ("rubygem($ruby_abi:$ruby_abi_version:$gem_name) = $gem_version_str\n");
   if ("provides" eq $mode) {
     print ("rubygem($gem_name) = $gem_version_str\n");

     for my $element (@release) {
       push(@gem_sub_version, $element);
       my $gem_sub_version_str = join('.', @gem_sub_version);
       print ("rubygem($ruby_abi:$ruby_abi_version:$gem_name:$gem_sub_version_str) = $gem_version_str\n");
     }
   }
}


my ($mode) = @ARGV;

if (not defined $mode) {
  die "Need to know if you want provides or conflicts\n";
}
my @modes = {conflicts => 1, provides => 1};
if (not $modes[$mode])  {
  die "No idea what to do with '$mode'\n";
}

# print(STDERR "Running $0 in $mode\n");
my $fh = *STDIN;
while ( ! eof($fh) ) {
  defined( my $line = readline $fh ) or die "readline failed: $!";
  if ($line =~ /(?<base_path>\/usr\/lib\d*\/ruby\/gems\/(?<ruby_abi_version>[^\/]+))\/specifications(?<has_default>\/default)?\/(?<gem_name>.+)-(?<gem_version>\d+\.[^-]+)\.gemspec\n\z/) {
    ## we only need need to conflict when we actually have conflicting files
    if ( ("provides" eq $mode ) || ( not(defined($+{has_default})) && "conflicts" eq $mode) ) {
      handle_line($line, 'ruby', $+{ruby_abi_version}, $+{gem_name}, $+{gem_version}, $mode);
    }
  };
}

