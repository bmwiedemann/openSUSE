#
# spec file for package python-pyjsparser
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyjsparser
Version:        2.7.1
Release:        0
Summary:        Javascript parser based on esprimajs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PiotrDabkowski/pyjsparser
Source:         https://files.pythonhosted.org/packages/source/p/pyjsparser/pyjsparser-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/PiotrDabkowski/pyjsparser/master/LICENSE
Patch0:         fix_version.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A JavaScript parser - a manual translation of esprima.js to Python.
It supports the whole of ECMAScript 5.1 and parts of ECMAScript 6.

%prep
%setup -q -n pyjsparser-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
