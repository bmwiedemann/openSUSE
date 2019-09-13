#
# spec file for package python-rustcfg
#
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


%global srcname rustcfg

# Python 2 isn't supported...
%global skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rustcfg
Version:        0.0.2
Release:        0
Summary:        Rust cfg expression parser in Python
Group:          Development/Libraries/Python
License:        MIT
URL:            https://pagure.io/fedora-rust/python-rustcfg
Source:         https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
Requires:       python-pyparsing
Recommends:     python-pytest
BuildArch:      noarch
%python_subpackages

%description
This package provides a Python module for parsing Config.toml files.

%prep
%autosetup -n %{srcname}-%{version}

%build
%python_build

%install
%python_install

%check
py.test-%{python3_version} -v

%files %{python_files}
%license LICENSE
%{python3_sitelib}/rustcfg-*.egg-info/
%{python3_sitelib}/rustcfg/

%changelog
