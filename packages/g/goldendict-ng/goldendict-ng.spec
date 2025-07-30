#
# spec file for package goldendict-ng
#
# Copyright (c) 2025 SUSE LLC
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


%define __builder ninja
%if 0%{?suse_version} < 1600
%define gcc_ver 11
%endif
Name:           goldendict-ng
Version:        25.06.0
Release:        0
Summary:        Dictionary Lookup Program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://xiaoyifang.github.io/goldendict-ng/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unzip
# /Section dependencies
BuildRequires:  eb-devel
BuildRequires:  hunspell-devel >= 1.2.4
BuildRequires:  pkgconfig(libzim)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapian-core)
BuildRequires:  pkgconfig(xtst)
# /Section Qt
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6TextToSpeech)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
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
Requires:       qt6-multimedia
Provides:       goldendict = %{version}
Obsoletes:      goldendict < 1.5.1

%description
The Next Generation GoldenDict: A feature-rich dictionaries lookup program,
supporting many dictionary formats.

%if 0%{?suse_version} >= 1600
%lang_package -b goldendict-lang
%else
%lang_package
%endif

%prep
%autosetup

%build
%cmake \
  -DCMAKE_C_COMPILER=gcc%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	%{nil}
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_bindir}/goldendict
%{_datadir}/goldendict
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/pixmaps/goldendict.png
%exclude %{_datadir}/goldendict/locale/

%files lang
%{_datadir}/goldendict/locale/
%exclude %{_datadir}/goldendict/locale/crowdin.qm

%changelog
