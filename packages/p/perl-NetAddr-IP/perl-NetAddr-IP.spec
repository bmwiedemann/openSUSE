#
# spec file for package perl-NetAddr-IP
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


Name:           perl-NetAddr-IP
Version:        4.079
Release:        0
%define cpan_name NetAddr-IP
Summary:        Manages IPv4 and IPv6 addresses and subnets
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/NetAddr-IP/
Source0:        http://www.cpan.org/authors/id/M/MI/MIKER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides an object-oriented abstraction on top of IP addresses
or IP subnets that allows for easy manipulations. Version 4.xx of
NetAddr::IP will work with older versions of Perl and is compatible with
Math::BigInt.

The internal representation of all IP objects is in 128 bit IPv6 notation.
IPv4 and IPv6 objects may be freely mixed.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc About-NetAddr-IP.txt Artistic Changes Copying docs TODO

%changelog
