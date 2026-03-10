#
# spec file for package cosmic-applets
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


%define         pkgname cosmic-applet
%define         bin cosmic-applet
%define         appid com.system76.Cosmic
%define         a11y AppletA11y
%define         applist AppList
%define         audio AppletAudio
%define         battery AppletBattery
%define         bluetooth AppletBluetooth
%define         inputsources AppletInputSources
%define         minimize AppletMinimize
%define         network AppletNetwork
%define         notifications AppletNotifications
%define         power AppletPower
%define         status AppletStatusArea
%define         statusnotifier StatusNotifierWatcher
%define         tiling AppletTiling
%define         time AppletTime
%define         workspaces AppletWorkspaces
%define         appbutton PanelAppButton
%define         workspacesbutton PanelWorkspacesButton
%define         launcherbutton PanelLauncherButton
Name:           cosmic-applets
Version:        1.0.8
Release:        0
Summary:        Applets for COSMIC DE
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-applets
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.90
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-icons

%package -n %{pkgname}-a11y
Summary:        %{summary}
Requires:       %{name} = %{version}

%description -n %{pkgname}-a11y
%{summary}.

%package -n %{pkgname}-app-list
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-app-list
%{summary}.

%package -n %{pkgname}-audio
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-audio
%{summary}.

%package -n %{pkgname}-battery
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-battery
%{summary}.

%package -n %{pkgname}-bluetooth
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-bluetooth
%{summary}.

%package -n %{pkgname}-input-sources
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-input-sources
%{summary}.

%package -n %{pkgname}-minimize
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-minimize
%{summary}.

%package -n %{pkgname}-network
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-network
%{summary}.

%package -n %{pkgname}-notifications
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-notifications
%{summary}.

%package -n %{pkgname}-power
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-power
%{summary}.

%package -n %{pkgname}-status-area
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-status-area
%{summary}.

%package -n %{pkgname}-tiling
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-tiling
%{summary}.

%package -n %{pkgname}-time
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-time
%{summary}.

%package -n %{pkgname}-workspaces
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-workspaces
%{summary}.

%package -n %{pkgname}-panel-button
Summary:        %{summary}
Requires:       %{name} = %{version}

%description -n %{pkgname}-panel-button
%{summary}.

%package -n %{pkgname}-launcher-button
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-launcher-button
%{summary}.

%description
%{summary}.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%fdupes %{buildroot}

%check
%{cargo_test}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/cosmic
%{_datadir}/metainfo/%{appid}Applets.metainfo.xml
%{_userunitdir}/%{appid}%{statusnotifier}.service
%{_datadir}/dbus-1/services/%{appid}%{statusnotifier}.service

%files -n %{pkgname}-a11y
%{_bindir}/cosmic-applet-a11y
%{_datadir}/applications/%{appid}%{a11y}.desktop

%files -n %{pkgname}-app-list
%{_bindir}/cosmic-app-list
%{_datadir}/applications/%{appid}%{applist}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{applist}.svg

%files -n %{pkgname}-audio
%{_bindir}/%{bin}-audio
%{_datadir}/applications/%{appid}%{audio}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{audio}-symbolic.svg

%files -n %{pkgname}-battery
%{_bindir}/%{bin}-battery
%{_datadir}/applications/%{appid}%{battery}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{battery}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-*.svg

%files -n %{pkgname}-bluetooth
%{_bindir}/%{bin}-bluetooth
%{_datadir}/applications/%{appid}%{bluetooth}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{bluetooth}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-bluetooth-*.svg

%files -n %{pkgname}-input-sources
%{_bindir}/%{bin}-input-sources
%{_datadir}/applications/%{appid}%{inputsources}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{inputsources}-symbolic.svg

%files -n %{pkgname}-minimize
%{_bindir}/%{bin}-minimize
%{_datadir}/applications/%{appid}%{minimize}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{minimize}.svg

%files -n %{pkgname}-network
%{_bindir}/%{bin}-network
%{_datadir}/applications/%{appid}%{network}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{network}-symbolic.svg

%files -n %{pkgname}-notifications
%{_bindir}/%{bin}-notifications
%{_datadir}/applications/%{appid}%{notifications}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{notifications}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-notification-*.svg

%files -n %{pkgname}-power
%{_bindir}/%{bin}-power
%{_datadir}/applications/%{appid}%{power}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{power}-symbolic.svg

%files -n %{pkgname}-status-area
%{_bindir}/%{bin}-status-area
%{_datadir}/applications/%{appid}%{status}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{status}.svg

%files -n %{pkgname}-tiling
%{_bindir}/%{bin}-tiling
%{_datadir}/applications/%{appid}%{tiling}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{tiling}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{tiling}.*.svg

%files -n %{pkgname}-time
%{_bindir}/%{bin}-time
%{_datadir}/applications/%{appid}%{time}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{time}-symbolic.svg

%files -n %{pkgname}-workspaces
%{_bindir}/%{bin}-workspaces
%{_datadir}/applications/%{appid}%{workspaces}.desktop
%{_datadir}/applications/%{appid}%{workspacesbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{workspaces}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{workspacesbutton}.svg

%files -n %{pkgname}-panel-button
%{_bindir}/cosmic-panel-button
%{_datadir}/applications/%{appid}%{appbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{appbutton}.svg

%files -n %{pkgname}-launcher-button
%{_datadir}/applications/%{appid}%{launcherbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}%{launcherbutton}.svg

%changelog
