#
# spec file for package gmobile
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


Name:           gmobile
Version:        0.2.1
Release:        0
Summary:        Some helpers for glib based environments on mobile devices
License:        LGPL-2.1-or-later
URL:            https://world.pages.gitlab.gnome.org/Phosh/gmobile/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6.2

%description
gmobile carries some helpers for glib based environments on mobile devices.

Some of those parts might move to glib or libgnome-desktop eventually. It can be used as a shared library or git submodule.
There aren't any API stability guarantees at this point in time.

%package -n libgmobile0
Summary:        Some helpers for glib based environments on mobile devices
Recommends:     %{name} >= %{version}

%description -n libgmobile0
gmobile carries some helpers for glib based environments on mobile devices.

Some of those parts might move to glib or libgnome-desktop eventually. It can be used as a shared library or git submodule.
There aren't any API stability guarantees at this point in time.

%package -n typelib-1_0-Gm-0
Summary:        Some helpers for glib based environments on mobile devices

%description -n typelib-1_0-Gm-0
gmobile carries some helpers for glib based environments on mobile devices.

Some of those parts might move to glib or libgnome-desktop eventually. It can be used as a shared library or git submodule.
There aren't any API stability guarantees at this point in time.

%package devel
Summary:        Some helpers for glib based environments on mobile devices
Requires:       libgmobile0 = %{version}
Requires:       typelib-1_0-Gm-0 = %{version}

%description devel
gmobile carries some helpers for glib based environments on mobile devices.

Some of those parts might move to glib or libgnome-desktop eventually. It can be used as a shared library or git submodule.
There aren't any API stability guarantees at this point in time.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Remove static library
rm %{buildroot}%{_libdir}/libgmobile.a

%check
%meson_test

%ldconfig_scriptlets -n libgmobile0

%files
%{_bindir}/gm-display-panel-preview
%{_bindir}/gm-display-panel-run-phosh
%{_bindir}/gm-timeout
%dir %{_udevhwdbdir}
%{_udevhwdbdir}/61-gmobile-wakeup.hwdb
%{_udevrulesdir}/61-gmobile.rules

%files -n libgmobile0
%{_libdir}/libgmobile.so.0

%files -n typelib-1_0-Gm-0
%{_libdir}/girepository-1.0/Gm-0.typelib

%files devel
%{_includedir}/gmobile/
%{_datadir}/gir-1.0/Gm-0.gir
%{_libdir}/pkgconfig/gmobile.pc
%{_libdir}/libgmobile.so

%changelog
