#
# spec file for package HeroicGamesLauncher
#
# Copyright (c) 2026 SUSE LLC
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

%ifarch x86_64
%global bin_subdir x64
%global arch_flag --x64
%global bin_subdir_opposite arm64
%endif
%ifarch aarch64
%global bin_subdir arm64
%global arch_flag --arm64
%global bin_subdir_opposite x64
%endif

Name:           heroic-games-launcher
Version:        2.22.0
Release:        0
Summary:        Native Games launcher for GOG, Epic and Amazon
License:        GPL-3.0-only
URL:            https://heroicgameslauncher.com/
Source:         %{name}-%{version}.tar.gz
Source1:        pnpm-offline-store.tar.gz
Source2:        heroic-games-launcher.rpmlintrc
Source3:        get-sources.sh
Source4:        extract-zip-cve-2026-56876.patch
BuildRequires:  comet
BuildRequires:  c++_compiler
BuildRequires:  esbuild
BuildRequires:  fdupes
BuildRequires:  heroic-epic-integration
BuildRequires:  heroic-gogdl
BuildRequires:  jq
BuildRequires:  legendary
BuildRequires:  nile
BuildRequires:  nodejs-electron
BuildRequires:  nodejs-electron-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SPIRV-Tools) >= 2026.2
BuildRequires:  pnpm
BuildRequires:  protobuf-devel
BuildRequires:  vulkan-devel
BuildRequires:  vulkan-helper
Recommends:     gamemode%{?_isa}
Recommends:     libvkd3d%{?_isa}
Recommends:     mangohud%{?_isa}
Recommends:     wine-staging%{?_isa}
Recommends:     winetricks%{?_isa}
Requires:       electron
Requires:       ca-certificates
Requires:       legendary
Requires:       heroic-gogdl
Requires:       nile
Requires:       comet
Requires:       heroic-epic-integration
Requires:       vulkan-helper
ExclusiveArch:  x86_64 aarch64
Provides:       heroic-games-launcher = %{version}
Obsoletes:      heroic-games-launcher < %{version}
Conflicts:      heroic-games-launcher-bin
Supplements:    (heroic-games-launcher and selinux-policy-targeted)
Supplements:    (heroic-games-launcher and selinux-policy-targeted-gaming)

%description
Game launcher and manager for GOG, Epic Games, and Amazon

%prep
%autosetup -n %{name}-%{version} -a1

sed -i -e "s/Exec=heroic-run /Exec=heroic /" flatpak/com.heroicgameslauncher.hgl.desktop

%build
# Remove precompiled binaries to build from source
rm public/bin/%{bin_subdir}/linux/vulkan-helper
rm -rf $HOME/.local/share/pnpm

# FORCE ELECTRON-VITE TO USE THE SYSTEM'S ESBUILD
export ESBUILD_BINARY_PATH=%{_bindir}/esbuild

# Build Heroic Games Launcher
export HOME=%{_builddir}/%{name}-%{version}
export CI=true
export npm_config_nodedir="/usr/include/electron"
export ELECTRON_BUILDER_DISABLE_DOWNLOAD=true
export ELECTRON_MIRROR="file://"

# PNPM OFFLINE HARD MODE
export COREPACK_ENABLE=0
export COREPACK_ENABLE_STRICT=0
export COREPACK_HOME=/dev/null
export PNPM_DISABLE_SELF_UPDATE_CHECK=1
export PNPM_IGNORE_NODE_VERSION=1
export PNPM_STORE_DIR=$PWD/.pnpm-store

export pnpm_config_minimum_release_age=0
export pnpm_config_trust_lockfile=true

export PATH=$PWD/node_modules/.bin:/usr/bin

pnpm config set store-dir .pnpm-store
export PNPM_STORE_DIR=.pnpm-store
pnpm install --offline --store-dir .pnpm-store --frozen-lockfile --ignore-scripts --strict-peer-dependencies=false
# Patch to fix CVE-2026-56876
patch -p1 -d node_modules/.pnpm/extract-zip@2.0.1/node_modules/extract-zip/ < %{SOURCE4}
# CVE-2026-54673: electron-updater (builder-util-runtime) Credential Leak
for file in $(find node_modules/.pnpm -type f -path "*/out/httpExecutor.js" 2>/dev/null); do
    sed -i 's/delete options.headers.authorization/for(let k of Object.keys(options.headers)){let kl=k.toLowerCase();if(kl==="authorization"||kl==="private-token")delete options.headers[k]}/g' "$file"
    sed -i 's/delete options.headers\["authorization"\]/for(let k of Object.keys(options.headers)){let kl=k.toLowerCase();if(kl==="authorization"||kl==="private-token")delete options.headers[k]}/g' "$file"
done

# CVE-2026-54672: app-builder-lib AppRun.sh LD_LIBRARY_PATH Hijack
for file in $(find node_modules/.pnpm -type f -path "*/app-builder-lib/templates/linux/AppRun.sh" 2>/dev/null); do
    sed -i 's/export LD_LIBRARY_PATH="${APPDIR}\/usr\/lib:${LD_LIBRARY_PATH}"/export LD_LIBRARY_PATH="${APPDIR}\/usr\/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"/g' "$file"
done
pnpm dist:linux %{arch_flag} --dir

%ifarch aarch64
mv dist/linux-arm64-unpacked dist/linux-unpacked
%endif
mkdir -p dist/linux-unpacked/resources/app.asar.unpacked/build
cp build/{icon.icns,icon.png,icon-light.png,icon-dark.png,mac-icon.icns,win_icon.ico} dist/linux-unpacked/resources/app.asar.unpacked/build

%install
install -d %{buildroot}%{_libdir}/Heroic %{buildroot}%{_bindir} %{buildroot}%{_datadir}/{applications,pixmaps,metainfo}
install -d %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux
install -d %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/win32

ln -sf %{_bindir}/legendary %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux/legendary
ln -sf %{_bindir}/gogdl %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux/gogdl
ln -sf %{_bindir}/nile %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux/nile
ln -sf %{_bindir}/comet %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux/comet
ln -sf %{_bindir}/vulkan-helper %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/linux/vulkan-helper
ln -sf %{_libexecdir}/heroic/EpicGamesLauncher.exe %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/win32/EpicGamesLauncher.exe
ln -sf %{_libexecdir}/heroic/GalaxyCommunication.exe %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir}/win32/GalaxyCommunication.exe

cp -a dist/linux-unpacked/. %{buildroot}%{_libdir}/Heroic/
ln -sf %{_libdir}/Heroic/heroic %{buildroot}%{_bindir}/heroic
install -m 644 flatpak/com.heroicgameslauncher.hgl.png %{buildroot}%{_datadir}/pixmaps/
install -m 644 flatpak/com.heroicgameslauncher.hgl.desktop %{buildroot}%{_datadir}/applications/
install -m 644 flatpak/templates/com.heroicgameslauncher.hgl.metainfo.xml.template \
    %{buildroot}%{_datadir}/metainfo/com.heroicgameslauncher.hgl.metainfo.xml

rm -rf %{buildroot}%{_libdir}/Heroic/resources/app/build/bin/%{bin_subdir_opposite}/
rm -rf %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/build/bin/%{bin_subdir_opposite}/
rm -rf %{buildroot}%{_libdir}/Heroic/resources/app.asar.unpacked/node_modules
find %{buildroot}%{_libdir}/Heroic -type f -name "*.node" -exec %{__strip} --strip-unneeded {} \; || true

%fdupes -s %{buildroot}%{_libdir}/Heroic

%check
test -x dist/linux-unpacked/heroic

%files
%license COPYING
%doc README.md
%{_bindir}/heroic
%{_libdir}/Heroic/
%{_datadir}/pixmaps/com.heroicgameslauncher.hgl.png
%{_datadir}/applications/com.heroicgameslauncher.hgl.desktop
%{_datadir}/metainfo/com.heroicgameslauncher.hgl.metainfo.xml

%changelog
