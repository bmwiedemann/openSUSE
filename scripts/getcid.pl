#!/usr/bin/perl -w
use strict;
use DB_File;
use Digest::MD5;
our $maxaddsize = 0;

sub get_md5($)
{
  my $path = shift;
  open(my $fd, "<", $path) or die $!;
  my $ctx = Digest::MD5->new;
  $ctx->addfile($fd);
  return $ctx->hexdigest;
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

print "/ipfs/",get_cid(shift),"\n";
