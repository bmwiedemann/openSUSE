#
# spec file for package perl-AnyEvent-HTTP
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


%define cpan_name AnyEvent-HTTP
Name:           perl-AnyEvent-HTTP
Version:        2.250.0
Release:        0
# 2.25 -> normalize -> 2.250.0
%define cpan_version 2.25
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple but non-blocking HTTP/HTTPS client
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent) >= 5.330
BuildRequires:  perl(common::sense) >= 3.300
Requires:       perl(AnyEvent) >= 5.330
Requires:       perl(common::sense) >= 3.300
Provides:       perl(AnyEvent::HTTP) = %{version}
%undefine       __perllib_provides
Recommends:     perl(URI)
%{perl_requires}

%description
This module is an AnyEvent user, you need to make sure that you use and run
a supported event loop.

This module implements a simple, stateless and non-blocking HTTP client. It
supports GET, POST and other request methods, cookies and more, all on a
very low level. It can follow redirects, supports proxies, and
automatically limits the number of connections to the values specified in
the RFC.

It should generally be a "good client" that is enough for most HTTP tasks.
Simple tasks should be simple, but complex tasks should still be possible
as the user retains control over request and response headers.

The caller is responsible for authentication management, cookies (if the
simplistic implementation in this module doesn't suffice), referer and
other high-level protocol details for which this module offers only limited
support.

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
%doc Changes README
%license COPYING

%changelog
