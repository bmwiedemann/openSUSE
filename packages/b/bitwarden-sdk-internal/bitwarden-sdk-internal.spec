#
# spec file for package bitwarden-sdk-internal
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


Name:           bitwarden-sdk-internal
Version:        0.2.0~main.311
%global toolchain clang
# Remove requires on type_fest
%global __requires_exclude ^npm(.*)

Release:        0
Summary:        Bitwarden WASM module
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND GPL-3.0-only AND MIT AND (MIT OR Unlicense) AND Unicode-3.0
Group:          System/Libraries
Url:            https://github.com/bitwarden/sdk-internal
# Created by create-tarball.sh
Source0:        sdk-internal-0.2.0-main.311.tar.zst
Patch0:         remove-nonfree.patch

#Is applied before vendor step as it adds additional dependencies.
Source3000:     wasm-bindgen-cli.patch

Source9999:     create-tarball.sh

BuildArch:      noarch
%if 0%{?fedora}
BuildRequires:  rust-srpm-macros
BuildRequires:  rust-std-static-wasm32-unknown-unknown
BuildRequires:  cargo
%else
BuildRequires:  cargo-packaging >= 1.2.0+3
BuildRequires:  cargo-auditable
%endif

BuildRequires: binaryen
BuildRequires: jq
BuildRequires: nodejs-packaging
%if 0%{?fedora}
BuildRequires: nodejs
%endif

%description
WebAssembly module used by the Bitwarden desktop application.

%package -n nodejs-bitwarden-sdk-internal
Summary:        Bitwarden WASM module — development files
# Apache-2.0 or MIT: glue code from wasm-bindgen
# CC0-1.0 or MIT: type-fest
# GPL-3.0-only: Bitwarden first-party code
License:        (Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT) AND GPL-3.0-only
Group:          Development/Languages/NodeJS
Requires:       bitwarden-sdk-internal = %{version}

%description -n nodejs-bitwarden-sdk-internal
WebAssembly module used by Bitwarden — NodeJS bindings and TypeScript headers
This package does not provide a stable API and is only intended for building the Bitwarden desktop application.


%prep
%autosetup -p1 -n sdk-internal

# https://blogs.gnome.org/mcatanzaro/2020/05/18/patching-vendored-rust-dependencies/
for i in \
aes-gcm \
chacha20poly1305 \
pkcs5 \
walrus \
slab \
; do
pushd vendor/$i
jq -cj '.files={}' .cargo-checksum.json >tmp && mv tmp .cargo-checksum.json && popd
done

%build
export MAKEFLAGS="%{_smp_mflags}"


#CFLAGS aren't used currently as of 0.2.0~main.198 but the below are the ones that should be used with if upstream ever adds C code to the wasm:


#remove arch-specific options
export CFLAGS="$(echo "-flto=auto -fvisibility=hidden %{optflags} "|sed 's/ -m\S*//g')"
#remove fedora spec which does not work on clang
export CFLAGS="$(echo "$CFLAGS"|sed 's/ --config \S*//g')"
#does not work with wasm and is useless anyway
export CFLAGS="$(echo "$CFLAGS"|sed 's/ -ffat-lto-objects\S*//g')"
#error: option 'cf-protection=return' cannot be specified on this target
export CFLAGS="$(echo "$CFLAGS"|sed 's/ -fcf-protection\S*//g')"
#debuginfo does not really work with wasm, but -g options have different meaning
export CFLAGS="$(echo "$CFLAGS"|sed 's/ -g\S*//g') -g0 "

#This may be a noarch package, but we still care about the target “hardware”
#The reason is that the compiler (LLVM) and VM (chromium/V8) are unrelated projects, and clang/rustc by default targets an ancient VM version.
#Enable instruction sets that our actual target (Chromium 134 atm) supports.
#See https://webassembly.org/features/ (note: for Electron only the Chromium version is relevant, not the Node version)
#“atomics” is special, it's not really a CPU flag as much as a threading model flag. We don't use threads here.
HWFLAGS='-mbulk-memory -mexception-handling -mextended-const -mmultimemory -mmultivalue -mmutable-globals -mnontrapping-fptoint -mreference-types -msign-ext -mtail-call'
# HWFLAGS="$HWFLAGS -mrelaxed-simd -msimd128" not supported on all hardware, see https://source.chromium.org/chromium/chromium/src/+/main:v8/src/wasm/function-body-decoder-impl.h;l=373
export CFLAGS="$CFLAGS $HWFLAGS"

export CXXFLAGS="$CFLAGS"
export LDFLAGS="%{?build_ldflags} $HWFLAGS -s -g0 -Wl,-O2 -Wl,--lto-O2 -Wl,--gc-sections"
export LDFLAGS="$(echo "$LDFLAGS"|sed 's/ --config \S*//g')"
export LDFLAGS="$(echo "$LDFLAGS"| sed 's/ -Wl,--as-needed//')"
export LDFLAGS="$(echo "$LDFLAGS"| sed 's/ -Wl,--build-id=\S*//')"
export LDFLAGS="$(echo "$LDFLAGS"|sed 's/ -ffat-lto-objects\S*//g')"


#extra verbose. Only use for debugging linker problems
#export LDFLAGS="$LDFLAGS -Wl,--print-gc-sections -Wl,-M -Wl,--verbose"


export RUSTFLAGS="%{build_rustflags} -Ctarget-feature=+bulk-memory,+exception-handling,+extended-const,+multimemory,+multivalue,+mutable-globals,+nontrapping-fptoint,+reference-types,+sign-ext,+tail-call --verbose -Cdebuginfo=none -Cstrip=symbols -Clink-arg=-s -Clink-arg=--gc-sections"
export RUSTC_LOG='rustc_codegen_ssa::back::link=info'
export CARGO_TERM_VERBOSE=true
# https://github.com/Firstyear/cargo-packaging/pull/10
export CARGO_INCREMENTAL=0
%if 0%{?suse_version}
export auditable='auditable -vv'
%endif

#see .cargo/config.toml
export RUSTFLAGS="$RUSTFLAGS --cfg getrandom_backend=\"wasm_js\""
#extra verbose. Only use for debugging linker problems
#export RUSTFLAGS="$RUSTFLAGS -Clink-arg=-M -Clink-arg=--print-gc-sections -Clink-arg=--verbose"

export RUSTFLAGS="$(echo " $RUSTFLAGS"|sed 's/ -Clink-arg=-Wl,-z,relro,-z,now //g')"
export RUST_BACKTRACE=full

# /usr/bin/wasm-opt: error while loading shared libraries: libbinaryen.so: cannot open shared object file: No such file or directory
%if 0%{?suse_version} < 1550
export LD_LIBRARY_PATH=%{_libdir}/binaryen
%endif

cargo -vv $auditable build -p bitwarden-wasm-internal  --target wasm32-unknown-unknown --release


RUSTFLAGS="%{build_rustflags}" cargo run -p wasm-bindgen-cli-runner -- bundler crates/bitwarden-wasm-internal/npm ./target/wasm32-unknown-unknown/release/bitwarden_wasm_internal.wasm


pushd crates/bitwarden-wasm-internal/npm
#The wasm had pruned exports via binary witchcraft therefore it should now be opted again to remove unused code
wasm-opt -O2 --strip \
--enable-bulk-memory \
--enable-exception-handling \
--enable-extended-const \
--enable-multimemory \
--enable-multivalue \
--enable-mutable-globals \
--enable-nontrapping-float-to-int \
--enable-reference-types \
--enable-sign-ext \
--enable-tail-call \
bitwarden_wasm_internal_bg.wasm -o tmp.wasm
mv -v tmp.wasm bitwarden_wasm_internal_bg.wasm

#Work around wasm-bindgen bug adding semicolons causing error TS1036: Statements are not allowed in ambient contexts
#Upstream uses prettier but adding it would make the build process much messier, so just fix it manually
sed -i 's[};$[}[' bitwarden_wasm_internal.d.ts


%install
install -pvDm 0644 crates/bitwarden-wasm-internal/npm/bitwarden_wasm_internal_bg.wasm %{buildroot}%{_datadir}/bitwarden/bitwarden_wasm_internal_bg.wasm
mkdir -pv %{buildroot}%{nodejs_sitelib}/@bitwarden
cp -alrvT crates/bitwarden-wasm-internal/npm %{buildroot}%{nodejs_sitelib}/@bitwarden/sdk-internal
ln -srvf %{buildroot}{%{_datadir}/bitwarden,%{nodejs_sitelib}/@bitwarden/sdk-internal}/bitwarden_wasm_internal_bg.wasm
rm -v %{buildroot}%{nodejs_sitelib}/@bitwarden/sdk-internal/{package-lock.json,.gitignore,node_modules/.package-lock.json}



%files
%defattr(-,root,root)
%license LICENSE LICENSE_GPL.txt
%dir %{_datadir}/bitwarden
%{_datadir}/bitwarden/bitwarden_wasm_internal_bg.wasm

%files -n nodejs-bitwarden-sdk-internal
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/@bitwarden

%changelog