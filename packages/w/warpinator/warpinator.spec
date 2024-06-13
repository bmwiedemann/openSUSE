#
# spec file for package warpinator
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


Name:           warpinator
Version:        1.8.4
Release:        0
Summary:        Share files across the LAN
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/warpinator
Source:         https://github.com/linuxmint/warpinator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  glib2-tools
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-grpcio
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-zeroconf
BuildRequires:  update-desktop-files
Requires:       python3-PyNaCl
Requires:       python3-cryptography
Requires:       python3-gobject-Gdk
Requires:       python3-grpcio
Requires:       python3-netifaces
Requires:       python3-protobuf
Requires:       python3-qrcode
Requires:       python3-setproctitle
Requires:       python3-xapp
Requires:       python3-zeroconf

BuildArch:      noarch
%lang_package

%description
Warpinator is a simple app that allows users to share files across the LAN.

%package -n nemo-extension-%{name}
Summary:        Warpinator extension for nemo
Requires:       nemo
Requires:       warpinator = %{version}
Supplements:    (nemo and warpinator)
BuildArch:      noarch

%description -n nemo-extension-%{name}
Warpinator is a simple app that allows users to share files across the LAN.

This package provides an extension to use warpinator from nemo file browser.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson \
%if 0%{?suse_version} >= 1550
       --sysconfdir=%{_distconfdir} \
%endif
       -Dbundle-zeroconf=false \
       -Dbundle-grpc=false \
       -Dinclude-firewall-mod=false
%meson_build

%install
%meson_install

# Files missing hashbangs
for f in config warp_pb2 warp_pb2_grpc
do
  sed -i "1i#!%{_bindir}/python3" %{buildroot}%{_libexecdir}/warpinator/${f}.py
done

chmod +x %{buildroot}%{_libexecdir}/warpinator/*.py

%suse_update_desktop_file -r org.x.Warpinator Network FileTransfer
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README.md
%if 0%{?suse_version} >= 1550
%{_distconfdir}/xdg/autostart/warpinator-autostart.desktop
%else
%{_sysconfdir}/xdg/autostart/warpinator-autostart.desktop
%endif
%{_bindir}/warpinator
%{_bindir}/warpinator-send
%{_libexecdir}/warpinator/
%{_datadir}/applications/org.x.Warpinator.desktop
%{_datadir}/glib-2.0/schemas/org.x.Warpinator.gschema.xml
%dir %{_datadir}/icons/hicolor/*@2
%dir %{_datadir}/icons/hicolor/*@2/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/org.x.Warpinator.appdata.xml
%{_datadir}/warpinator/

%files -n nemo-extension-%{name}
%dir %{_datadir}/nemo
%dir %{_datadir}/nemo/actions
%{_datadir}/nemo/actions/warpinator*

%files lang -f %{name}.lang

%changelog
