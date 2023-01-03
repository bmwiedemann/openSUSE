#
# spec file for package qsynth
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           qsynth
Version:        0.9.9
Release:        0
Summary:        Graphical User Interface for fluidsynth
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://qsynth.sourceforge.net/qsynth-index.html
Source:         https://sourceforge.net/projects/qsynth/files/qsynth/%{version}/qsynth-%{version}.tar.gz
Patch1:         qsynth-fix_desktop_file.patch
BuildRequires:  cmake
%if 0%{?sle_version} >= 150400
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(fluidsynth) >= 2.0.0
Recommends:     %{name}-lang

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around the Qt5
toolkit using Qt Designer.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?sle_version} >= 150400
export CXX=g++-11
%endif
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r "org.rncbc.%{name}" AudioVideo Midi
%find_lang %{name} --with-qt

%files
%doc ChangeLog
%license LICENSE
%{_bindir}/qsynth
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/*/*/apps/org.rncbc.qsynth.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.qsynth.svg
%{_datadir}/metainfo
%{_datadir}/qsynth
%exclude %{_datadir}/qsynth/translations
%{_mandir}/man1/qsynth.1%{ext_man}
%{_mandir}/fr/man1/qsynth.1%{ext_man}

%files lang -f %{name}.lang
%{_datadir}/qsynth/translations

%changelog
