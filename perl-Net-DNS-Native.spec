#
# spec file for package perl-Net-DNS-Native
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Net-DNS-Native
Name:           perl-Net-DNS-Native
Version:        0.220.0
Release:        0
%define cpan_version 0.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Non-blocking system DNS resolver
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLEG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Socket) >= 1.94
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Socket) >= 1.94
Provides:       perl(Net::DNS::Native) = 0.220.0
Provides:       perl(Net::DNS::Native::Handle)
%define         __perllib_provides /bin/true
%{perl_requires}

%description
This class provides several methods for host name resolution. It is
designed to be used with event loops. All resolving are done by
getaddrinfo(3) implemented in your system library. Since getaddrinfo() is
blocking function and we don't want to block, calls to this function will
be done in separate thread. This class uses system native threads and not
perl threads. So overhead shouldn't be too big.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
