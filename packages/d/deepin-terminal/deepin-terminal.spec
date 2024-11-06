#
# spec file for package deepin-terminal
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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


%define  _name  deepin-terminal-reborn
%define  apiver 5
%define  sover  0
%define  dtkver 5.5.0

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-terminal
Version:        5.4.33
Release:        0
Summary:        Deepin terminal
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        https://github.com/linuxdeepin/deepin-terminal/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM recompile-with-fPIC.patch hillwood@opensuse.org - Fix build on 64bit arch
Patch1:         recompile-with-fPIC.patch
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  cmake
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  gmock
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(lxqt-build-tools)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkcore) >= 5.5.0
BuildRequires:  pkgconfig(dtkgui) >= 5.5.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.5.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xcb-ewmh)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%lang_package

%description
Deepin Terminal is an advanced terminal emulator with workspace, multiple 
windows, remote management, quake mode and other features.

%package -n libterminalwidget%{apiver}-%{sover}
Summary:        Deepin-terminal libraries
Group:          System/Libraries

%description -n libterminalwidget%{apiver}-%{sover}
This package contains the libraries for deepin-terminal

%package devel
Summary:        Development tools for deepin-terminal
Group:          Development/Libraries/Other
Requires:       libterminalwidget%{apiver}-%{sover}

%description devel
The deepin-terminal-devel package contains the header files and developer
docs for deepin-terminal.

%prep
%autosetup -n %{name}-%{version}
# sed -i '/<QHash>/i#include <QObject>\n#include <QMap>' 3rdparty/terminalwidget/lib/SessionManager.h
sed -i '/LXQtCompilerSettings/a remove_definitions(-DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_TO_ASCII)' 3rdparty/terminalwidget/CMakeLists.txt
sed -i 's|default-config.json|src/assets/other/default-config.json|' CMakeLists.txt


%build
%cmake -DCMAKE_INSTALL_DIR=%{_prefix} \
       -DDTKCORE_TOOL_DIR=%{_libdir}/libdtk-%{dtkver}/DCore/bin/ \
       -DVERSION=%{version}-%{distribution}
%if 0%{?sle_version} > 150000 && 0%{?is_opensuse}
%cmake_build
%else
make %{?_smp_mflags}
%endif

%install
%cmake_install

%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%post -n libterminalwidget%{apiver}-%{sover} -p /sbin/ldconfig
%postun -n libterminalwidget%{apiver}-%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/terminalwidget%{apiver}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%exclude %{_datadir}/terminalwidget%{apiver}/translations

%files -n libterminalwidget%{apiver}-%{sover}
%defattr(-,root,root,-)
%{_libdir}/libterminalwidget%{apiver}.so.*

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations
%{_datadir}/terminalwidget%{apiver}/translations

%files devel
%defattr(-,root,root,-)
%{_libdir}/libterminalwidget%{apiver}.so
%{_libdir}/pkgconfig/terminalwidget%{apiver}.pc
%{_includedir}/terminalwidget%{apiver}
%{_libdir}/cmake/terminalwidget%{apiver}

%changelog
