#
# spec file for package aalib
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


Name:           aalib
%define lname	libaa1
Version:        1.4.0
Release:        0
Summary:        An ASCII Art Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://aa-project.sourceforge.net/
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
BuildRequires:  fdupes
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(x11)
PreReq:         %install_info_prereq
# bug437293
%ifarch ppc64
Obsoletes:      aalib-64bit
%endif

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
Requires:       %lname = %version
Requires:       glibc-devel
Obsoletes:      aalibdev

%description devel
Files needed for developing software that uses AAlib.

%prep
%setup -q -a 1 -b 2
%patch -P 1
%patch -P 3
%patch -P 10
%patch -P 11
%patch -P 12
%patch -P 13 -p1
cd aavga-1.0
%patch -P 2
cd ../../aview-*
%patch -P 4
%patch -P 7
%patch -P 8
cd ..
%patch -P 5
%patch -P 6
%patch -P 9

%build
%{?suse_update_config}
autoreconf -fiv
export CFLAGS="%{optflags} -fstrength-reduce -fomit-frame-pointer -fpermissive"
%ifarch %ix86
export CFLAGS="$CFLAGS -falign-loops=2 -falign-jumps=2 -falign-functions=2"
%endif
%configure --disable-static --with-slang-driver=no --with-ncurses
%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
cp -av ANNOUNCE AUTHORS COPYING INSTALL NEWS README %{buildroot}/%{_defaultdocdir}/%{name}
cd ../aview-1.3.0
PATH=%{buildroot}/%{_bindir}:$PATH \
   CFLAGS="%{optflags} -fpermissive -I%{buildroot}/usr/include" \
   LDFLAGS="-L%{buildroot}/%{_libdir}" \
   LD_LIBRARY_PATH="%{buildroot}/%{_libdir}" \
   ./configure --prefix=/usr --mandir=%{_mandir}
make
%make_install
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/aview
cp -av README* ANNOUNCE COPYING TODO *.lsm %{buildroot}/%{_defaultdocdir}/%{name}/aview
cd -
cd aavga-1.0
make CFLAGS="%{optflags} -fpermissive"
cp -av aavga.so %{buildroot}/%_libdir
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/aavga
cp -av aavga.lsm COPYING README %{buildroot}/%{_defaultdocdir}/%{name}/aavga
cd ..
rm -f %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}/%{_prefix}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%ldconfig_scriptlets -n %lname

%files
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
%_libdir/libaa.so.1.0.4
%_libdir/libaa.so.1
%_libdir/aavga.so

%files devel
%_includedir/aalib.h
%_libdir/libaa.so
%_datadir/aclocal/aalib.m4
%_bindir/aalib-config
%{_mandir}/man3/aa_*.3.gz
%{_mandir}/man3/mem_d.3.gz
%{_mandir}/man3/save_d.3.gz

%changelog
