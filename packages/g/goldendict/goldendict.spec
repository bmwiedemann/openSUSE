#
# spec file for package goldendict
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2013 Tvangeste <i.4m.l33t@yandex.ru>
# Copyright 2011-2021 <opensuse.lietuviu.kalba@gmail.com>
# Copyright 2021 <coder53@gmail.com>
# Copyright 2008-2009 Buschmann <buschmann23@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
# 

Name:           goldendict
Summary:        Dictionary Lookup Program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
Url:            http://goldendict.org/
Version:        1.5.0~rc2+git.20211231T234821
Release:        0
Source0:        goldendict-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  libbz2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hunspell-devel >= 1.2.4
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(libzip)
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xz
# Qt 5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(x11)
# AV
BuildRequires:  libao-devel
BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  libavutil-devel
#BuildRequires:  libffmpeg-devel
# eb-devel / libeb-dev for epwing. Otherwise use "CONFIG+=no_epwing_support"
%if 0%{?is_opensuse}
BuildRequires:  eb-devel
%endif
# Zstd compression required for optional ZIM format support. It can be enabled by "CONFIG+=zim_support"
BuildRequires:  pkgconfig(libzstd)



%description
Feature-rich dictionary lookup program.
    * Support of multiple dictionary file formats:
      * Babylon .BGL files
      * StarDict .ifo/.dict/.idx/.syn dictionaries
      * Dictd .index/.dict(.dz) dictionary files
      * ABBYY Lingvo .dsl source files
      * ABBYY Lingvo .lsa/.dat audio archives
    * Support for Wikipedia, Wiktionary or any other MediaWiki-based sites
    * Scan popup functionality. A small window pops up with translation of a
      word chosen from antoher application.
    * Full-text search.
    * And much more...

Author:
-------
    Konstantin Isakov

%lang_package

%prep
%setup -n goldendict-%{version} -q 
git init 
%if 0%{?suse_version} < 1550
  # For Qt5.12 compatibility in openSUSE Leap 15.3
  find -name '*.cc' -exec sed -i 's/Qt::SkipEmptyParts/QString::SkipEmptyParts/g' {} +
  find -name '*.cc' -exec sed -i 's/errorOccurred/error/g' {} +
%endif

%build
%if 0%{?is_opensuse}
  %qmake5 PREFIX=%{_prefix} "CONFIG+=zim_support" goldendict.pro
%else
  %qmake5 PREFIX=%{_prefix} "CONFIG+=no_ffmpeg_player" "CONFIG+=no_epwing_support" \
    "CONFIG+=zim_support" goldendict.pro
%endif
%make_jobs

%install
%qmake5_install
%suse_update_desktop_file -r org.goldendict.GoldenDict Office Dictionary

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%license LICENSE.txt
%defattr(755,root,root,755)
%{_bindir}/%{name}
%defattr(644,root,root,755)
%{_datadir}/%{name}
%{_datadir}/applications/org.goldendict.GoldenDict.desktop
%{_datadir}/metainfo/org.goldendict.GoldenDict.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/locale/

%files lang
%{_datadir}/%{name}/locale/

%changelog
