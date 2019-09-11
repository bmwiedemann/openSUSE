#
# spec file for package perl-AnyEvent-HTTP
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-AnyEvent-HTTP
Version:        2.24
Release:        0
%define cpan_name AnyEvent-HTTP
Summary:        Simple but Non-Blocking Http/Https Client
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/AnyEvent-HTTP/
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent) >= 5.33
BuildRequires:  perl(common::sense) >= 3.3
Requires:       perl(AnyEvent) >= 5.33
Requires:       perl(common::sense) >= 3.3
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
%license COPYING

%changelog
