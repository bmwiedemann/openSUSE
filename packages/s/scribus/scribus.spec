#
# spec file for package scribus
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) Peter Linnell and 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           scribus
Version:        1.5.5
Release:        0
Summary:        Page Layout and Desktop Publishing (DTP)
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Other
URL:            https://www.scribus.net/
# https://sourceforge.net/projects/scribus/files/scribus-devel/1.5.5/
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Make-sure-information-displayed-on-the-about-window-.patch
# PATCH-FEATURE-UPSTREAM
Patch1:         port-scripter-to-Python-3.patch
# PATCH-FIX-UPSTREAM
Patch2:         Work-around-poppler-0.82-signature-changes.patch
# PATCH-FIX-UPSTREAM
Patch3:         Use-same-mechanism-as-with-previous-poppler-versions.patch
# PATCH-FIX-UPSTREAM
Patch4:         Fix-failure-to-build-against-poppler-0.83.0.patch
# PATCH-FIX-UPSTREAM
Patch5:         Fix-failure-to-build-with-poppler-0.84.0.patch
# PATCH-FIX-UPSTREAM
Patch6:         Fails-to-build-with-python-3.8.patch
# PATCH-FIX-UPSTREAM
Patch7:         0001-PDF-import-plugin-support-poppler-0.86.x.patch
# PATCH-FIX-UPSTREAM
Patch8:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  libcdr-devel
BuildRequires:  libfreehand-devel
BuildRequires:  libmspub-devel
BuildRequires:  libpagemaker-devel
BuildRequires:  libpodofo-devel
BuildRequires:  libqxp-devel
BuildRequires:  librevenge-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvisio-devel
BuildRequires:  libwpd-devel
BuildRequires:  libwpg-devel
BuildRequires:  libzmf-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui) >= 5.7.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.7.0
BuildRequires:  cmake(Qt5Network) >= 5.7.0
BuildRequires:  cmake(Qt5OpenGL) >= 5.7.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.7.0
BuildRequires:  cmake(Qt5Widgets) >= 5.7.0
BuildRequires:  cmake(Qt5Xml) >= 5.7.0
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Recommends:     python3-Pillow
Recommends:     python3-tk
# Only available in graphics for the moment
Recommends:     uniconvertor
Recommends:     scribus-doc

# Not packaged anymore
Provides:       scribus-devel = %{version}
Obsoletes:      scribus-devel < %{version}

%description
Scribus is a page layout program which produces output in PDF and
Postscript.

Scribus supports publishing features such as CMYK and spot colors,
PDF creation, Encapsulated Postscript import and export and creation
of color separations.

%package doc
Summary:        Documentation for Scribus
Group:          Documentation/HTML

%description doc
This package provides the documentation for Scribus.

%prep
%setup -q
# W: wrong-script-end-of-line-encoding
# also required for cherry-picked patches
find . -type f \( -iname \*.py -o -iname \*.cpp -o -iname \*.h \) -exec dos2unix {} \;

%autopatch -p1

%build
# Don't use the %%cmake macro, it causes crashes when starting scribus
mkdir build
pushd build
cmake .. \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DWANT_RELEASEWITHDEBUG=1 \
  -DWANT_DISTROBUILD=1 \
  -DWANT_HUNSPELL=1 \
  -DWANT_GRAPHICSMAGICK=1 \
%if "%{_lib}" == "lib64"
  -DWANT_LIB64=1
%endif

%cmake_build
popd

%install
%cmake_install

# These files are required at runtime to populate the help/about window
mkdir -p %{buildroot}%{_datadir}/scribus/aboutData
mv %{buildroot}%{_datadir}/doc/scribus/{AUTHORS,COPYING,LINKS,TRANSLATION} %{buildroot}%{_datadir}/scribus/aboutData/

# Already in %%doc
rm -f %{buildroot}%{_datadir}/doc/scribus/{ChangeLog,README}

%fdupes %{buildroot}%{_datadir}/doc/scribus
%fdupes %{buildroot}%{_datadir}/scribus

%suse_update_desktop_file -r scribus Qt Office WordProcessor

%files doc
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/doc/scribus/
%lang(de) %{_datadir}/doc/scribus/de/
%lang(it) %{_datadir}/doc/scribus/it/
%{_datadir}/doc/scribus/en/

%files
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/doc/scribus/
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%lang(de) %dir %{_mandir}/de
%lang(de) %dir %{_mandir}/de/man1
%lang(de) %{_mandir}/de/man1/scribus.1%{?ext_man}
%lang(pl) %dir %{_mandir}/pl
%lang(pl) %dir %{_mandir}/pl/man1
%lang(pl) %{_mandir}/pl/man1/scribus.1%{?ext_man}
%{_bindir}/scribus
%{_datadir}/applications/scribus.desktop
%{_datadir}/icons/hicolor/*/apps/scribus.png
%{_datadir}/metainfo/scribus.appdata.xml
%{_datadir}/mime/packages/scribus.xml
%{_datadir}/scribus/
%{_libdir}/scribus/
%{_mandir}/man1/scribus.1%{?ext_man}

%changelog
