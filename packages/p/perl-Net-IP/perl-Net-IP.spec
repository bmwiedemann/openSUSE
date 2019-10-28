#
# spec file for package perl-Net-IP
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-IP
Version:        1.26
Release:        0
Summary:        Allows easy manipulation of IPv4 and IPv6 addresses
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://cpan.org/modules/by-module/Net/
Source:         http://search.cpan.org/CPAN/authors/id/M/MA/MANU/Net-IP-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         %{name}-1.25-zero_address.diff
Patch1:         ipcount-invalid_chars_in_IP.patch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl_Net-IP = %{version}
Obsoletes:      perl_Net-IP < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This is the Net::IP module, designed to allow easy manipulation of IPv4
and IPv6 addresses.

%prep
%setup -q -n Net-IP-%{version}
%patch0
%patch1 -p1

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{_bindir}/*
%{_mandir}/man3/*
%dir %{perl_vendorlib}/Net
%{perl_vendorlib}/Net/IP.pm
%dir %{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Net/IP

%changelog
