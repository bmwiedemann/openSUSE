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


Name:       bitwarden
Version:    2023.2.0
Release:    0
Summary:    A secure and free password manager for all of your devices
Group:      Productivity/Security
License:    GPL-3.0-only and MIT and (Apache-2.0 or MIT)
URL:        https://github.com/bitwarden/clients

#x86 electron requires SSE2
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags") -march=pentium4 -mtune=generic}
%{expand:%%global build_rustflags %(echo "%build_rustflags") -C target-cpu=pentium4 -Z tune-cpu=generic}
%endif

%define version_suffix desktop

# created by create-tarball.sh
Source0:   bitwarden-%{version}.tar.zst

Source2:   bitwarden.sh
Source3:   bitwarden.desktop

Source4:   vendor.tar.zst
Source5:   cargo_config

Source99:  create-tarball.sh

#this one is already applied in tarball
Source100: remove-unnecessary-deps.patch

#openSUSE-specific patches
Patch1:    fix-desktop-file.patch
Patch3:    do-not-install-font-privately.patch
Patch4:    desktop_native-rust-arch.patch
Patch5:    use-node-argon2.patch
Patch6:    argon2-binary-path.patch
Patch7:    bug-reporting-url.patch


#patches to use system libs
Patch1000: system-libargon2.patch

#patches to fix upstream hostility (DRM etc.)
Patch4000: remove-esbuild-version-check.patch

#tools we use explicitly
%if 0%{?fedora_version}
%define _ttfontsdir %{_datadir}/fonts/truetype
%endif
BuildRequires: npm
BuildRequires: cargo
BuildRequires: rust-packaging
BuildRequires: fdupes
BuildRequires: fontpackages-devel
BuildRequires: hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires: nodejs-packaging
%endif
BuildRequires: nodejs-electron-devel
BuildRequires: pkgconfig(libargon2)
BuildRequires: sed
BuildRequires: zstd
#Tools used by npm
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsecret-1)

Requires: (google-opensans-fonts or open-sans-fonts)
Requires: nodejs-electron%{_isa}

%global __requires_exclude ^npm(.*)|^nodejs(.*)

%description
Bitwarden is a free and open-source password management service that stores sensitive information such as website credentials in an encrypted vault.  Bitwarden offers a cloud-hosted service as well as the ability to deploy the solution on-premises. This package provides the GUI client.

%prep
%autosetup -n bitwarden -p1


# Remove unused postinstall script (electron-rebuild)
sed -i '/"postinstall":/d' apps/desktop/package.json

#Remove bundled open sans
cp -v /dev/null libs/angular/src/scss/webfonts.css
rm -rvf libs/angular/src/scss/webfonts




#Do not install font privately

mv -v libs/angular/src/scss/bwicons/fonts/bwi-font.woff %{_builddir}
rm -rvf libs/angular/src/scss/bwicons/fonts


mkdir %{_builddir}/cargo


#Rust config
cd apps/desktop/desktop_native
mkdir -pv .cargo
cp -pv %SOURCE5 .cargo/config
tar --zstd -xf %SOURCE4

# Make `node` and `npm` binaries refer to Electron
%if 0%{?suse_version}
NODEJS_DEFAULT_VER=$(echo %nodejs_version|sed 's/\..*//')
%else
NODEJS_DEFAULT_VER=
%endif


# Electron has a little known feature that make it work like a nodejs binary.
# We make use of it since the system node may be too bleeding-edge
# and to avoid building the same modules twice.
# Not all scripts work when run under electron,
# but importantly npm/yarn and GYP do.
mkdir %{_builddir}/path



cp -v /dev/stdin  %{_builddir}/path/node << EOF
#!/bin/sh
ELECTRON_RUN_AS_NODE=1 exec %{_libdir}/electron/electron "\$@"
EOF

# HACK: This will refer to /usr/bin/npm17 on openSUSE, /usr/bin/npm on Fedora which are Node scripts
cp -v /dev/stdin  %{_builddir}/path/npm << EOF
#!/bin/sh
exec node %{_bindir}/npm${NODEJS_DEFAULT_VER} "\$@"
EOF

cp -v /dev/stdin  %{_builddir}/path/npx << EOF
#!/bin/sh
exec node %{_bindir}/npx${NODEJS_DEFAULT_VER} "\$@"
EOF


chmod +x %{_builddir}/path/*



%build
export PATH="%{_builddir}/cargo:$PATH"
%ifarch %ix86
export RUSTC_BOOTSTRAP=1
%endif
export RUSTC_LOG='rustc_codegen_ssa::back::link=info'
export RUSTFLAGS="%{build_rustflags} --verbose"
export CARGO_TERM_VERBOSE=true

export ELECTRON_SKIP_BINARY_DOWNLOAD=1

#esbuild is not actually used, it is only declared as a dependency of some webpack plugin
export ESBUILD_BINARY_PATH=/bin/true


export CFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export CXXFLAGS="%{optflags} -fpic -fno-semantic-interposition -fvisibility=hidden"
export LDFLAGS="%{?build_ldflags}"





PATH="%{_builddir}/path:$PATH" npm rebuild --verbose --foreground-scripts --nodedir=%{_includedir}/electron

cd apps/desktop
pushd desktop_native
cargo -vv build --release
popd

npm run build
npm run clean:dist

#copy this manually instead of using electron-builder. there's few enough dependencies.
cd build
mkdir -pv node_modules/@bitwarden/desktop-native
cp -plv ../desktop_native/{package.json,index.js} -t node_modules/@bitwarden/desktop-native
cp -plvT ../desktop_native/target/release/*.so node_modules/@bitwarden/desktop-native/desktop_native.node
rm -v ../../../node_modules/argon2/build-tmp-napi-v3/node_gyp_bins/python3
cp -plvr ../../../node_modules/argon2 -t node_modules/
cp -plvr '../../../node_modules/@phc' -t node_modules/


%install
cd %{_builddir}/bitwarden/apps/desktop
mkdir -pv %{buildroot}%{_libdir}
cp -plr build %{buildroot}%{_libdir}/%{name}
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

# Remove empty directories
find . -type d -empty -print -delete


%if 0%{?suse_version}
%reconfigure_fonts_scriptlets
%endif

%check
# Sanity check that we don't have unresolved symbols, and only call napi_* functions (which are ABI stable, unlike node_* ones)
cd %{buildroot}%{_libdir}/%{name}
find . -name '*.node' -print0 | xargs -0 -t -IXXX sh -c '! ldd -d -r XXX | \
grep    '\''^undefined symbol'\'' | \
grep -v '\''^undefined symbol: napi_'\'' '



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
