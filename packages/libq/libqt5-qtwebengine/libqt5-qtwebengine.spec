#
# spec file for package libqt5-qtwebengine
#
# Copyright (c) 2020 SUSE LLC
# Copyright © 2017 Kevin Kofler <Kevin@tigcc.ticalc.org>
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


%define qt5_snapshot 0

%if %{?suse_version} > 1500 || 0%{?sle_version} > 150100
%bcond_without system_harfbuzz
%bcond_without system_icu
%else
%bcond_with system_harfbuzz
%bcond_with system_icu
%endif
%if %{?suse_version} > 1500 || 0%{?sle_version} > 150200
%bcond_without system_vpx
%else
%bcond_with system_vpx
%endif
%bcond_without system_ffmpeg
%bcond_without system_minizip

# spellchecking dictionary directory
%global _qtwebengine_dictionaries_dir %{_libqt5_datadir}/qtwebengine_dictionaries

Name:           libqt5-qtwebengine
Version:        5.15.1
Release:        0
Summary:        Qt 5 WebEngine Library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
Group:          Development/Libraries/X11
URL:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtwebengine-everywhere-src-5.15.1
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM armv6-ffmpeg-no-thumb.patch - Fix ffmpeg configuration for armv6
Patch1:         armv6-ffmpeg-no-thumb.patch
# PATCH-FIX-UPSTREAM disable-gpu-when-using-nouveau-boo-1005323.diff
Patch2:         disable-gpu-when-using-nouveau-boo-1005323.diff
Patch7:         fix1163766.patch
# PATCH-FIX-OPENSUSE
Patch9:         rtc-dont-use-h264.patch
# http://www.chromium.org/blink not ported to PowerPC
ExcludeArch:    ppc ppc64 ppc64le s390 s390x
# Try to fix i586 MemoryErrors with rpmlint
#!BuildIgnore: rpmlint
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  gperf
# It really wants a commit hash, even if it's not in a .git checkout...
BuildRequires:  binutils-gold
BuildRequires:  git-core
BuildRequires:  krb5
BuildRequires:  krb5-devel
BuildRequires:  libQt5QuickControls2-devel
# For building pdf exmples...
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libcap-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt5-qtbase-private-headers-devel >= 5.9
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= 5.9
BuildRequires:  libqt5-qtlocation-private-headers-devel >= 5.9
BuildRequires:  libqt5-qttools-private-headers-devel >= 5.9
BuildRequires:  libqt5-qtwebchannel-private-headers-devel >= 5.9
BuildRequires:  libqt5-qtxmlpatterns-private-headers-devel >= 5.9
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  pam-devel
BuildRequires:  pciutils-devel
BuildRequires:  perl-JSON
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-xml
BuildRequires:  re2-devel
BuildRequires:  re2c
BuildRequires:  sed
BuildRequires:  snappy-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  usbutils
BuildRequires:  util-linux
%ifnarch %arm
BuildRequires:  valgrind-devel
%endif
BuildRequires:  wdiff
BuildRequires:  xz
BuildRequires:  yasm
BuildRequires:  perl(Switch)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(jsoncpp)
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsrtp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  yasm-devel
%if %{with system_minizip}
BuildRequires:  pkgconfig(minizip)
%endif
%if %{with system_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz) >= 2.2.0
%endif
%if %{with system_icu}
BuildRequires:  pkgconfig(icu-uc) >= 64.0
BuildRequires:  pkgconfig(icu-i18n) >= 64.0
%endif
%if %{with system_vpx}
BuildRequires:  pkgconfig(vpx) >= 1.8.0
%endif
%if %{with system_ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
%requires_ge libQt5Network5
%requires_ge libQtQuick5
%requires_ge libQt5Widgets5

%description
Qt WebEngine provides functionality for rendering regions of dynamic
web content.

The functionality in Qt WebEngine is divided into the following
modules:

* QtWebEngineCore: Provides public API shared by both QtWebEngine and
  QtWebEngineWidgets
* QtWebEngine: Provides QML types for rendering web content within a
  QML application
* QtWebEngineWidgets: Provides a web browser engine as well as C++
  classes to render and interact with web content

%package devel
Summary:        Development files for the Qt5 WebEngine library
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
You need this package if you want to compile programs with Qt WebEngine.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebEngine library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
%requires_ge    libqt5-qtbase-private-headers-devel
%requires_ge    libqt5-qtdeclarative-private-headers-devel

%description private-headers-devel
This package provides private headers of libqt5-qtwebengine that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 WebEngine examples
Group:          Development/Libraries/X11
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtwebengine module.

%package -n libQt5Pdf5
Summary:        Qt5 PDF library
Group:          Development/Libraries/X11

%description -n libQt5Pdf5
Main library of the Qt PDF module.

%package -n libQt5PdfWidgets5
Summary:        Qt5 PDF library for Qt Widgets
Group:          Development/Libraries/X11

%description -n libQt5PdfWidgets5
Library of the Qt PDF module with support for Qt Widgets.

%package -n libqt5-qtpdf-imports
Summary:        Qt5 PDF module for QML
Group:          Development/Libraries/X11

%description -n libqt5-qtpdf-imports
Qt Quick module for the Qt PDF library.

%package -n libqt5-qtpdf-devel
Summary:        Development files for the Qt5 PDF library
Group:          Development/Libraries/X11
Requires:       libQt5Pdf5 = %{version}
Requires:       libQt5PdfWidgets5 = %{version}

%description -n libqt5-qtpdf-devel
You need this package if you want to compile programs with Qt PDF.

%package -n libqt5-qtpdf-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 PDF library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       libqt5-qtpdf-devel = %{version}
%requires_ge    libqt5-qtbase-private-headers-devel

%description -n libqt5-qtpdf-private-headers-devel
This package provides private headers of libqt5-qtpdf that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libqt5-qtpdf-examples
Summary:        Qt5 PDF examples
Group:          Development/Libraries/X11
Recommends:     libqt5-qtpdf-devel

%description -n libqt5-qtpdf-examples
Examples for the libqt5-qtpdf module.

%prep
%setup -q -n %{tar_version}
sed -i 's|$(STRIP)|strip|g' src/core/core_module.pro
%autopatch -p1

# QTBUG-61128
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' \
  src/3rdparty/chromium/build/toolchain/linux/BUILD.gn

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif

# TODO: Get the manual unbundling from chromium.spec working here as well
rm -r src/3rdparty/chromium/third_party/openh264/src

%ifnarch x86_64
RPM_OPT_FLAGS="$RPM_OPT_FLAGS "
export RPM_OPT_FLAGS=${RPM_OPT_FLAGS/-g / }
%endif
# Upstream does not care about those warnings, but optflags has -Werror=return-type.
export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -Wno-return-type"
# It does not actually include proprietary codecs, it only makes it attempt to use ffmpeg
# Link pulseaudio to work around QTBUG-77037
%qmake5 QMAKE_CFLAGS="$RPM_OPT_FLAGS" \
        QMAKE_CXXFLAGS="$RPM_OPT_FLAGS" \
        QMAKE_LFLAGS+="-Wl,--no-keep-memory -Wl,--hash-size=31 -Wl,--reduce-memory-overheads" \
        gn_args+="link_pulseaudio=true" \
%if 0%{?suse_version} < 1330
        QMAKE_CC=gcc-7 QMAKE_CXX=g++-7 CONFIG+=c++14 \
%endif
        qtwebengine.pro -- \
        -webengine-alsa -webengine-kerberos -no-webengine-embedded-build \
%if %{with system_icu}
        -system-webengine-icu \
%endif
%if %{with system_ffmpeg}
        -system-webengine-ffmpeg \
        -webengine-proprietary-codecs \
%endif
        -system-webengine-opus -system-webengine-webp -webengine-pepper-plugins -webengine-printing-and-pdf

# Determine the right number of parallel processes based on the available memory
%limit_build -m 2500

# Ensure that also the internal chromium build follows the right number of parallel
# processes instead of its defaults.
export NINJAFLAGS="%{_smp_mflags}"

make %{_smp_mflags} VERBOSE=1

%install
%qmake5_install
#cat %{buildroot}/%{_libdir}/pkgconfig/Qt*Web*.pc
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%libqt5_bindir/moc," -e "s,uic_location=.*,uic_location=%libqt5_bindir/uic," {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -exec sed -i -e "/^RPM_BUILD_DIR/d" {} +
sed -i '/^Libs.private/d' %{buildroot}%{_libdir}/pkgconfig/Qt*Web*.pc
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/*.la
# webenginecore expects icudatl.dat at this location
# ln -sf %{_datadir}/icu/*/icudt*l.dat %{buildroot}%{_datadir}/qt5/icudtl.dat

# Workaround to allow using QtWE with older Qt versions
sed -i -r '/ EXACT\)/d' \
  %{buildroot}%{_libqt5_libdir}/cmake/Qt5WebEngine*/Qt5WebEngine*Config.cmake

sed -i '/find_package/!b;n;s/'%{so_version}/$(rpm -q --qf %%{version} libQt5Core5 | sed 's/~.*$//')/ \
  %{buildroot}%{_libqt5_libdir}/cmake/Qt5WebEngine*/Qt5WebEngine*Config.cmake

# Hunspell dictionaries will be converted and put here on package installation
mkdir -p %{buildroot}%{_qtwebengine_dictionaries_dir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libQt5Pdf5 -p /sbin/ldconfig
%postun -n libQt5Pdf5 -p /sbin/ldconfig
%post -n libQt5PdfWidgets5 -p /sbin/ldconfig
%postun -n libQt5PdfWidgets5 -p /sbin/ldconfig

%if 0%{?suse_version} >= 1500
%filetriggerin -- %{_datadir}/hunspell
# Convert Hunspell dictionaries on package installation
while read filename ; do
  case "$filename" in
    *.dic)
      bdicname=%{_qtwebengine_dictionaries_dir}/`basename -s .dic "$filename"`.bdic
      %{_libqt5_bindir}/qwebengine_convert_dict "$filename" "$bdicname" &> /dev/null || :
      ;;
  esac
done
%endif

%files
%license LICENSE.*
%{_libqt5_libdir}/libQt5WebEngine.so.*
%{_libqt5_libdir}/libQt5WebEngineCore.so.*
%{_libqt5_libdir}/libQt5WebEngineWidgets.so.*
%dir %{_datadir}/qt5/
%dir %{_datadir}/qt5/translations/
%{_datadir}/qt5/translations/qtwebengine_locales/
%dir %{_datadir}/qt5/resources/
%{_datadir}/qt5/resources/qtwebengine_*
%if %{without system_icu}
%{_datadir}/qt5/resources/icudtl.dat
%endif
%dir %{_qtwebengine_dictionaries_dir}
%dir %{_libqt5_libexecdir}
%{_libqt5_libexecdir}/QtWebEngineProcess
%{_libqt5_archdatadir}/qml/QtWebEngine/
%{_libqt5_bindir}/qwebengine_convert_dict

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtWebEngine*/%{so_version}

%files devel
%exclude %{_libqt5_includedir}/QtWebEngine*/%{so_version}
%{_libqt5_includedir}/QtWebEngine*/
%{_libqt5_libdir}/libQt5WebEngine*.so
%{_libqt5_libdir}/libQt5WebEngine*.prl
%{_libqt5_libdir}/pkgconfig/Qt5WebEngine*.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_webengine*.pri
%dir %{_libqt5_libdir}/cmake/Qt5Designer/
%{_libqt5_libdir}/cmake/Qt5Designer/Qt5Designer_QWebEngineViewPlugin.cmake
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/libqwebengineview.so
%{_libqt5_libdir}/cmake/Qt5WebEngine*/

%files examples
%license LICENSE.*
%dir %{_libqt5_examplesdir}
%{_libqt5_examplesdir}/webengine*/

%files -n libQt5Pdf5
%license LICENSE.*
%{_libqt5_libdir}/libQt5Pdf.so.*
%{_libqt5_archdatadir}/plugins/imageformats/libqpdf.so
# Not quite sure what this would be used by
%dir %{_libqt5_libdir}/cmake/
%dir %{_libqt5_libdir}/cmake/Qt5Gui/
%{_libqt5_libdir}/cmake/Qt5Gui/Qt5Gui_QPdfPlugin.cmake

%files -n libQt5PdfWidgets5
%license LICENSE.*
%{_libqt5_libdir}/libQt5PdfWidgets.so.*

%files -n libqt5-qtpdf-imports
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick/Pdf/

%files -n libqt5-qtpdf-private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtPdf/%{so_version}
%{_libqt5_includedir}/QtPdfWidgets/%{so_version}

%files -n libqt5-qtpdf-devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtPdf*/%{so_version}
%{_libqt5_includedir}/QtPdf/
%{_libqt5_includedir}/QtPdfWidgets/
%{_libqt5_libdir}/cmake/Qt5Pdf/
%{_libqt5_libdir}/cmake/Qt5PdfWidgets/
%{_libqt5_libdir}/libQt5Pdf.so
%{_libqt5_libdir}/libQt5PdfWidgets.so
%{_libqt5_libdir}/libQt5Pdf.prl
%{_libqt5_libdir}/libQt5PdfWidgets.prl
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_pdf*.pri
%{_libqt5_libdir}/pkgconfig/Qt5Pdf.pc
%{_libqt5_libdir}/pkgconfig/Qt5PdfWidgets.pc

%files -n libqt5-qtpdf-examples
%license LICENSE.*
%dir %{_libqt5_examplesdir}
%{_libqt5_examplesdir}/pdf*/

%changelog
