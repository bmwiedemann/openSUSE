#
# spec file for package libuninameslist
#
# Copyright (c) 2022 SUSE LLC
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


%define somajor 1
Name:           libuninameslist
Version:        20221022
Release:        0
Summary:        A library providing Unicode character names and annotations
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/fontforge/libuninameslist
Source0:        https://github.com/fontforge/libuninameslist/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libuninameslist provides Unicode name and annotation data from the official Unicode Character Database.

%package     -n %{name}%{somajor}
Summary:        A library providing Unicode character names and annotations
Group:          System/Libraries

%description -n %{name}%{somajor}
libuninameslist provides Unicode name and annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{somajor} = %{version}

%description    devel
This package contains header files for %{name}.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{name}%{somajor} -p /sbin/ldconfig
%postun -n %{name}%{somajor} -p /sbin/ldconfig

%files -n libuninameslist%{somajor}
%license LICENSE
%{_libdir}/libuninameslist.so.%{somajor}*

%files devel
%{_libdir}/libuninameslist.so
%{_libdir}/pkgconfig/libuninameslist.pc
%{_mandir}/man3/libuninameslist.3%{?ext_man}
%{_includedir}/uninameslist.h

%changelog
