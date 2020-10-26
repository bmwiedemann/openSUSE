#
# spec file for package libwpe
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


# When updating this, do so in baselibs.conf too
%define major_minor 1.0
%define sover 1_0-1

Name:           libwpe
Version:        1.8.0
Release:        0
Summary:        General-purpose library for the WPE-flavored port of WebKit
License:        BSD-2-Clause
URL:            https://github.com/WebPlatformForEmbedded/libwpe
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  c++_compiler
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(xkbcommon)

%description
General-purpose library developed for the WPE-flavored port of
WebKit.

%package     -n %{name}-%{sover}
Summary:        Shared library for %{name}

%description -n %{name}-%{sover}
General-purpose library developed for the WPE-flavored port of
WebKit.
This package contains the shared libary of libwpe.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%post -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%files -n %{name}-%{sover}
%license COPYING
%doc NEWS
%{_libdir}/%{name}-%{major_minor}.so.*

%files devel
%{_includedir}/wpe-%{major_minor}/
%{_libdir}/%{name}-%{major_minor}.so
%{_libdir}/pkgconfig/wpe-%{major_minor}.pc

%changelog
