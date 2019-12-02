#
# spec file for package python-javaproperties
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-javaproperties
Version:        0.5.2
Release:        0
License:        MIT
Summary:        Read & write Java properties files
Url:            https://github.com/jwodder/javaproperties
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/javaproperties/javaproperties-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  %{python_module six < 2.0}
BuildRequires:  fdupes
Requires:       python-six < 2.0
Requires:       python-six >= 1.4
BuildArch:      noarch

%python_subpackages

%description
Read & write Java .properties files

%prep
%setup -q -n javaproperties-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
