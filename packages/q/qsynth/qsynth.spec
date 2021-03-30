#
# spec file for package qsynth
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.9.2
Release:        0
Summary:        Graphical User Interface for fluidsynth
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://qsynth.sourceforge.net/qsynth-index.html
Source:         https://sourceforge.net/projects/qsynth/files/qsynth/%{version}/qsynth-%{version}.tar.gz
Patch1:         qsynth-fix_desktop_file.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(fluidsynth) >= 0.80.0
Recommends:     %{name}-lang

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around the Qt5
toolkit using Qt Designer.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r "%{name}" AudioVideo Midi
%find_lang %{name} --with-qt

%files
%doc ChangeLog
%license COPYING
%{_bindir}/qsynth
%{_datadir}/applications/qsynth.desktop
%{_datadir}/icons/*/*/apps/qsynth.png
%{_datadir}/icons/hicolor/scalable/apps/qsynth.svg
%{_datadir}/metainfo
%{_datadir}/qsynth
%exclude %{_datadir}/qsynth/translations
%{_mandir}/man1/qsynth.1%{ext_man}
%{_mandir}/fr/man1/qsynth.1%{ext_man}

%files lang -f %{name}.lang
%{_datadir}/qsynth/translations

%changelog
