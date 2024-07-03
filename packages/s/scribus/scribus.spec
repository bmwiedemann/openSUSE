#
# spec file for package scribus
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without podofo
%bcond_without released
Name:           scribus
Version:        1.6.2
Release:        0
Summary:        Page Layout and Desktop Publishing (DTP)
License:        GPL-2.0-or-later
URL:            https://www.scribus.net/
# https://sourceforge.net/projects/scribus/files/scribus/1.6.2/
Source0:        %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.asc
Source2:        scribus.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Make-sure-information-displayed-on-the-about-window-.patch
# PATCH-FIX-UPSTREAM poppler...

BuildRequires:  cmake >= 3.14.0
BuildRequires:  cups-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  libcdr-devel
BuildRequires:  libfreehand-devel
BuildRequires:  libmspub-devel
BuildRequires:  libpagemaker-devel
%if %{with podofo}
BuildRequires:  libpodofo-devel
%endif
BuildRequires:  libqxp-devel
BuildRequires:  librevenge-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvisio-devel
BuildRequires:  libwpd-devel
BuildRequires:  libwpg-devel
BuildRequires:  libzmf-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libpng16)
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
BuildRequires:  pkgconfig(poppler) > 21.03.0
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Recommends:     python3-Pillow
Recommends:     python3-tk
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

%description doc
This package provides the documentation for Scribus.

%prep
# Convert line endings before patching
%setup -q
# W: wrong-script-end-of-line-encoding
find . -type f \( -iname \*.py -o -iname \*.cpp -o -iname \*.h \) -exec dos2unix {} \;

%autopatch -p1

# Unused test file still using QQC1
rm scribus/ui/qml/qtq_test1.qml

find . \( -name "*.py" -o -name "*.html" \) -exec sed -i 's#/usr/bin/env python.*#/usr/bin/python3#' {} \;

%build
# Don't use the %%cmake macro, it causes crashes when starting scribus
mkdir build
pushd build
cmake .. \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DWANT_DISTROBUILD=TRUE \
  -DWANT_HUNSPELL=TRUE \
  -DWANT_GRAPHICSMAGICK=TRUE \
  -DWANT_CPP17=TRUE \
%if "%{_lib}" == "lib64"
  -DWANT_LIB64=TRUE \
%endif
%if %{without podofo}
  -DWITH_PODOFO=FALSE
%endif

%cmake_build
popd

%install
%cmake_install

# These files are required at runtime to populate the help/about window
mkdir -p %{buildroot}%{_datadir}/scribus/aboutData
mv %{buildroot}%{_datadir}/doc/scribus/{AUTHORS,COPYING,LINKS,TRANSLATION} %{buildroot}%{_datadir}/scribus/aboutData/

# Already in %%doc
rm %{buildroot}%{_datadir}/doc/scribus/{ChangeLog,README}

%fdupes %{buildroot}%{_datadir}/doc/scribus
%fdupes %{buildroot}%{_datadir}/scribus

%files doc
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/doc/scribus/
%lang(de) %{_datadir}/doc/scribus/de/
%lang(it) %{_datadir}/doc/scribus/it/
%lang(ru) %{_datadir}/doc/scribus/ru/
%{_datadir}/doc/scribus/en/

%files
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/doc/scribus/
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%lang(de) %{_mandir}/de/man1/scribus.1%{?ext_man}
%lang(pl) %{_mandir}/pl/man1/scribus.1%{?ext_man}
%{_bindir}/scribus
%{_datadir}/applications/scribus.desktop
%{_datadir}/icons/hicolor/*/apps/scribus.png
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.scribus.png
%{_datadir}/metainfo/scribus.appdata.xml
%{_datadir}/mime/packages/scribus.xml
%{_datadir}/scribus/
%{_libdir}/scribus/
%{_mandir}/man1/scribus.1%{?ext_man}

%changelog
