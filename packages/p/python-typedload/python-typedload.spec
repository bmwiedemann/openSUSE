#
# spec file for package python-typedload
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-typedload
Version:        2.19
Release:        0
Summary:        Load and dump data from json-like format into typed data structures
License:        GPL-3.0-only
URL:            https://ltworf.github.io/typedload/
# The Github release archive contains both setup.py and the tests. PyPI lacks tests, Github repo lacks generated setup.py
Source0:        https://github.com/ltworf/typedload/releases/download/%{version}/typedload_%{version}.orig.tar.gz
Source1:        https://github.com/ltworf/typedload/releases/download/%{version}/typedload_%{version}.orig.tar.gz.asc
# https://github.com/ltworf/typedload/raw/master/debian/upstream/signing-key.asc
Source2:        python-typedload.keyring
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Load and dump data from json-like format into typed data structures

%prep
%setup -q -n typedload

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/__main__.py has a version specific test collection and calls unittest.main()
%python_exec -B -m tests

%files %{python_files}
%{python_sitelib}/typedload
%{python_sitelib}/typedload-%{version}*-info

%changelog
