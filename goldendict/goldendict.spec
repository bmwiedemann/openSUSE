#
# spec file for package goldendict
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2013 Tvangeste <i.4m.l33t@yandex.ru>
# Copyright 2011-2018 <opensuse.lietuviu.kalba@gmail.com>
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           goldendict
Summary:        Dictionary Lookup Program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
Url:            http://goldendict.org/
Version:        1.5.0~rc2+git.20190215T001516
Release:        0
Source0:        goldendict-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  eb-devel
BuildRequires:  git
BuildRequires:  hunspell-devel >= 1.2.4
BuildRequires:  libtiff-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libzip-devel
BuildRequires:  lzo-devel
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zlib-devel

%if 0%{?suse_version}
BuildRequires:  libbz2-devel
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ) || ( 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
%else
BuildRequires:  libQtWebKit-devel
BuildRequires:  libqt4-devel >= 4.5.0
%endif
%if ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ) || 0%{?suse_version} > 1320
BuildRequires:  libao-devel
BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  libavutil-devel
#BuildRequires:  libffmpeg-devel
%endif
%endif

%if 0%{?fedora_version}
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXtst-devel
BuildRequires:  qt-devel
BuildRequires:  qt-webkit-devel >= 4.5
%endif
Recommends:     %{name}-lang

%description
Feature-rich dictionary lookup program.
    * Use of WebKit for an accurate articles' representation, complete with
      all formatting, colors, images and links.
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

%build
%if 0%{?suse_version}
  %if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ) || (0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200)
    %if 0%{?is_opensuse}
      %qmake5 \
        PREFIX=%{_prefix} \
        %if 0%{?sle_version} < 150000
        "CONFIG+=old_hunspell" \
        %endif
        "CONFIG+=zim_support" goldendict.pro
      %make_jobs
    %else
      %qmake5 \
        PREFIX=%{_prefix} "CONFIG+=no_ffmpeg_player" \
        %if 0%{?sle_version} < 150000
        "CONFIG+=old_hunspell" \
        %endif
        "CONFIG+=zim_support" goldendict.pro
      %make_jobs
    %endif
  %else
      qmake PREFIX=/usr "CONFIG+=no_ffmpeg_player" "CONFIG+=no_qtmultimedia_player" "CONFIG+=old_hunspell" goldendict.pro && make clean && make
      make %{?jobs:-j %jobs}
  %endif
%endif
%if 0%{?fedora_version}
  qmake-qt4 PREFIX=/usr "CONFIG+=no_ffmpeg_player" "CONFIG+=old_hunspell" && make clean && make
  make %{?jobs:-j %jobs}
%endif

%install
%if 0%{?suse_version}
  %if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?is_opensuse} ) || ( 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200)
    %qmake5_install
  %else
    INSTALL_ROOT=%{buildroot} %makeinstall
  %endif
  %suse_update_desktop_file -r %{name} Office Dictionary
%endif
%if 0%{?fedora_version}
   rm -rf %{buildroot}
   make install DESTDIR=%buildroot INSTALL_ROOT=%{buildroot} INSTALL="install -p"
%endif

%clean
  rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%license LICENSE.txt
%defattr(755,root,root,755)
%_bindir/%{name}
%defattr(644,root,root,755)
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{name}.png
%_datadir/%{name}
%exclude %{_datadir}/%{name}/locale/

%files lang
%{_datadir}/%{name}/locale/

%changelog
