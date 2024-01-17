#
# spec file for package motif
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


Name:           motif
Version:        2.3.8
Release:        0
Summary:        Motif Runtime Programs
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://motif.ics.com/
Source0:        https://sourceforge.net/projects/motif/files/Motif%%20%{version}%%20Source%%20Code/motif-%{version}.tar.gz
Source1:        mwm.desktop
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM 02-fix-format-security.patch -- http://bugs.motifzone.net/show_bug.cgi?id=1574
Patch0:         fix-format-security.patch
# PATCH-FEATURE-UPSTREAM 03-no-demos.patch -- Disable demos if not needed
Patch1:         no-demos.patch
# PATCH-FIX-UPSTREAM fix_underlinking.patch -- http://bugs.motifzone.net/show_bug.cgi?id=1583
Patch2:         fix_underlinking.patch
# PATCH-FIX-UPSTEAM 13-fix_hardcoded_x11rgb_path.patch -- http://bugs.motifzone.net/show_bug.cgi?id=1585
Patch3:         fix_hardcoded_x11rgb_path.patch
# PATCH-FIX-UPSTREM 16-fix-undefined-use-of-sprintf.patch -- http://bugs.motifzone.net/show_bug.cgi?id=1628
Patch4:         fix-undefined-use-of-sprintf.patch
Patch5:         https://git.alpinelinux.org/aports/plain/community/motif/18-option-main.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu) >= 1.1.1
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
Conflicts:      lestif2
Provides:       openmotif = %{version}
Obsoletes:      openmotif < %{version}

%description
This package provides programs of the Motif runtime enviroment.

%package -n libMrm4
Summary:        Motif Resource Manager library
Group:          System/Libraries

%description -n libMrm4
The Motif resource manager (MRM) is responsible for creating widgets
based on definitions contained in user interface definition (UID)
files created by the UIL compiler. MRM interprets the output of the
UIL compiler and generates the appropriate argument lists for widget
creation functions.

%package -n libUil4
Summary:        Motif User Interface Language library
Group:          System/Libraries

%description -n libUil4
The Motif user interface language (UIL) is a specification language
for describing the initial state of a Motif application's user
interface.

%package -n libXm4
Summary:        Motif runtime library
Group:          System/Libraries
Provides:       openmotif-libs = %{version}-%{release}
Obsoletes:      openmotif-libs < %{version}-%{release}

%description -n libXm4
This package provides the main Motif shared library.

%package devel
Summary:        Motif Include Files and Libraries Mandatory for Development
Group:          Development/Libraries/X11
Requires:       libMrm4 = %{version}
Requires:       libUil4 = %{version}
Requires:       libXm4 = %{version}
Requires:       pkgconfig(printproto)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xft)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(xt)
Conflicts:      lesstif-devel
Conflicts:      lesstifd
Conflicts:      lestif2d
Provides:       openmotif-devel = %{version}-%{release}
Obsoletes:      openmotif-devel < %{version}-%{release}

%description devel
This package provies the include files and libraries necessary for developing
Motif applications.

%prep
%autosetup -p1
sed -i 's|{libdir}/X11|{datadir}/X11|' configure.ac

%build
autoreconf -fi
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-static \
    --disable-demos \
    --with-x11rgbdir="%{_datadir}/X11" \
    --enable-xft \
    --enable-jpeg \
    --enable-png
%make_build MWMRCDIR=%{_sysconfdir}/X11 XMBINDDIR_FALLBACK=%{_datadir}/X11/bindings

%install
%make_install MWMRCDIR=%{_sysconfdir}/X11 XMBINDDIR_FALLBACK=%{_datadir}/X11

install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/mwm.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/mwm.desktop

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libMrm4 -p /sbin/ldconfig

%postun -n libMrm4 -p /sbin/ldconfig

%post   -n libUil4 -p /sbin/ldconfig

%postun -n libUil4 -p /sbin/ldconfig

%post   -n libXm4  -p /sbin/ldconfig

%postun -n libXm4  -p /sbin/ldconfig

%files
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/xm_*
%{_datadir}/X11/bindings
%{_bindir}/mwm
%{_bindir}/xmbind
%config %{_sysconfdir}/X11/system.mwmrc
%{_mandir}/man1/mwm.1%{ext_man}
%{_mandir}/man1/xmbind.1%{ext_man}
%{_mandir}/man4/*.4%{ext_man}
%{_datadir}/xsessions/*

%files -n libMrm4
%{_libdir}/libMrm.so.4*

%files -n libUil4
%{_libdir}/libUil.so.4*

%files -n libXm4
%{_libdir}/libXm.so.4*

%files devel
%{_bindir}/uil
%{_includedir}/Mrm
%{_includedir}/uil
%{_includedir}/Xm
%{_libdir}/*.so
%{_mandir}/man1/uil.1%{ext_man}
%{_mandir}/man3/*%{ext_man}
%{_mandir}/man5/*%{ext_man}

%changelog
