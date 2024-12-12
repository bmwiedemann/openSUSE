#
# spec file for package pixman
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


Name:           pixman
Version:        0.43.4
Release:        0
Summary:        Pixel manipulation library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/pixman/pixman
Source:         https://www.cairographics.org/releases/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  meson

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
%autosetup -p1

%build
#
# For now: disable neon on all ARMv6/7
#
%meson \
%ifnarch %{ix86}
       -Dmmx="disabled" \
       -Dsse2="disabled" \
       -Dssse3="disabled" \
%endif
       -Dvmx="disabled" \
       -Dloongson-mmi="disabled" \
       -Darm-simd="disabled" \
       -Dneon="disabled" \
%ifarch aarch64
       -Da64-neon="enabled" \
%else
       -Da64-neon="disabled" \
%endif
       -Diwmmxt="disabled" \
       -Dmips-dspr2="disabled" \
       -Ddemos=disabled \
       -Dlibpng=disabled
%meson_build

%check
%ifarch s390x
%meson_test -t 5
%else
%meson_test
%endif

%install
%meson_install

%ldconfig_scriptlets -n libpixman-1-0

%files -n libpixman-1-0
%license COPYING
%{_libdir}/libpixman-1.so.*

%files -n libpixman-1-0-devel
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
