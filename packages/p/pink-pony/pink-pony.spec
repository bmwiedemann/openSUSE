#
# spec file for package pink-pony
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           pink-pony
Version:        1.4.1
Release:        0
Summary:        3D racing game with ponies
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://ginkgo.github.io/pink-pony/
Source0:        https://github.com/ginkgo/pink-pony/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         datadir.patch
Patch1:         script.patch
Patch2:         pink-pony-1.4.1.diff
Patch3:         pink-pony-1.4.1-protobuf.diff
Patch4:         0001-Fix-compile-issues-caused-by-Imath-being-moved-out-o.patch
BuildRequires:  DevIL-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ftgl-devel
BuildRequires:  ilmbase-devel
BuildRequires:  libsigc++2-devel
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libglfw)
BuildRequires:  pkgconfig(protobuf)
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
Requires:       pink-pony-data = %{version}

%package data
Summary:        3D racing game with ponies - data files
License:        CC-BY-3.0 AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND OFL-1.1 AND CC0-1.0
Group:          Amusements/Games/Action/Arcade
Requires:       pink-pony = %{version}
BuildArch:      noarch

%description
Pink Pony is a Tron­-like multiplayer racing­ game. You control
little ponies that leave a trail of flowers everywhere they step.
You have to evade these trails and force other ponies into them.
The last pony standing wins the game.

%description data
Pink Pony is a Tron­-like multiplayer racing­ game. You control
little ponies that leave a trail of flowers everywhere they step.
You have to evade these trails and force other ponies into them.
The last pony standing wins the game.

 This package contains architecture-independent game data

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
# apply patch3 and patch4 only on openSUSE Tumbleweed
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} == 1500 && 0%{?sle_version} > 150300)
%patch -P 3 -p1
%endif
%if 0%{?suse_version} >= 1550
%patch -P 4 -p1
%endif

%build
export CCFLAGS="%{optflags}"
scons -f SConstruct %{?_smp_mflags} \
	prefix=%{_prefix} \
	resources_dir=%{_datadir}/pink-pony \
	lib_dir="${PWD}"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_prefix}/lib/pink-pony
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -m 755 %{buildroot}%{_datadir}/pink-pony
install -m 755 Pony %{buildroot}%{_prefix}/lib/pink-pony/pink-pony.bin
install -m 755 install/pink-pony %{buildroot}%{_bindir}/
install -m 644 install/pink-pony.png %{buildroot}%{_datadir}/pixmaps
install -m 644 pony.options %{buildroot}%{_datadir}/pink-pony
cp -r resources/* %{buildroot}%{_datadir}/pink-pony

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications           \
  install/pink-pony.desktop

%files
%doc README
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_prefix}/lib/pink-pony

%files data
%{_datadir}/pink-pony

%changelog
