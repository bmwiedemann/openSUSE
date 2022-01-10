#
# spec file for package python-setuptools-rust
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global skip_python2 1
Name:           python-setuptools-rust
Version:        1.0.0
Release:        0
Summary:        Setuptools plugin for Rust extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/PyO3/setuptools-rust
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-rust/setuptools-rust-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module semantic_version >= 2.8.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-semantic_version >= 2.8.2
Requires:       python-tomli
Requires:       python-typing_extensions >= 3.7.4.3
BuildArch:      noarch
%python_subpackages

%description
setuptools-rust is a plugin for setuptools to build Rust Python extensions
implemented with PyO3 or rust-cpython.

Compile and distribute Python extensions written in Rust as easily as if they
were written in C.

%prep
%setup -q -n setuptools-rust-%{version}

%build
%python_build

%install
%python_install

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
