#
# spec file for package python-unicode-segmentation-rs
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


Name:           python-unicode-segmentation-rs
Version:        0.2.1
Release:        0
Summary:        Unicode segmentation and width for Python using Rust
License:        MIT AND CC0-1.0
URL:            https://weblate.org/
Source:         https://files.pythonhosted.org/packages/source/u/unicode-segmentation-rs/unicode_segmentation_rs-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module maturin >= 1.10.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  zstd
%python_subpackages

%description
Python bindings for the Rust [unicode-segmentation](https://docs.rs/unicode-segmentation/) and [unicode-width](https://docs.rs/unicode-width/) crates, providing Unicode text segmentation and width calculation according to Unicode standards.

%prep
%autosetup -a1 -p1 -n unicode_segmentation_rs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%{python_sitearch}/unicode_segmentation_rs
%{python_sitearch}/unicode_segmentation_rs-%{version}.dist-info

%changelog
