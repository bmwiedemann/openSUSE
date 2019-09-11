#
# spec file for package perl-qpid
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


Name:           perl-qpid
Version:        1.38.0
Release:        0
Summary:        Perl bindings for the Qpid messaging framework
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://qpid.apache.org/
Source0:        http://www.apache.org/dist/qpid/cpp/%{version}/qpid-cpp-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  qpid-cpp-client-devel = %{version}
BuildRequires:  swig >= 2.0.9
Requires:       perl = %{perl_version}

%description
Perl bindings needed for the Qpid messaging framework.

%prep
%setup -q -n qpid-cpp-%{version}

%build
pushd bindings/qpid/perl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
popd

%install
pushd bindings/qpid/perl
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
rm -rf %{buildroot}%{perl_vendorarch}/auto/
popd

%files
%{perl_vendorarch}/*
%doc LICENSE.txt
%{_mandir}/man3/*

%changelog
