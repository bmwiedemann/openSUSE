#!/usr/bin/perl -w
#
# unsquid v0.2 -- Squid object dumper.
#   Copyright (C) 2000 Avatar <avatar@deva.net>.
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110-1335, USA
#
# $Id: unsquid,v 1.4 2000/03/11 17:31:06 avatar Exp $

=pod

=head1 NAME

unsquid - dump Squid objects

=head1 SYNOPSIS

B<unsquid> S<[ B<-d>I<dir> ]>
S<[ B<-t>I<type> ]>
S<[ B<-fv> ]>
S<[ B<-Vh> ]>

=head1 DESCRIPTION

unsquid dumps Squid cache files specified on the command line into
directories reflecting their original URLs, hence preserving the
original site layouts for off-line browsing.

Typically usage is

	find /usr/local/squid/cache/??/ -type f -print | \
		xargs unsquid -t 'image/.*' -d /tmp

The command line options are explained below.

=over

=item B<-t>I<type> S<B<--type> I<dir>>

Dump only files matching the MIME type regex I<type>.

=item B<-f> B<--force>

Overwrite existing files.  For security reason, this option is disabled
when run as root.

=item B<-v> B<--verbose>

Print the URLs of dumped objects.

=item B<-d>I<dir> S<B<--dest> I<dir>>

Dump the files inside I<dir>.

=item B<-V> B<--version>

Print the version number.

=item B<-h> B<--help>

Print a summary of command line options.

=back

=head1 AUTHOR

Avatar <F<avatar@deva.net>>

=cut

use POSIX;
use Getopt::Long;
use strict;

my $help = <<EOT;
Usage: $0 [OPTION]... FILE...
Dumps Squid objects.

  -t, --type TYPE           only dump objects matching the regex TYPE
  -v, --verbose             print dumped object urls
  -f, --force               overwrite existing files
  -d, --dest DIR            use DIR as the destination directory for dumping
  -V, --version             print the version string
  -h, --help                show this help
EOT

my ($type, $size, $force, $verbose, $showver, $showhelp);
my $destdir = ".";
my $defaultindex = "index.html";

Getopt::Long::Configure("no_ignore_case");
GetOptions("dest=s" => \$destdir,
	"type=s" => \$type,
	"verbose|v+" => \$verbose,
	"force!" => \$force,
	"version|V" => \$showver,
	"help" => \$showhelp);

if ($showver) {
	print <<EOT;
Unsquid version 0.2

Copyright (C) 2000 Avatar <avatar\@deva.net>.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE,
to the extent permitted by law.
EOT
	exit;
}

if ($#ARGV < 0 or $showhelp) {
	print $help;
	exit;
}

if ($force and $< == 0) {
	die "$0: root is not allowed to use the force option";
}

for (@ARGV) {
	my ($url, $urllen);

	# read 4 bytes from offset 56 as the length of the url
	open(INFILE, "<$_") or die "$0: cannot open file $_ for reading: $!";
	seek(INFILE, 56, SEEK_SET) or die "$0: cannot seek 56 bytes: $!";
	read(INFILE, $urllen, 4) or die "$0: cannot read 4 bytes: $!";
	$urllen = ord($urllen) - 1; # kill the last NUL

	# read the url
	read(INFILE, $url, $urllen);

	# expand index urls
	$url =~ s-/$-/$defaultindex-m;

	# scan the contents
	my ($seenheader);
	while (<INFILE>) {
		if ($seenheader) {
			print OUTFILE;
			next;
		}

		# if type is specified, do matching
		if (/^Content-Type: /i and defined $type) {
			m-[^:]*: (\w+/\w+)-;
			last if $1 !~ /$type/;
			next;
		}

		# at this point we must have matched the type
		if (/^\r$/) {
			$seenheader = 1;

			makedir($url);
			if (! defined $force and -e "$destdir/$url") {
				warn "$0: file $destdir/$url exists, skipped";
				last;
			}
			open(OUTFILE, ">$destdir/$url")
				or die "$0: cannot open file $destdir/$url for writing: $!";
			print "$url\n" if $verbose;
		}
	}
	close(INFILE);
	close(OUTFILE);
}

sub makedir {
	my ($basename) = @_;
	my $path = $destdir;

	if (! -d $destdir) {
		warn "$0: destination directory $destdir does not exist, making it";
		mkdir $destdir, 0777 or die "$0: cannot mkdir $destdir: $!";
	}

	while( $basename =~ m-^([^/]*)/- ) {
		$path .= "/".$1;
		if (! -d $path) {
			if (! mkdir $path, 0777) {
				if (-f $path) {
					# move the file in
					open FILE, $path
						or die "$0: cannot open $path for reading: $!";
					undef $/;
					my $buf = <FILE>;
					$/ = "\n";
					close FILE;
					unlink $path;

					mkdir $path, 0777
						or die "$0: cannot make directory $path: $!";

					open FILE, ">$path-redirect"
						or die "$0: cannot open $path/$defaultindex for writing: $!";
					print FILE $buf;
					close FILE;
				} else {
					die "d$0: cannot mkdir $path: $!";
				}
			}
		}
		$basename = $';
	}
}
