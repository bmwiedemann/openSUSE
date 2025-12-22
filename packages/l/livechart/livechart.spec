#
# spec file for package livechart
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         sover 2
Name:           livechart
Version:        2.0.0
Release:        0
Summary:        A real-time charting library for Vala and GTK4 based on Cairo
License:        MIT
URL:            https://github.com/elementary/live-chart
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-html
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4) >= 4.0

%description
Live Chart is a real-time charting library for GTK4 and Vala, based on Cairo.

Features

    Live animated series (lines, smooth lines, area, bar) within a single chart
    Smart y-axis computation
    Highly configurable
    Extendable

%package -n lib%{name}-2-%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}-2-%{sover}
%summary.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}-2-%{sover} = %{version}

%description devel
%summary.

%prep
%autosetup -n live-chart-%{version}

%build
%meson -Ddocs=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n lib%{name}-2-%{sover}

%files -n lib%{name}-2-%{sover}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}-2.so.%{sover}
%{_libdir}/lib%{name}-2.so.%{version}

%files devel
%license LICENSE
%doc README.md
%{_datadir}/vala/vapi/%{name}-2.vapi
%{_includedir}/%{name}-2.h
%{_libdir}/lib%{name}-2.so
%{_libdir}/pkgconfig/%{name}-2.pc

%changelog
