#
# spec file for package libyami
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


%define sover   1
%define libname %{name}%{sover}

Name:           libyami
Version:        1.3.1
### FIXME ### On next version bump, please remove export CXXFLAGS="-Wno-error" -- WIP progress upstream to fix gcc9 buildfail
Release:        0
Summary:        Media Library with support for Intel hardware acceleration
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/intel/libyami
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 0.39.3
BuildRequires:  pkgconfig(libva-x11)

# Intel graphics hardware only available on these platforms
ExclusiveArch:  %{ix86} x86_64
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libva-wayland)
%endif

%description
Intel VA-API Media Library with support for hardware acceleration.

The library loads libva to interface with a hardware-dependent driver.

%package -n %{libname}
Summary:        Library components for %{name}
Group:          System/Libraries

%description -n %{libname}
The libyami library implements an interface to libva for Linux.
This package provides the runtime environment for libyami.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
export CXXFLAGS="-Wno-error"
autoreconf -fiv
%configure \
  --disable-static \
  --with-package-name="Libyami Media Infrastructure (openSUSE)" \
  --with-package-origin="http://www.opensuse.org/" \
  --enable-h265dec \
  --enable-vc1dec \
  --enable-h264dec \
  --enable-jpegdec \
  --enable-mpeg2dec \
  --enable-vp8dec \
  --enable-vp9dec \
  --enable-h265enc \
  --enable-h264enc \
  --enable-jpegenc \
  --enable-vp8enc \
%if 0%{?suse_version} >= 1500
  --enable-wayland="yes" \
%endif
  %{nil}
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%doc README.md NEWS
%{_libdir}/%{name}.so.%{sover}*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
