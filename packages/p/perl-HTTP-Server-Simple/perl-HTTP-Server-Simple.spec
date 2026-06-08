#
# spec file for package perl-HTTP-Server-Simple
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name HTTP-Server-Simple
Name:           perl-HTTP-Server-Simple
Version:        0.520.0
Release:        0
# 0.52 -> normalize -> 0.520.0
%define cpan_version 0.52
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Lightweight HTTP server
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Socket) >= 1.94
Requires:       perl(CGI)
Requires:       perl(Socket) >= 1.94
Provides:       perl(HTTP::Server::Simple) = %{version}
Provides:       perl(HTTP::Server::Simple::CGI)
Provides:       perl(HTTP::Server::Simple::CGI::Environment)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  netcfg
# MANUAL END

%description
This is a simple standalone HTTP server. By default, it doesn't thread or
fork. It does, however, act as a simple frontend which can be used to build
a standalone web-based application or turn a CGI into one.

It is possible to use Net::Server classes to create forking, pre-forking,
and other types of more complicated servers; see net_server.

By default, the server traps a few signals:

* HUP

When you 'kill -HUP' the server, it lets the current request finish being
processed, then uses the 'restart' method to re-exec itself. Please note
that in order to provide restart-on-SIGHUP, HTTP::Server::Simple sets a
SIGHUP handler during initialisation. If your request handling code forks
you need to make sure you reset this or unexpected things will happen if
somebody sends a HUP to all running processes spawned by your app (e.g. by
"kill -HUP <script>")

* PIPE

If the server detects a broken pipe while writing output to the client, it
ignores the signal. Otherwise, a client closing the connection early could
kill the server.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
