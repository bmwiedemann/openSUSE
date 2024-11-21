#
# spec file for package python-tomli
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-tomli
Version:        2.1.0
Release:        0
Summary:        A lil' TOML parser
License:        MIT
URL:            https://github.com/hukkin/tomli
# prefer github archive over pypi sdist for pacakged tests
Source:         https://github.com/hukkin/tomli/archive/refs/tags/%{version}.tar.gz#/tomli-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
# Avoid build cycles
# https://flit.readthedocs.io/en/latest/bootstrap.html
#!BuildIgnore:  python3-tomli
#!BuildIgnore:  python36-tomli
#!BuildIgnore:  python38-tomli
#!BuildIgnore:  python39-tomli
#!BuildIgnore:  python310-tomli
#!BuildIgnore:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Tomli is a Python library for parsing TOML

%prep
%autosetup -p1 -n tomli-%{version}

%build
# flit_core requires tomli
export PYTHONPATH=$PWD/src
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/tomli
%{python_sitelib}/tomli-%{version}.dist-info

%changelog
