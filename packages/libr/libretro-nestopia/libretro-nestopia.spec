#
# spec file for package libretro-nestopia
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


Name:           libretro-nestopia
Version:        1.50~git20200510
Release:        0
Summary:        Nintendo NES / FDS Emulator for Retro-based frontends
License:        GPL-2.0-only
Group:          Amusements/Games/Other
URL:            https://github.com/libretro/nestopia
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++

%description
This package contains a libretro port of the Nestopia emulator.
It can be used by various frontends to load Nintendo Entertainement System
/ Famicom Disk System games.

%prep
%setup -q

%build
make %{?_smp_mflags} --directory=libretro prefix=%{_prefix} core_installdir=%{_libdir}/libretro/

%install
make --directory=libretro DESTDIR=%{buildroot} install prefix=%{_prefix} libdir=%{_libdir}

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/nestopia_libretro.so

%changelog
