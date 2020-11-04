#
# spec file for package python-deepmerge
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-deepmerge
Version:        0.1.0
Release:        0
License:        MIT
Summary:        A toolset to deeply merge python dictionaries
Url:            http://deepmerge.readthedocs.io/en/latest/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/deepmerge/deepmerge-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/toumorokoshi/deepmerge/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcver}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Python module to deeply merge python dictionaries.

%prep
%setup -q -n deepmerge-%{version}
cp %{S:99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
