#!/usr/bin/perl -w
# zypper in perl-Text-Glob
use strict;
use File::Find;
use Text::Glob;
our $indir=shift || "in";
our $outdir=shift || "packages";
our @list=();
our $binaryre;

sub wanted
{
  push @list, $File::Find::name;
}

sub make_ipfs_link($$)
{
  my ($in, $out) = @_;
  #print "would ipfs $in -> $out\n";
  my $dontadd="";
  $dontadd="-n" if (-s $in > 9000*1024);
  my $cid=`ipfs add --cid-version 1 --raw-leaves -Q $dontadd $in`;
  chomp($cid);
  symlink("/ipfs/$cid", $out);
}

sub process($) {
  my $path = shift;
  my $n = $path;
  return if ($n=~m(/MD5SUMS(?:\.meta)?$));
  $n=~s/^$indir\///;
  my $first=lc(substr($n, 0, 1));
  if($n=~/^lib./) {$first=lc($&)}
  my $d="$outdir/$first";
  #like system(qw(cp -al)... );
  if(-d $path) {
    mkdir $d;
    mkdir "$d/$n"
  } else {
    if($n =~ $binaryre) {
      make_ipfs_link($path, "$d/$n");
    } else {
      link($path, "$d/$n")
    }
  }
  #print "$n\n";
}

sub load_ignores()
{
  open(my $f, "< binary-list.txt") or die "$!";
  my @ignores = <$f>;
  foreach(@ignores) {chomp($_)}
  my $ignorerestr = join("|", map {"(?:".Text::Glob::glob_to_regex_string($_).'$)'} @ignores);
  $binaryre = qr(/$ignorerestr);
}

# main
load_ignores;
mkdir $outdir;
find(\&wanted, $indir);
foreach(@list) {process($_)}
