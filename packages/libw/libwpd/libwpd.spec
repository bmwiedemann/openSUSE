#
# spec file for package libwpd
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libname libwpd-0_10-10
Name:           libwpd
Version:        0.10.2
Release:        0
Summary:        Library for importing WordPerfect documents
License:        LGPL-2.1-or-later AND MPL-2.0+
Group:          Productivity/Publishing/Word
URL:            http://libwpd.sourceforge.net
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-Resolves-rhbz-1643752-bounds-check-m_currentTable-ac.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libwpd is a general purpose library for reading or interpreting data
from WordPerfect files. The library is not a stand-alone utility: it is
designed to be used by another program (for example, a word processor)
as an in-process component.

%package -n %{libname}
Summary:        Library for importing WordPerfect Documents
Group:          System/Libraries

%description -n %{libname}
libwpd is a general purpose library for reading or interpreting data
from WordPerfect files. The library is not a stand-alone utility: it is
designed to be used by another program (for example, a word processor)
as an in-process component.

%package devel
Summary:        Development files for libwpd, a library for importing WordPerfect documents
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libstdc++-devel

%description devel
libwpd is a general purpose library for reading (or, interpreting data
from) WordPerfect files. The library is not a stand-alone utility: it
is designed to be used by another program (e.g.: a word processor) as
an in-process component.

%package devel-doc
Summary:        Documentation for the libwpd API
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libwpd API.

%package tools
Summary:        Tool from libwpd, a library for importing WordPerfect documents
Group:          Productivity/Publishing/Word

%description tools
Tools to transform WordPerfect Documents into other formats. Currently
supported: html, raw, text

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
    --disable-static \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_mandir}/man1
for i in %{buildroot}%{_bindir}/*; do
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
  help2man -N -o %{buildroot}%{_mandir}/man1/$(basename $i).1 $i
done
%fdupes -s %{buildroot}%{_docdir}/%{name}/html

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.LGPL
%license COPYING.MPL
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwpd*.pc
%{_includedir}/libwpd-*

%files devel-doc
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/libwpd.*

%files tools
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}
%doc ChangeLog CREDITS NEWS

%changelog
