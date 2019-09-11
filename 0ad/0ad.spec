#
# spec file for package 0ad
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


# Enable NVTT only on arch supported by nvidia-texture-tools
%ifarch %{ix86} x86_64 ppc
%bcond_without enable_nvtt
%else
%bcond_with enable_nvtt
%endif

Name:           0ad
Version:        0.0.23b
Release:        0
Summary:        A real-time strategy game of ancient warfare
License:        GPL-2.0-or-later AND LGPL-3.0-or-later AND CC-BY-SA-3.0 AND MIT AND ISC AND MPL-2.0 AND BSD-3-Clause
Group:          Amusements/Games/Strategy/Real Time
Url:            https://play0ad.com/
#Source:         http://sourceforge.net/projects/zero-ad/files/releases/%{name}-%{version}-alpha-unix-build.tar.xz
# SF is repeatedly not up to date. Let's use their site
Source:         https://releases.wildfiregames.com/%{name}-%{version}-alpha-unix-build.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  nasm
%if %{with enable_nvtt}
BuildRequires:  nvidia-texture-tools
%endif
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(gloox)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libsodium) >= 1.0.13
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mozjs-38)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires:       0ad-data = %{version}

%description
0 A.D. (pronounced "zero ey-dee") is a real-time strategy (RTS) game
of ancient warfare. It is a historically-based war/economy game that
allows players to relive or rewrite the history of Western
civilizations, focusing on the years between 500 B.C. and 500 A.D.
The project contains 3D graphics, detailed artwork, sound, and a
flexible game engine.

%prep
%setup -q -n %{name}-%{version}-alpha

%build
export CFLAGS="%{optflags}"
# bundled Collada uses CCFLAGS
export CCFLAGS="%{optflags}"
export CPPFLAGS="%{optflags} -fpermissive"
build/workspaces/update-workspaces.sh \
    %{?_smp_mflags} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --libdir=%{_libdir}/%{name} \
%if %{with enable_nvtt}
    --with-system-nvtt \
%else
   --without-nvtt \
%endif
    --with-system-mozjs38 \

pushd build/workspaces/gcc
make verbose=1 %{?_smp_mflags}
popd

%install
install -Dm 0755 binaries/system/ActorEditor %{buildroot}%{_bindir}/ActorEditor
install -Dm 0755 binaries/system/pyrogenesis %{buildroot}%{_bindir}/pyrogenesis
install -Dm 0755 binaries/system/libCollada.so %{buildroot}%{_libdir}/%{name}/libCollada.so
install -Dm 0755 binaries/system/libAtlasUI.so %{buildroot}%{_libdir}/%{name}/libAtlasUI.so

install -Dm 0644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 build/resources/0ad.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dm 0644 build/resources/0ad.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{name}

install -Dm 0755 build/resources/0ad.sh %{buildroot}%{_bindir}/0ad

mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}

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
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}

%changelog
