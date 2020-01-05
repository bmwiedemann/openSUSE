#
# spec file for package switcheroo-control
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


Name:           switcheroo-control
Version:        2.1
Release:        0
Summary:        D-Bus service to check the availability of dual-GPU
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://gitlab.freedesktop.org/hadess/switcheroo-control
Source0:        https://gitlab.freedesktop.org/hadess/switcheroo-control/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(udev)
%{?systemd_requires}

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
NOCONFIGURE=1 sh autogen.sh
%configure \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-hwdbdir=%{_udevhwdbdir} \
    --enable-gtk-doc
make %{?_smp_mflags}

%install
%make_install

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
%defattr(-,root,root)
%license COPYING
%doc NEWS README
%{_libexecdir}/switcheroo-control
%{_unitdir}/switcheroo-control.service
%{_udevhwdbdir}/30-pci-intel-gpu.hwdb
# Own dirs to avoid depending on dbus while building.
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf

%files doc
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%{name}/

%changelog
