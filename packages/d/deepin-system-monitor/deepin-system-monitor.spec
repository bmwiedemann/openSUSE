#
# spec file for package deepin-system-monitor
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


Name:           deepin-system-monitor
Version:        1.5.2
Release:        0
Summary:        A user-friendly system monitor
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        https://github.com/linuxdeepin/deepin-system-monitor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-UPSTEAM Fix-redefinition-error.patch hillwood@opensuse.org - Fix redefinition of 'struct std::hash<QString>' error
Patch0:         Fix-redefinition-error.patch
# PATCH-FIX-UPSTEAM deepin-system-monitor-Qt-5_15.patch hillwood@opensuse.org - Support Qt 5.15
Patch1:         %{name}-Qt-5_15.patch
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcap-devel
BuildRequires:  libpcap-devel
BuildRequires:  libqt5-linguist
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Requires:       hicolor-icon-theme
Recommends:     %{name}-lang

%description
deepin-system-monitor is a simple process and system monitor for the
Deepin Desktop.

%lang_package

%prep
%setup -q
%patch0 -p1
%if 0%{?suse_version} > 1500
%patch1 -p1
%endif
sed -i 's/lrelease/lrelease-qt5/g' translations/translate_generation.sh

%build
%qmake5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%suse_update_desktop_file -r %{name} QT System Monitor
%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}/

%changelog
