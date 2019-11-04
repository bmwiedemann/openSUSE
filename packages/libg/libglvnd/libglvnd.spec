#
# spec file for package libglvnd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           libglvnd
Version:        1.2.0
Release:        0
Summary:        The GL Vendor-Neutral Dispatch library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/NVIDIA/libglvnd
# Source is _service generated
Source:         %name-%version.tar.gz
Source1:        baselibs.conf
Patch0:         n_0001-GL-Bump-GL-version-to-9-2.patch
Patch1:         0001-include-install-GL-headers-when-GL-is-enabled.patch
Patch2:         0002-Add-a-configure-option-to-disable-glesv1-or-glesv2.patch
Patch3:         0003-egl-Sync-with-Khronos.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       libglvnd0 = %version-%release
Obsoletes:      libglvnd0 <= %version-%release

%description
Vendor-neutral dispatch layer for arbitrating OpenGL API calls between
multiple vendors on a per-screen basis, as described by Andy Ritger's
OpenGL ABI proposal.
 
%package devel
Summary:        Development files for libglvnd
Group:          Development/Libraries/C and C++
Requires:       %name = %version

%description devel
Vendor-neutral dispatch layer for arbitrating OpenGL API calls between
multiple vendors on a per-screen basis, as described by Andy Ritger's
OpenGL ABI proposal. This package contains the required files for
development.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# fix env shebang to call py3 directly
sed -i -e "1s|#!.*|#!/usr/bin/python3|" src/generate/*.py

%build
./autogen.sh
%configure \
%if 0%{?suse_version} < 1330
    --libdir=/usr/X11R6/%_lib \
%endif
    --disable-static \
    --disable-headers \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete
>%_builddir/%name-%version/filelist.rpm
%if 0%{?suse_version} < 1330
mkdir -p %buildroot/%_libdir/pkgconfig
mv %buildroot/usr/X11R6/%_lib/pkgconfig/*.pc %buildroot/%_libdir/pkgconfig
if [ "%_lib" == "lib64" ]; then
  mkdir -p %buildroot/%_sysconfdir/ld.so.conf.d
  cat > %buildroot/%_sysconfdir/ld.so.conf.d/%name.conf << EOF
/usr/X11R6/%_lib
/usr/X11R6/lib
EOF
  echo "%config %_sysconfdir/ld.so.conf.d/%name.conf" >%_builddir/%name-%version/filelist.rpm
fi
%endif
mkdir -p %buildroot/usr/share/doc/packages/%name/pkgconfig
mv %buildroot/%_libdir/pkgconfig/{gl,egl,glesv1_cm,glesv2}.pc \
   %buildroot/usr/share/doc/packages/%name/pkgconfig

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f filelist.rpm
%defattr(-,root,root)
%doc README.md
/usr/share/doc/packages/%name/pkgconfig
%if 0%{?suse_version} < 1330
%dir /usr/X11R6
%dir /usr/X11R6/%_lib
/usr/X11R6/%_lib/lib*.so.*
%else
%_libdir/lib*.so.*
%endif

%files devel
%defattr(-,root,root)
%if 0%{?suse_version} < 1330
%dir /usr/X11R6
%dir /usr/X11R6/%_lib
/usr/X11R6/%_lib/lib*.so
%else
%_libdir/lib*.so
%endif
%_libdir/pkgconfig/*.pc
%_includedir/glvnd/

%changelog
