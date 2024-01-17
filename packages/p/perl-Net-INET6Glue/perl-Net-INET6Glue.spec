#
# spec file for package perl-Net-INET6Glue
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


%define cpan_name Net-INET6Glue
Name:           perl-Net-INET6Glue
Version:        0.604
Release:        0
Summary:        Make common modules IPv6 ready by hotpatching
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::IP) >= 0.25
Requires:       perl(IO::Socket::IP) >= 0.25
%{perl_requires}

%description
Net::INET6Glue is a collection of modules to make common modules IPv6 ready
by hotpatching them.

Unfortunatly the current state of IPv6 support in perl is that no IPv6
support is in the core and that a lot of important modules (like Net::FTP,
Net::SMTP, LWP,...) do not support IPv6 even if the modules for IPv6
sockets like Socket6, IO::Socket::IP or IO::Socket::INET6 are available.

This module tries to mitigate this by hotpatching. Currently the following
submodules are available:

* Net::INET6Glue::INET_is_INET6

Makes IO::Socket::INET behave like IO::Socket::IP (with fallback to like
IO::Socket::INET6), especially make it capable to create IPv6 sockets. This
makes LWP, Net::SMTP and others IPv6 capable.

* Net::INET6Glue::FTP

Hotpatches Net::FTP to support EPRT and EPSV commands which are needed to
deal with FTP over IPv6. Also loads Net::INET6Glue::INET_is_INET6.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes COPYRIGHT README

%changelog
