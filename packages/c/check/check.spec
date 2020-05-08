#
# spec file for package check
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libcheck0
Name:           check
Version:        0.14.0
Release:        0
Summary:        Unit Test Framework for C
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://libcheck.github.io/check/
Source:         https://github.com/libcheck/check/releases/download/%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  sed

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, limitating the developer the less possible.

%package -n %{libname}
Summary:        Unit Test Framework for C
Group:          System/Libraries
Obsoletes:      check < %{version}-%{release}
Provides:       check = %{version}-%{release}

%description -n %{libname}
Check is a unit test framework for C. It features a simple interface for
defining unit tests, limitating the developer the less possible. Tests
are run in a separate address space, so Check cancatch both, assertion
failures and code errors that cause segmentationfaults or other
signals. The output of unit tests can be used within source code
editors and IDEs.

%package devel
Summary:        Development files for the CHECK unit test framework
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description devel
Check is a unit test framework for C. It features a simple interface
for defining unit tests, putting little in the way of the developer.
Tests are run in a separate address space, so Check can catch both
assertion failures and code errors that cause segmentation faults or
other signals. The output from unit tests can be used within source
code editors and IDEs.

%prep
%setup -q

%build
autoreconf -fiv
export CFLAGS="%{optflags} -std=gnu99"
export CXXFLAGS="%{optflags} -std=gnu99"
export FFLAGS="%{optflags} -std=gnu99"
%configure \
    --disable-static
%make_build docdir=%{_docdir}/%{name}

%install
%make_install docdir=%{_docdir}/%{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_datadir}

# We package these either with %%license or %%doc macros
rm %{buildroot}%{_docdir}/%{name}/{COPYING.LESSER,ChangeLog,NEWS,README}

%post -n %{libname} -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n %{libname} -p /sbin/ldconfig
%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -n %{libname}
%license COPYING.LESSER
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_infodir}/%{name}.info*
%{_mandir}/man1/checkmk.1%{?ext_man}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/example
%{_bindir}/checkmk
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
