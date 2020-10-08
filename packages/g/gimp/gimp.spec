#
# spec file for package gimp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global abiver 4
%global apiver 2.0
%if 0%{?sle_version}
%bcond_with python2
%else
%bcond_without python2
%endif
Name:           gimp
Version:        2.10.22
Release:        0
Summary:        The GNU Image Manipulation Program
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://www.gimp.org/
Source:         http://download.gimp.org/pub/gimp/v2.10/%{name}-%{version}.tar.bz2
Source1:        macros.gimp
# openSUSE palette file
Source2:        openSUSE.gpl
Source99:       baselibs.conf

BuildRequires:  aalib-devel
BuildRequires:  alsa-devel >= 1.0.0
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel >= 2.12.4
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  gdk-pixbuf-loader-rsvg
# For some odd reason build needs gegl executable.
BuildRequires:  gegl
BuildRequires:  ghostscript-devel
# Explicitly needed, otherwise ghostscript-mini is used during the
# build, and it's not enough for gimp.
BuildRequires:  ghostscript-library
BuildRequires:  glib-networking
BuildRequires:  intltool >= 0.40.1
BuildRequires:  iso-codes-devel
BuildRequires:  libbz2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  librsvg-devel >= 2.40.6
BuildRequires:  libtiff-devel
BuildRequires:  libwmf-devel >= 0.2.8
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
%if %{with python2}
BuildRequires:  python-gtk-devel >= 2.10.4
%endif
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk) >= 2.2.0
BuildRequires:  pkgconfig(babl) >= 0.1.78
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(cairo-pdf) >= 1.12.2
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.24
BuildRequires:  pkgconfig(gexiv2) >= 0.10.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.54.2
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.10
BuildRequires:  pkgconfig(gudev-1.0) >= 167
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libexif) >= 0.6.15
# TODO: BuildRequires:  pkgconfig(libheif) >= 1.1.0
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(libmypaint) >= 1.3.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libpng) >= 1.6.25
BuildRequires:  pkgconfig(libwebp) >= 0.6.0
BuildRequires:  pkgconfig(mypaint-brushes-1.0)
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(pango) >= 1.29.4
BuildRequires:  pkgconfig(poppler-data) >= 0.4.7
BuildRequires:  pkgconfig(poppler-glib) >= 0.44.0
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  xdg-utils
# obs does not automaticaly add this
Requires:       libglib-2_0-0 >= 2.54.2
Requires:       libgexiv2-2 >= 0.10.6
Requires:       libbabl-0_1-0 >= 0.1.46
# Explicitly declare the libgimp versions for upgrade purposes
Requires:       libgimp-2_0-0 = %{version}
Requires:       libgimpui-2_0-0 = %{version}
Requires:       xdg-utils
Recommends:     %{name}-lang
%if %{with python2}
Recommends:     %{name}-plugins-python = %{version}
%endif
Recommends:     iso-codes
Suggests:       AdobeICCProfiles
Suggests:       gimp-2.0-scanner-plugin
Obsoletes:      %{name}-help-browser
Provides:       gimp-2.0 = %{version}
Provides:       gimp(abi) = %{abiver}
Provides:       gimp(api) = %{apiver}

%description
The GIMP is an image composition and editing program, which can be
used for creating logos and other graphics for Web pages. The GIMP
offers many tools and filters, and provides a large image
manipulation toolbox, including channel operations and layers,
effects, subpixel imaging and antialiasing, and conversions, together
with multilevel undo. The GIMP offers a scripting facility, but many
of the included scripts rely on fonts that we cannot distribute.

%package -n libgimp-2_0-0
Summary:        The GNU Image Manipulation Program - Libraries
Group:          System/Libraries
%requires_ge    libbabl-0_1-0
%requires_ge    libgegl-0_4-0

%description -n libgimp-2_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP libraries.

%package -n libgimpui-2_0-0
Summary:        The GNU Image Manipulation Program - UI Libraries
Group:          System/Libraries

%description -n libgimpui-2_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP UI libraries.

%if %{with python2}
%package plugins-python
Summary:        The GNU Image Manipulation Program - python-gtk based plugins
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{version}
Requires:       python-gtk
Supplements:    %{name}
Provides:       gimp-2.0-plugins-python = %{version}
Obsoletes:      gimp-unstable-plugins-python < 2.6.0
# For update from <= 10.3 and SLED 10:
Provides:       %{name}:%{_libdir}/gimp/2.0/plug-ins/pyconsole.py = %{version}

%description plugins-python
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.
%endif

%package plugin-aa
Summary:        The GNU Image Manipulation Program -- ASCII-Art output plugin
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{version}
# Let's trigger automatic installation if the user already has libaa installed.
Supplements:    packageand(%{name}:libaa1)

%description plugin-aa
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

%package devel
Summary:        The GNU Image Manipulation Program
Group:          Development/Libraries/Other
Requires:       libgimp-2_0-0 = %{version}
Requires:       libgimpui-2_0-0 = %{version}
Provides:       gimp-2.0-devel = %{version}
Provides:       gimp-doc = 2.6.4
Obsoletes:      gimp-doc < 2.6.4
Obsoletes:      gimp-unstable-devel < 2.6.0

%description devel
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This subpackage contains libraries and header files for developing
applications that want to make use of the GIMP libraries.

%lang_package

%prep
%setup -q

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
translation-update-upstream
translation-update-upstream po-libgimp gimp20-libgimp
translation-update-upstream po-python gimp20-python
translation-update-upstream po-script-fu gimp20-script-fu
translation-update-upstream po-plug-ins gimp20-std-plug-ins
translation-update-upstream po-tips gimp20-tips
# Safety check for ABI version change.
vabi=`printf "%d" $(sed -n '/#define GIMP_MODULE_ABI_VERSION/{s/.* //;p}' libgimpmodule/gimpmodule.h)`
if test "x${vabi}" != "x%{abiver}"; then
   : Error: Upstream ABI version is now ${vabi}, expecting %{abiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi
# Safety check for API version change.
vapi=`sed -n '/#define GIMP_API_VERSION/{s/.* //;p}' libgimpbase/gimpversion.h | sed -e 's@"@@g'`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

%build
%if 0%{?suse_version} < 1500
test -x "$(type -p %{_bindir}/gcc-7)" && export CC="%{_bindir}/gcc-7"
test -x "$(type -p %{_bindir}/g++-7)" && export CXX="%{_bindir}/g++-7"
%endif
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export CFLAGS="%{optflags} -fno-strict-aliasing"
export LDFLAGS="%{optflags} -lm"
%configure \
	--disable-silent-rules \
	--disable-static\
%if 0%{?suse_version} >= 1330
	--without-webkit\
	--with-lcms=lcms2\
%endif
%if %{without python2}
	--disable-python \
%endif
	--libexecdir=%{_libexecdir}\
	--enable-default-binary\
	--disable-check-update\
	--enable-mp

make %{?_smp_mflags}

%install
%make_install
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/gimp/2.0/palettes
%suse_update_desktop_file -N GIMP gimp
rm %{buildroot}%{_libdir}/gimp/2.0/*/*.*a
%find_lang gimp20 %{?no_lang_C}
%find_lang gimp20-libgimp %{?no_lang_C} gimp20.lang
%find_lang gimp20-python %{?no_lang_C} gimp20.lang
%find_lang gimp20-script-fu %{?no_lang_C} gimp20.lang
%find_lang gimp20-std-plug-ins %{?no_lang_C} gimp20.lang
%find_lang gimp20-tips %{?no_lang_C} gimp20.lang
echo "%%defattr(-,root,root)" >plugins.list
echo "%%defattr(-,root,root)" >plugins-python.list
for PLUGIN in %{buildroot}%{_libdir}/gimp/2.0/plug-ins/* ; do
    if grep -q '^#!.*python' $PLUGIN ; then
	echo "${PLUGIN#%{buildroot}}" >>plugins-python.list
    else
	echo "${PLUGIN#%{buildroot}}" >>plugins.list
    fi
done
find %{buildroot} -type f -name "*.la" -delete -print
# Install the macros file:
install -d %{buildroot}%{_sysconfdir}/rpm
sed -e "s/@GIMP_APIVER@/%{apiver}/;s/@GIMP_ABIVER@/%{abiver}/" \
    < $RPM_SOURCE_DIR/macros.gimp > macros.gimp
install -m 644 -c macros.gimp \
           %{buildroot}%{_sysconfdir}/rpm/macros.gimp
%fdupes %{buildroot}%{_datadir}/gtk-doc/
%fdupes %{buildroot}%{_libdir}/gimp/2.0/python/
%fdupes %{buildroot}%{_datadir}/gimp/2.0/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} < 1500
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%post -n libgimp-2_0-0 -p /sbin/ldconfig
%postun -n libgimp-2_0-0 -p /sbin/ldconfig
%post -n libgimpui-2_0-0 -p /sbin/ldconfig
%postun -n libgimpui-2_0-0 -p /sbin/ldconfig

%files -f plugins.list
%license COPYING LICENSE
%doc AUTHORS ChangeLog NEWS* README
%{_bindir}/gimp
%{_bindir}/gimp-2.*
%{_bindir}/gimp-console
%{_bindir}/gimp-console-2.*
# should this maybe be in _libexecdir too?
%{_bindir}/gimp-test-clipboard-2.0
%{_libexecdir}/gimp-debug-tool-2.0
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/gimp-data-extras.metainfo.xml
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_datadir}/applications/gimp.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gimp/
%{_datadir}/gimp/2.0/images/gimp-splash.png
%{_libdir}/gimp/2.0/environ/default.env
%{_libdir}/gimp/2.0/interpreters/default.interp
# Explicitly list modules so we don't lose one by accident
%{_libdir}/gimp/2.0/modules/libcolor-selector-cmyk.so
%{_libdir}/gimp/2.0/modules/libcolor-selector-water.so
%{_libdir}/gimp/2.0/modules/libcolor-selector-wheel.so
%{_libdir}/gimp/2.0/modules/libcontroller-linux-input.so
%{_libdir}/gimp/2.0/modules/libcontroller-midi.so
%{_libdir}/gimp/2.0/modules/libdisplay-filter-color-blind.so
%{_libdir}/gimp/2.0/modules/libdisplay-filter-gamma.so
%{_libdir}/gimp/2.0/modules/libdisplay-filter-high-contrast.so
%{_libdir}/gimp/2.0/modules/libdisplay-filter-clip-warning.so
%{_mandir}/man?/gimp.*
%{_mandir}/man?/gimp-2.*
%{_mandir}/man?/gimp-console.*
%{_mandir}/man?/gimp-console-2.*
%{_mandir}/man?/gimprc.*
%{_mandir}/man?/gimprc-2.*
%{_mandir}/man?/gimptool-2.*
%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/2.0
%config %{_sysconfdir}/gimp/2.0/*rc
# split file-aa into own package (bnc#851509
%exclude %{_libdir}/gimp/2.0/plug-ins/file-aa

%files plugin-aa
%{_libdir}/gimp/2.0/plug-ins/file-aa

%files -n libgimp-2_0-0
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.0
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.0
%dir %{_libdir}/gimp/2.0/environ
%dir %{_libdir}/gimp/2.0/interpreters
%dir %{_libdir}/gimp/2.0/modules
%dir %{_libdir}/gimp/2.0/plug-ins
%{_libdir}/libgimp-2.0.so.*
%{_libdir}/libgimpbase-2.0.so.*
%{_libdir}/libgimpcolor-2.0.so.*
%{_libdir}/libgimpconfig-2.0.so.*
%{_libdir}/libgimpmath-2.0.so.*
%{_libdir}/libgimpmodule-2.0.so.*

%files -n libgimpui-2_0-0
%{_libdir}/libgimpthumb-2.0.so.*
%{_libdir}/libgimpui-2.0.so.*
%{_libdir}/libgimpwidgets-2.0.so.*

%if %{with python2}
%files plugins-python -f plugins-python.list
%{_libdir}/gimp/2.0/environ/pygimp.env
%{_libdir}/gimp/2.0/interpreters/pygimp.interp
%{_libdir}/gimp/2.0/python/
# FIXME: Maybe split gimp-lang and gimp-plugins-python-lang
%endif

%files lang -f gimp20.lang

%files devel
%doc README.i18n
%{_bindir}/gimptool-2.0
#{_mandir}/man?/gimptool-2.0%%{?ext_man}
%{_includedir}/gimp-2.0/
%{_libdir}/*.so
%{_datadir}/aclocal/gimp-2.0.m4
%{_libdir}/pkgconfig/gimp-2.0.pc
%{_libdir}/pkgconfig/gimpthumb-2.0.pc
%{_libdir}/pkgconfig/gimpui-2.0.pc
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/html/
%config %{_sysconfdir}/rpm/macros.gimp

%changelog
