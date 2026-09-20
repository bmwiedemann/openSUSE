#!/usr/bin/perl -w
# Map the rsync copy of Factory in $indir to $outdir/<letter>/<pkg>/, like
# rsync would: source files are hardlinked, binaries become symlinks into
# ipfs, entries with no counterpart in the source are removed, and nothing
# that is already right is touched. With PKG set only that package is done.
# zypper in perl-Text-Glob
use strict;
use File::Find;
use File::Path qw(remove_tree);
use Text::Glob;
use DB_File;
use Fcntl qw(:DEFAULT);
use FindBin;
use lib $FindBin::Bin;
use pkglib;
our $indir=shift || "in";
our $outdir=shift || "packages";
$pkglib::outdir = $outdir;
our $binaryre;
our $maxaddsize = 0;
our %md5cid;

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
  my $cid=$md5cid{$md5};
  if(!$cid) {
    my $dontadd="";
    $dontadd="-n" if (-s $path > $maxaddsize);
    $cid=`ipfs add --cid-version 1 --raw-leaves -Q $dontadd $path`;
    chomp($cid);
    die "ipfs add failed for $path" unless $cid;
    $md5cid{$md5}=$cid;
  }
  return $cid;
}

sub is_binary($)
{
  my $path = shift;
  return ($path =~ $binaryre or (-s $path > 15000000));
}

# make $out the mapping of $in, touching nothing that already is
sub map_entry($$)
{
  my ($in, $out) = @_;
  if(-d $in) {
    if(-l $out or (-e $out and !-d $out)) { unlink($out) or die "unlink $out: $!" }
    -d $out or mkdir($out) or die "mkdir $out: $!";
  } elsif(is_binary($in)) {
    my $target = "/ipfs/".get_cid($in);
    return if -l $out and readlink($out) eq $target;
    if(-l $out or -e $out) {
      -d $out ? remove_tree($out) : unlink($out) or die "unlink $out: $!";
    }
    symlink($target, $out) or die "symlink $out: $!";
  } else {
    my @sin = lstat($in);
    my @sout = lstat($out);
    return if @sout and $sin[0] == $sout[0] and $sin[1] == $sout[1];
    if(@sout) {
      -d _ ? remove_tree($out) : unlink($out) or die "unlink $out: $!";
    }
    link($in, $out) or die "link $in $out: $!";
  }
}

sub remove_pkgdir($)
{
  my $dir = shift;
  if(-d "$dir/.git") {
    warn "$dir holds a .git - not removing it\n";
    return;
  }
  remove_tree($dir);
  my $letterdir = $dir;
  $letterdir =~ s(/[^/]+$)();
  rmdir($letterdir); # only succeeds when it was the last package there
}

sub sync_pkg($)
{
  my $pkg = shift;
  my $src = "$indir/$pkg";
  my $dst = pkgdir($pkg);
  my $letterdir = $dst;
  $letterdir =~ s(/[^/]+$)();
  if(!-d $src or -l $src) { # a symlink would map to an empty package
    remove_pkgdir($dst) if -d $dst;
    return;
  }
  -d $letterdir or mkdir($letterdir) or die "mkdir $letterdir: $!";
  map_entry($src, $dst);
  my %want;
  find({no_chdir => 1, wanted => sub {
    my $rel = substr($File::Find::name, length($src));
    return if $rel eq "";
    $rel =~ s(^/)();
    return if $rel =~ m(^MD5SUMS(?:\.meta)?$);
    $want{$rel} = 1;
    map_entry($File::Find::name, "$dst/$rel");
  }}, $src);
  # rsync --delete: drop what the source no longer has, deepest first
  find({no_chdir => 1, bydepth => 1, wanted => sub {
    my $rel = substr($File::Find::name, length($dst));
    return if $rel eq "";
    $rel =~ s(^/)();
    return if $want{$rel};
    if(-d $File::Find::name and !-l $File::Find::name) {
      rmdir($File::Find::name);
    } else {
      unlink($File::Find::name) or die "unlink $File::Find::name: $!";
    }
  }, preprocess => sub { grep {$_ ne ".git"} @_ }}, $dst);
}

sub load_ignores()
{
  open(my $f, "<", "$FindBin::Bin/binary-list.txt") or die "$!";
  my @ignores = <$f>;
  foreach(@ignores) {chomp($_)}
  my $ignorerestr = join("|", map {"(?:".Text::Glob::glob_to_regex_string($_).'$)'} @ignores);
  $binaryre = qr(/$ignorerestr);
}

# main
load_ignores;
tie(%md5cid, 'DB_File', "$ENV{HOME}/.cache/bmwiedemann-openSUSE-ipfs-md5-cid.dbm", O_RDWR|O_CREAT, 0666) or die "error opening DB: $!";
-d $outdir or mkdir($outdir) or die "mkdir $outdir: $!";
if($ENV{PKG}) {
  sync_pkg(checkpkg($ENV{PKG}));
} else {
  opendir(my $dh, $indir) or die "opendir $indir: $!";
  my %inpkgs = map {$_ => 1} grep {!/^\./} readdir($dh);
  closedir($dh);
  sync_pkg($_) for sort keys %inpkgs;
  for my $dir (glob("$outdir/*/*")) {
    my $pkg = $dir;
    $pkg =~ s(.*/)();
    next if $inpkgs{$pkg} and $dir eq pkgdir($pkg);
    remove_pkgdir($dir);
  }
}
untie %md5cid;
