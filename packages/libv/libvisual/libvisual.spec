#
# spec file for package libvisual
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libvisual
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
Version:        0.4.0
Release:        0
# bug437293
%ifarch ppc64
Obsoletes:      libvisual-64bit
%endif
#
Summary:        Sound Visualization Library
License:        GPL-2.0+ and LGPL-2.1+
Group:          Productivity/Multimedia/Sound/Visualization
Url:            http://localhost.nl/~synap/libvisual-wiki/index.php/Main_Page
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %name-%{version}.tar.bz2
Source2:        baselibs.conf
Patch:          %name-%{version}.diff
Patch1:         %name-%{version}-compiler_warnings.diff
Patch2:         libvisual.visual_cpu_get_altivec.patch
Patch3:         %name-%{version}-unref-static.diff
Patch4:         libvisual-0.4.0-2.1-nmu.diff
Patch5:         libvisual-0.4.0-inlinedefineconflict.patch

%description
Libvisual is a library that acts as a middle layer between applications
that need audio visualization and audio visualization plug-ins.



Authors:
--------
    Dennis Smit <synap@nerds-incorporated.org>
    Duilio J. Protti <dprotti@users.sourceforge.net>
    Vitaly V. Bursov <vitalyb@mail333.com>
    Gustavo Sverzut Barbieri <gsbarbieri@yahoo.com.br>

%package devel
Summary:        sound visualisation library
Group:          Productivity/Multimedia/Sound/Visualization
Requires:       %{name} = %{version}
Requires:       glibc-devel
# bug437293
%ifarch ppc64
Obsoletes:      libvisual-devel-64bit
%endif
#

%description devel
Libvisual is a library that acts as a middle layer between applications
that want audio visualisation and audio visualisation plugins.

This library is used by amaroK for example.



Authors:
--------
    Dennis Smit <synap@nerds-incorporated.org>
    Duilio J. Protti <dprotti@users.sourceforge.net>
    Vitaly V. Bursov <vitalyb@mail333.com>
    Gustavo Sverzut Barbieri <gsbarbieri@yahoo.com.br>

%prep
%setup -q
%patch
%patch1
%patch2 -p1
%patch3
%patch4 -p1
%patch5 -p1

%build
autoreconf -fiv
%if %suse_version > 1000
CFLAGS="$RPM_OPT_FLAGS -fstack-protector"
%endif
%ifarch %ix86
CFLAGS="$RPM_OPT_FLAGS -mmmx"
%else
CFLAGS="$RPM_OPT_FLAGS"
%endif
export CFLAGS="$CFLAGS -fno-strict-aliasing"
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%_libdir/%name/{morph,input,actor,transform} $RPM_BUILD_ROOT%_datadir/%name/{morph,input,actor,transform}
sed -e 's, -L%{_builddir}/libvisual-%{version}/libvisual , ,' $RPM_BUILD_ROOT/%_libdir/libvisual-0.4.la > $RPM_BUILD_ROOT/%_libdir/libvisual-0.4.la.1
mv $RPM_BUILD_ROOT/%_libdir/libvisual-0.4.la.1 $RPM_BUILD_ROOT/%_libdir/libvisual-0.4.la
# *fixme*
rm -rf $RPM_BUILD_ROOT/%_datadir/locale

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO COPYING
%_libdir/libvisual-0.4.so.*
%_libdir/libvisual
%_datadir/libvisual

%files devel
%defattr(-,root,root)
/usr/include/libvisual-0.4
%_libdir/pkgconfig/libvisual-0.4.pc
%_libdir/libvisual-0.4.so
%_libdir/libvisual-0.4.la

%changelog
