#!/usr/bin/perl -w
# zypper in perl-Text-Glob
use strict;
use File::Find;
use Text::Glob;
use DB_File;
use Fcntl qw(:DEFAULT);
our $indir=shift || "in";
our $outdir=shift || "packages";
our @list=();
our $binaryre;
our $maxaddsize = 0;

sub wanted
{
  push @list, $File::Find::name;
}

sub get_md5($)
{
  my $path = shift;
  my $dir = $path;
  $dir =~s(/[^/]+$)();
  my $file = $path;
  $file =~s(.*/)();
  open(my $f, "<", "$dir/MD5SUMS") or die "could not open $dir/MD5SUMS : $!";
  while(<$f>) {
    chomp;
    my @a=split(" ", $_);
    next unless $a[1] eq $file;
    return $a[0];
  }
  die "pre-computed MD5 value of $path not found"
}
sub get_cid($)
{
  my $path = shift;
  my $md5=get_md5($path);
  my %md5cid;
  tie(%md5cid, 'DB_File', "$ENV{HOME}/.cache/bmwiedemann-openSUSE-ipfs-md5-cid.dbm", O_RDWR|O_CREAT, 0666) or die "error opening DB: $!";
  my $cid=$md5cid{$md5};
  if(!$cid) {
    my $dontadd="";
    $dontadd="-n" if (-s $path > $maxaddsize);
    $cid=`ipfs add --cid-version 1 --raw-leaves -Q $dontadd $path`;
    chomp($cid);
    $md5cid{$md5}=$cid;
  }
  untie %md5cid;
  return $cid;
}

sub make_ipfs_link($$)
{
  my ($in, $out) = @_;
  #print "would ipfs $in -> $out\n";
  my $cid = get_cid($in);
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
    if($n =~ $binaryre or (-s $path > 15000000)) {
      make_ipfs_link($path, "$d/$n");
    } else {
      link($path, "$d/$n")
    }
  }
  #print "$n\n";
}

sub load_ignores()
{
  open(my $f, "<", "scripts/binary-list.txt") or die "$!";
  my @ignores = <$f>;
  foreach(@ignores) {chomp($_)}
  my $ignorerestr = join("|", map {"(?:".Text::Glob::glob_to_regex_string($_).'$)'} @ignores);
  $binaryre = qr(/$ignorerestr);
}

# main
load_ignores;
mkdir $outdir;
my $finddir=$indir;
$finddir .= "/".$ENV{PKG} if $ENV{PKG};
find(\&wanted, $finddir);
foreach(@list) {process($_)}
