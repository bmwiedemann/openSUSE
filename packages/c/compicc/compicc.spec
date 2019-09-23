#
# spec file for package compicc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           compicc
Version:        0.8.10
Release:        0
Summary:        Compiz ICC Colour Management Server
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
Url:            https://github.com/compiz-reloaded/compicc
Source:         https://github.com/compiz-reloaded/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE pic-flag.patch schwab@suse.de -- Always compile shared objects with -fPIC.
Patch0:         pic-flag.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oyranos) >= 0.9.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcm)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       compiz < 0.9
Requires:       oyranos-monitor
Recommends:     ccsm < 0.9
Recommends:     oyranos-qcmsevents

%description
The Compiz ICC colour server, or short compicc, lets you colour
manage your whole desktop at once and in hardware. Play movies,
watch images on wide or narrow gamut displays. Each connected
monitor is colour corrected for its own.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --disable-static \
  --enable-debug
make %{?_smp_mflags} V=1

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%post
/sbin/ldconfig
%icon_theme_cache_post

%postun
/sbin/ldconfig
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS.md ChangeLog.md COPYING.md README.md
%dir %{_libdir}/compiz/
%{_libdir}/compiz/*libcompicc.*
%dir %{_datadir}/compiz/
%{_datadir}/compiz/*compicc.*
%{_datadir}/ccsm/

%changelog
