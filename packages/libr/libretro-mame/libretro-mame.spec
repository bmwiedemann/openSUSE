#
# spec file for package libretro-mame
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libretro-mame
Version:        0~git20200205
Release:        0
Summary:        MAME libretro core for arcade emulation
License:        GPL-2.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-xml

%description
MAME is a multi-purpose emulation framework.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
%ifarch x86_64 aarch64 ppc64 ppc64le
make %{?_smp_mflags} -f Makefile.libretro PTR64=1 PYTHON_EXECUTABLE=python3
%else
make %{?_smp_mflags} -f Makefile.libretro PYTHON_EXECUTABLE=python3
%endif

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp mame_libretro.so %{buildroot}%{_libdir}/libretro

%files
%license LICENSE.md
%dir %{_libdir}/libretro
%{_libdir}/libretro/mame_libretro.so

%changelog
