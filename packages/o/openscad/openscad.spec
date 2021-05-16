#
# spec file for package openscad
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


Name:           openscad
Version:        2021.01
Release:        0
Summary:        Programmers Solid 3D CAD Modeller
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.openscad.org/
Source:         https://files.openscad.org/%{name}-%{version}.src.tar.gz
BuildRequires:  bison
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  harfbuzz-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libcgal-devel
BuildRequires:  libqscintilla-qt5-devel
BuildRequires:  libspnav-devel
BuildRequires:  memory-constraints
BuildRequires:  opencsg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
# With v2019.05, openGL is required but Arm uses openGL ES
ExcludeArch:    %{arm} aarch64

%description
OpenSCAD is a software for creating solid 3D CAD objects. It does not
focus on the artistic aspects of 3D modelling and does not target the
creation of, say, computer-animated movies, but instead on the CAD
aspects, e.g. modelling of machine parts.

%prep
%setup -q

%build
%qmake5 PREFIX=%{_prefix} CONFIG+=qopenglwidget CONFIG+=c++14
# As of 08.05.2021, memoryperjob constraint is not working correctly,
# so limit memory per job here.
%limit_build -m 2500
%make_build

%install
make INSTALL_ROOT=%{buildroot} install
install -D -m 0644 doc/openscad.1 %{buildroot}%{_mandir}/man1/openscad.1
# remove bundled liberation fonts
rm -rf %{buildroot}%{_datadir}/openscad/fonts
%find_lang %{name}

rm %{buildroot}%{_datadir}/openscad/libraries/MCAD/.gitignore

%files -f %{name}.lang
%dir %{_datadir}/metainfo

%doc README.md doc/*.pdf
%license COPYING

%{_bindir}/openscad
%{_datadir}/applications/openscad.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.openscad.OpenSCAD.appdata.xml
%{_datadir}/mime/packages/openscad.xml
%{_datadir}/openscad/
%{_mandir}/man1/*

%changelog
