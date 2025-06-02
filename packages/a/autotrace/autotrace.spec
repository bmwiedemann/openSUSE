#
# spec file for package autotrace
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


%define so_ver 3
%define sh_lib lib%{name}%{so_ver}
Name:           autotrace
Version:        0.31.10
Release:        0
Summary:        Program for Converting Bitmaps to Vector Graphics
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/autotrace/autotrace
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM autotrace-pkgconfig-private-libs.patch gh#autotrace/autotrace#124 badshah400@gmail.com -- [pkgconfig] Move some libraries to Libs.private
Patch0:         https://github.com/autotrace/autotrace/commit/eeeb813a416ff309804f6833729fab20d036e667.patch#/autotrace-pkgconfig-private-libs.patch
# PATCH-FIX-UPSTREAM autotrace-ac_subst-magick-vars.patch gh#autotrace/autotrace#160 badshah400@gmail.com -- Fix unexpanded MAGICK_* variables in pkgconfig file
Patch1:         autotrace-ac_subst-magick-vars.patch
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
# Tests need pkill
BuildRequires:  procps
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pstoedit)
Provides:       bitmap_tracing

%description
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%package -n %{sh_lib}
Summary:        Library for converting bitmaps to vector graphics
Group:          System/Libraries

%description -n %{sh_lib}
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%package devel
Summary:        Library for converting bitmaps to vector graphics
Group:          Development/Libraries/C and C++
Requires:       %{sh_lib} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(ImageMagick)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gmodule-2.0)
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(pstoedit)

%description devel
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some aspects,
it is already better. Originally created as a plug-in for the GIMP,
AutoTrace is now a stand-alone program and can be compiled on any UNIX
platform using GCC.

%lang_package

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
  --enable-magick-readers \
  --disable-static \
  %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%check
%make_build check

%ldconfig_scriptlets -n %{sh_lib}

%files
%license COPYING
%doc AUTHORS FAQ NEWS README.md THANKS TODO
%{_bindir}/autotrace
%{_mandir}/man1/autotrace.1%{?ext_man}

%files -n %{sh_lib}
%license COPYING.LIB
%{_libdir}/*.so.*

%files devel
%license COPYING.LIB COPYING
%{_includedir}/autotrace
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
