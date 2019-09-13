#
# spec file for package perl-Crypt-SmbHash
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Crypt-SmbHash
Version:        0.12
Release:        0
Summary:        perl module Crypt::SmbHash
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/perldoc?Crypt::SmbHash
Source:         http://search.cpan.org/CPAN/authors/id/B/BJ/BJKUIT/Crypt-SmbHash-%{version}.tar.gz
BuildRequires:  perl-Digest-MD4
BuildRequires:  perl-macros
Requires:       perl-Digest-MD4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This module provides functions to generate LM/NT hashes as used by
Samba

%prep
%setup -n Crypt-SmbHash-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%defattr(-, root, root)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Crypt
%{perl_vendorarch}/auto/Crypt

%changelog
