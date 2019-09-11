#
# spec file for package perl-Test-LWP-UserAgent
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Test-LWP-UserAgent
Version:        0.033
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name Test-LWP-UserAgent
Summary:        LWP::UserAgent suitable for simulating and testing network calls
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-LWP-UserAgent/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::IP) >= 0.31
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.62
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response)
Requires:       perl(HTTP::Status)
Requires:       perl(IO::Socket::IP) >= 0.31
Requires:       perl(LWP::UserAgent)
Requires:       perl(Safe::Isa)
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.62
Requires:       perl(namespace::clean) >= 0.19
Requires:       perl(parent)
%{perl_requires}

%description
This module is a subclass of LWP::UserAgent which overrides a few key
low-level methods that are concerned with actually sending your request
over the network, allowing an interception of that request and simulating a
particular response. This greatly facilitates testing of client networking
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING docs examples LICENCE README

%changelog
