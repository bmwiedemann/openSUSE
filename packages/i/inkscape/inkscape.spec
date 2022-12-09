#
# spec file for package inkscape
#
# Copyright (c) 2022 SUSE LLC
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


%define _version 1.2.1_2022-07-14_9c6d41e410

Name:           inkscape
Version:        1.2.1
Release:        0
Summary:        Vector Illustration Program
License:        GPL-3.0-only
URL:            https://inkscape.org/

Source:         https://inkscape.org/gallery/item/34673/inkscape-%{version}.tar.xz#/inkscape-%{_version}.tar.xz
# openSUSE palette file
Source1:        openSUSE.gpl
Source2:        inkscape-split-extensions-extra.py
Source98:       https://media.inkscape.org/media/resources/sigs/inkscape-%{_version}.tar.xz.sig
Source99:       https://inkscape.org/~MarcJeanmougin/gpg#/%name.keyring
# PATCH-FIX-UPSTREAM 2f3101417.patch -- Fix build with Poppler 22.09.0
Patch0:         https://gitlab.com/inkscape/inkscape/-/commit/2f3101417.patch

BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  gc-devel
%if 0%{suse_version} < 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  intltool
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  libxslt-devel
BuildRequires:  ninja
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  potrace-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(2geom)
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdl-3.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpg-0.3)
# extensions use annotations which requires 3.7+
Requires:       python(abi) >= 3.7
Requires:       python3-gobject
Recommends:     python3-lxml
Recommends:     python3-numpy
Recommends:     python3-scour
Recommends:     python3-xml
Obsoletes:      %{name}-extensions-dia < %{version}
Obsoletes:      %{name}-extensions-skencil < %{version}

%description
Inkscape is a vector graphics editor.

%package extensions-extra
Summary:        Additional extensions for Inkscape
Requires:       %{name} = %{version}
# ps_input.py is a wrapper around ps2pdf, which lives in ghostscript package.
Requires:       ghostscript
Requires:       python3-lxml
Requires:       python3-numpy
Requires:       python3-scour
Requires:       python3-xml
Enhances:       %{name}
Supplements:    (%{name} and python3-lxml and python3-numpy and python3-scour and python3-xml)

%description extensions-extra
Extra extensions for Inkscape. Recommended for everybody who wants to
use Inkscape.

Inkscape is a vector graphics editor.

%package extensions-fig
Summary:        Fig import extensions for Inkscape
Requires:       %{name} = %{version}
Requires:       %{name}-extensions-extra = %{version}
Requires:       transfig
Enhances:       %{name}
Supplements:    (%{name} and transfig)

%description extensions-fig
Fig family (XFig, Figurine, JFig, WinFig,...) import extension for
Inkscape.

Inkscape is a vector graphics editor.

%package extensions-gimp
Summary:        GIMP extensions for Inkscape
Requires:       %{name} = %{version}
Requires:       %{name}-extensions-extra = %{version}
Requires:       gimp
Enhances:       %{name}
Supplements:    (%{name} and gimp)

%description extensions-gimp
The GIMP import and export extensions for Inkscape.

Inkscape is a vector graphics editor.

%package extensions-scribus
Summary:        Scribus extensions for Inkscape
Requires:       %{name} = %{version}
Requires:       %{name}-extensions-extra = %{version}
Requires:       scribus
Enhances:       %{name}
Supplements:    (%{name} and scribus)

%description extensions-scribus
The Scribus-based PDF export extension for Inkscape.

Inkscape is a vector graphics editor.

%lang_package

%prep
%autosetup -n %{name}-%{_version} -p1

%build
%ifarch %{arm}
export LDFLAGS+="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%if 0%{suse_version} < 1550
export CXX=g++-10
%endif
%cmake \
  -GNinja \
  -DINKSCAPE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DWITH_MANPAGE_COMPRESSION=OFF \
  -DWITH_DBUS=ON \
  %{nil}
%ninja_build

%install
%ninja_install -C build

# Only useful for translators.
rm %{buildroot}%{_datadir}/inkscape/extensions/genpofiles.sh
# Packaging/distribution info.
rm %{buildroot}%{_datadir}/inkscape/extensions/{LICENSE.txt,MANIFEST.in,README.md,TESTING.md,CONTRIBUTING.md}
# Test framework.
rm %{buildroot}%{_datadir}/inkscape/extensions/tox.ini        \
   %{buildroot}%{_datadir}/inkscape/extensions/.pylintrc      \
   %{buildroot}%{_datadir}/inkscape/extensions/doxygen-main.dox
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/.pytest_cache
# extensions/doc
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/docs
rm %{buildroot}%{_datadir}/inkscape/extensions/{.darglint,.pre-commit-config.yaml,inkscape.extension.schema,poetry.lock,pyproject.toml}

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/inkscape/palettes/

%find_lang %{name} %{?no_lang_C}

sed -i -e "1 s|#! *%{_bindir}/env python|#!%{_bindir}/python3|" %{buildroot}%{_datadir}/inkscape/extensions/*.py

# Split extensions.
python3 %{SOURCE2} %{buildroot}%{_datadir}/inkscape/extensions "%%{_datadir}/inkscape/extensions/"

%fdupes %{buildroot}

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files -f inkscape.lst
%{_bindir}/*
%dir %{_libdir}/inkscape
%{_libdir}/inkscape/lib%{name}_base.so
%{_datadir}/applications/*Inkscape.desktop
%{_datadir}/icons/hicolor/*/apps/*Inkscape.png
%{_datadir}/icons/hicolor/*/apps/*Inkscape.svg
%{_datadir}/icons/hicolor/*/apps/*Inkscape-symbolic.svg
%{_datadir}/metainfo/*Inkscape.appdata.xml
%dir %{_datadir}/inkscape/
%{_datadir}/inkscape/[cdf-z]*
%{_datadir}/inkscape/examples/
%dir %{_datadir}/inkscape/extensions/
%{_datadir}/inkscape/extensions/svg_fonts/
%{_datadir}/inkscape/extensions/xaml2svg/
%{_datadir}/inkscape/extensions/*.xsl*
%{_datadir}/inkscape/extensions/colors.xml
%{_datadir}/inkscape/extensions/Poly3DObjects/
%{_datadir}/inkscape/extensions/alphabet_soup/
%{_datadir}/inkscape/extensions/inkweb.js
%{_datadir}/inkscape/extensions/jessyInk.js
%{_datadir}/inkscape/extensions/jessyInk_core_mouseHandler_noclick.js
%{_datadir}/inkscape/extensions/jessyInk_core_mouseHandler_zoomControl.js
%{_datadir}/inkscape/extensions/jessyink_video.svg
%{_datadir}/inkscape/extensions/fontfix.conf
%{_datadir}/inkscape/extensions/inkscape.extension.rng
%{_datadir}/inkscape/extensions/seamless_pattern.svg
%{_datadir}/inkscape/extensions/raster_output_jpg.svg
%{_datadir}/inkscape/attributes/
%{_datadir}/inkscape/branding/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/inkscape
%{_mandir}/man1/*.1%{?ext_man}
# We can't really move the localized manpages to the lang package, since they'd
# create a conflict between the lang subpackage and bundles
%dir %{_mandir}/hr/
%dir %{_mandir}/hr/man1/
%{_mandir}/*/man1/*.1%{?ext_man}

%files extensions-extra -f inkscape-extensions-extra.lst
%{_datadir}/inkscape/extensions/output_scour.svg
%{_datadir}/inkscape/extensions/dxf14_*.txt
%{_datadir}/inkscape/extensions/dxf_input_text_scale_factor.svg

%files extensions-fig
%{_datadir}/inkscape/extensions/fig*

%files extensions-gimp
# NOTE: export_gimp_palette* does not depend on gimp, but belongs here logically:
%{_datadir}/inkscape/extensions/*gimp*

%files extensions-scribus
%{_datadir}/inkscape/extensions/*scribus*

%files lang -f %{name}.lang

%changelog
