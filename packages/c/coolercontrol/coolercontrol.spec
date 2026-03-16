#
# spec file for package coolercontrol
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%global ap_id org.coolercontrol.CoolerControl
%global _daemon coolercontrold
%{!?_metainfodir: %define _metainfodir %{_datadir}/metainfo}
Name:           coolercontrol
Version:        4.0.1
Release:        0
Summary:        Cooling control and monitoring
License:        GPL-3.0-or-later
URL:            https://gitlab.com/coolercontrol/coolercontrol
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo >= 1.84
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(protobuf)
Recommends:     %{_daemon} = %{version}

%description
This is the desktop application for CoolerControl,
an application for monitoring and controlling supported cooling
devices. It features flexible control options, and live thermal data.

%package -n %{_daemon}
Summary:        Cooling control and monitoring

%description -n %{_daemon}
This is the system daemon for CoolerControl,
an application for monitoring and controlling supported cooling
devices. It features flexible control options, and live thermal data.

%prep
%autosetup -a1 -p1

%build
orig="$PWD"
cd coolercontrol
%cmake
%cmake_build
cd "$orig"

cd coolercontrold
export RUSTFLAGS="%{build_rustflags}"
%{cargo_build}

%install
orig="$PWD"
cd coolercontrol
%cmake_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications metadata/%{ap_id}.desktop
install -Dpm 644 metadata/%{ap_id}.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -Dpm 644 metadata/%{ap_id}-alert.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -Dpm 644 metadata/%{ap_id}-symbolic.svg -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
install -Dpm 644 metadata/%{ap_id}-symbolic-alert.svg -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
install -Dpm 644 metadata/%{ap_id}.png -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dpm 644 metadata/%{ap_id}-alert.png -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dpm 644 metadata/%{ap_id}.metainfo.xml -t %{buildroot}%{_metainfodir}
install -Dpm 644 man/%{name}.1 -t %{buildroot}%{_mandir}/man1
cd "$orig"

cd coolercontrold
export RUSTFLAGS="%{build_rustflags}"
orig="$PWD"
cd daemon
%{cargo_install}
rm -rf %{buildroot}%{_datadir}/cargo
cd "$orig"
install -Dpm 644 systemd/%{_daemon}.service -t %{buildroot}%{_unitdir}
install -Dpm 644 man/%{_daemon}.8 -t %{buildroot}%{_mandir}/man8

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{ap_id}.metainfo.xml
orig="$PWD"
cd coolercontrold
%{cargo_test}
cd "$orig"
%{buildroot}%{_bindir}/%{_daemon} --version

%pre -n %{_daemon}
%systemd_pre %{_daemon}.service

%post -n %{_daemon}
%systemd_post %{_daemon}.service

%preun -n %{_daemon}
%systemd_preun %{_daemon}.service

%postun -n %{_daemon}
%systemd_postun_with_restart %{_daemon}.service

%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/%{ap_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{ap_id}-alert.svg
%{_datadir}/icons/hicolor/scalable/apps/%{ap_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{ap_id}-symbolic-alert.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{ap_id}-symbolic.svg
%{_datadir}/icons/hicolor/256x256/apps/%{ap_id}-alert.png
%{_datadir}/icons/hicolor/256x256/apps/%{ap_id}.png
%{_metainfodir}/%{ap_id}.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n %{_daemon}
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/%{_daemon}
%{_unitdir}/%{_daemon}.service
%{_mandir}/man8/%{_daemon}.8%{?ext_man}

%changelog
