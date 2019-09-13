#
# spec file for package libretro-pcsx_rearmed
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libretro-pcsx_rearmed
Version:        0~20160921.9766e77
Release:        0
Summary:        Playstation Emulator for Retro-based frontends
License:        GPL-2.0
Group:          Amusements/Games/Other
Url:            https://github.com/libretro/pcsx_rearmed
Source:         pcsx_rearmed-%{version}.tar.xz
Source1:        pcsx_rearmed.libretro
Source2:        pcsx_rearmed-Makefile.install
# PATCH-FIX-OPENSUSE uncompress2-rename-to-static.patch rename static uncompress2 to prevent conflict with zlib.h declaration
Patch1:         uncompress2-rename-to-static.patch
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a libretro port of the PCSX-ReARMed emulator.
It can be used by various frontends to load Playstation games.

%prep
%setup -q -n pcsx_rearmed-%{version}
cp %{S:2} Makefile.install
%patch1 -p1

%build
make %{?_smp_mflags} --makefile=Makefile.install prefix=%{_prefix} core_installdir=%{_libdir}/libretro/

%install
make DESTDIR=%{buildroot} install --makefile=Makefile.install prefix=%{_prefix} core_installdir=%{_libdir}/libretro/
mkdir -p %{buildroot}%{_libdir}/libretro/
install -m644 -p %{SOURCE1} %{buildroot}%{_libdir}/libretro/

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/libretro
%{_libdir}/libretro/pcsx_rearmed.libretro
%{_libdir}/libretro/pcsx_rearmed_libretro.so

%changelog
