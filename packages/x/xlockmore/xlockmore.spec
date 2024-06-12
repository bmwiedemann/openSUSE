#
# spec file for package xlockmore
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


Name:           xlockmore
Version:        5.78
Release:        0
Summary:        Screen Saver and Locker for the X Window System
License:        MIT
Group:          System/X11/Utilities
URL:            https://sillycycle.com/xlockmore.html
Source:         https://sillycycle.com/xlock/%{name}-%{version}.tar.xz
Source1:        xlock.pamd
Source2:        xlock-wrapper
Source3:        xlock-wrapper_xorg6
Source4:        http://sillycycle.com/xlock/%{name}-%{version}.tar.xz.asc
Source5:        %{name}.keyring
# apply even patches when X.org < 7.0 else apply odd patches
Patch1:         %{name}-bitmaps.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch3:         xlockmore-ttf_dir.patch
# end of X.org related patches
Patch7:         xlockmore-strict-aliasing.patch
# PATCH-FIX-UPSTREAM xlockmore-extend-freetype-include-search.patch -- search only for freetype.h, not the half path. Also,
# extended list of directories where could freetype be found
Patch9:         xlockmore-extend-freetype-include-search.patch
Patch10:        xlockmore-nose_mode_crash.patch
BuildRequires:  ImageMagick-devel
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  libXdmcp-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libdrm-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig

%description
The xlock utility locks your X Window System session and runs a screen
saver until a password is entered.

%define _xorg7libs %{_lib}
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %{_mandir}
%define _xorg7pixmaps include
%define _xorg7libshare lib
%define _xorg7_xkb %{_datadir}/X11/xkb
%define _xorg7_termcap %{_prefix}/lib/X11%{_sysconfdir}
%define _xorg7_serverincl %{_includedir}/xorg
%define _xorg7_fonts %{_datadir}/fonts
%define _xorg7_prefix %{_prefix}

%prep
%setup -q
chmod -x README docs/Revisions
%patch -P 1
%patch -P 3
%patch -P 7
%patch -P 9 -p1
%patch -P 10 -p1

%build
aclocal
autoconf
export CPPFLAGS="-I/usr/include/FTGL $(freetype-config --cflags)"
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure \
	--prefix=%{_xorg7_prefix}\
	--with-libraries=%{_libdir}\
	--with-magick\
	--with-xinerama\
	--with-xpm\
	--without-gtk\
	--without-motif\
	--disable-bomb\
	--enable-pam\
	--enable-vtlock\
	--disable-allow-root\
	--x-includes=%{_xorg7_prefix}/include\
	--x-libraries=%{_xorg7_prefix}/%{_lib}
%make_build

%install
install -d -m 755 %{buildroot}%{_prefix}/%{_xorg7bin}/
install -d -m 755 %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/app-defaults/
install -d -m 755 %{buildroot}%{_xorg7_mandir}/man1/
install -d -m 755 %{buildroot}%{_prefix}/%{_xorg7libs32}/xlock
install -m 755 xlock/xlock %{buildroot}%{_prefix}/%{_xorg7libs32}/xlock/xlock
install -m 644 xlock/XLock.ad %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/app-defaults/XLock
install -m 644 xlock/xlock.man %{buildroot}%{_xorg7_mandir}/man1/xlock.1x
%if 0%{?suse_version} > 1500
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE1} %{buildroot}%{_pam_vendordir}/xlock
%else
install -d -m 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/xlock
%endif

%if "%(pkg-config --variable prefix x11 || echo %{_prefix}/X11R6)" == "%{_prefix}"
install -m 755 %{SOURCE2} %{buildroot}%{_prefix}/%{_xorg7bin}/xlock
%else
install -m 755 %{SOURCE3} %{buildroot}%{_prefix}/%{_xorg7bin}/xlock
%endif
%fdupes %{buildroot}%{_prefix}

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/xlock ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/xlock ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%doc %{_xorg7_mandir}/man1/xlock.1x.gz
%doc README docs/3d.howto docs/Purify docs/Revisions docs/TODO docs/cell_automata
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/xlock
%else
%config %{_sysconfdir}/pam.d/xlock
%endif
%{_prefix}/%{_xorg7libshare}/X11/app-defaults
%{_prefix}/%{_xorg7bin}/xlock
%{_prefix}/%{_xorg7libs32}/xlock

%changelog
