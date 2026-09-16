#
# spec file for package photon-node
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


# npm 0.3.4 was published from this commit; the crate itself still says
# 0.3.3 and the repository has no tag for either.
%global commit e4ef13d602828b171e04bf232741d63621dfec14
%global shortcommit e4ef13d6
# The wasm-bindgen crate compiled into the module and the wasm-bindgen CLI
# that writes the JavaScript glue must be the same version. The lockfile
# pins the crate to the distribution's CLI; photon-node_vendor regenerates
# both when either side moves.
%global wasm_bindgen_version 0.2.100
Name:           photon-node
Version:        0.3.4
Release:        0
Summary:        Image processing library compiled to WebAssembly for Node.js
License:        Apache-2.0 AND MIT AND BSD-3-Clause
# Legal-Review-Notice: 117 crates go into the wasm module (cargo tree -e normal
# -p photon-rs --target wasm32-unknown-unknown). Apache-2.0 is photon's own
# licence and that of ab_glyph_rasterizer, approx, owned_ttf_parser, perlin2d
# and simba; BSD-3-Clause comes from instant and nalgebra; the rest are MIT or
# dual MIT/Apache-2.0. The unicode-ident Unicode-3.0 crate is a proc-macro
# dependency and is not compiled into the module.
URL:            https://github.com/silvia-odwyer/photon
Source0:        https://github.com/silvia-odwyer/photon/archive/%{commit}.tar.gz#/photon-%{version}+git.%{shortcommit}.tar.gz
Source1:        vendor.tar.zst
Source2:        Cargo.lock
Source3:        photon-node_vendor
BuildRequires:  cargo-packaging
BuildRequires:  nodejs26
BuildRequires:  python3-base
BuildRequires:  rust >= 1.80
BuildRequires:  wasm-bindgen = %{wasm_bindgen_version}
# The wasm32-unknown-unknown standard library ships only on these.
ExclusiveArch:  x86_64 aarch64
BuildArch:      noarch

%description
photon is an image processing library written in Rust. This package
compiles it to WebAssembly with wasm-bindgen's Node.js target and ships
the module together with the generated JavaScript glue, as the
@silvia-odwyer/photon-node npm package does, so that programs compiled
with Bun or Node can resize and transform images without a native addon.

%prep
%autosetup -n photon-%{commit} -p1 -a1
cp %{SOURCE2} Cargo.lock
locked=$(grep -A1 '^name = "wasm-bindgen"$' Cargo.lock | sed -n 's/^version = "\(.*\)"/\1/p')
if [ "$locked" != "%{wasm_bindgen_version}" ]; then
    echo "Cargo.lock pins wasm-bindgen $locked, the spec expects %{wasm_bindgen_version}: run photon-node_vendor" >&2
    exit 1
fi

%build
# Plain cargo: the %%cargo_build macro adds host linker flags that a
# wasm32 link rejects.
cargo build --release --offline --target wasm32-unknown-unknown -p photon-rs
wasm-bindgen --target nodejs --out-dir pkg --out-name photon_rs \
    target/wasm32-unknown-unknown/release/photon_rs.wasm

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm 0644 pkg/photon_rs_bg.wasm pkg/photon_rs.js pkg/photon_rs.d.ts \
    pkg/photon_rs_bg.wasm.d.ts %{buildroot}%{_datadir}/%{name}/

%check
# Decode a generated PNG, resize it and re-encode: exercises the module,
# the glue and the memory transfer in both directions.
python3 - <<'EOF'
import struct, zlib
def chunk(t, d):
    return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
w = h = 8
raw = b''.join(b'\x00' + b''.join(bytes([x * 30 % 256, y * 30 % 256, 128, 255]) for x in range(w)) for y in range(h))
open('check.png', 'wb').write(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b''))
EOF
node -e '
const p = require("%{buildroot}%{_datadir}/%{name}/photon_rs.js")
const img = p.PhotonImage.new_from_byteslice(require("fs").readFileSync("check.png"))
const out = p.resize(img, 4, 4, 1)
if (out.get_width() !== 4 || out.get_height() !== 4 || out.get_bytes().length < 40) process.exit(1)
'

%files
%license LICENSE.md
%doc README.md
%{_datadir}/%{name}/

%changelog
