#
# spec file
#
# Copyright (c) 2025 SUSE LLC
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


%global         flavor @BUILD_FLAVOR@%{nil}
%define         psuffix %{nil}
%define         wow64 0
%define         staging 0
%if "%{flavor}" == "wow64"
%define         psuffix -wow64
%define         wow64 1
%endif
%if "%{flavor}" == "staging"
%define         psuffix -staging
%define         staging 1
%endif
%if "%{flavor}" == "staging-wow64"
%define         psuffix -staging-wow64
%define         wow64 1
%define         staging 1
%endif

%define         _lto_cflags %{nil}
Name:           wine%{psuffix}
%define downloadver  10.0-rc5
Version:        10.0~rc5
Release:        0
Summary:        An MS Windows Emulator
License:        LGPL-2.1-or-later
URL:            https://winehq.org
Source0:        https://dl.winehq.org/wine/source/10.0/wine-%{downloadver}.tar.xz
Source1:        https://dl.winehq.org/wine/source/10.0/wine-%{downloadver}.tar.xz.sign
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xda23579a74d4ad9af9d3f945cefac8eaaf17519d#/wine.keyring
%if %{staging}
Source3:        https://github.com/wine-staging/wine-staging/archive/v%{downloadver}.tar.gz#/wine-staging-%{downloadver}.tar.xz
%endif
Source97:       baselibs.conf
Source98:       wine.rpmlintrc
Source99:       get-sources.sh
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  giflib-devel
BuildRequires:  libgsm-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libvkd3d)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(osmesa)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
%ifarch aarch64
BuildRequires:  clang >= 5
BuildRequires:  lld
BuildRequires:  llvm
%endif
%ifarch %{ix86}
BuildRequires:  mingw32-cross-gcc
%endif
%ifarch x86_64
BuildRequires:  mingw64-cross-gcc
%if %{wow64}
BuildRequires:  mingw32-cross-gcc
%endif
%endif
%if 0%{?suse_version} < 1600
BuildRequires:  gcc14-c++
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(FAudio)
BuildRequires:  pkgconfig(capi20)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libattr)
%else
BuildRequires:  FAudio-devel
BuildRequires:  cups-devel
BuildRequires:  libattr-devel
%ifnarch %{ix86}
BuildRequires:  libcapi20-devel
%endif
%endif
%if %{staging}
BuildRequires:  git-core
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libva)
%endif
%ifarch x86_64
Requires:       wine-32bit = %{version}
%endif
Requires:       samba-winbind
Recommends:     wine-gecko >= 2.47.4
Recommends:     wine-mono >= 9.4.0
Recommends:     winetricks
Conflicts:      wine-gecko < 2.47.4
Conflicts:      wine-mono < 9.4.0
Conflicts:      otherproviders(wine)
Provides:       wine-mp3 = %version
Obsoletes:      wine-mp3 < %version
%if "%{flavor}" != ""
Provides:       wine = %{version}-%{release}
%endif
%if "%{flavor}" == "wow64" || "%{flavor}" == "staging-wow64"
Conflicts:      otherproviders(wine-32bit)
Provides:       wine-32bit = %{version}-%{release}
%endif
ExclusiveArch:  aarch64 %{ix86} x86_64

%description
Wine is a compatibility layer capable of running Windows
applications. Instead of simulating internal Windows logic like a
virtual machine or emulator, Wine translates Windows API calls into
POSIX calls on-the-fly, eliminating the performance and memory
penalties of other methods and allowing you to cleanly integrate
Windows applications into your desktop.

%if %{staging}
This WINE flavor contains the "staging" development patchset
on top of the regular Wine release.
%endif

%package devel
Summary:        Files for Wine development
%if "%{flavor}" != ""
Provides:       wine-devel = %{version}
%endif
Conflicts:      otherproviders(wine-devel)

%description devel
This RPM contains the header files and development tools for the WINE
libraries.

%prep
%autosetup -n wine-%{downloadver}
%if %{staging}
tar xf %{SOURCE3}
python3 wine-staging-%{downloadver}/staging/patchinstall.py --all
%endif

%build
%if 0%{?suse_version} < 1600
export CC="/usr/bin/gcc-14"
export CXX="/usr/bin/g++-14"
%endif
%ifarch %{ix86}
export CFLAGS="%{optflags} -fno-omit-frame-pointer"
export CXXFLAGS="%{optflags} -fno-omit-frame-pointer"
%endif
export WIDL_TIME_OVERRIDE="0" 	# for reproducible builds.
%if %{staging}
autoreconf -i -f
%endif
%configure \
	--with-x \
	--with-wayland \
	--with-gstreamer \
%ifarch aarch64 x86_64
	--enable-win64 \
%if %{wow64}
	--enable-archs=x86_64,i386 \
%endif
%endif
	--verbose || cat config.log
grep "have_x=yes" config.log || exit 1
# generate baselibs.conf
%ifarch %ix86 aarch64
echo "# autogenerated in .spec file" >%SOURCE97
echo "%name" >> %SOURCE97
echo "  +^/usr/bin/wine\$" >> %SOURCE97
echo "  +^/usr/bin/wine-preloader\$" >> %SOURCE97
echo "  +^/usr/lib/wine/i386-windows" >> %SOURCE97
echo "  +^/usr/lib/wine/i386-unix" >> %SOURCE97
grep SONAME_ config.log
grep SONAME_ config.log|grep -v 'so"'|sed -e 's/^.*\(".*"\).*$/ requires \1/;'|sort -u >>%SOURCE97
echo " recommends \"libpulse0-32bit\""	>> %SOURCE97
echo " recommends \"pipewire-alsa-32bit\""	>> %SOURCE97
echo " recommends \"alsa-plugins-32bit\""	>> %SOURCE97
echo " recommends \"Mesa-libGL1-32bit\""	>> %SOURCE97
# indirect deps of libvulkan
echo " requires \"libvulkan_intel-32bit\""		>> %SOURCE97
echo " requires \"libvulkan_radeon-32bit\""		>> %SOURCE97
# now included
echo " obsoletes \"wine-mp3-32bit\""		>> %SOURCE97
echo " requires \"p11-kit-32bit\""		>> %SOURCE97
%if "%{flavor}" != ""
echo " provides \"wine-<targettype> = <version>\""		>> %SOURCE97
%endif
echo " conflicts \"otherproviders(wine-<targettype>)\""		>> %SOURCE97
echo "%name-devel" >> %SOURCE97
echo "  +^/usr/lib/wine/.*def" >> %SOURCE97
%if "%{flavor}" != ""
echo " provides \"wine-devel-<targettype> = <version>\""		>> %SOURCE97
%endif
echo " conflicts \"otherproviders(wine-devel-<targettype>)\""		>> %SOURCE97

cat %SOURCE97
%endif
%make_build all

%install
%make_install DESTDIR=%{buildroot}

%ifarch %{ix86} x86_64
find %{buildroot}/usr/lib*/wine/*-windows/ -type f -exec strip --strip-debug {} +
%endif

rm -rf %{buildroot}%{_mandir}/{pl,de,fr}.UTF-8

# find the implicit dependencies
%define winedir %_builddir/wine-%downloadver
cat >%winedir/my-find-requires.sh <<EOF
#!/bin/bash
%{__find_requires}
%ifarch x86_64 aarch64
grep SONAME_ %winedir/config.log|grep -v 'so"'|sed -e 's/^.*"\(.*\)".*$/\1()(64bit)/;'|sort -u
%else
grep SONAME_ %winedir/config.log|grep -v 'so"'|sed -e 's/^.*"\(.*\)".*$/\1/;'|sort -u
%endif
EOF
chmod 755 %winedir/my-find-requires.sh
%define _use_internal_dependency_generator 0
%define __find_requires %winedir/my-find-requires.sh

%ldconfig_scriptlets

%files
%license LICENSE LICENSE.OLD
%doc ANNOUNCE.md AUTHORS README.md
%{_bindir}/function_grep.pl
%{_bindir}/msidb
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wineboot
%{_bindir}/winecfg
%{_bindir}/wineconsole
%{_bindir}/winedbg
%{_bindir}/winefile
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/wineserver
%{_datadir}/applications/wine.desktop
%{_mandir}/man?/winedbg.?%{?ext_man}
%{_mandir}/man?/wineserver.?%{?ext_man}
%{_mandir}/man?/msiexec.?%{?ext_man}
%{_mandir}/man?/notepad.?%{?ext_man}
%{_mandir}/man?/regedit.?%{?ext_man}
%{_mandir}/man?/regsvr32.?%{?ext_man}
%{_mandir}/man?/wineboot.?%{?ext_man}
%{_mandir}/man?/winebuild.?%{?ext_man}
%{_mandir}/man?/winecfg.?%{?ext_man}
%{_mandir}/man?/wineconsole.?%{?ext_man}
%{_mandir}/man?/winecpp.?%{?ext_man}
%{_mandir}/man?/winefile.?%{?ext_man}
%{_mandir}/man?/winemine.?%{?ext_man}
%{_mandir}/man?/winepath.?%{?ext_man}
%{_datadir}/wine
%dir %{_libdir}/wine
%ifarch aarch64
%{_bindir}/wine
%{_bindir}/wine-preloader
%{_mandir}/man?/wine.?%{?ext_man}
%if !%{wow64}
%{_libdir}/wine/aarch64-windows
%exclude %{_libdir}/wine/aarch64-windows/*.a
%endif
%{_libdir}/wine/aarch64-unix
%if %{wow64}
%{_libdir}/wine/i386-windows
%exclude %{_libdir}/wine/i386-windows/*.a
%{_libdir}/wine/x86_64-windows
%exclude %{_libdir}/wine/x86_64-windows/*.a
%endif
%endif
%ifarch %{ix86}
%{_bindir}/wine
%{_bindir}/wine-preloader
%{_mandir}/man?/wine.?%{?ext_man}
%{_libdir}/wine/i386-windows
%exclude %{_libdir}/wine/i386-windows/*.a
%{_libdir}/wine/i386-unix
%exclude %{_libdir}/wine/i386-unix/*.a
%endif
%ifarch x86_64
%if %{wow64}
%{_bindir}/wine
%{_bindir}/wine-preloader
%{_mandir}/man?/wine.?%{?ext_man}
%{_libdir}/wine/i386-windows
%exclude %{_libdir}/wine/i386-windows/*.a
%{_libdir}/wine/x86_64-windows
%exclude %{_libdir}/wine/x86_64-windows/*.a
%{_libdir}/wine/x86_64-unix
%exclude %{_libdir}/wine/x86_64-unix/*.a
%else
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%{_libdir}/wine/x86_64-unix
%exclude %{_libdir}/wine/x86_64-unix/*.a
%{_libdir}/wine/x86_64-windows
%exclude %{_libdir}/wine/x86_64-windows/*.a
%endif
%endif

%files devel
%{_includedir}/wine
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/winedump
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_mandir}/man?/winemaker.?%{?ext_man}
%{_mandir}/man?/widl.?%{?ext_man}
%{_mandir}/man?/winedump.?%{?ext_man}
%{_mandir}/man?/wineg++.?%{?ext_man}
%{_mandir}/man?/winegcc.?%{?ext_man}
%{_mandir}/man?/wmc.?%{?ext_man}
%{_mandir}/man?/wrc.?%{?ext_man}
%ifarch aarch64
%if !%{wow64}
%{_libdir}/wine/aarch64-windows/*.a
%endif
%if %{wow64}
%{_libdir}/wine/i386-windows/*.a
%{_libdir}/wine/x86_64-windows/*.a
%endif
%endif
%ifarch %{ix86}
%{_libdir}/wine/i386-unix/*.a
%if 0%{?suse_version} >= 1600
%{_libdir}/wine/i386-windows/*.a
%endif
%endif
%ifarch x86_64
%if %{wow64}
%{_libdir}/wine/i386-windows/*.a
%{_libdir}/wine/x86_64-windows/*.a
%else
%{_libdir}/wine/x86_64-windows/*.a
%endif
%endif

%changelog
