#
# spec file for package perl-Data-Validate-IP
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


%define cpan_name Data-Validate-IP
Name:           perl-Data-Validate-IP
Version:        0.310.0
Release:        0
# 0.31 -> normalize -> 0.310.0
%define cpan_version 0.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        IPv4 and IPv6 validation methods
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(NetAddr::IP) >= 4
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
Requires:       perl(NetAddr::IP) >= 4
Provides:       perl(Data::Validate::IP) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides a number IP address validation subs that both validate
and untaint their input. This includes both basic validation ('is_ipv4()'
and 'is_ipv6()') and special cases like checking whether an address belongs
to a specific network or whether an address is public or private
(reserved).

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
