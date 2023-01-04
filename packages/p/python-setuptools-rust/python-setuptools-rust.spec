#
# spec file for package python-setuptools-rust
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


Name:           python-setuptools-rust
Version:        1.5.2
Release:        0
Summary:        Setuptools plugin for Rust extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/PyO3/setuptools-rust
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-rust/setuptools-rust-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module semantic_version >= 2.8.2}
BuildRequires:  %{python_module setuptools >= 62.4}
BuildRequires:  %{python_module setuptools_scm >= 6.3.2}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust
Requires:       cargo
Requires:       python-semantic_version >= 2.8.2
Requires:       python-setuptools >= 62.4
Requires:       python-typing_extensions >= 3.7.4.3
Requires:       rust
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
setuptools-rust is a plugin for setuptools to build Rust Python extensions
implemented with PyO3 or rust-cpython.

Compile and distribute Python extensions written in Rust as easily as if they
were written in C.

%prep
%setup -q -n setuptools-rust-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# network / crates.io access
%pytest tests/ -k "not test_get_lib_name_namespace_package"
pushd examples/hello-world
%{python_expand # See noxfile.py
# hello-world is the only example which does not need extra rust packages (via cargo_vendor)
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m pip install --no-build-isolation --target=$PWD/build/exampleinstall/ --no-deps --no-index .
$PWD/build/exampleinstall/bin/hello-world
}
popd

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/setuptools_rust-%{version}*-info
%{python_sitelib}/setuptools_rust

%changelog
