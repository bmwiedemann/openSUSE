#
# spec file for package libvisual
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


Name:           libvisual
Version:        0.4.0
Release:        0
%ifarch ppc64
# bug437293
Obsoletes:      libvisual-64bit
%endif
Summary:        Sound Visualization Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Visualization
URL:            http://localhost.nl/~synap/libvisual-wiki/index.php/Main_Page
Source:         %name-%{version}.tar.bz2
Source2:        baselibs.conf
Patch:          %name-%{version}.diff
Patch1:         %name-%{version}-compiler_warnings.diff
Patch2:         libvisual.visual_cpu_get_altivec.patch
Patch3:         %name-%{version}-unref-static.diff
Patch4:         libvisual-0.4.0-2.1-nmu.diff
Patch5:         libvisual-0.4.0-inlinedefineconflict.patch
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Libvisual is a library that acts as a middle layer between applications
that need audio visualization and audio visualization plug-ins.

%package -n libvisual-0_4-0
Summary:        Sound Visualization library
Group:          System/Libraries

%description -n libvisual-0_4-0
Libvisual is a library that acts as a middle layer between applications
that need audio visualization and audio visualization plug-ins.

%package devel
Summary:        Headers for the libvisual sound visualization library
Group:          Productivity/Multimedia/Sound/Visualization
Requires:       glibc-devel
Requires:       libvisual-0_4-0 = %{version}-%{release}
# bug437293
%ifarch ppc64
Obsoletes:      libvisual-devel-64bit
%endif

%description devel
Libvisual is a library that acts as a middle layer between applications
that want audio visualisation and audio visualisation plugins.

This library is used by amaroK for example.

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
CFLAGS="%optflags -fstack-protector"
%endif
%ifarch %ix86
CFLAGS="%optflags -mmmx"
%else
CFLAGS="%optflags"
%endif
export CFLAGS="$CFLAGS -fno-strict-aliasing"
%configure --disable-static
%make_build

%install
%make_install
for i in morph input actor transform; do
	mkdir -p %buildroot/%_libdir/%name/$i %buildroot/%_datadir/%name/$i
done
rm -v %buildroot/%_libdir/*.la
# *fixme*
rm -rf %buildroot/%_datadir/locale

%post   -n libvisual-0_4-0 -p /sbin/ldconfig
%postun -n libvisual-0_4-0 -p /sbin/ldconfig

%files -n libvisual-0_4-0
%_libdir/libvisual-0.4.so.*
%_libdir/libvisual
%_datadir/libvisual

%files devel
%doc AUTHORS README ChangeLog NEWS TODO
%license COPYING
%_includedir/libvisual-0.4
%_libdir/pkgconfig/libvisual-0.4.pc
%_libdir/libvisual-0.4.so

%changelog
