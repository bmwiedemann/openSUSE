#
# spec file for package winboat
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

Name:           winboat
Version:        0.9.0
Release:        0
Summary:        Run Windows applications on Linux with seamless integration
License:        MIT
URL:            https://github.com/TibixDev/winboat
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.obsinfo
Source2:        vendor.tar.zstd
Source3:        %{name}.rpmlintrc
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Patch0:         use-application-resource-path.patch
Patch1:         guest-server-build-metadata.patch
%include        %{_sourcedir}/node_modules.spec.inc
BuildRequires:  desktop-file-utils
BuildRequires:  esbuild
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  nodejs-electron-devel
BuildRequires:  python3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  zip
BuildRequires:  zstd
Requires:       ((docker and docker-compose) or (podman and podman-compose))
Requires:       freerdp >= 3
Requires:       nodejs-electron%{_isa}
Requires:       util-linux
Recommends:     psmisc
Recommends:     usbutils
ExclusiveArch:  x86_64

%description
WinBoat is an Electron application for running Windows applications on Linux.
It creates and manages a Windows virtual machine in a Docker or Podman
container and uses FreeRDP RemoteApp support to display Windows applications
alongside native Linux applications. It also provides shared-folder and USB
integration and access to the complete Windows desktop.

%prep
%autosetup -p1

tar -xf %{SOURCE2} -C guest_server

cp %{SOURCE10} package-lock.json
# The source service turns Electron's Git-pinned node-gyp fork into an
# npm-shaped tarball. Make npm request that tarball from the local registry.
node_gyp_git="git+https://github.com/electron/node-gyp.git#06b29aafb7708acef8b3669835c8a7857ebc92d2"
node_gyp_tgz="https://registry.npmjs.org/@electron/node-gyp/-/node-gyp-10.2.0-electron.1.tgz"
sed -i \
  -e "s|\"resolved\": \"${node_gyp_git}\"|\"resolved\": \"${node_gyp_tgz}\"|" \
  -e "s|\"${node_gyp_git}\"|\"10.2.0-electron.1\"|g" \
  package-lock.json
npm pkg set 'overrides.@electron/node-gyp=10.2.0-electron.1'
local-npm-registry %{_sourcedir} install --include=dev --legacy-peer-deps --ignore-scripts

%build
export CFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export CXXFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export LDFLAGS="%{?build_ldflags}"
export MAKEFLAGS="%{_smp_mflags}"
export ELECTRON_SKIP_BINARY_DOWNLOAD=1
export ESBUILD_BINARY_PATH=%{_bindir}/esbuild
export GOFLAGS=-mod=vendor
export PATH="$PWD/node_modules/.bin:$PATH"

%electron_rebuild

export COMMIT_HASH="$(sed -n 's/^commit: //p' %{SOURCE1} | cut -c1-7)"
export BUILD_TIMESTAMP="$(date -u -d "@${SOURCE_DATE_EPOCH:-0}" '+%%Y-%%m-%%dT%%H:%%M:%%S')"
npm run build-guest-server
# The vendor tree is a build input, not part of the Windows guest payload.
zip -qd guest_server/winboat_guest_server.zip 'vendor/*'
rm -rf guest_server/vendor
node scripts/build.ts
npm prune --omit=dev --ignore-scripts --offline --no-audit

%install
install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_libdir}/%{name}/app
cp -a build/main build/renderer node_modules package.json \
  %{buildroot}%{_libdir}/%{name}/app/
cp -a data guest_server %{buildroot}%{_libdir}/%{name}/

# Remove the foreign prebuilt binaries shipped by the two native modules.
# Keep only their Linux x86-64 glibc binaries.
rm -rf \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/darwin-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/darwin-x64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/freebsd-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/freebsd-x64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/linux-arm \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/linux-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/win32-x64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/android-arm \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/android-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/darwin-x64+arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/linux-arm \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/linux-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/linux-ia32 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/win32-arm64 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/win32-ia32 \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/win32-x64
rm \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/argon2/prebuilds/linux-x64/argon2.musl.node \
  %{buildroot}%{_libdir}/%{name}/app/node_modules/usb/prebuilds/linux-x64/node.napi.musl.node

install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/sh
exec electron %{_libdir}/winboat/app "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

install -Dpm 0644 icons/winboat_logo.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Name=WinBoat
Comment=Run Windows applications with seamless integration
Exec=winboat %%U
Icon=winboat
Terminal=false
Type=Application
Categories=Utility;Emulator;
StartupWMClass=WinBoat
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# npm ships one copy of the @types/node license with an executable bit. Make
# license permissions consistent so fdupes can consolidate all copies.
find %{buildroot}%{_libdir}/%{name}/app/node_modules \
  -type f -name LICENSE -exec chmod 0644 {} +
%fdupes -s %{buildroot}%{_libdir}/%{name}

%check
%electron_check_native

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/app
%{_libdir}/%{name}/app/main/
%{_libdir}/%{name}/app/renderer/
%{_libdir}/%{name}/app/node_modules/
%{_libdir}/%{name}/app/package.json
%{_libdir}/%{name}/data/
%{_libdir}/%{name}/guest_server/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
