#
# spec file for package perl-Test-LWP-UserAgent
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Test-LWP-UserAgent
Name:           perl-Test-LWP-UserAgent
Version:        0.36.0
Release:        0
# 0.036 -> normalize -> 0.36.0
%define cpan_version 0.036
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        LWP::UserAgent suitable for simulating and testing network calls
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Warnings) >= 0.9
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.620
BuildRequires:  perl(namespace::clean) >= 0.190
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response)
Requires:       perl(HTTP::Status)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Safe::Isa)
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.620
Requires:       perl(namespace::clean) >= 0.190
Requires:       perl(parent)
Provides:       perl(Test::LWP::UserAgent) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is a subclass of LWP::UserAgent which overrides a few key
low-level methods that are concerned with actually sending your request
over the network, allowing an interception of that request and simulating a
particular response. This greatly facilitates testing of networking client
code where the server follows a known protocol.

The synopsis describes a typical case where you want to test how your
application reacts to various responses from the server. This module will
let you send back various responses depending on the request, without
having to set up a real server to test against. This can be invaluable when
you need to test edge cases or error conditions that are not normally
returned from the server.

There are a lot of different ways you can set up the response mappings, and
hook into this module; see the documentation for the individual interface
methods.

You can use a PSGI app to handle the requests - see _examples/call_psgi.t_
in this distribution, and also register_psgi below.

OR, you can route some or all requests through the network as normal, but
still gain the hooks provided by this class to test what was sent and
received:

    my $useragent = Test::LWP::UserAgent->new(network_fallback => 1);

or:

    $useragent->map_network_response(qr/real.network.host/);

    # ... generate a request...

    # and then in your tests:
    is(
        $useragent->last_useragent->timeout,
        180,
        'timeout was overridden properly',
    );
    is(
        $useragent->last_http_request_sent->uri,
        'uri my code should have constructed',
    );
    is(
        $useragent->last_http_response_received->code,
        '200',
        'I should have gotten an OK response',
    );

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING docs examples README
%license LICENCE

%changelog
