#
# spec file for package 0ad
#
# Copyright (c) 2023 SUSE LLC
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
# We can use the system mozjs on Tumbleweed and Leap 15.4.
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without system_mozjs
%else
%bcond_with system_mozjs
%endif
# Use provided library
%bcond_without system_nvtt
Name:           0ad
Version:        0.0.26
Release:        0
Summary:        A real-time strategy game of ancient warfare
License:        BSD-3-Clause AND CC-BY-SA-3.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ISC AND MPL-2.0
Group:          Amusements/Games/Strategy/Real Time
URL:            https://play0ad.com/
Source:         https://releases.wildfiregames.com/%{name}-%{version}-alpha-unix-build.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         avoid_duplicate_global_symbol_from_asm.patch
# PATCH-FIX-OPENSUSE -- Disable the mozjs version check
Patch1:         no-version-check.patch
# PATCH-FIX-OPENSUSE -- Use the newer variant of this function (related to mozjs78 upgrade)
Patch2:         PrepareZoneForGC.patch
# PATCH-FIX-OPENSUSE -- Skip automatic addition of an RPATH.
Patch3:         premake-no-automatic-rpath.patch
# PATCH-FIX-UPSTREAM -- Fix build with GCC 13
Patch4:         fix-gcc13-build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-nostl-devel
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
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires:       0ad-data = %{version}
%if %{with nvtt} && %{with system_nvtt}
BuildRequires:  nvidia-texture-tools >= 2.1
%endif
%if %{with system_mozjs}
#FIXME: Depends on source/scriptinterface/ScriptTypes.h
# This is "fixed" by disabling the version check.
BuildRequires:  pkgconfig(mozjs-78) >= 78.7
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
%setup -q -n %{name}-%{version}-alpha
%patch0 -p1
%patch3 -p1
%patch4 -p1
%if %{with system_mozjs}
%patch1 -p1
%patch2 -p1
%endif

%build
export CFLAGS="%{optflags}"
# bundled Collada uses CCFLAGS
export CCFLAGS="%{optflags}"
export CPPFLAGS="%{optflags} -fpermissive"
# Copied from macros.cmake.
export LDFLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"
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
%doc README.txt
%license LICENSE.txt license_gpl-2.0.txt license_lgpl-2.1.txt license_mit.txt
%{_bindir}/0ad
%{_bindir}/pyrogenesis
%{_bindir}/ActorEditor
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}

%changelog
