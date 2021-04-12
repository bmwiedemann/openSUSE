#
# spec file for package perl-Net-CIDR
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


%define cpan_name Net-CIDR
Name:           perl-Net-CIDR
Version:        0.21
Release:        0
Summary:        Manipulate IPv4/IPv6 netblocks in CIDR notation
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRSAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The Net::CIDR package contains functions that manipulate lists of IP
netblocks expressed in CIDR notation. The Net::CIDR functions handle both
IPv4 and IPv6 addresses.

The cidrvalidate() function, described below, checks that its argument is a
single, valid IP address or a CIDR. The remaining functions expect that
their parameters consist of validated IPs or CIDRs. See cidrvalidate() and
BUGS, below, for more information.

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
%doc ChangeLog README
%license COPYING

%changelog
