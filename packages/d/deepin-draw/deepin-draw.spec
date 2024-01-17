#
# spec file for package deepin-draw
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

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-draw
Version:        5.11.4
Release:        0
Summary:        A calendar application for Deepin Desktop
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        https://github.com/linuxdeepin/deepin-draw/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gtest
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
Recommends:     %{name}-lang

%description
Draw is a lightweight drawing tool for users to freely draw and simply edit
images developed by Deepin Technology.

%lang_package

%prep
%setup -q -n %{name}-%{version}
# sed -i 's/Exec=dde-calendar/Exec=env QT_QPA_PLATFORMTHEME=deepin dde-calendar/g' \
# calendar-client/assets/dde-calendar.desktop
sed -i '/MimeTypeDir/s|application|mime/application|' src/CMakeLists.txt

%build
%cmake -DVERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file -r %{name} Graphics 2DGraphics RasterGraphics

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/mime/application
%{_datadir}/mime/application/x-ddf.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/icons/deepin
%dir %{_datadir}/icons/deepin/apps
%dir %{_datadir}/icons/deepin/apps/scalable
%{_datadir}/icons/deepin/apps/scalable/%{name}.svg
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%{_datadir}/mime/packages/%{name}.xml

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
