#
# spec file for package deepin-system-monitor
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

%define    procps_version    %(rpm -q --queryformat '%%{VERSION}' procps-devel)

Name:           deepin-system-monitor
Version:        5.8.27
Release:        0
Summary:        A user-friendly system monitor
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        https://github.com/linuxdeepin/deepin-system-monitor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source2:        %{name}.svg
# PATCH-FIX-UPSTREAN fix-return-type-errors.patch hillwood@opensuse.org
Patch0:         fix-return-type-errors.patch
# PATCH-FIX-UPSTREAN fix-c++17.patch hillwood@opensuse.org - ICU 75 needs c++17
Patch1:         fix-c++17.patch
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  appstream-glib
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libqt5-linguist
BuildRequires:  ncurses-devel
BuildRequires:  procps-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Requires:       /usr/bin/pkexec
Requires:       hicolor-icon-theme
Requires:       qt5integration
Recommends:     %{name}-lang

%description
deepin-system-monitor is a simple process and system monitor for the Deepin
Desktop.

%lang_package

%prep
%autosetup -p1
sed -i 's/Exec=deepin-music/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-system-monitor/g' \
translations/desktop/%{name}.desktop
%if "%{procps_version}" >= "4.0.0"
sed -i '/find_library/s|procps|proc-2|' src/CMakeLists.txt
%endif

%build
%cmake -DVERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%find_lang %{name} --with-qt
%suse_update_desktop_file -r %{name} QT System Monitor
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.deepin.pkexec.%{name}.policy
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files lang -f %{name}.lang
# RPM currently can not handle Asturian
%dir %{_datadir}/deepin-system-monitor
%dir %{_datadir}/deepin-system-monitor/translations
%{_datadir}/deepin-system-monitor/translations/deepin-system-monitor.qm
%lang(ast) %{_datadir}/deepin-system-monitor/translations/deepin-system-monitor_ast.qm

%changelog
