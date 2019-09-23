#
# spec file for package mkvtoolnix
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        37.0.0
Release:        0
Summary:        Tools to Create, Alter, and Inspect Matroska Files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
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
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel >= 5.4.0
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  pugixml-devel
BuildRequires:  ruby >= 1.9
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(Qt5DBus) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.4.0
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebml) >= 1.3.7
BuildRequires:  pkgconfig(libmatroska) >= 1.5.0
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(rake)
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(fmt)
%endif
%else
BuildRequires:  boost-devel >= 1.49
BuildRequires:  gcc7-c++
%endif

%package gui
Summary:        Graphical user interface for mkvtoolnix utils
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}

%description
Tools to create and manipulate Matroska files (extensions .mkv and .mka), a new
container format for audio and video files. Includes command line tools
mkvextract, mkvinfo, mkvmerge and mkvpropedit.

%description gui
This package contains the graphical user interface for the mkvtoolnix utils.

%prep
%setup -q
%patch0 -p1
# Make sure to use system libs:
rm -rf lib/{boost,libebml,libmatroska,pugixml}
%if 0%{?suse_version} > 1500
rm -rf lib/fmt
%endif

%build
%if 0%{?suse_version} <= 1320
# Leap 42.3 is using gcc48 by default (which does not support full c++11)
export CC=gcc-7
export CXX=g++-7
%endif
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

%if 0%{?suse_version} < 1330
%post gui
%icon_theme_cache_post
%mime_database_post
%desktop_database_post

%postun gui
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun
%endif

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
%doc %lang(ko) %dir %{_mandir}/ko
%doc %lang(ko) %dir %{_mandir}/ko/man1
%doc %lang(uk) %dir %{_mandir}/uk
%doc %lang(uk) %dir %{_mandir}/uk/man1

%files gui -f mkvtoolnix-gui.lang
%{_bindir}/mkvtoolnix-gui
# Not included in 42.3
%if 0%{?sle_version} == 120300 && 0%{?is_opensuse}
%dir %{_datadir}/metainfo
%endif
%{_datadir}/metainfo/org.bunkus.mkvtoolnix-gui.appdata.xml
%{_datadir}/mime/packages/org.bunkus.mkvtoolnix-gui.xml
%{_datadir}/%{name}/sounds
%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
%{_datadir}/icons/hicolor/*/apps/mkv*.png
%{_mandir}/man1/mkvtoolnix-gui.1%{ext_man}

%changelog
