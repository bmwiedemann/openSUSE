#
# spec file for package perl-Data-Validate-IP
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Validate-IP
Version:        0.27
Release:        0
%define cpan_name Data-Validate-IP
Summary:        IPv4 and IPv6 validation methods
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Validate-IP/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(NetAddr::IP) >= 4
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
Requires:       perl(NetAddr::IP) >= 4
%{perl_requires}

%description
This module provides a number IP address validation subs that both validate
and untaint their input. This includes both basic validation ('is_ipv4()'
and 'is_ipv6()') and special cases like checking whether an address belongs
to a specific network or whether an address is public or private
(reserved).

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
%doc Changes CONTRIBUTING.md LICENSE README.md test-vars-ignore

%changelog
