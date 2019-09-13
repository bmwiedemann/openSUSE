#
# spec file for package motif
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           motif
Version:        2.3.4
Release:        0
Summary:        Motif Runtime Programs
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://motif.ics.com/
Source0:        http://sourceforge.net/projects/motif/files/Motif%20%{version}%20Source%20Code/%{name}-%{version}-src.tgz
Source1:        mwm.desktop
Source2:        baselibs.conf
Patch0:         openmotif-2.3.3.diff
Patch1:         warn.patch
Patch2:         strcmp.diff
Patch3:         openmotif-xpm.diff
Patch4:         sentinel.diff
Patch5:         openmotif-uil.diff
Patch6:         openmotif-unaligned.diff
Patch7:         mwm.diff
Patch8:         openmotif-editres.diff
Patch9:         openmotif-editres-prototype.patch
Patch10:        motif-avoid-empty-include.diff
Patch11:        motif-sequence-points.diff
Patch12:        openmotif-2.3.1-suse-stipple.patch
# PATCH-FIX-UPSTREAM fix implicit-fortify-decl errors
Patch13:        motif-2.3.4-implicit-fortify-decl.patch
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q
# remove all files that have strange licenses
rm lib/Xm/regexp.c
rm lib/Xm/regexpI.h
rm localized/util/mkcatdefs.c
rm tests/doc/Output/draft/ps/title.ps
rm tests/doc/title.sm
sed -e '/regexpI.h/d' -i lib/Xm/Makefile.am
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch -P 10 -P 11 -p1
%patch12 -p1
%patch13 -p1

%build
./autogen.sh
%ifarch %arm
# miscompilation?
RPM_OPT_FLAGS="%{optflags} -O1"
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-static \
    --enable-xft \
    --enable-jpeg \
    --enable-png \
    --with-pic
# parallel make is broken
make --jobs 1 MWMRCDIR=%{_sysconfdir}/X11

%install
make install DESTDIR=%{buildroot} MWMRCDIR=%{_sysconfdir}/X11

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
%defattr(-, root, root)
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
%defattr(-,root,root)
%{_libdir}/libMrm.so.4*

%files -n libUil4
%defattr(-,root,root)
%{_libdir}/libUil.so.4*

%files -n libXm4
%defattr(-,root,root)
%{_libdir}/libXm.so.4*

%files devel
%defattr(-, root, root)
%{_bindir}/uil
%{_includedir}/Mrm
%{_includedir}/uil
%{_includedir}/Xm
%{_libdir}/*.so
%{_mandir}/man1/uil.1%{ext_man}
%{_mandir}/man3/*%{ext_man}
%{_mandir}/man5/*%{ext_man}

%changelog
