#
# spec file for package flacon
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014-2018 Alexander Evseev <aevseev@gmail.com>
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


Name:           flacon
Version:        9.5.1
Release:        0
Summary:        Audio File Encoder
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://flacon.github.io/
Source:         https://github.com/flacon/flacon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(uchardet)
Recommends:     faac
Recommends:     flac
Recommends:     lame
Recommends:     mac
Recommends:     mp3gain
Recommends:     opus-tools
Recommends:     sox
Recommends:     ttaenc
Recommends:     vorbis-tools
Recommends:     vorbisgain
Recommends:     wavpack

%description
Flacon extracts individual tracks from one big audio file containing the entire
album of music and saves them as separate audio files. To do this, it uses
information from the appropriate CUE file. Besides, Flacon makes it possible
to conveniently revise or specify tags both for all tracks at once or for each
tag separately.

%lang_package

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/flacon.png
%{_datadir}/icons/hicolor/scalable/apps/flacon.svg
%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
