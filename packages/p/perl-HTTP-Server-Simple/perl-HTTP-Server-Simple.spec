#
# spec file for package perl-HTTP-Server-Simple
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


Name:           perl-HTTP-Server-Simple
Version:        0.52
Release:        0
%define cpan_name HTTP-Server-Simple
Summary:        Lightweight HTTP server
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Server-Simple/
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(Socket) >= 1.94
Requires:       perl(CGI)
Requires:       perl(Socket) >= 1.94
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
%doc Changes README

%changelog
