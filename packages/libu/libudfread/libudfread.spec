#
# spec file for package libudfread
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands
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


%if ! 0%{?_smp_build_ncpus}
# needed by %%meson
%define  _smp_build_ncpus %{?jobs:%{jobs}}
%endif

%define         sover 3
Name:           libudfread
Version:        1.2.0
Release:        0
Summary:        UDF Reader Library
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/libudfread/-/archive/%{version}/libudfread-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  meson

%description
This library allows reading UDF filesystems, like raw devices and image files.

%package -n libudfread%{sover}
Summary:        UDF Reader Library
Group:          System/Libraries

%description -n libudfread%{sover}
This library allows reading UDF filesystems, like raw devices and image files.

%package devel
Summary:        UDF Reader Library - Development files
Group:          Development/Languages/C and C++
Requires:       libudfread%{sover} = %{version}

%description devel
Development files for libudfread.

%prep
%autosetup -p1

%build
%meson --default-library=shared
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libudfread%{sover}

%files -n libudfread%{sover}
%license COPYING
%{_libdir}/libudfread.so.*

%files devel
%license COPYING ChangeLog
%{_includedir}/udfread/
%{_libdir}/libudfread.so
%{_libdir}/pkgconfig/libudfread.pc

%changelog
