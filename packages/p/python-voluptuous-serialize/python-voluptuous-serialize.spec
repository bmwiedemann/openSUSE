#
# spec file for package python-voluptuous-serialize
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
%define skip_python2 1
Name:           python-voluptuous-serialize
Version:        2.2.0
Release:        0
Summary:        Python module to convert voluptuous schemas to dictionaries
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://github.com/balloob/voluptuous-serialize
Source:         https://files.pythonhosted.org/packages/source/v/voluptuous-serialize/voluptuous-serialize-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/balloob/voluptuous-serialize/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module voluptuous}
# /SECTION
BuildRequires:  fdupes
Requires:       python-voluptuous
BuildArch:      noarch

%python_subpackages

%description
A Python module to convert voluptuous schemas to dictionaries.

%prep
%setup -q -n voluptuous-serialize-%{version}
cp %{S:99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
