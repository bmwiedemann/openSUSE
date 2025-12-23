#
# spec file for package ryokucha
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


%define         sover 0
Name:           ryokucha
Version:        0.3.1
Release:        0
Summary:        A GTK4 library that includes customized widgets
License:        LGPL-3.0-or-later
URL:            https://github.com/ryonakano/ryokucha
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-meson.build.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-html
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.74
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pango)

%description
Ryokucha (緑茶, meaning green tea in Japanese) is a GTK4 library that includes
customized widgets.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package demo
Summary:        Demo for %{name}

%description demo
%{summary}.

%prep
%autosetup -p1

%build
%meson -Ddoc=true -Ddemo=true
%meson_build

%install
%meson_install
install -Dpm0755 %{_builddir}/%{name}-%{version}/%{_arch}-suse-linux/demo/demo %{buildroot}%{_bindir}/%{name}-demo

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}

%files devel
%license LICENSE
%doc README.md docs
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}.{deps,vapi}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files demo
%{_bindir}/%{name}-demo

%changelog
