#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper;
use JSON;
use LWP::UserAgent;

open(SPEC, '<vim-plugins.spec') or die "cannot open spec";
my $spec;
{
	local $/ = undef;
	$spec = <SPEC>;
}
close(SPEC);

my $child = open(SPEC, '-|', qw|rpm -E|, $spec) // die "cannot run rpm";
exit 0 unless ($child);

my $ua = LWP::UserAgent->new;
my $json = JSON->new->allow_nonref;

while (<SPEC>) {
	chomp;
	my ($org, $repo, $rel, $ver) = (m@^Source\d+:\s+https://github\.com/([^/]+)/([^/]+)/(?:archive/refs/tags|releases/download/([^/]+))/([^/]+)\.tar\.gz#@);
	next unless defined $ver;
	$ver = $rel if defined $rel;

	my $req_url = defined $rel ? 'releases/latest' : 'tags';
	my $req = HTTP::Request->new(GET => "https://api.github.com/repos/$org/$repo/$req_url");
	my $res = $ua->request($req);
	die "bad HTTP reply for $org/$repo -- \"" . $res->status_line . '"' unless ($res->is_success);

	my $j = $json->decode($res->content);
	$j = @{$j}[0] unless (defined $rel);
	my $ver2 = $j->{'name'} || $j->{'tag_name'};

	if ($ver2 ne $ver) {
		print "$org, $repo, $ver -> $ver2\n";
	}
}
close(SPEC);

1;
