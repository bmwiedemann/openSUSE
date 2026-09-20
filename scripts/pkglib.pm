# shared helpers for the package scripts: where a package lives in the
# monorepo, which ref holds its package repo, and where its pagure repo is
package pkglib;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT = qw(checkpkg pkgdir pkgref refpkg pagure_url EMPTY_TREE git_out git_ok);

use constant EMPTY_TREE => '4b825dc642cb6eb9a060e54bf8d69288fbee4904';
our $outdir = 'packages';

# a package name as OBS allows them; also what makes pkgref a valid ref
sub checkpkg($)
{
  my $pkg = shift;
  die "invalid package name '$pkg'\n"
    if $pkg eq "" or $pkg =~ m/[^a-zA-Z0-9._+-]/ or $pkg =~ m/^\./ or $pkg =~ m/\.\./ or $pkg =~ m/\.$/;
  return $pkg;
}

# packages/<first letter>/<pkg>, with lib* packages under packages/lib<x>/
sub pkgdir($)
{
  my $pkg = shift;
  my $first = lc(substr($pkg, 0, 1));
  if($pkg =~ /^lib./) {$first = lc($&)}
  return "$outdir/$first/$pkg";
}

# the ref that holds the package repo. The .git suffix keeps names like
# python-flufl.lock valid: no ref component may end in .lock
sub pkgref($)
{
  return "refs/pkg/".checkpkg(shift).".git";
}

# reverse of pkgref, also for the pkg-pushed and pkg-remote namespaces
sub refpkg($)
{
  my $ref = shift;
  $ref =~ s!^refs/pkg(?:-pushed|-remote)?/!! or return undef;
  $ref =~ s/\.git$// or return undef;
  return $ref;
}

sub pagure_url($)
{
  my $pkg = shift;
  my $base = $ENV{PAGURE_BASE} // "https://code.opensuse.org/package";
  return "$base/$pkg.git";
}

# stdout of a git command, chomped; undef when it failed
sub git_out
{
  open(my $fh, "-|", "git", @_) or die "git @_: $!";
  my $out = do { local $/; <$fh> };
  close($fh) or return undef;
  $out =~ s/\n\z// if defined $out;
  return $out;
}

sub git_ok
{
  return system("git", @_) == 0;
}

1;
