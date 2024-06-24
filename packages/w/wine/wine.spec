#
# spec file
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


%define projectname wine
%global flavor @BUILD_FLAVOR@%nil
%define staging 0

%ifarch x86_64 aarch64
%define wow64_build 0
%endif
%ifarch %ix86
%define wow64_build 0
%endif

%if "%flavor" == "staging"
%define staging 1
%endif

%if "%flavor" == "wow64"
%define wow64_build 1
%endif

%if "%flavor" == "staging-wow64"
%define staging 1
%define wow64_build 1
%endif

# needs to be on top due to usage of %version macro below
%define realver 9.11
Version:        9.11
Release:        0

%if "%{flavor}" != ""
Name:           wine%{?flavor:-}%{?flavor}
Provides:       wine = %{version}-%{release}
%else
Name:           wine
%endif
Conflicts:      otherproviders(wine)
# the wow64 is now a 64bit flavor of the 32bit build.
%if "%{flavor}" == "wow64" || "%{flavor}" == "staging-wow64"
Conflicts:      otherproviders(wine-32bit)
Provides:       wine-32bit = %{version}-%{release}
%endif
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  bison
%ifarch aarch64
BuildRequires:  clang >= 5
BuildRequires:  lld
BuildRequires:  llvm
%endif
BuildRequires:  cups-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  libcapi20-devel
BuildRequires:  vkd3d-devel
%endif
BuildRequires:  FAudio-devel
BuildRequires:  dbus-1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel
BuildRequires:  glib2-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  krb5-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libgsm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpcap-devel
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
BuildRequires:  libtiff-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  mpg123-devel
BuildRequires:  vulkan-devel
%ifarch %{ix86} x86_64
Requires:       libvulkan_intel
%endif
Requires:       libvulkan_radeon
Provides:       wine-mp3 = %version
Obsoletes:      wine-mp3 < %version
%else
Recommends:     wine-mp3
%endif
BuildRequires:  SDL2-devel
BuildRequires:  git
BuildRequires:  ncurses-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  sane-backends-devel
BuildRequires:  update-desktop-files
BuildRequires:  valgrind-devel
%if 0%{?suse_version} >= 1550
%ifarch x86_64
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-zlib-devel
Requires:       mingw64-libz
%if %{wow64_build}
BuildRequires:  mingw32-cross-gcc
%endif
%endif
%ifarch %ix86
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-zlib-devel
Requires:       mingw32-libz
%endif
%endif
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(osmesa)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
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
Summary:        An MS Windows Emulator
License:        LGPL-2.1-or-later
Group:          System/Emulators/PC
URL:            https://www.winehq.org/
Source0:        https://dl.winehq.org/wine/source/9.x/%{projectname}-%{realver}.tar.xz
Source41:       wine.keyring
Source42:       https://dl.winehq.org/wine/source/9.x/%{projectname}-%{realver}.tar.xz.sign
Source2:        http://kegel.com/wine/wisotool
Source3:        README.SUSE
Source4:        wine.desktop
Source6:        wine-msi.desktop
Source5:        ubuntuwine.tar.bz2
Source7:        baselibs.conf
Source8:        wine-rpmlintrc
# SUSE specific patches
# - currently none, but add them here
Patch0:         0001-mf-tests-help-older-compilers-by-using-defines.patch
Recommends:     wine-gecko >= 2.47.4
Conflicts:      wine-gecko < 2.47.4
Recommends:     wine-mono >= 9.0.0
Conflicts:      wine-mono < 9.0.0
# not packaged in distro...
Recommends:     wine-mono
Recommends:     alsa-plugins
Recommends:     dosbox
Recommends:     pipewire-alsa
Recommends:     winetricks
Requires:       samba-winbind
%if "%{flavor}" != "wow64" && "%{flavor}" != "staging-wow64"
%ifarch x86_64
Requires:       %{name}-32bit = %{version}
%endif
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 ppc armv7l armv7hl aarch64
%if %{staging}
# upstream patch target version
%define staging_version 9.11
Source100:      wine-staging-%{staging_version}.tar.xz
BuildRequires:  gtk3-devel
BuildRequires:  libOSMesa-devel
BuildRequires:  libva-devel
BuildRequires:  python3
%endif
# wine bundles multiple unix libraries to be able to build PE files without dependencies
# current versions are from 7.22 (update this if you update the versions below):
Provides:       bundled(FAudio) = 23.12.0
Provides:       bundled(fluidsynth) = 2.3.3
Provides:       bundled(jpeg) = 9e
Provides:       bundled(libgsm) = 1.10.19
Provides:       bundled(libjxr) = 1.1
Provides:       bundled(liblcms2) = 2.15
Provides:       bundled(libpng) = 1.6.40
Provides:       bundled(libxml2) = 2.11.5
Provides:       bundled(libxslt) = 1.1.38
Provides:       bundled(mpg123) = 1.32.2
Provides:       bundled(musl) = 1.2.3
Provides:       bundled(openldap2) = 2.5.16
Provides:       bundled(tiff) = 4.6.0
Provides:       bundled(vkd3d) = 1.10
Provides:       bundled(zlib) = 1.3

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

You can run your Windows executables with it and write your Windows
programs under Linux and link against the WINE libraries. It is not
necessary to have a Windows installation to run WINE.

Refer to %{_datadir}/doc/packages/wine/README.SUSE. There is more
documentation available in that directory. Read 'man wine' for further
information.

You can invoke wine by entering 'wine program.exe'. Configure it by
running 'winecfg'.

%package devel
Summary:        Files for Wine development
Group:          Development/Libraries/C and C++
%if "%{flavor}" != ""
Provides:       wine-devel = %{version}
%endif
Conflicts:      otherproviders(wine-devel)

%description devel
This RPM contains the header files and development tools for the WINE
libraries.

%prep
%setup -q -n wine-%{realver}
%autopatch -p1
#
cp %{S:3} .
#
%if %{staging}
# apply wine staging patch set on top of the wine release.
tar xf %{SOURCE100}
python3 ./wine-staging-%staging_version/staging/patchinstall.py --all
%endif

%build
# currently not building with LTO
%define _lto_cflags %{nil}
cat VERSION
export WIDL_TIME_OVERRIDE="0" 	# for reproducible builds.
%ifarch %ix86
# e.g. Steam and other copy protections hate EBP being used for something else.
export RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-fomit-frame-pointer//'`
%endif

%ifarch aarch64
# ARM64 now requires clang
# https://source.winehq.org/git/wine.git/commit/8fb8cc03c3edb599dd98f369e14a08f899cbff95
export CC="/usr/bin/clang"
%endif

%if %{staging}
autoreconf -i -f
%endif
# keep just for susepatches with configure changes
#autoconf
#autoheader -I include
CFLAGS="$RPM_OPT_FLAGS" \
%configure \
	--with-x \
%ifarch %{arm}
	--with-float-abi=hard \
%endif
%ifarch x86_64 aarch64
	--enable-win64 \
%if %{wow64_build}
	--enable-archs=x86_64,i386 \
%endif
%endif
	--verbose || cat config.log

grep "have_x=yes" config.log || exit 1
# generate baselibs.conf
%ifarch %ix86 aarch64
echo "# autogenerated in .spec file" >%SOURCE7
echo "%name" >> %SOURCE7
echo "  +^/usr/bin/wine\$" >> %SOURCE7
echo "  +^/usr/bin/wine-preloader\$" >> %SOURCE7
echo "  +^/usr/lib/wine/i386-windows" >> %SOURCE7
echo "  +^/usr/lib/wine/i386-unix" >> %SOURCE7
grep SONAME_ config.log
grep SONAME_ config.log|grep -v 'so"'|sed -e 's/^.*\(".*"\).*$/ requires \1/;'|sort -u >>%SOURCE7
echo " recommends \"libpulse0-32bit\""	>> %SOURCE7
echo " recommends \"pipewire-alsa-32bit\""	>> %SOURCE7
echo " recommends \"alsa-plugins-32bit\""	>> %SOURCE7
echo " recommends \"Mesa-libGL1-32bit\""	>> %SOURCE7
%if 0%{?suse_version} >= 1330
# indirect deps of libvulkan
echo " requires \"libvulkan_intel-32bit\""		>> %SOURCE7
echo " requires \"libvulkan_radeon-32bit\""		>> %SOURCE7
# now included
echo " obsoletes \"wine-mp3-32bit\""		>> %SOURCE7
%else
echo " recommends \"wine-mp3-32bit\""		>> %SOURCE7
%endif
%if 0%{?suse_version} >= 1310
echo " requires \"p11-kit-32bit\""		>> %SOURCE7
%endif
%if "%{flavor}" != ""
echo " provides \"wine-<targettype> = <version>\""		>> %SOURCE7
%endif
echo " conflicts \"otherproviders(wine-<targettype>)\""		>> %SOURCE7
echo "%name-devel" >> %SOURCE7
echo "  +^/usr/lib/wine/.*def" >> %SOURCE7
%if "%{flavor}" != ""
echo " provides \"wine-devel-<targettype> = <version>\""		>> %SOURCE7
%endif
echo " conflicts \"otherproviders(wine-devel-<targettype>)\""		>> %SOURCE7

cat %SOURCE7
%endif
make %{?_smp_mflags} all

%install
make install DESTDIR=%{buildroot}

%ifarch x86_64
%if !%{wow64_build}
mkdir -p \
   %{buildroot}/usr/lib/wine/i386-windows \
   %{buildroot}/usr/lib/wine/i386-unix
ln -s \
    /usr/lib/wine/i386-windows \
    /usr/lib/wine/i386-unix    \
  %buildroot/usr/%_lib/wine/
%endif
%endif

# install desktop file
install -d %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file %{SOURCE4} System Emulator

install -m 0644 %SOURCE4 %{buildroot}%{_datadir}/applications/
install -m 0644 %SOURCE6 %{buildroot}%{_datadir}/applications/
install -m 0755 %SOURCE2 %{buildroot}%{_bindir}/
mv %{buildroot}/%{_mandir}/de.UTF-8 %{buildroot}/%{_mandir}/de
mv %{buildroot}/%{_mandir}/fr.UTF-8 %{buildroot}/%{_mandir}/fr
%ifnarch x86_64
mv %{buildroot}/%{_mandir}/pl.UTF-8 %{buildroot}/%{_mandir}/pl
%endif
%if %{wow64_build}
mv %{buildroot}/%{_mandir}/pl.UTF-8 %{buildroot}/%{_mandir}/pl
%endif

%ifarch %ix86 x86_64
# Use plain strip, which unlike the MinGW variant preserves the wine builtin marker
find %{buildroot}/usr/lib*/wine/*-windows/ -type f -exec strip --strip-debug {} +
%endif

%ifarch aarch64
# Do not ship static *.a libs
rm %{buildroot}%{_libdir}/wine/*-windows/*.a
%endif

tar -xjf %{SOURCE5}
# Copied from Ubuntu Wine out of debian.diff
# https://launchpad.net/~ubuntu-wine/+archive/ppa/+packages
# taken on 1.2rc2 time.
cd ubuntuwine
        install -d %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
        install -c -m 644 wine.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged

        # Install application-specific desktop files
        install -d %{buildroot}%{_datadir}/applications
        install -c -m 644 *.desktop %{buildroot}%{_datadir}/applications/
        sed -i "/X-SuSE-translate/d" %{buildroot}%{_datadir}/applications/*.desktop

        install -d %{buildroot}%{_datadir}/desktop-directories/
        install -c -m 644 *.directory %{buildroot}%{_datadir}/desktop-directories/

	    # Correct desktop files' categories
	    %suse_update_desktop_file -n -r wine-notepad Utility TextEditor
	    %suse_update_desktop_file -n -r wine-uninstaller System Emulator
	    %suse_update_desktop_file -n -r wine-winecfg System Emulator
        %suse_update_desktop_file -n -r wine-regedit System Emulator
        %suse_update_desktop_file -n -r wine-winehelp System Emulator
        %suse_update_desktop_file -n -r wine-msi System Emulator
        %suse_update_desktop_file -n -r wine-browsedrive System Emulator
	    %suse_update_desktop_file -n -r wine-winefile System FileManager
	    %suse_update_desktop_file -n -r wine-winemine Game BoardGame

        # Install icons
        install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
        install -c -m 644 *.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cd ..

# find the implicit dependencies
%define winedir %_builddir/%projectname-%realver
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

# breaks btrfs installation, see bnc#723402
# %%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE LICENSE.OLD
%doc ANNOUNCE.md AUTHORS README*
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
%{_bindir}/wisotool
%{_datadir}/wine
%ifnarch x86_64
%doc %{_mandir}/man1/wine.1*
%endif
%if %{wow64_build}
%doc %{_mandir}/man1/wine.1*
%endif
%doc %{_mandir}/man1/winedbg.1*
%doc %{_mandir}/man1/wineserver.1*
%ifnarch x86_64
%doc %dir %doc %{_mandir}/pl
%doc %dir %doc %{_mandir}/pl/man1
%doc %{_mandir}/*/man1/wine.1*
%endif
%if %{wow64_build}
%doc %dir %doc %{_mandir}/pl
%doc %dir %doc %{_mandir}/pl/man1
%doc %{_mandir}/*/man1/wine.1*
%endif
%doc %{_mandir}/*/man1/wineserver.1*
%doc %{_mandir}/man1/msiexec.1.*
%doc %{_mandir}/man1/notepad.1.*
%doc %{_mandir}/man1/regedit.1.*
%doc %{_mandir}/man1/regsvr32.1.*
%doc %{_mandir}/man1/wineboot.1.*
%doc %{_mandir}/man1/winebuild.1.*
%doc %{_mandir}/man1/winecfg.1.*
%doc %{_mandir}/man1/wineconsole.1.*
%doc %{_mandir}/man1/winecpp.1.*
%doc %{_mandir}/man1/winefile.1.*
%doc %{_mandir}/man1/winemine.1.*
%doc %{_mandir}/man1/winepath.1.*
%dir %{_sysconfdir}/xdg/menus/
%dir %{_sysconfdir}/xdg/menus/applications-merged
%config %{_sysconfdir}/xdg/menus/applications-merged/*.menu
%{_datadir}/applications/*.desktop
%dir %{_datadir}/desktop-directories/
%{_datadir}/desktop-directories/*.directory
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%ifarch %ix86 aarch64
%{_bindir}/wine
%{_bindir}/wine-preloader
%endif
%ifarch ppc %arm
%{_bindir}/wine
%endif
%ifarch x86_64
%if %{wow64_build}
%{_bindir}/wine
%{_bindir}/wine-preloader
%else
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%endif
%endif

%ifarch x86_64
%if !%{wow64_build}
%dir /usr/lib/wine/
%dir /usr/lib/wine/i386-windows
%dir /usr/lib/wine/i386-unix
%{_libdir}/wine/i386-unix
%{_libdir}/wine/i386-windows
%else
%dir %{_libdir}/wine/i386-windows
%exclude %{_libdir}/wine/i386-windows/*.a
%endif

%dir %{_libdir}/wine/x86_64-windows
%dir %{_libdir}/wine/x86_64-unix
%dir %{_libdir}/wine
%else
%dir %{_libdir}/wine
%dir %{_libdir}/wine/*-windows
%dir %{_libdir}/wine/*-unix
%endif

%{_libdir}/wine/*-windows/*.[b-z]*
%{_libdir}/wine/*-windows/*.ax
%{_libdir}/wine/*-windows/*.acm
#ifarch aarch64
#{_libdir}/wine/*-windows/st*
#endif
%{_libdir}/wine/*-unix/*.so*

%files devel
%defattr(-,root,root)
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
%ifnarch aarch64
%{_libdir}/wine/*-unix/*.a
%endif
%if 0%{?suse_version} >= 1550
%ifarch %{ix86} x86_64
%ifarch x86_64
%dir %{_libdir}/wine/x86_64-windows
%dir %{_libdir}/wine/x86_64-unix
%endif
# only generated with mingw
%{_libdir}/wine/*-windows/*.a
%endif
%endif
%doc %{_mandir}/man1/winemaker.1*
%doc %{_mandir}/*/man1/winemaker.1*
%doc %{_mandir}/man1/widl.1*
%doc %{_mandir}/man1/winedump.1*
%doc %{_mandir}/man1/wineg++.1*
%doc %{_mandir}/man1/winegcc.1*
%doc %{_mandir}/man1/wmc.1*
%doc %{_mandir}/man1/wrc.1*

# {_datadir}/aclocal/wine.m4

%changelog
