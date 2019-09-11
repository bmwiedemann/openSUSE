#
# spec file for package aalib
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           aalib
%define lname	libaa1
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} > 1130
BuildRequires:  gpm-devel
%else
BuildRequires:  gpm
%endif
Url:            http://aa-project.sourceforge.net/
# bug437293
%ifarch ppc64
Obsoletes:      aalib-64bit
%endif
#
Version:        1.4.0
Release:        0
Summary:        An ASCII Art Library
License:        GPL-2.0+
Group:          System/Libraries
Source:         http://sourceforge.net/projects/aa-project/files/aa-lib/1.4rc5/%{name}-1.4rc5.tar.gz
Source1:        http://downloads.sourceforge.net/project/aa-project/aavga/1.0rc1/aavga-1.0rc1.tar.gz
Source2:        http://downloads.sourceforge.net/project/aa-project/aview/1.3.0rc1/aview-1.3.0rc1.tar.gz
Source3:        baselibs.conf
Patch1:         fix_gpm_fd_handling.diff
Patch2:         aavga.dif
Patch3:         aalib-1.4.0.dif
Patch4:         aview-1.3.0.patch
Patch5:         aview-1.3.0-tmpvuln.diff
Patch6:         aalib-distint.patch
Patch7:         aview-signed-char.patch
Patch8:         aview-includes.patch
Patch9:         aalib-includes.patch
Patch10:        aalib-reentrant.patch
Patch11:        aalib-1.4.0-config.patch
Patch12:        aalib-1.4.0-fdleak.patch
Patch13:        aalib-ncurses-6.0-accessors.patch
PreReq:         %install_info_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
AA-lib is a low level gfx library. AA-lib does not require a graphics
device. In fact, there is no graphical output possible. AA-lib replaces
old-fashioned output methods with a powerful ASCII art renderer.

%package -n %lname
Summary:        An ASCII Art Library
Group:          System/Libraries

%description -n %lname
AA-lib is a low level gfx library. AA-lib does not require a graphics
device. In fact, there is no graphical output possible. AA-lib replaces
old-fashioned output methods with a powerful ASCII art renderer.

%package devel
Summary:        Development Package for AAlib
Group:          Development/Libraries/C and C++
# bug437293
%ifarch ppc64
Obsoletes:      aalib-devel-64bit
%endif
#
Requires:       %lname = %version
Requires:       glibc-devel
Obsoletes:      aalibdev

%description devel
Files needed for developing software that uses AAlib.

%prep
%setup -q -a 1 -b 2
%patch1
%patch3
%patch10
%patch11
%patch12
%patch13 -p1
cd aavga-1.0 
%patch2
cd ../../aview-*
%patch4
%patch7
%patch8
cd ..
%patch5
%patch6
%patch9

%build
%{?suse_update_config}
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fstrength-reduce -ffast-math -fomit-frame-pointer"
%ifarch %ix86
export CFLAGS="$CFLAGS -falign-loops=2 -falign-jumps=2 -falign-functions=2"
%endif
%configure --disable-static --with-pic --with-slang-driver=no --with-ncurses
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
cp -av ANNOUNCE AUTHORS COPYING INSTALL NEWS README $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
cd ../aview-1.3.0
PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
   CFLAGS="$RPM_OPT_FLAGS -I$RPM_BUILD_ROOT/usr/include" \
   LDFLAGS="-L$RPM_BUILD_ROOT%{_libdir}" \
   LD_LIBRARY_PATH="$RPM_BUILD_ROOT%{_libdir}" \
   ./configure --prefix=/usr --mandir=%{_mandir}
make
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/aview
cp -av README* ANNOUNCE COPYING TODO *.lsm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/aview
cd -
cd aavga-1.0 
make CFLAGS="$RPM_OPT_FLAGS"
cp -av aavga.so $RPM_BUILD_ROOT%_libdir
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/aavga
cp -av aavga.lsm COPYING README $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/aavga
cd ..
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%docdir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}
%_bindir/aafire
%_bindir/aaflip
%_bindir/aainfo
%_bindir/aasavefont
%_bindir/aatest
%_bindir/asciiview
%_bindir/aview
%{_infodir}/aalib.info.gz
%{_infodir}/aalib.info-?.gz
%{_mandir}/man1/aafire.1.gz
%{_mandir}/man1/aview.1.gz
%{_mandir}/man1/asciiview.1.gz

%files -n %lname
%defattr(-,root,root)
%_libdir/libaa.so.1.0.4
%_libdir/libaa.so.1
%_libdir/aavga.so

%files devel
%defattr(-,root,root)
%_includedir/aalib.h
%_libdir/libaa.so
%_datadir/aclocal/aalib.m4
%_bindir/aalib-config
%{_mandir}/man3/aa_*.3.gz
%{_mandir}/man3/mem_d.3.gz
%{_mandir}/man3/save_d.3.gz

%changelog
