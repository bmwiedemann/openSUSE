#
# spec file for package goldendict-ng
#
# Copyright (c) 2023 SUSE LLC
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


%define qt_version 5
Name:           goldendict-ng
Version:        23.05.03
Release:        0
Summary:        Dictionary Lookup Program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://xiaoyifang.github.io/goldendict-ng/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
# /Section dependencies
BuildRequires:  eb-devel
BuildRequires:  hunspell-devel >= 1.2.4
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapian-core)
BuildRequires:  pkgconfig(xtst)
# /Section Qt
BuildRequires:  pkgconfig(Qt%{qt_version}Concurrent)
BuildRequires:  pkgconfig(Qt%{qt_version}Core)
BuildRequires:  pkgconfig(Qt%{qt_version}Gui)
BuildRequires:  pkgconfig(Qt%{qt_version}Multimedia)
BuildRequires:  pkgconfig(Qt%{qt_version}Svg)
BuildRequires:  pkgconfig(Qt%{qt_version}TextToSpeech)
BuildRequires:  pkgconfig(Qt%{qt_version}WebEngineWidgets)
BuildRequires:  pkgconfig(Qt%{qt_version}Widgets)
BuildRequires:  pkgconfig(Qt%{qt_version}Xml)
%if %{qt_version} >= 6
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6Core5Compat)
%else
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5X11Extras)
%endif
# /Section compresion libraries
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(zlib)
# /Section ffmpeg 6
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%if %{qt_version} >= 6
Requires:       qt6-multimedia
%endif
Provides:       goldendict = %{version}
Obsoletes:      goldendict < 1.5.1
Obsoletes:      goldendict-lang < 1.5.1

%description
The Next Generation GoldenDict: A feature-rich dictionaries lookup program, supporting many dictionary formats.

%lang_package

%prep
%autosetup

%build
%if %{qt_version} >= 6
%qmake6 PREFIX=%{_prefix} "CONFIG+=use_xapian" "CONFIG+=zim_support" "CONFIG+=chinese_conversion_support" goldendict.pro
%qmake6_build
%else
%qmake5 PREFIX=%{_prefix} "CONFIG+=use_xapian" "CONFIG+=zim_support" "CONFIG+=chinese_conversion_support" goldendict.pro
%make_jobs
%endif

%install
%if %{qt_version} >= 6
%qmake6_install
%else
%qmake5_install
%endif
%suse_update_desktop_file -r org.goldendict.GoldenDict Office Dictionary

%files
%license LICENSE.txt
%{_bindir}/goldendict
%{_datadir}/goldendict
%{_datadir}/applications/org.goldendict.GoldenDict.desktop
%{_datadir}/metainfo/org.goldendict.GoldenDict.metainfo.xml
%{_datadir}/pixmaps/goldendict.png
%exclude %{_datadir}/goldendict/locale/

%files lang
%{_datadir}/goldendict/locale/
%exclude %{_datadir}/goldendict/locale/crowdin.qm

%changelog
