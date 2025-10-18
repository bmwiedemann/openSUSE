# spec file for package bitwarden
#
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021–2023 Bruno Pitrus
# Based on the Arch Linux PKGBUILD (c) 2017 prozum
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

#not running the tests on OBS — extremely flaky
%bcond_with test_rust

%global sdk_internal_req_version 0.2.0~main.311


Name:       bitwarden
Version:    2025.10.0
Release:    0
Summary:    A secure and free password manager for all of your devices
Group:      Productivity/Security
License:    (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND GPL-3.0-only AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0
URL:        https://github.com/bitwarden/clients

#x86 electron requires SSE2
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags") -march=pentium4 -mtune=generic}
%{expand:%%global build_rustflags %(echo "%build_rustflags") -C target-cpu=pentium4 -Z tune-cpu=generic}
%endif

%define version_suffix desktop

# created by OBS service
Source0:   bitwarden-%{version}.tar

# created by prepare-vendor.sh
Source1:   vendor.tar.zst

Source2:   bitwarden.sh
Source3:   bitwarden.desktop

Source99:  prepare-vendor.sh



#openSUSE-specific patches
Patch0:    remove-unnecessary-deps.patch
Patch1:    fix-desktop-file.patch
Patch3:    do-not-install-font-privately.patch
Patch4:    desktop_native-rust-arch.patch
Patch7:    bug-reporting-url.patch
Patch8:    no-sourcemaps.patch
Patch9:    main-getPath-exe.patch
Patch10:   native-messaging.main-fix-path.patch


#patches to use system libs
Patch1001: system-roboto-font.patch

#patches to fix interaction with other software
Patch2000: cxxbridge-cmd.patch

#patches to fix upstream hostility (DRM etc.)
Patch4000: remove-esbuild-version-check.patch

#tools we use explicitly
%if 0%{?fedora_version}
%define _ttfontsdir %{_datadir}/fonts/truetype
BuildRequires: glibc-all-langpacks
%endif
%if 0%{?fedora} >= 37
BuildRequires:  nodejs-npm
%else
BuildRequires:  npm
%endif
BuildRequires: cargo
%if 0%{?fedora}
BuildRequires:  rust-srpm-macros
%else
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  cargo-auditable
%endif
BuildRequires: fdupes
BuildRequires: fontpackages-devel
BuildRequires: hicolor-icon-theme
BuildRequires: jq
BuildRequires: nodejs-packaging
BuildRequires: nodejs-bitwarden-sdk-internal = %sdk_internal_req_version
BuildRequires: nodejs-electron-devel
BuildRequires: sed
BuildRequires: sqlite-devel
BuildRequires: zstd
#Tools used by npm
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(wayland-protocols)

#For tests
%if %{with test_rust}
BuildRequires:  gnome-keyring
%if 0%{?fedora}
BuildRequires:  dbus-daemon
%else
BuildRequires:  dbus-1-daemon
%endif
%endif

Requires: bitwarden-sdk-internal = %sdk_internal_req_version
Requires: nodejs-electron%{_isa}
Requires: google-roboto-fonts

%global __requires_exclude ^npm(.*)|^nodejs(.*)
%global __provides_exclude ^npm(.*)|^nodejs(.*)|^lib.*\\.so.*$



%description
Bitwarden is a free and open-source password management service that stores sensitive information such as website credentials in an encrypted vault.  Bitwarden offers a cloud-hosted service as well as the ability to deploy the solution on-premises. This package provides the GUI client.

%prep
%autosetup -p1 -a1

#Sanity check that we've declared the correct version in header
test $(jq -cj '.version' node_modules/@bitwarden/sdk-internal/package.json | sed 's/-/~/g') = %sdk_internal_req_version


rm -rvf node_modules/@bitwarden/sdk-internal
cp -arvLT {%{nodejs_sitelib},node_modules}/@bitwarden/sdk-internal

#remove bundled font
rm -v libs/components/src/webfonts/roboto.woff2

#fix exe path
sed -i 's[XXXLIBDIRXXX[%{_libdir}[g' apps/desktop/src/main/native-messaging.main.ts


# Remove unused postinstall script (electron-rebuild)
sed -i '/"postinstall":/d' apps/desktop/package.json





#Do not install font privately

mv -v libs/angular/src/scss/bwicons/fonts/bwi-font.woff %{_builddir}
rm -rvf libs/angular/src/scss/bwicons/fonts


#Rust config
cd apps/desktop/desktop_native
rm -rf vendor/wayland-protocols/protocols
ln -svT /usr/share/wayland-protocols vendor/wayland-protocols/protocols
# https://blogs.gnome.org/mcatanzaro/2020/05/18/patching-vendored-rust-dependencies/
for i in \
wayland-protocols \
libloading \
pkcs5 \
aes-gcm \
libsqlite3-sys \
vcpkg \
; do
pushd vendor/$i
jq -cj '.files={}' .cargo-checksum.json >tmp && mv tmp .cargo-checksum.json && popd
done



%build
%ifarch %ix86
export RUSTC_BOOTSTRAP=1
%endif
export RUSTC_LOG='rustc_codegen_ssa::back::link=info'
export RUSTFLAGS="%{build_rustflags} --verbose -Cstrip=none"
export CARGO_TERM_VERBOSE=true

export ELECTRON_SKIP_BINARY_DOWNLOAD=1

#esbuild is not actually used, it is only declared as a dependency of some webpack plugin
export ESBUILD_BINARY_PATH=/bin/true


export CFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export CXXFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export LDFLAGS="%{?build_ldflags}"
export MAKEFLAGS="%{_smp_mflags}"
export CRATE_CC_NO_DEFAULTS=1
export CARGO_PROFILE_RELEASE_DEBUG=2
export CC_ENABLE_DEBUG_OUTPUT=1
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1

%if 0%{?suse_version}
auditable='auditable -vv'
%endif




%electron_rebuild

cd apps/desktop
pushd desktop_native
cargo -vv $auditable rustc --offline --release --package desktop_napi --lib --crate-type cdylib
#RUSTFLAGS="$RUSTFLAGS -Crelocation-model=pie"
cargo -vv $auditable rustc --offline --release --package desktop_proxy --bin desktop_proxy -- -Crelocation-model=pie
popd

npm run build
npm run clean:dist

#copy this manually instead of using electron-builder. there's few enough dependencies.
cd build
mkdir -pv node_modules/@bitwarden/desktop-napi
cp -plv ../desktop_native/napi/{package.json,index.js} -t node_modules/@bitwarden/desktop-napi
cp -plvT ../desktop_native/target/release/*.so node_modules/@bitwarden/desktop-napi/desktop_napi.node
cp -plv -t . ../desktop_native/target/release/desktop_proxy


%install
cd %{_builddir}/bitwarden-%{version}/apps/desktop
mkdir -pv %{buildroot}%{_libdir}
cp -ar build %{buildroot}%{_libdir}/%{name}
for i in %{buildroot}%{_libdir}/%{name}/*.wasm; do
cmp %{_datadir}/bitwarden/*.wasm "$i"
ln -svf %{_datadir}/bitwarden/*.wasm "$i"
done
for i in 16 32 64 128 256 512 1024
do
install -pvDm644 resources/icons/${i}x${i}.png "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png"
done
install -pvDm755 "%{_sourcedir}/%{name}.sh" "%{buildroot}%{_bindir}/bitwarden-desktop"
sed -i "s,XXXLIBDIRXXX,%{_libdir},g" "%{buildroot}%{_bindir}/bitwarden-desktop"
install -pvDm644 "%{_sourcedir}"/%{name}.desktop -t "%{buildroot}%{_datadir}"/applications
install -pvDm644 %{_builddir}/bwi-font.woff -t%{buildroot}%{_ttfontsdir}

%fdupes %{buildroot}%{_prefix}

#Remove development garbage
cd %{buildroot}%{_libdir}/%{name}
#JS debug symbols (unusable)
find -name '*.map' -type f -print -delete
#Source code
find -name '*.c' -type f -print -delete
find -name '*.cpp' -type f -print -delete
find -name '*.h' -type f -print -delete
find -name '*.gyp' -type f -print -delete
find -name '*.gypi' -type f -print -delete
find -name '*.ts' -type f -print -delete
find -name '*.cts' -type f -print -delete
find -name build-tmp-napi-v3  -print0 |xargs -r0 -- rm -rvf --
find -name src -print0 |xargs -r0 -- rm -rvf --
find -name Makefile -type f -print -delete
find -name 'Pipfile*' -type f -print -delete
find -name '*.patch' -type f -print -delete
#Temporary build files
find -name '.deps' -print0 |xargs -r0 -- rm -rvf --
find -name 'obj.target' -print0 |xargs -r0 -- rm -rvf --
find -name 'vendor' -print0 |xargs -r0 -- rm -rvf --
find -name '*package-lock.json' -type f -print -delete
find -name '*.mk' -type f -print -delete
find -name '*.Makefile' -type f -print -delete

#Documentation
find -name '*.md' -type f -print -delete
find -name doc -print0 |xargs -r0 -- rm -rvf --
find -name test -print0 |xargs -r0 -- rm -rvf --
#Compile-time-only dependencies
find -name nan -print0 |xargs -r0 -- rm -rvf --
find -name node-addon-api -print0 |xargs -r0 -- rm -rvf --
#Other trash
find -name '*.yml' -type f -print -delete
find -name '.npmignore' -type f -print -delete
find -name '.gitignore' -type f -print -delete

#Fix file mode
find . -type f -exec chmod 644 {} \;
find . -name '*.node' -exec chmod 755 {} \;
chmod 755 desktop_proxy

# Remove empty directories
find . -type d -empty -print -delete


%if 0%{?suse_version}
%reconfigure_fonts_scriptlets
%endif

%check
%electron_check_native

#Rust tests
%if %{with test_rust}
%ifarch %ix86
export RUSTC_BOOTSTRAP=1
%endif
export RUSTC_LOG='rustc_codegen_ssa::back::link=info'
export RUSTFLAGS="%{build_rustflags} --verbose -Cstrip=none"
export CARGO_TERM_VERBOSE=true
export CFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export CXXFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export LDFLAGS="%{?build_ldflags}"
export MAKEFLAGS="%{_smp_mflags}"
export CRATE_CC_NO_DEFAULTS=1
export CARGO_PROFILE_RELEASE_DEBUG=2
export CC_ENABLE_DEBUG_OUTPUT=1
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
%if 0%{?suse_version}
auditable='auditable -vv'
%endif
cd apps/desktop
pushd desktop_native
# see .github/workflows/test.yml
export XDG_CONFIG_HOME=$(mktemp -d)

dbus-run-session sh -c ' echo '' | gnome-keyring-daemon --unlock && echo '' | gnome-keyring-daemon --start && exec cargo -vv '"$auditable"' test --release --no-fail-fast --workspace -- --test-threads=1'
%endif

%files
%defattr(-,root,root)
%{_bindir}/bitwarden-desktop
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/1024x1024
%{_datadir}/icons/hicolor/128x128/apps/bitwarden.png
%{_datadir}/icons/hicolor/16x16/apps/bitwarden.png
%{_datadir}/icons/hicolor/256x256/apps/bitwarden.png
%{_datadir}/icons/hicolor/32x32/apps/bitwarden.png
%{_datadir}/icons/hicolor/512x512/apps/bitwarden.png
%{_datadir}/icons/hicolor/64x64/apps/bitwarden.png
%{_ttfontsdir}/
%license LICENSE.txt
%license LICENSE_GPL.txt

%changelog
