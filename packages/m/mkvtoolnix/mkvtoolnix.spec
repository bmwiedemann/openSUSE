#
# spec file for package mkvtoolnix
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


Name:           mkvtoolnix
Version:        85.0
Release:        0
Summary:        Tools to Create, Alter, and Inspect Matroska Files
License:        GPL-2.0-or-later
URL:            http://bunkus.org/videotools/mkvtoolnix/
#Git:           http://github.com/mbunkus/mkvtoolnix
Source0:        https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz
Source1:        https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz.sig
# Sub-key ID 0x74AF00AD F2E32C85 of key ID 0x0F92290A 445B9007 is used for signing
Source2:        mkvtoolnix.keyring
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  libboost_filesystem-devel >= 1.66.0
BuildRequires:  libboost_headers-devel >= 1.66.0
BuildRequires:  libboost_system-devel >= 1.66.0
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmp)
%else
BuildRequires:  gcc10-c++
BuildRequires:  gmp-devel
%endif
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt-tools
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  pugixml-devel
BuildRequires:  ruby >= 1.9
BuildRequires:  shared-mime-info
BuildRequires:  utfcpp-devel
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core) >= 6.2.0
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fmt) >= 8.0.0
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebml) >= 1.4.4
BuildRequires:  pkgconfig(libmatroska) >= 1.7.1
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(rake)

%description
Tools to create and manipulate Matroska files (extensions .mkv and .mka), a new
container format for audio and video files. Includes command line tools
mkvextract, mkvinfo, mkvmerge and mkvpropedit.

%package gui
Summary:        Graphical user interface for mkvtoolnix utils
Requires:       %{name} = %{version}
Requires:       qt6-multimedia

%description gui
This package contains the graphical user interface for the mkvtoolnix utils.

%package tools
Summary:        Additional command line tools for mkv files

%description tools
This package contains extra command line tools for mkv diagnostic.

%prep
%autosetup -p1
# Make sure to use system libs:
rm -rf lib/{libebml,libmatroska,nlohmann-json,pugixml,fmt,utf8-cpp}

%build
export CXX=g++
test -x "$(type -p g++-10)" && export CXX=g++-10
export CPPFLAGS="%{optflags} -I%{_includedir}/utf8cpp"
%configure --disable-update-check --enable-debug --enable-optimization
rake --verbose %{?_smp_mflags} V=1

%install
rake --verbose DESTDIR=%{buildroot} install
%find_lang %{name} --all-name
%find_lang mkvpropedit --with-man
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvinfo --with-man
%find_lang mkvtoolnix-gui --with-man

# tools are built but not installed automatically
install -m0755 src/tools/ac3parser src/tools/base64tool src/tools/bluray_dump \
  src/tools/checksum src/tools/diracparser src/tools/ebml_validator \
  src/tools/hevcc_dump src/tools/pgs_dump src/tools/vc1parser \
  src/tools/xyzvc_dump -t %{buildroot}%{_bindir}

%fdupes %{buildroot}/%{_prefix}

%files -f %{name}.lang -f mkvpropedit.lang -f mkvextract.lang -f mkvmerge.lang -f mkvinfo.lang
%license COPYING
%doc AUTHORS NEWS.md README.md
%doc examples
%dir %{_datadir}/%{name}
%{_bindir}/mkvextract
%{_bindir}/mkvinfo
%{_bindir}/mkvmerge
%{_bindir}/mkvpropedit
%{_mandir}/man1/mkvinfo.1%{ext_man}
%{_mandir}/man1/mkvextract.1%{ext_man}
%{_mandir}/man1/mkvmerge.1%{ext_man}
%{_mandir}/man1/mkvpropedit.1%{ext_man}
%doc %lang(be) %dir %{_mandir}/be
%doc %lang(be) %dir %{_mandir}/be/man1
%doc %lang(bg) %dir %{_mandir}/bg
%doc %lang(bg) %dir %{_mandir}/bg/man1
%doc %lang(ko) %dir %{_mandir}/ko
%doc %lang(ko) %dir %{_mandir}/ko/man1
%doc %lang(uk) %dir %{_mandir}/uk
%doc %lang(uk) %dir %{_mandir}/uk/man1

%files gui -f mkvtoolnix-gui.lang
%{_bindir}/mkvtoolnix-gui
%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/%{name}/qt_resources.rcc
%{_datadir}/%{name}/sounds
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/icons/hicolor/*/apps/mkv*.png
%{_mandir}/man1/mkvtoolnix-gui.1%{ext_man}

%files tools
%{_bindir}/ac3parser
%{_bindir}/base64tool
%{_bindir}/bluray_dump
%{_bindir}/checksum
%{_bindir}/diracparser
%{_bindir}/ebml_validator
%{_bindir}/hevcc_dump
%{_bindir}/pgs_dump
%{_bindir}/vc1parser
%{_bindir}/xyzvc_dump

%changelog
