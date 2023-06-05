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


Name:           goldendict-ng
Version:        23.05.03
Release:        0
Summary:        Dictionary Lookup Program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://xiaoyifang.github.io/goldendict-ng/
Source0:        goldendict-ng-%{version}.tar.xz
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
# /Section Qt 6
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6TextToSpeech)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  qt6-tools-linguist
# /Section compresion libraries
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
# /Section ffmpeg 6
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
Requires:       qt6-multimedia
Provides:       goldendict = %{version}
Obsoletes:      goldendict < 1.5.1
Obsoletes:      goldendict-lang < 1.5.1

%description
The Next Generation GoldenDict: A feature-rich dictionaries lookup program, supporting many dictionary formats.

%lang_package

%prep
%autosetup -p1

%build
%qmake6 PREFIX=%{_prefix} "CONFIG+=use_xapian" "CONFIG+=zim_support" "CONFIG+=chinese_conversion_support" goldendict.pro
%qmake6_build

%install
%qmake6_install
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
