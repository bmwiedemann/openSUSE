#
# spec file for package autotrace
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


Name:           autotrace
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pstoedit-devel
Summary:        Program for Converting Bitmaps to Vector Graphics
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Graphics/Convertors
Provides:       bitmap_tracing
Version:        0.31.1
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        pstoedit.m4
Patch0:         %{name}-%{version}-quotefix.diff
# PATCH-FIX-OPENSUSE 0001-fix_input_png.patch sfalken@opensuse.org -- fixes build failure against libpng15
Patch1:         0001-fix_input_png.patch
# PATCH-FIX-SECURITY CVE-2019-19004.patch bsc1182158 CVE-2019-19004 -- biWidth*biBitCnt integer overflow fix
Patch2:         CVE-2019-19004.patch
# PATCH-FIX-SECURITY CVE-2019-19005.patch bsc1182159 CVE-2019-19005 CVE-2017-9182, CVE-2017-9190 -- bitmap double free fix
Patch3:         CVE-2019-19005.patch
# PATCH-FIX-SECURITY CVE-2022-32323.patch bsc1201529 -- Heap overflow
Patch4:         CVE-2022-32323.patch
URL:            http://autotrace.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick-devel
# FIXME: Broken with the latest pstoedit. See Fedora patches for partial fix.
#BuildConflicts: pstoedit-devel

%description
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%package -n libautotrace3
Summary:        Library for converting bitmaps to vector graphics
Group:          System/Libraries

%description -n libautotrace3
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%package devel

Summary:        Library for converting bitmaps to vector graphics
Group:          Development/Libraries/C and C++
Requires:       libautotrace3 = %{version}

%description devel
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-tree-sra"
cat %{SOURCE1} >>acinclude.m4
autoreconf -f -i
%configure\
	--disable-static
%{__make} %{?jobs:-j%jobs}

%install
%make_install
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -n libautotrace3 -p /sbin/ldconfig

%postun -n libautotrace3 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING FAQ NEWS README README.MING THANKS TODO
%{_bindir}/autotrace
%{_mandir}/man1/autotrace.1*

%files -n libautotrace3
%defattr(-, root, root)
%doc COPYING.LIB
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/*-config
%{_datadir}/aclocal/*.m4
%{_includedir}/autotrace
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
