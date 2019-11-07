#
# spec file for package inkscape
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


Name:           inkscape
Version:        0.92.4
Release:        0
Summary:        Vector Illustration Program
License:        GPL-3.0-only
Group:          Productivity/Graphics/Vector Editors
Url:            http://www.inkscape.org/
#Source:        https://media.inkscape.org/dl/resources/file/%%{name}-%%{version}.tar.bz2
Source:         %{name}-%{version}.tar.bz2

# openSUSE palette file
Source1:        openSUSE.gpl
Source2:        inkscape-split-extensions-extra.sh
# PATCH-FIX-OPENSUSE inkscape-packages.patch sbrabec@suse.cz -- Suggest packages instead of compilation from source.
Patch0:         inkscape-packages.patch
# PATCH-FIX-OPENSUSE build_internal_libraries_as_static.patch -- Avoid problems with dynamic library default from %%cmake macro
Patch1:         build_internal_libraries_as_static.patch
# PATCH-FIX-OPENSUSE fix_install_targets.patch -- use correct libdir etc.
Patch2:         fix_install_targets.patch
# PATCH-FIX-UPSTREAM inkscape-fix-for-poppler-0.76.patch -- Fix build with poppler 0.76
Patch3:         inkscape-fix-for-poppler-0.76.patch
# PATCH-FIX-OPENSUSE -- run i18n string extraction with python3
Patch4:         0001-Run-python-script-for-translations-with-Python-3.patch
# PATCH-FIX-UPSTREAM https://gitlab.com/inkscape/inkscape/merge_requests/568.patch -- fixed in 0.92.5
Patch5:         mr_568_extensions_python3_compatibility.patch
# PATCH-FIX-UPSTREAM https://gitlab.com/inkscape/inkscape/commit/f5e0ea893f34c91f25d4781b37ee6eff15a7e213
Patch6:         f5e0ea893f34_extensions_python3_compatibility.patch
# PATCH-FIX-UPSTREAM https://gitlab.com/inkscape/inkscape/merge_requests/582.patch -- fixed in 0.92.5
Patch7:         mr_582_extensions_python3_compatibility.patch
# PATCH-FIX-UPSTREAM inkscape-fix-for-poppler-0.82.patch -- Fix build poppler 0.82
Patch8:         inkscape-fix-for-poppler-0.82.patch

BuildRequires:  gtkspell-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  intltool
# Disabling IM until inkscape upstream supports IM7
#BuildRequires:  libMagick++-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  perl
BuildRequires:  popt-devel
BuildRequires:  potrace-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpg-0.3)
Requires:       python3-gobject
Recommends:     %{name}-lang
Recommends:     python3-lxml
Recommends:     python3-scour

%description
Inkscape is a vector graphics editor.

%package extensions-extra
Summary:        Additional extensions for Inkscape
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}
# ps2pdf-ext.py is a wrapper around ps2pdf, which lives in ghostscript package.
Requires:       ghostscript
Requires:       python3-lxml
Requires:       python3-xml
# for cdr and wmf modules
Recommends:     yudit
# dxf_output.inx, eqtexsvg.inx:
Requires:       pstoedit
Enhances:       %{name}
# python3-xml is already likely installed, so the big dependency is python3-lxml. Hence this supplements.
Supplements:    packageand(%{name}:python3-lxml)

%description extensions-extra
Extra extensions for Inkscape. Recommended for everybody who wants to
use Inkscape.

Inkscape is a vector graphics editor.

%package extensions-dia
Summary:        Dia import extension for Inkscape
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}
Requires:       dia
Enhances:       %{name}
Supplements:    packageand(%{name}:dia)

%description extensions-dia
Dia import extension for Inkscape.

Inkscape is a vector graphics editor.

%package extensions-fig
Summary:        Fig import extensions for Inkscape
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}
Requires:       transfig
Enhances:       %{name}
Supplements:    packageand(%{name}:transfig)

%description extensions-fig
Fig family (XFig, Figurine, JFig, WinFig,...) import extension for
Inkscape.

Inkscape is a vector graphics editor.

%package extensions-gimp
Summary:        GIMP extensions for Inkscape
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}
Requires:       %{name}-extensions-extra = %{version}
Requires:       gimp
Enhances:       %{name}
Supplements:    packageand(%{name}:gimp)

%description extensions-gimp
The GIMP import and export extensions for Inkscape.

Inkscape is a vector graphics editor.

%package extensions-skencil
Summary:        Skencil import extension for Inkscape
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}
Requires:       skencil
Enhances:       %{name}
Supplements:    packageand(%{name}:skencil)

%description extensions-skencil
Skencil import extension for Inkscape.

Inkscape is a vector graphics editor.

%lang_package

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%ifarch %{arm}
export LDFLAGS+="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%cmake
%{make_jobs}

# Unmangle XML and merge translations
# Currently missing from CMake build (https://bugs.launchpad.net/inkscape/+bug/1710337)
(cd ..
sed -ie 's:<_:<:g; s:</_:</:g' inkscape.appdata.xml.in
# msgfmt --xml ... is available since 0.19.7
%if 0%{?suse_version} >= 1500
msgfmt --xml -d ./po/ --template inkscape.appdata.xml.in -o inkscape.appdata.xml
%else
cp inkscape.appdata.xml.in inkscape.appdata.xml
%endif
)

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/locale/en_US@piglatin
rm -rf %{buildroot}%{_datadir}/inkscape/filters/filters.svg.h
rm -rf %{buildroot}%{_datadir}/inkscape/patterns/patterns.svg.h

# its not really an extension (missing .inx), but a standalone script
# avoid perl dependency, same can be achieved with 'cat foo.svg | extensions/embedimage.py'
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/embed_raster_in_svg.pl
# only useful for translators
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/genpofiles.sh
# ruby port of simplepath.py, which is not used anywhere
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/simplepath.rb
# only required on Windows
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/print_win32_vector.*
# packaging/distribution info
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/README

install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/inkscape/palettes

%suse_update_desktop_file -N "Inkscape" -G "SVG Vector Illustrator" inkscape

%find_lang %{name} %{?no_lang_C}

# split extensions
bash %{SOURCE2} %{buildroot}%{_datadir}/inkscape/extensions "%%{_datadir}/inkscape/extensions/"

sed -i -e "1 s,#! */usr/bin/env python,#!/usr/bin/python3," %{buildroot}%{_datadir}/inkscape/extensions/*.py

# Localized man pages, correct install path
for man in %{buildroot}%{_mandir}/man1/inkscape.*.1; do
    LOCALE=`echo $man | sed "s:.*%{_mandir}/man1/.*\.\([a-zA-Z_]\+\)\.1:\1:g"`
    mkdir -m755 -p %{buildroot}%{_mandir}/$LOCALE/man1
    mv $man %{buildroot}%{_mandir}/$LOCALE/man1/%{name}.1
    echo "%%lang($LOCALE) %%dir %%{_mandir}/$LOCALE" >> %{name}.man-lang.tmp
    echo "%%lang($LOCALE) %%dir %%{_mandir}/$LOCALE/man1" >> %{name}.man-lang.tmp
    echo "%%lang($LOCALE) %%doc %%{_mandir}/$LOCALE/man1/inkscape.1*" >> %{name}.man-lang.tmp
done
sort -u %{name}.man-lang.tmp > %{name}.man-lang
rm %{name}.man-lang.tmp

# Install appdata
install -D -m 0644 inkscape.appdata.xml %{buildroot}%{_datadir}/metainfo/inkscape.appdata.xml

%fdupes %{buildroot}

# We can't really move the localized manpages to the lang package, since they'd
# create a conflict between the lang subpackage and bundles

%files -f inkscape.lst -f %{name}.man-lang
%{_bindir}/*
%{_libdir}/libinkscape_base.so
%{_datadir}/applications/inkscape.desktop
%{_datadir}/icons/hicolor/*/apps/inkscape.png
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/inkscape.appdata.xml
%dir %{_datadir}/inkscape
%{_datadir}/inkscape/[cf-z]*
%{_datadir}/inkscape/examples
%dir %{_datadir}/inkscape/extensions
%dir %{_datadir}/inkscape/extensions/ink2canvas
%{_datadir}/inkscape/extensions/xaml2svg
%{_datadir}/inkscape/extensions/*.xsl*
%{_datadir}/inkscape/extensions/colors.xml
%{_datadir}/inkscape/extensions/Poly3DObjects/
%{_datadir}/inkscape/extensions/alphabet_soup/
%{_datadir}/inkscape/extensions/inkweb.js
%{_datadir}/inkscape/extensions/jessyInk.js
%{_datadir}/inkscape/extensions/jessyInk_core_mouseHandler_noclick.js
%{_datadir}/inkscape/extensions/jessyInk_core_mouseHandler_zoomControl.js
%{_datadir}/inkscape/extensions/jessyInk_video.svg
%{_datadir}/inkscape/extensions/fontfix.conf
%{_datadir}/inkscape/extensions/ink2canvas/*
%{_datadir}/inkscape/extensions/inkscape.extension.rng
%{_datadir}/inkscape/extensions/seamless_pattern.svg
%{_datadir}/inkscape/attributes/
%{_datadir}/inkscape/branding/
%doc %{_mandir}/man?/*.*
# exclude extensions that go in other packages:
%exclude %{_datadir}/inkscape/extensions/Barcode
%exclude %{_datadir}/inkscape/extensions/ps2pdf-ext.py
%exclude %{_datadir}/inkscape/extensions/ps_input.inx
%exclude %{_datadir}/inkscape/extensions/eps_input.inx
%exclude %{_datadir}/inkscape/extensions/cdr*
%exclude %{_datadir}/inkscape/extensions/wmf*
%exclude %{_datadir}/inkscape/extensions/dia*
%exclude %{_datadir}/inkscape/extensions/fig*
%exclude %{_datadir}/inkscape/extensions/*gimp*
%exclude %{_datadir}/inkscape/extensions/sk*
%exclude %{_datadir}/inkscape/extensions/*dxf*
# this one is in extras, manually added there due to large dependencies on ghostscript
%exclude %{_datadir}/inkscape/extensions/ps2pdf-ext.py

%files extensions-extra -f inkscape-extensions-extra.lst
%{_datadir}/inkscape/extensions/Barcode
# ps2pdf-ext is a wrapper around ps2pdf binary (part of ghostscript)
%{_datadir}/inkscape/extensions/ps_input.inx
%{_datadir}/inkscape/extensions/eps_input.inx
%{_datadir}/inkscape/extensions/ps2pdf-ext.py
# ps2dxf is a wrapper around pstoedit
%{_datadir}/inkscape/extensions/dxf_output.inx
%{_datadir}/inkscape/extensions/ps2dxf.sh
# This extensions seems erronous being copied in here too.
%exclude %{_datadir}/inkscape/extensions/*gimp*
%exclude %{_datadir}/inkscape/extensions/sk*

%files extensions-dia
%{_datadir}/inkscape/extensions/dia*

%files extensions-fig
%{_datadir}/inkscape/extensions/fig*

%files extensions-gimp
# NOTE: export_gimp_palette* does not depend on gimp, but belongs here logically:
%{_datadir}/inkscape/extensions/*gimp*

%files extensions-skencil
%{_datadir}/inkscape/extensions/sk*

%files lang -f %{name}.lang

%changelog
