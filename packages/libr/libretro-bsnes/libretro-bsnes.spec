#
# spec file for package libretro-bsnes
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


Name:           libretro-bsnes
Version:        0~20170724.263e94f9
Release:        0
Summary:        SNES Emulator for Retro-based frontends
License:        GPL-3.0
Group:          Amusements/Games/Other
Url:            https://github.com/libretro/bsnes-libretro
Source:         bsnes-libretro-%{version}.tar.xz
Source1:        bsnes_balanced.libretro
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a libretro port of the BSNES emulator.
It can be used by various frontends to load SNES ROMs.

%prep
%setup -q -n bsnes-libretro-%{version}

%build
make %{?_smp_mflags} prefix=%{_prefix} core_installdir=%{_libdir}/libretro/ profile=balanced

%install
make DESTDIR=%{buildroot} install prefix=%{_prefix} core_installdir=%{_libdir}/libretro/ profile=balanced
mkdir -p %{buildroot}%{_libdir}/libretro/
install -m644 -p %{SOURCE1} %{buildroot}%{_libdir}/libretro/

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/libretro
%{_libdir}/libretro/bsnes_balanced.libretro
%{_libdir}/libretro/bsnes_balanced_libretro.so

%changelog
