#
# spec file for package pixman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pixman
Version:        0.36.0
Release:        0
Summary:        Pixel manipulation library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/
Source:         http://cairographics.org/releases/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  pkgconfig

%description
Pixman is a pixel manipulation library for X and cairo.

%package -n libpixman-1-0
Summary:        Pixel manipulation library
Group:          System/Libraries

%description -n libpixman-1-0
Pixman is a pixel manipulation library for X and cairo.

%package -n libpixman-1-0-devel
Summary:        Development files for the Pixel Manipulation library
Group:          Development/Libraries/C and C++
Requires:       libpixman-1-0 = %{version}

%description -n libpixman-1-0-devel
Pixman is a pixel manipulation library for X and cairo.

%prep
%setup -q

%build
#autoreconf -fi
#
# For now: disable neon on all ARMv6/7
%configure \
%ifarch %{arm}
       --disable-arm-iwmmxt \
       --disable-arm-neon \
%endif
%ifarch ppc64le
        --disable-vmx \
%endif
       --disable-static
make V=1 %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libpixman-1.la

%post -n libpixman-1-0 -p /sbin/ldconfig
%postun -n libpixman-1-0 -p /sbin/ldconfig

%files -n libpixman-1-0
%license COPYING

%{_libdir}/libpixman-1.so.*

%files -n libpixman-1-0-devel
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
