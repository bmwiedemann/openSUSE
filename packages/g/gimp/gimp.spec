#
# spec file for package gimp
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
%if %{undefined requires_eq}
%define requires_eq() %(echo '%*' | LC_ALL=C xargs -r rpm -q --qf 'Requires: %%{name} = %%{epoch}:%%{version}\\n' | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")
%endif
%define requires_file() %( readlink -f '%*' | LC_ALL=C xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' -f | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

%if 0%{?suse_version} >= 1550
%bcond_without libheif
%else
%bcond_with    libheif
%endif

# --without-jpegxl on SLES 15 SP6
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%bcond_with    libjpegxl
%else
%bcond_without libjpegxl
%endif

%bcond_with debug_in_build_gimp

%define alsa_version            1.0.0
%define appstream_glib_version  0.7.7
%define atk_version             2.4.0
%define babl_version            0.1.110
%define cairo_version           1.14.0
%define cairo_pdf_version       1.14.0
%define dbus_glib_version       0.70
%define gdk_pixbuf_version      2.30.8
%define fontconfig_version      2.12.4
%define freetype2_version       2.1.7
%define exiv2_version           0.27.4
%define gdk_pixbuf_version      2.30.8
%define gegl_version            0.4.52
%define gexiv2_version          0.14.0
%define glib_version            2.70.0
%define gtk3_version            3.24.0
%define gudev_version           167
%define harfbuzz_version        2.8.2
%define lcms2_version           2.8
%define libexif_version         0.6.15
%define libheif_version         1.15.1
%define liblzma_version         5.0.0
%define libmypaint_version      1.4.0
%define libopenjp2_version      2.1.0
%define libpng_version          1.6.25
%define librsvg_version         2.40.6
%define libunwind_version       1.1.0
%define libwebp_version         0.6.0
%define mypaint_brushes_version 1.3.0
%define OpenEXR_version         1.6.1
%define pango_version           1.50.0
%define poppler_data_version    0.4.9
%define poppler_glib_version    0.69.0
%define vapigen_version         0.40.0
%define libvala_version         0.40.0
%define webkit2gtk_version      2.20.3
%define libtiff_version         4.0.0
%define libjxl_version          0.7.0

# seems lua 5.3 is the latest supported version
%global lua_lgi lua53-lgi

%global abiver 5
%global apiver 3.0

%if 0%{?sle_version}
%bcond_with python_plugin
%else
%bcond_without python_plugin
%endif


%define pkg_name gimp

Name:           gimp
Version:        3.0.0~RC2
Release:        0
%global pkg_version 3.0.0-RC2
Summary:        The GNU Image Manipulation Program
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://www.gimp.org/
Source:         https://download.gimp.org/pub/gimp/v3.0/%{pkg_name}-%{pkg_version}.tar.xz
Source1:        macros.gimp
# openSUSE palette file
Source2:        openSUSE.gpl
# imported from fedora
Patch1:         gimp-2.99.19-cm-system-monitor-profile-by-default.patch
Patch2:         gimp-2.99.19-external-help-browser.patch
Patch3:         gimp-2.99.19-no-phone-home-default.patch
Patch4:         33ab56f55406cc3cbe3cc7c0627340da1c1f2d6a.patch
Patch5:         gdb.patch
%if %{with debug_in_build_gimp}
BuildRequires:  gdb
%endif
%if %{with python_plugin}
BuildRequires:  python3 >= 3.6.0
BuildRequires:  python3-gobject
%endif
BuildRequires:  AppStream
BuildRequires:  python3-gi-docgen
BuildRequires:  meson
# meson looks for it
BuildRequires:  cmake
BuildRequires:  aalib-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# For some odd reason build needs gegl executable.
BuildRequires:  gegl >= %{gegl_version}
# Explicitly needed, otherwise ghostscript-mini is used during the
# build, and it's not enough for gimp.
BuildRequires:  ghostscript-devel
BuildRequires:  ghostscript-library
BuildRequires:  glib-networking
BuildRequires:  gtk-doc
BuildRequires:  intltool >= 0.40.1
BuildRequires:  libwmf-devel >= 0.2.8
%if %{with gimp_lua}
BuildRequires:  %{lua_lgi}
%endif
BuildRequires:  pkgconfig
%if 0%{?suse_version}
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  libxslt-tools
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  /usr/bin/gtk-update-icon-cache
%endif
BuildRequires:  xdg-utils
BuildRequires:  libbacktrace-devel
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(libjxl) >= %{libjxl_version}
BuildRequires:  pkgconfig(OpenEXR) >= %{OpenEXR_version}
BuildRequires:  pkgconfig(alsa) >= %{alsa_version}
BuildRequires:  pkgconfig(appstream-glib) >= %{appstream_glib_version}
BuildRequires:  pkgconfig(atk) >= %{atk_version}
BuildRequires:  pkgconfig(babl-0.1) >= %{babl_version}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-pdf) >= %{cairo_pdf_version}
BuildRequires:  pkgconfig(dbus-glib-1) >= %{dbus_glib_version}
BuildRequires:  pkgconfig(fontconfig) >= %{fontconfig_version}
BuildRequires:  pkgconfig(freetype2) >= %{freetype2_version}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf_version}
BuildRequires:  pkgconfig(gegl-0.4) >= %{gegl_version}
BuildRequires:  pkgconfig(gexiv2) >= %{gexiv2_version}
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0) >= %{gudev_version}
BuildRequires:  pkgconfig(harfbuzz) >= %{harfbuzz_version}
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(lcms2) >= %{lcms2_version}
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libexif) >= %{libexif_version}
%if %{with libheif}
BuildRequires:  pkgconfig(libheif) >= %{libheif_version}
%endif
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma) >= %{liblzma_version}
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= %{libmypaint_version}
BuildRequires:  pkgconfig(libopenjp2) >= %{libopenjp2_version}
BuildRequires:  pkgconfig(libpng) >= %{libpng_version}
BuildRequires:  pkgconfig(librsvg-2.0) >= %{librsvg_version}
BuildRequires:  pkgconfig(libtiff-4) >= %{libtiff_version}
BuildRequires:  pkgconfig(libunwind) >= %{libunwind_version}
BuildRequires:  pkgconfig(libwebp) >= %{libwebp_version}
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= %{mypaint_brushes_version}
BuildRequires:  pkgconfig(pango) >= %{pango_version}
BuildRequires:  pkgconfig(poppler-data) >= %{poppler_data_version}
BuildRequires:  pkgconfig(poppler-glib) >= %{poppler_glib_version}
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(vapigen) >= %{vapigen_version}
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= %{webkit2gtk_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3 >= 3.6.0
BuildRequires:  python3-gobject
BuildRequires:  typelib-1_0-Babl-0_1 >= %{babl_version}
BuildRequires:  typelib-1_0-Gegl-0_4 >= %{gegl_version}
%requires_eq    gegl-0_4
Requires:       gjs
# Explicitly declare the libgimp versions for upgrade purposes
Requires:       libgimp-3_0-0 = %{version}
Requires:       libgimpui-3_0-0 = %{version}
%if %{with gimp_lua}
Requires:       %{lua_lgi}
%endif
Requires:       shared-mime-info
Requires:       xdg-utils
Requires:       typelib-1_0-Babl-0_1 >= %{babl_version}
Requires:       typelib-1_0-Gegl-0_4 >= %{gegl_version}
Recommends:     %{name}-plugins-python3 = %{version}
Recommends:     iso-codes
Suggests:       AdobeICCProfiles
# TODO: Suggests:       gimp-2.0-scanner-plugin
Obsoletes:      %{name}-help-browser
Provides:       gimp-3.0 = %{version}
Provides:       gimp(abi) = %{abiver}
Provides:       gimp(api) = %{apiver}
%if "%{name}" != "%{pkg_name}"
Conflicts:      gimp
%endif

%description
The GIMP is an image composition and editing program, which can be
used for creating logos and other graphics for Web pages. The GIMP
offers many tools and filters, and provides a large image
manipulation toolbox, including channel operations and layers,
effects, subpixel imaging and antialiasing, and conversions, together
with multilevel undo. The GIMP offers a scripting facility, but many
of the included scripts rely on fonts that we cannot distribute.

%package -n libgimp-3_0-0
Summary:        The GNU Image Manipulation Program - Libraries
Group:          System/Libraries

%requires_file %{_libdir}/libbabl-0.1.so
%requires_file %{_libdir}/libgegl-0.4.so
%requires_file %{_libdir}/libgexiv2.so

%description -n libgimp-3_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP libraries.

%package -n libgimpui-3_0-0
Summary:        The GNU Image Manipulation Program - UI Libraries
Group:          System/Libraries

%description -n libgimpui-3_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP UI libraries.

%if %{with python_plugin}
%package plugin-python3
Summary:        The GNU Image Manipulation Program - python3 goject introspection plugins
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{version}
Requires:       python3 >= 3.6.0
Requires:       python3-gobject
Provides:       gimp-3.0-plugin-python3 = %{version}-%{release}
Supplements:    %{name}
Provides:       gimp-plugins-python3 = %{version}-%{release}
Obsoletes:      gimp-plugins-python3 < %{version}-%{release}
%description plugin-python3
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.
%endif

%package vala
Summary:        The GNU Image Manipulation Program - Vala development files
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name}-devel = %{version}
Provides:       gimp-3.0-vala = %{version}-%{release}
%description vala
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

%package plugin-aa
Summary:        The GNU Image Manipulation Program -- ASCII-Art output plugin
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{version}
# Let's trigger automatic installation if the user already has libaa installed.
Supplements:    (%{name} and libaa1)
Provides:       gimp-3.0-plugin-aa = %{version}-%{release}

%description plugin-aa
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

%package devel
Summary:        The GNU Image Manipulation Program
Group:          Development/Libraries/Other
Requires:       libgimp-3_0-0 = %{version}
Requires:       libgimpui-3_0-0 = %{version}
Provides:       gimp-3.0-devel = %{version}
Provides:       gimp-doc = 2.6.4
Obsoletes:      gimp-doc < 2.6.4
Obsoletes:      gimp-unstable-devel < 2.6.0

%description devel
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This subpackage contains libraries and header files for developing
applications that want to make use of the GIMP libraries.

%package extension-goat-excercises
Summary:        The GNU Image Manipulation Program
Group:          Development/Libraries/Other
Requires:       libgimpui-3_0-0 = %{version}
Requires:       gimp-3.0-vala = %{version}
Requires:       gimp-3.0-devel = %{version}
Requires:       gimp-3.0-plugin-python3 = %{version}

%description extension-goat-excercises
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This subpackage contains example the goat extension examples
that extend gimp.

%lang_package

%prep
%autosetup -p1 -n %{pkg_name}-%{pkg_version}

%build
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

%if 0%{?suse_version} && %{with translation_update}
translation-update-upstream
translation-update-upstream po-libgimp gimp30-libgimp
translation-update-upstream po-python gimp30-python
translation-update-upstream po-script-fu gimp30-script-fu
translation-update-upstream po-plug-ins gimp30-std-plug-ins
translation-update-upstream po-tips gimp30-tips
%endif

%meson \
  -Drelocatable-bundle=platform-default \
  -Denable-multiproc=true \
  -Denable-console-bin=true \
  -Dcheck-update=no \
  -Dbug-report-url=https://bugzilla.opensuse.org/ \
  -Dgi-docgen=disabled \
  -Dilbm=disabled \
  %if %{with with_headless_tests}
  -Dheadless-tests=enabled \
  %else
  -Dheadless-tests=disabled \
  %endif
%{nil}

# Safety check for ABI version change.
vabi=$(printf "%%d" $(sed -n '/#define GIMP_MODULE_ABI_VERSION/{s/.* //;p}' libgimpmodule/gimpmodule.h))
if test "x${vabi}" != "x%{abiver}"; then
   : Error: Upstream ABI version is now ${vabi}, expecting %{abiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi
# Safety check for API version change.
vapi=$(sed -n '/#define GIMP_API_VERSION/{s/.* //;p}' */libgimpbase/gimpversion.h | sed -e 's@"@@g')
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

%meson_build

%install
%meson_install

install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/gimp/3.0/palettes

%if 0%{?suse_version}
%suse_update_desktop_file -N GIMP gimp
%endif

touch gimp_all_parts.lang

for lang_part in gimp30 gimp30-libgimp gimp30-python gimp30-script-fu gimp30-std-plug-ins ; do
%find_lang ${lang_part} %{?no_lang_C} ${lang_part}.lang
cat ${lang_part}.lang >> gimp_all_parts.lang
done

echo "%%defattr(-,root,root)" >plugins.list
echo "%%defattr(-,root,root)" >plugins-python.list

for PLUGIN in %{buildroot}%{_libdir}/gimp/3.0/plug-ins/* ; do
    if grep -q '^#!.*python' ${PLUGIN}/* ; then
	echo "${PLUGIN#%{buildroot}}" >>plugins-python.list
    else
	echo "${PLUGIN#%{buildroot}}" >>plugins.list
    fi
done

%if ! 0%{?suse_version}
cat gimp_all_parts.lang >> plugins.list
%endif

find %{buildroot} -type f -name "*.la" -delete -print

# Install the macros file:
install -d %{buildroot}%{_rpmmacrodir}
sed -e "s/@GIMP_APIVER@/%{apiver}/;s/@GIMP_ABIVER@/%{abiver}/" \
    < $RPM_SOURCE_DIR/macros.gimp > macros.gimp
install -m 644 -c macros.gimp \
           %{buildroot}%{_rpmmacrodir}/macros.gimp

%fdupes %{buildroot}%{_datadir}/gtk-doc/
%fdupes %{buildroot}%{_libdir}/gimp/3.0/python/
%fdupes %{buildroot}%{_datadir}/gimp/3.0/

%post -n libgimp-3_0-0 -p /sbin/ldconfig
%postun -n libgimp-3_0-0 -p /sbin/ldconfig
%post -n libgimpui-3_0-0 -p /sbin/ldconfig
%postun -n libgimpui-3_0-0 -p /sbin/ldconfig

%files -f plugins.list
%license COPYING LICENSE
%doc AUTHORS NEWS* README MAINTAINERS
%{_bindir}/gimp
%{_bindir}/gimp-3*
%{_bindir}/gimp-console
%{_bindir}/gimp-console-3*
%{_bindir}/gimp-script-fu-interpreter-3.0
# should this maybe be in _libexecdir too?
%{_bindir}/gimp-test-clipboard*
%{_libexecdir}/gimp-debug-tool*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_datadir}/applications/gimp.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/gimp/
%{_libdir}/gimp/3.0/environ/default.env
%{_libdir}/gimp/3.0/interpreters/default.interp
%if %{with gimp_lua}
%{_libdir}/gimp/3.0/interpreters/lua.interp
%endif
# Explicitly list modules so we don't lose one by accident
%{_libdir}/gimp/3.0/modules/libcolor-selector-cmyk.so
%{_libdir}/gimp/3.0/modules/libcolor-selector-water.so
%{_libdir}/gimp/3.0/modules/libcolor-selector-wheel.so
%{_libdir}/gimp/3.0/modules/libcontroller-linux-input.so
%{_libdir}/gimp/3.0/modules/libcontroller-midi.so
%{_libdir}/gimp/3.0/modules/libdisplay-filter-aces-rrt.so
%{_libdir}/gimp/3.0/modules/libdisplay-filter-clip-warning.so
%{_libdir}/gimp/3.0/modules/libdisplay-filter-color-blind.so
%{_libdir}/gimp/3.0/modules/libdisplay-filter-gamma.so
%{_libdir}/gimp/3.0/modules/libdisplay-filter-high-contrast.so
%{_mandir}/man?/gimp.*
%{_mandir}/man?/gimp-3*
%{_mandir}/man?/gimp-console.*
%{_mandir}/man?/gimp-console-3*
%{_mandir}/man?/gimprc.*
%{_mandir}/man?/gimprc-3*
%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/3.0
%config %{_sysconfdir}/gimp/3.0/*rc
%config %{_sysconfdir}/gimp/3.0/*css
# split file-aa into own package (bnc#851509)
%exclude %{_libdir}/gimp/3.0/plug-ins/file-aa
%{_libdir}/girepository-1.0/Gimp-3.0.typelib
%{_libdir}/girepository-1.0/GimpUi-3.0.typelib

%files plugin-aa
%{_libdir}/gimp/3.0/plug-ins/file-aa

%files -n libgimp-3_0-0
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/3.0
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/3.0
%dir %{_libdir}/gimp/3.0/environ
%dir %{_libdir}/gimp/3.0/interpreters
%dir %{_libdir}/gimp/3.0/modules
%dir %{_libdir}/gimp/3.0/plug-ins
%dir %{_libdir}/gimp/3.0/extensions
%{_libdir}/libgimp-3.0.so.*
%{_libdir}/libgimpbase-3.0.so.*
%{_libdir}/libgimpcolor-3.0.so.*
%{_libdir}/libgimpconfig-3.0.so.*
%{_libdir}/libgimpmath-3.0.so.*
%{_libdir}/libgimpmodule-3.0.so.*
%{_libdir}/libgimp-scriptfu-3.0.so.*

%files -n libgimpui-3_0-0
%{_libdir}/libgimpthumb-3.0.so.*
%{_libdir}/libgimpui-3.0.so.*
%{_libdir}/libgimpwidgets-3.0.so.*

%if %{with python_plugin}
%files plugin-python3 -f plugins-python.list
%{_libdir}/gimp/3.0/environ/python.env
%endif

%files vala
%{_datadir}/vala/vapi/gimp-3.0.deps
%{_datadir}/vala/vapi/gimp-3.0.vapi
%{_datadir}/vala/vapi/gimp-ui-3.0.deps
%{_datadir}/vala/vapi/gimp-ui-3.0.vapi

# FIXME: Maybe split gimp-lang and gimp-plugins-python-lang
%files lang -f gimp_all_parts.lang

%files devel
%doc README.i18n
%{_bindir}/gimptool*
%{_includedir}/gimp-3.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gimp-3.0.pc
%{_libdir}/pkgconfig/gimpthumb-3.0.pc
%{_libdir}/pkgconfig/gimpui-3.0.pc
%{_rpmmacrodir}/macros.gimp
%{_datadir}/gir-1.0/Gimp-3.0.gir
%{_datadir}/gir-1.0/GimpUi-3.0.gir
%{_mandir}/man1/gimptool*.1*

%files extension-goat-excercises
%{_libdir}/gimp/3.0/extensions/org.gimp.extension.goat-exercises
%dir %{_libdir}/gimp/3.0/extensions/org.gimp.extension.goat-exercises/locale/*/
%dir %{_libdir}/gimp/3.0/extensions/org.gimp.extension.goat-exercises/locale/*/*/

%changelog
