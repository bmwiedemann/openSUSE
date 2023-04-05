#
# spec file for package snobol4
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


%global _smp_mflags -j1
%global optflags %{optflags} -Wno-error=unused-result -Wno-error=unused-but-set-variable -Wno-error=restrict -Wno-error=unused-variable -Wno-error=maybe-uninitialized -Wno-error=uninitialized
Name:           snobol4
Version:        2.3.1
Release:        0
Summary:        A port of Macro SNOBOL4
License:        BSD-2-Clause
URL:            https://www.regressive.org/snobol4/csnobol4/curr/
Source0:        https://ftp.regressive.org/snobol4/%{name}-%{version}.tar.gz
# Do not hardcode -O3.
Patch1:         snobol4-2.3.1-configure-no-opt.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libbz2-devel
BuildRequires:  libedit-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  tcl-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
This is a free port of the original SIL (SNOBOL4 Implementation
Language) "macro" version of SNOBOL4 (developed at Bell Labs) with the
`C' language as a target.

SNOBOL4, while known primarily as a string language excels at any task
involving symbolic manipulations.  It provides dynamic typing, garbage
collection, user data types, on the fly compilation.

%package devel
Summary:        Development files for snobol4
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for snobol4.

%prep
%autosetup -p1

# Remove version control files
rm -r doc/CVS doc/.cvsignore

%build
# This isn't a real configure script, hence, no macro.
./configure --add-cflags="%{optflags}" --add-cppflags="%{optflags}" --prefix=%{_prefix} --mandir=%{_mandir} --snolibdir=%{_libdir}/snobol4 --with-tcl=%{_libdir}/tclConfig.sh
%make_build

%install
%make_install

# all in libdir? What is this, 1985? Oh wait, this is SNOBOL, so maybe 1969.
mkdir -p %{buildroot}%{_includedir}/snobol4
mv %{buildroot}%{_libdir}/%{name}/%{version}/include/* %{buildroot}%{_includedir}/snobol4
pushd %{buildroot}%{_libdir}/%{name}/%{version}/
rm -rf include
ln -s ../../../include/snobol4 include
popd

# We rather install doc/ ourselves
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
rm -rf %{buildroot}%{_libdir}/%{name}/%{version}/CHANGES %{buildroot}%{_libdir}/%{name}/%{version}/README

%files
%doc CHANGES README doc/
%license COPYRIGHT
%{_bindir}/sdb*
%{_bindir}/snobol4
%{_bindir}/snobol4-%{version}
%{_bindir}/snopea*
%{_libdir}/snobol4/
%exclude %{_libdir}/snobol4/%{version}/include
%{_mandir}/man1/sdb.1%{?ext_man}
%{_mandir}/man1/snobol4*.1%{?ext_man}
%{_mandir}/man1/snopea.1%{?ext_man}
%{_mandir}/man3/snolib.3%{?ext_man}
%{_mandir}/man3/snobol4*.3%{?ext_man}
%{_mandir}/man7/snopea.7%{?ext_man}

%files devel
%{_includedir}/%{name}
%{_libdir}/snobol4/%{version}/include

%changelog
