#
# spec file for package qpwgraph
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


Name:           qpwgraph
Version:        0.7.4
Release:        0
Summary:        PipeWire Graph Qt GUI Interface
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://gitlab.freedesktop.org/rncbc/qpwgraph
Source:         https://gitlab.freedesktop.org/rncbc/qpwgraph/-/archive/v%{version}/qpwgraph-v%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpipewire-0.3)

%description
qpwgraph is a graph manager dedicated for PipeWire, using the
Qt C++ framework, based and pretty much like the same of QjackCtl.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake_qt6 \
  -DCONFIG_ALSA_MIDI=ON
%qt6_build

%install
%qt6_install

%files
%license LICENSE.md
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.rncbc.%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/org.rncbc.%{name}*.*
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/mime/packages/org.rncbc.%{name}.xml

%changelog
