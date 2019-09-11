#
# spec file for package switcheroo-control
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.3.1
Release:        0
Summary:        D-Bus service to check the availability of dual-GPU
License:        GPL-3.0-only
Group:          Hardware/Other
Url:            https://github.com/hadess/switcheroo-control
Source0:        https://github.com/hadess/switcheroo-control/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
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
%configure \
    --with-systemdsystemunitdir=%{_unitdir} \
    --enable-gtk-doc
make %{?_smp_mflags}

%install
%make_install

%pre
%service_add_pre switcheroo-control.service

%post
%service_add_post switcheroo-control.service

%preun
%service_del_preun switcheroo-control.service

%postun
%service_del_postun switcheroo-control.service

%files
%defattr(-,root,root)
%license COPYING
%doc NEWS README
%{_libexecdir}/switcheroo-control
%{_unitdir}/switcheroo-control.service
# Own dirs to avoid depending on dbus while building.
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf

%files doc
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%{name}/

%changelog
