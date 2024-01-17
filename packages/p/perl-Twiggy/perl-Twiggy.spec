#
# spec file for package perl-Twiggy
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Twiggy
Name:           perl-Twiggy
Version:        0.1026
Release:        0
Summary:        AnyEvent HTTP server for PSGI
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Plack) >= 0.99
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(AnyEvent)
Requires:       perl(HTTP::Status)
Requires:       perl(Plack) >= 0.99
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Twiggy is a lightweight and fast HTTP server with unique features such as:

* PSGI

Can run any PSGI applications. Fully supports _psgi.nonblocking_ and
_psgi.streaming_ interfaces.

* AnyEvent

This server uses AnyEvent and runs in a non-blocking event loop, so it's
best to run event-driven web applications that runs I/O bound jobs or
delayed responses such as long-poll, WebSocket or streaming content (server
push).

This software used to be called Plack::Server::AnyEvent but was renamed to
Twiggy.

* Fast header parser

Uses XS/C based HTTP header parser for the best performance. (optional,
install the HTTP::Parser::XS module to enable it; see also
Plack::HTTPParser for more information).

* Lightweight and Fast

The memory required to run twiggy is 6MB and it can serve more than 4500
req/s with a single process on Perl 5.10 with MacBook Pro 13" late 2009.

* Superdaemon aware

Supports Server::Starter for hot deploy and graceful restarts.

To use it, instead of the usual:

    plackup --server Twiggy --port 8111 app.psgi

install Server::Starter and use:

    start_server --port 8111 -- plackup --server Twiggy app.psgi

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README
%license LICENSE

%changelog
