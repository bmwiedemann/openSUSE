#
# spec file for package deepin-system-monitor
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


Name:           deepin-system-monitor
Version:        5.8.0.9
Release:        0
Summary:        A user-friendly system monitor
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        https://github.com/linuxdeepin/deepin-system-monitor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source2:        %{name}-root.desktop
BuildRequires:  appstream-glib
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libqt5-linguist
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Requires:       hicolor-icon-theme
Requires:       qt5integration
Recommends:     %{name}-lang

%description
deepin-system-monitor is a simple process and system monitor for the Deepin
Desktop.

%lang_package

%prep
%setup -q
sed -i 's/Exec=deepin-music/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-system-monitor/g' \
translations/desktop/%{name}.desktop

%if 0%{?suse_version} > 1500
# Workaround build failure with GCC 10
sed -e 's|print_err|print_err_system|g' -i src/process/system_stat.cpp
sed -e 's|print_err|print_err_process|g' -i src/process/process_stat.cpp
sed -e 's|print_err|print_err_desktop|g' -i src/process/desktop_entry_stat.cpp
%endif

%build
%cmake
%make_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

# Should be reviewed by security team first, workaround boo#1181886
rm -rf %{buildroot}%{_datadir}/polkit-1

%suse_update_desktop_file -r %{name} QT System Monitor
%suse_update_desktop_file -r %{name}-root QT System Monitor
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-root.desktop
# %dir %{_datadir}/polkit-1
# %dir %{_datadir}/polkit-1/actions
# %{_datadir}/polkit-1/actions/com.deepin.pkexec.%{name}.policy
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/deepin-system-monitor.svg

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
