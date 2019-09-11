#
# spec file for package libqt5-qtwebengine
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without system_vpx
%else
%bcond_with system_vpx
%endif
%if 0%{?suse_version} > 1500
# Needs ICU >= 63
%bcond_without system_icu
%else
%bcond_with system_icu
%endif
%if %{?suse_version} >= 1330 || (0%{?is_opensuse} && 0%{?sle_version} >= 120200)
%bcond_without system_ffmpeg
%else
%bcond_with system_ffmpeg
%endif
%if %{?suse_version} >= 1320 || (0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200)
%bcond_without system_minizip
%else
%bcond_with system_minizip
%endif
# Not even in Tumbleweed as of 2019-03-22
%bcond_with system_harfbuzz
# This is just overall condition to contain everything we can't provide on SLE12
%if 0%{?suse_version} >= 1320 || 0%{?is_opensuse}
%bcond_with sle_bundles
%else
%bcond_without sle_bundles
%endif
# spellchecking dictionary directory
%global _qtwebengine_dictionaries_dir %{_libqt5_datadir}/qtwebengine_dictionaries

Name:           libqt5-qtwebengine
Version:        5.13.0
Release:        0
Summary:        Qt 5 WebEngine Library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtwebengine-everywhere-src-5.13.0
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM armv6-ffmpeg-no-thumb.patch - Fix ffmpeg configuration for armv6
Patch1:         armv6-ffmpeg-no-thumb.patch
# PATCH-FIX-UPSTREAM disable-gpu-when-using-nouveau-boo-1005323.diff
Patch2:         disable-gpu-when-using-nouveau-boo-1005323.diff
# PATCH-FIX-UPSTREAM 0001-fix-build-after-y2038-changes-in-glibc.patch
Patch3:         0001-fix-build-after-y2038-changes-in-glibc.patch
# PATCH-FIX-UPSTREAM harmony-fix.diff -- Show the patent-free LCD rendering. Without this patch, only grayscale rendering is used. (for freetype-2.8.1) boo#1061344
Patch5:         harmony-fix.diff
# PATCH-FIX-OPENSUSE (copied from the chromium package)
Patch9:         chromium-non-void-return.patch
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
BuildRequires:  valgrind-devel
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
%if !%{with sle_bundles}
BuildRequires:  yasm-devel
%endif
%if %{with system_minizip}
BuildRequires:  pkgconfig(minizip)
%endif
%if %{with system_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz) >= 2.0.0
%endif
%if %{with system_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 63.0
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
Summary:        Qt5 location examples
Group:          Development/Libraries/X11
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtwebengine module.

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

%if 0%{?suse_version} < 1330
# WE checks the version of GCC qtbase was built with, not the version it's building with.
# ARGH!
echo "QT_GCC_MAJOR_VERSION = 7" > qtwebengine_new.pro
echo "QT_GCC_MINOR_VERSION = 2" >> qtwebengine_new.pro
echo "QT_CONFIG += c++14" >> qtwebengine_new.pro
cat qtwebengine.pro >> qtwebengine_new.pro
mv qtwebengine{_new,}.pro
%endif

%ifnarch x86_64
RPM_OPT_FLAGS="$RPM_OPT_FLAGS "
export RPM_OPT_FLAGS=${RPM_OPT_FLAGS/-g / }
%endif
# It does not actually include proprietary codecs, it only makes it attempt to use ffmpeg
%qmake5 QMAKE_CFLAGS="$RPM_OPT_FLAGS" \
        QMAKE_LFLAGS+="-Wl,--no-keep-memory -Wl,--hash-size=31 -Wl,--reduce-memory-overheads" \
%if 0%{?suse_version} < 1330
        QMAKE_CC=gcc-7 QMAKE_CXX=g++-7 CONFIG+=c++14 \
%endif
        qtwebengine.pro -- \
        -webengine-alsa -no-webengine-embedded-build \
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

%if 0%{?suse_version} < 1330
    export CC=gcc-7
    export CXX=g++-7
%endif

make %{_smp_mflags} VERBOSE=1

%install
%qmake5_install
#cat %{buildroot}/%{_libdir}/pkgconfig/Qt*Web*.pc
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%libqt5_bindir/moc," -e "s,uic_location=.*,uic_location=%libqt5_bindir/uic," {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -exec sed -i -e "/^RPM_BUILD_DIR/d" {} +
sed -i '/^Libs.private/d' %{buildroot}%{_libdir}/pkgconfig/Qt*Web*.pc
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la
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
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt*Web*.so.*
%{_datadir}/qt5/
%dir %{_libqt5_libexecdir}
%dir %{_qtwebengine_dictionaries_dir}
%{_libqt5_libexecdir}/QtWebEngineProcess
%{_libqt5_archdatadir}/qml/QtWebEngine/
%{_libqt5_plugindir}/designer/
%{_libqt5_bindir}/qwebengine_convert_dict

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/*/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/*/%{so_version}
%{_libqt5_includedir}/*/
%{_libqt5_libdir}/cmake/Qt5*/
%{_libqt5_libdir}/libQt*Web*.so
%{_libqt5_libdir}/libQt*Web*.prl
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_*.pri
%{_libqt5_libdir}/pkgconfig/Qt*Web*.pc

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
