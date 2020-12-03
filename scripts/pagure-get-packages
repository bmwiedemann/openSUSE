#!/usr/bin/perl -w
# zypper in perl-libwww-perl perl-LWP-Protocol-https perl-JSON-XS
use strict;
use LWP::Simple;
use JSON::XS;

sub process($)
{ my $url = shift;
    while($url) {
	my $json = get($url);
	my $data = decode_json($json);
	for my $p (@{$data->{projects}}) {
	    print $p->{name},"\n";
	}
	$url = $data->{pagination}->{next};
    }
}
process("https://code.opensuse.org/api/0/projects?namespace=package&short=1&per_page=100");
