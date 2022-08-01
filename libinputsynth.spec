#
# spec file for package libinputsynth
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

%define _libver 0.15
%define _sover 0
%define _underver 0_15

Name:           libinputsynth
Version:        0.15.0
Release:        0
Summary:        Keyboard and mouse input synthesis for X11 and Wayland with various backends
License:        MIT
URL:            https://gitlab.freedesktop.org/xrdesktop/libinputsynth
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  meson
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(gulkan-0.15)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(libxdo)

%description
Synthesize keyboard and mouse input on X11 and Wayland with various backends.

%package -n %{name}%{_underver}-%{_sover}
Summary:        Synthesize keyboard and mouse input on X11 and Wayland with various backends

%description -n %{name}%{_underver}-%{_sover}
Synthesize keyboard and mouse input on X11 and Wayland with various backends.

%package devel
Summary:        Synthesize keyboard and mouse input on X11 and Wayland with various backends
Requires:       %{name}%{_underver}-%{_sover} = %{version}

%description devel
Synthesize keyboard and mouse input on X11 and Wayland with various backends.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n %{name}%{_underver}-%{_sover} -p /sbin/ldconfig
%postun -n %{name}%{_underver}-%{_sover} -p /sbin/ldconfig

%files -n %{name}%{_underver}-%{_sover}
%dir %{_libdir}/%{name}-%{_libver}
%dir %{_libdir}/%{name}-%{_libver}/plugins

%{_libdir}/%{name}-%{_libver}.so.*
%{_libdir}/%{name}-%{_libver}/plugins/*.so

%files devel
%dir %{_includedir}/%{name}-%{_libver}
%{_includedir}/%{name}-%{_libver}/inputsynth-version.h
%{_includedir}/%{name}-%{_libver}/inputsynth.h
%{_libdir}/%{name}-%{_libver}.so
%{_libdir}/pkgconfig/%{name}-%{_libver}.pc

%changelog
