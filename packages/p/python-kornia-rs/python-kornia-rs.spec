#
# spec file for package python-kornia-rs
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


%{?sle15_python_module_pythons}
Name:           python-kornia-rs
Version:        0.1.14
Release:        0
Summary:        Low-level computer vision library implemented in Rust
# Legal-Review-Notice: cargo tree --offline -p kornia-py -e normal over
# registry.tar.zst (update=true) shows only permissive licences
# (MIT/Apache-2.0/BSD/Zlib/Unlicense/Unicode-3.0/IJG from jpeg-encoder).
# No GPL/LGPL/MPL/EPL/CDDL is linked. Workspace crates inherit Apache-2.0.
License:        Apache-2.0
URL:            https://github.com/kornia/kornia-rs
Source0:        https://files.pythonhosted.org/packages/source/k/kornia_rs/kornia_rs-%{version}.tar.gz
Source1:        registry.tar.zst
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module maturin >= 1.9}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libturbojpeg)
ExclusiveArch:  %{rust_tier1_arches}
%python_subpackages

%description
Python bindings for kornia-rs, a low-level computer vision library
written in Rust. It provides image I/O (JPEG via libjpeg-turbo, PNG,
TIFF, WebP), image processing, AprilTag detection, and 3D vision
helpers used by python-kornia.

%prep
%autosetup -p1 -n kornia_rs-%{version}
rm -rf .cargo
tar xf %{SOURCE1} -C $PWD

%build
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
# turbojpeg-sys defaults to a bundled libjpeg-turbo cmake build; force the
# system copy (pkgconfig(libturbojpeg)).
export TURBOJPEG_SOURCE=pkg-config
export TURBOJPEG_DYNAMIC=1
%pyproject_wheel

%install
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export TURBOJPEG_SOURCE=pkg-config
export TURBOJPEG_DYNAMIC=1
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c "import kornia_rs as k; assert k.__version__ == '%{version}', k.__version__"
# Full suite needs torch, Pillow, OpenCV and the apriltag-imgs submodule.
# Run the self-contained numpy tests shipped in the sdist.
%pytest_arch kornia-py/tests/test_package.py kornia-py/tests/test_color.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/kornia_rs*

%changelog
