#
# spec file for package sane-airscan
#
# Copyright (c) 2024 SUSE LLC
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


%define         soversion 1
Name:           sane-airscan
Version:        0.99.29
Release:        0
Summary:        Universal driver for Apple AirScan (eSCL) and WSD
License:        SUSE-GPL-2.0+-with-sane-exception
URL:            https://github.com/alexpevzner/sane-airscan
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  zstd

%package devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.

%package -n lib%{name}%{soversion}
Summary:        Library files for %{name}

%description -n lib%{name}%{soversion}
Libary files for %{name}.

%description
This package contains a SANE backend for MFP and document scanners that
implements either eSCL (AirScan/AirPrint scanning) or WSD "driverless"
scanning protocol

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE COPYING
%doc README.md
%{_bindir}/airscan-discover
%config %{_sysconfdir}/sane.d/airscan.conf
%config %{_sysconfdir}/sane.d/dll.d/airscan
%{_mandir}/man?/{sane-airscan,airscan-discover}.?.gz
%if 0%{?suse_version} == 1500
%dir %{_sysconfdir}/sane.d/dll.d
%endif

%files -n lib%{name}%{soversion}
%{_libdir}/sane/libsane-airscan.so.1

%files devel
%license LICENSE COPYING
%doc README.md
%{_libdir}/sane/libsane-airscan.so

%changelog
