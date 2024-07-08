#
# spec file for package fooyin
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


Name:           fooyin
Version:        0.5.3
Release:        0
Summary:        A customisable music player built with Qt
License:        GPL-3.0-only
URL:            https://github.com/ludouzi/%{name}
Source:         https://github.com/ludouzi/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt6-base-devel
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xkbcommon)

%description
fooyin is a Qt6 music player built around customisation. It offers a
growing list of widgets to manage and play a local music collection.
It is extendable through the use of plugins, and many widgets make
use of FooScript to offer an even deeper level of control.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# No header files were installed, so... no point in keeping the
# component libraries' devel files.
rm -fv %{buildroot}/%{_libdir}/fooyin/*.so

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/doc/%{name}
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.*
%{_datadir}/%{name}
%{_libdir}/%{name}/

%changelog
