#
# spec file for package switcheroo-control
#
# Copyright (c) 2021 SUSE LLC
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


Name:           switcheroo-control
Version:        2.4
Release:        0
Summary:        D-Bus service to check the availability of dual-GPU
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://gitlab.freedesktop.org/hadess/switcheroo-control
Source0:        https://gitlab.freedesktop.org/hadess/switcheroo-control/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(udev)
%{?systemd_requires}
# SECTION For tests
BuildRequires:  %{python_module dbus-python}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(umockdev-1.0)
# /SECTION

%description
switcheroo-control is a D-Bus service to check the availability of dual-GPU.

%package doc
Summary:        Documentation for %{name}
Group:          Hardware/Other
BuildArch:      noarch

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q

%build
%meson \
   -Dsystemdsystemunitdir=%{_unitdir} \
   -Dhwdbdir=%{_udevhwdbdir} \
   -Dgtk_doc=true

%meson_build

%install
%meson_install

%check
%meson_test

%pre
%service_add_pre switcheroo-control.service

%post
%service_add_post switcheroo-control.service
%udev_hwdb_update

%preun
%service_del_preun switcheroo-control.service

%postun
%service_del_postun switcheroo-control.service
%udev_hwdb_update

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/switcherooctl
%{_libexecdir}/switcheroo-control
%{_mandir}/man1/switcherooctl.1%{?ext_man}
%{_unitdir}/switcheroo-control.service
%{_udevhwdbdir}/30-pci-intel-gpu.hwdb
# Own dirs to avoid depending on dbus while building.
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf

%files doc
%doc %{_datadir}/gtk-doc/html/%{name}/

%changelog
