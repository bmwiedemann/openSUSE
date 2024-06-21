#
# spec file for package element-desktop
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


Name:           element-desktop
Version:        1.11.69
Release:        0
Summary:        A glossy Matrix collaboration client - desktop
License:        Apache-2.0
URL:            https://github.com/vector-im/element-desktop
Source0:        https://github.com/vector-im/element-desktop/archive/v%{version}.tar.gz#/element-desktop-%{version}.tar.gz
Source2:        vendor.tar.zst
Source3:        io.element.Element.desktop
Source4:        element-desktop.sh
Source5:        prepare.sh
Patch0:         hak-remove-devdependencies.patch
Patch1:         7za-path.patch
Patch2:         cc-link-lib-no-static.patch
Patch3:         remove-fuses.patch
Patch4:         disable-spellchecker.patch
BuildRequires:  element-web = %{version}
BuildRequires:  app-builder
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jq
BuildRequires:  nodejs-electron-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  zstd
%if 0%{?fedora}
BuildRequires:  rust-srpm-macros
%else
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  cargo-auditable
%endif

BuildRequires:  libsecret-devel
BuildRequires:  gcc-c++
Requires:       element-web = %{version}
Requires:       nodejs-electron%{_isa}

#x86 electron requires SSE2
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags") -march=pentium4 -mtune=generic}
%{expand:%%global build_rustflags %(echo "%build_rustflags") -C target-cpu=pentium4 -Z tune-cpu=generic}
%endif


%description
A glossy Matrix collaboration client - desktop

%prep
%setup -q -a2
%autopatch -p1

# https://blogs.gnome.org/mcatanzaro/2020/05/18/patching-vendored-rust-dependencies/
for i in cc libloading libsqlite3-sys openssl-src rustix seshat vcpkg; do
pushd .hak/hakModules/matrix-seshat/vendor/$i
jq -cj '.files={}' .cargo-checksum.json >tmp && mv tmp .cargo-checksum.json && popd
done


jq -cj '.piwik=false | .update_base_url=null' < element.io/release/config.json > tmp && mv -v tmp element.io/release/config.json


%build
export CFLAGS="%{optflags} -fpic -fno-semantic-interposition -fno-fat-lto-objects -fvisibility=hidden"
export CXXFLAGS="%{optflags} -fpic -fno-semantic-interposition -fno-fat-lto-objects -fvisibility=hidden"
export LDFLAGS="%{?build_ldflags}"
export MAKEFLAGS="%{_smp_mflags}"
export ELECTRON_SKIP_BINARY_DOWNLOAD=1
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
export USE_SYSTEM_APP_BUILDER=true
export OPENSSL_NO_VENDOR=1
# The `cc` crate tries to be too clever and passes some default cflags when building sqlcipher.
# Disable these and use only the ones from CFLAGS env. variable
export CRATE_CC_NO_DEFAULTS=1


%ifarch %ix86
export RUSTC_BOOTSTRAP=1
%endif
#I want to actually see the build logs for Cargo. Especially the gcc command line for dependent modules.
export RUSTC_LOG='rustc_codegen_ssa::back::link=info'
export RUSTFLAGS="%{build_rustflags} --verbose -Cstrip=none"
export CARGO_TERM_VERBOSE=true

%electron_rebuild


#We do manually the rough equivalent of `hak build` to inject correct optflags
pushd .hak/hakModules/keytar
%electron_rebuild
popd

pushd .hak/hakModules/matrix-seshat
%if 0%{?suse_version}
auditable='auditable -vv'
%endif
cargo -vv $auditable rustc --offline --release --features=bundled-sqlcipher --lib --crate-type cdylib
ln -Tv target/release/*.so index.node
popd


#Compare definition of `build:universal` in package.json
npm run build:ts
npm run build:res
npx --no-install electron-builder --linux dir --universal -c.electronDist=%{_libdir}/electron -c.asar=false -c.nodeGypRebuild=false -c.npmRebuild=false




%install
#Remove sources an other files that should not be shipped
pushd dist/linux-universal-unpacked/resources/app
rm -rf node_modules/matrix-seshat/{.cargo,false,src,target,test,vendor,Cargo.lock,Cargo.toml}
find -name '*.c' -type f -print -delete
find -name '*.cc' -type f -print -delete
find -name '*.cpp' -type f -print -delete
find -name '*.h' -type f -print -delete
find -name '*.m' -type f -print -delete
find -name '*.map' -type f -print -delete
find -name '*.ts' -type f -print -delete
find -name '*.tsx' -type f -print -delete
find -name '*.gyp' -type f -print -delete
find -name '*.gypi' -type f -print -delete
find -name '*.mk' -type f -print -delete
find -name '*.Makefile' -type f -print -delete
find -name '.eslint*' -type f -print -delete
find -name .editorconfig -type f -print -delete
find -name .nvmrc -type f -print -delete
find -name .nycrc -type f -print -delete
find -name Makefile -type f -print -delete
find -name '.jscs*' -type f -print -delete
find -name obj.target -print0 |xargs -r0 -- rm -rvf --
find -name '*.d' -type f -print -delete

#Documentation
find -name '*.md' -type f -print -delete
find -name '*.markdown' -type f -print -delete
find -name '*.bnf' -type f -print -delete
find -name '*.mli' -type f -print -delete
find -name CHANGES -type f -print -delete
find -name TODO -type f -print -delete
find -name usage.txt -type f -print -delete

# Remove empty directories
find . -type d -empty -print -delete

# fix file mode
find . -type f -exec chmod 0644 {} \;
find . -name '*.node' -exec chmod 0755 {} \;
popd



# Install the app content, replace the webapp with a symlink to the system package
install -vd -m 0755 "%{buildroot}%{_datadir}/element/"
cp -lrv dist/linux-universal-unpacked/resources/* -t "%{buildroot}%{_datadir}/element/"
ln -vs %{_datadir}/webapps/element "%{buildroot}%{_datadir}/element/webapp"

# Install binaries to /usr/lib
install -vd -m 0755 "%{buildroot}%{_prefix}/lib/element/"
install -pvm0755 dist/linux-universal-unpacked/resources/app/node_modules/keytar/build/Release/keytar.node "%{buildroot}%{_prefix}/lib/element/keytar.node"
install -pvm0755 dist/linux-universal-unpacked/resources/app/node_modules/matrix-seshat/index.node "%{buildroot}%{_prefix}/lib/element/matrix-seshat.node"
ln -sfv "%{_prefix}/lib/element/keytar.node" "%{buildroot}%{_datadir}/element/app/node_modules/keytar/build/Release/keytar.node"
ln -sfv "%{_prefix}/lib/element/matrix-seshat.node" "%{buildroot}%{_datadir}/element/app/node_modules/matrix-seshat/index.node"

# Config file
install -vm 0755 -d %{buildroot}%{_sysconfdir}/element
install -pvm 0644 element.io/release/config.json "%{buildroot}%{_sysconfdir}/element/config.json"

install -pvm 0755 -d %{buildroot}%{_sysconfdir}/webapps/element
ln -vs %{_sysconfdir}/element/config.json "%{buildroot}%{_sysconfdir}/webapps/element/config.json"

install -vd -m 0755 "%{buildroot}%{_datadir}/webapps/element/"
ln -vs %{_sysconfdir}/element/config.json "%{buildroot}%{_datadir}/webapps/element/config.json" # moved here from element-web to make symlink check happy

# Required extras
install -vd -m 0755 "%{buildroot}%{_datadir}/applications/"
install -pvm 0644 %{SOURCE3} "%{buildroot}%{_datadir}/applications/io.element.Element.desktop"
install -vd -m 0755 "%{buildroot}%{_bindir}/"
install -pvm 0755 %{SOURCE4} "%{buildroot}%{_bindir}/%{name}"

# Icons
install -vd -m 0755 "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/"
for i in 16 24 48 64 96 128 256 512; do
	install -vd -m 0755 "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/"
	install -pvm 0644 build/icons/${i}x${i}.png "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.element.Element.png"
done

%fdupes %{buildroot}%{_datadir}

%check
%electron_check_native

%files
%license LICENSE
%{_bindir}/%{name}

%dir %{_datadir}/element/
%{_datadir}/element/webapp
%{_datadir}/element/app-update.yml
%dir %{_datadir}/element/app
%{_datadir}/element/app/lib
%{_datadir}/element/app/node_modules
%{_datadir}/element/app/package.json
%dir %{_datadir}/element/img
%{_datadir}/element/img/element.ico
%{_datadir}/element/img/element.png

%{_prefix}/lib/element/
%config(noreplace) %{_sysconfdir}/element/config.json
%{_sysconfdir}/webapps/element/config.json
%{_datadir}/webapps/element/config.json
%dir %{_sysconfdir}/element/
%{_datadir}/applications/io.element.Element.desktop
%{_datadir}/icons/hicolor/*/apps/io.element.Element.png

%changelog
