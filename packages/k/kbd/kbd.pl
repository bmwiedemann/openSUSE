#! /usr/bin/perl -w
#
# simple script to switch the keyboard language
# (c) 2014 jw@owncloud.om

my $sysconffile = '/etc/vconsole.conf';
my $mapdir = '/usr/share/kbd/keymaps/xkb';

my $version = '1.0';

my $what = shift || '-h';


my $v = slurp_sysconf($sysconffile);
my $m = find_maps();

my $l = {
  'english' => 'us.map',
  'german'  => 'de-latin1-nodeadkeys.map',
  'french'  => 'fr-latin1.map',
  'spanish' => 'es.map',
  'italian' => 'it.map',
  'dutch'   => 'nl.map',
};

for my $k (keys %$l)
  {
    # zap non-installed languages from our pretty printed list.
    delete $l->{$k} unless $m->{$l->{$k}} or $m->{"$l->{$k}.gz"};
  }

if ($what eq '-h')
  {
    print qq{kbd Version $version

Usage: $0 [option] [mapping]

Available options are:
  -l	list typical language mappings.
  -a	list all maps
  -h	print this usage

Specify as a mapping either a language name (seen with -l)
or a mapping name (seen with -a). For a mapping name, add a .map suffix.

Current keymap: $v->{KEYTABLE}
};
    exit 0;
  }
  
if ($what eq '-l')
  {
    for my $k (sort keys %$l)
      {
        printf "%-10s %s\n",  $k, $l->{$k};
      }
    exit 0;
  }

if ($what eq '-a' || $what eq '-m')
  { 
    my @k = map { $1 if /(.*).map(.gz)?$/ } sort keys %$m;
    print "current keymap: $v->{KEYTABLE}\n";
    print "available keymaps: @k\n";
    print "\n\nuse '$0 MAPNAME' to change.\n";
    exit 0;
  }

$what = $l->{$what} if $l->{$what};

$what = "$what.gz"     if $m->{"$what.gz"};
$what = "$what.map"    if $m->{"$what.map"};
$what = "$what.map.gz" if $m->{"$what.map.gz"};

die "$what: keymap not found.\n Try $0 -h\n" unless $m->{$what};

write_sysconf($sysconffile, { 'KEYMAP' => $what } );
# system("kbd_mode -u");		# switch to unicode. Should be the default anyway.
system("loadkeys $what");	# now set the keymap.

# FIXME: is that all?
# mayb also do: systemctl restart kbd.service 

exit 0;
###################################################################

sub find_maps
{
  my $maps;

  opendir DIR, $mapdir or die "$0: cannot readdir $mapdir: !$\n";
  my @d = grep { -d "$mapdir/$_" && !/^\./ } readdir DIR;
  closedir DIR;
  for my $d (@d)
    {
      opendir DIR, "$mapdir/$d" or die "$0: cannot readdir $mapdir/$d: !$\n";
      my @f = grep { /\.map(.gz)?$/ } readdir DIR;
      closedir DIR;
      for my $f (@f)
        {
          $maps->{$f} = "$d/$f";
        }
    }
  return $maps;
}

sub slurp_sysconf
{
  my ($file) = @_;
  
  my $vals;
  open my $fd, "<", $file or die "$0: cannot read config file $file: $!\n";
  while (defined(my $line = <$fd>))
    {
      chomp $line;
      $vals->{$1} = $2 if $line =~ m{^([A-Z_]+)\s*=\s*"(.*)"};
    }
  close $fd; 
  return $vals;
}

sub write_sysconf
{
  my ($file, $vals) = @_;
  
  my @sysconf = ();
  open my $fd, "<", $file or die "$0: cannot read config file $file: $!\n";
  while (defined(my $line = <$fd>))
    {
      chomp $line;
      push @sysconf, $line;
    }
  close $fd; 
  open $fd, ">", $file or die "$0: cannot write config file $file: $!\n";
  for my $line (@sysconf)
    {
      if ($line =~ m{^([A-Z_]+)\s*=\s*"(.*)"})
        {
           my ($keyword,$value) = ($1,$2);
           if (defined $vals->{$keyword})
             {
               $line =~ s{\Q$value\E}{$vals->{$keyword}};
             }
        }
      print $fd "$line\n";
    }
  close $fd or die "$0: could not write config file $file: $!\n";
}
