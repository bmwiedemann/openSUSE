#
# spec file for package mkvtoolnix
#
# Copyright (c) 2020 SUSE LLC
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
Version:        51.0.0
Release:        0
Summary:        Tools to Create, Alter, and Inspect Matroska Files
License:        GPL-2.0-or-later
URL:            http://bunkus.org/videotools/mkvtoolnix/
#Git:           http://github.com/mbunkus/mkvtoolnix
Source0:        https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz
Source1:        https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz.sig
# Sub-key ID 0x74AF00AD F2E32C85 of key ID 0x0F92290A 445B9007 is used for signing
Source2:        mkvtoolnix.keyring
# PATCH-OPENSUSE-FIX mkvtoolnix-use-system-boost.patch -- Fix includes to use boost from system
Patch0:         mkvtoolnix-use-system-boost.patch
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel >= 1.60.0
BuildRequires:  libboost_headers-devel >= 1.60.0
BuildRequires:  libboost_system-devel >= 1.60.0
BuildRequires:  libxslt-tools
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  pugixml-devel
BuildRequires:  ruby >= 1.9
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.9.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9.0
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fmt) >= 6.1.0
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebml) >= 1.4.0
BuildRequires:  pkgconfig(libmatroska) >= 1.6.1
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(rake)

%package gui
Summary:        Graphical user interface for mkvtoolnix utils
Requires:       %{name} = %{version}

%description
Tools to create and manipulate Matroska files (extensions .mkv and .mka), a new
container format for audio and video files. Includes command line tools
mkvextract, mkvinfo, mkvmerge and mkvpropedit.

%description gui
This package contains the graphical user interface for the mkvtoolnix utils.

%prep
%autosetup -p1
# Make sure to use system libs:
rm -rf lib/{boost,libebml,libmatroska,nlohmann-json,pugixml,fmt}

%build
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
%{_datadir}/%{name}/sounds
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/icons/hicolor/*/apps/mkv*.png
%{_mandir}/man1/mkvtoolnix-gui.1%{ext_man}

%changelog
