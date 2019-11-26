#
# spec file for package perl-Net-IP
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           perl-Net-IP
Version:        1.26
Release:        0
%define cpan_name Net-IP
Summary:        Perl extension for manipulating IPv4/IPv6 addresses
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANU/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         %{name}-1.25-zero_address.diff
Patch1:         ipcount-invalid_chars_in_IP.patch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl_Net-IP = %{version}
Obsoletes:      perl_Net-IP < %{version}
BuildArch:      noarch
%{perl_requires}

%description
This module provides functions to deal with *IPv4/IPv6* addresses. The
module can be used as a class, allowing the user to instantiate IP objects,
which can be single IP addresses, prefixes, or ranges of addresses. There
is also a procedural way of accessing most of the functions. Most
subroutines can take either *IPv4* or *IPv6* addresses transparently.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes MANIFEST README
%license COPYING

%changelog
