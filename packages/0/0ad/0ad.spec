#
# spec file for package 0ad
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


# Enable NVTT only on arch supported by nvidia-texture-tools
%ifarch %{ix86} x86_64 ppc
%bcond_without nvtt
%else
%bcond_with nvtt
%endif

%bcond_without system_mozjs

# Use provided library
%bcond_without system_nvtt

# 0ad needs a c++17 compiler at least
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%global force_gcc_version 13
%endif

Name:           0ad
Version:        0.27.0
Release:        0
Summary:        A real-time strategy game of ancient warfare
License:        BSD-3-Clause AND CC-BY-SA-3.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ISC AND MPL-2.0
Group:          Amusements/Games/Strategy/Real Time
URL:            https://play0ad.com/
Source:         https://releases.wildfiregames.com/%{name}-%{version}-unix-build.tar.xz
Source1:        premake-disable-rpath.patch
Source100:      0ad-rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-curses
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gloox)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libsodium) >= 1.0.13
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires:       0ad-data = %{version}
BuildRequires:  m4
%if %{with nvtt} && %{with system_nvtt}
BuildRequires:  nvidia-texture-tools >= 2.1
%endif
%if %{with system_mozjs}
#FIXME: Depends on source/scriptinterface/ScriptTypes.h
BuildRequires:  pkgconfig(mozjs-115)
%else
BuildRequires:  cargo
BuildRequires:  rust
%endif
ExcludeArch:    s390x

%description
0 A.D. (pronounced "zero ey-dee") is a real-time strategy (RTS) game
of ancient warfare. It is a historically-based war/economy game that
allows players to relive or rewrite the history of Western
civilizations, focusing on the years between 500 B.C. and 500 A.D.
The project contains 3D graphics, detailed artwork, sound, and a
flexible game engine.

%prep
%setup -q -n %{name}-%{version}
cp %SOURCE1 libraries/source/premake-core/patches/
sed -i -e 's_# patch_# patch\npatch -d "premake-core-${PV}" -p1 <patches/premake-disable-rpath.patch_' libraries/source/premake-core/build.sh

%build
%if 0%{?force_gcc_version}
export CXX="g++-%{force_gcc_version}"
%endif
export CFLAGS="%{optflags}"
# bundled Collada uses CCFLAGS
export CCFLAGS="%{optflags}"
export CPPFLAGS="%{optflags} -fpermissive"
# Copied from macros.cmake.
export LDFLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"
libraries/source/cxxtest-4.4/build.sh
libraries/source/fcollada/build.sh
libraries/source/premake-core/build.sh
build/workspaces/update-workspaces.sh \
    %{?_smp_mflags} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --libdir=%{_libdir}/%{name} \
    --without-tests \
%if %{with nvtt}
%if %{with system_nvtt}
    --with-system-nvtt \
%endif
%else
    --without-nvtt \
%endif
%if %{with system_mozjs}
    --with-system-mozjs
%else
export CARGO_PROFILE_RELEASE_LTO=true
%endif

pushd build/workspaces/gcc
%make_build verbose=1
popd

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
# Install binaries and wrapper
install -Dm 0755 binaries/system/ActorEditor %{buildroot}%{_bindir}/ActorEditor
install -Dm 0755 binaries/system/pyrogenesis %{buildroot}%{_bindir}/pyrogenesis
install -Dm 0755 build/resources/0ad.sh %{buildroot}%{_bindir}/0ad
# Install game libraries
install -m 0644 binaries/system/libCollada.so %{buildroot}%{_libdir}/%{name}/libCollada.so
install -m 0644 binaries/system/libAtlasUI.so %{buildroot}%{_libdir}/%{name}/libAtlasUI.so
# If without system mozjs we need to install the bundled one
%if %{without system_mozjs}
install -m 0644 binaries/system/libmozjs*-ps-release.so %{buildroot}%{_libdir}/%{name}/
%endif
# Install appdata
install -Dm 0644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 build/resources/0ad.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dm 0644 build/resources/0ad.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{name}

%files
%doc README.md
%license LICENSE.md license_gpl-2.0.txt license_lgpl-2.1.txt license_mit.txt
%{_bindir}/0ad
%{_bindir}/pyrogenesis
%{_bindir}/ActorEditor
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}

%changelog
