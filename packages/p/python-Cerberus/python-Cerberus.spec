#
# spec file for package python-Cerberus
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-Cerberus
Version:        1.3.2
Release:        0
Summary:        Extensible schema and data validation tool for Python dictionaries
License:        ISC
Group:          Development/Languages/Python
URL:            http://github.com/nicolaiarocci/cerberus
Source:         https://files.pythonhosted.org/packages/source/C/Cerberus/Cerberus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module pytest-runner}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Cerberus provides type checking and other base functionality out of the box and
is designed to be non-blocking and extensible, allowing for custom
validation.

%prep
%setup -q -n Cerberus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand rm -rf _build*/ build/
$python setup.py test
}

%files %{python_files}
%doc README.rst UPGRADING.rst AUTHORS
%license LICENSE
%{python_sitelib}/*

%changelog
