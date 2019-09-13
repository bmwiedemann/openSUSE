#
# spec file for package python-dis3
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
%define         skip_python3 1
Name:           python-dis3
Version:        0.1.3
Release:        0
Summary:        Backport of the "dis" module from Python 3
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/KeyWeeUsr/python-dis3
Source:         https://files.pythonhosted.org/packages/source/d/dis3/dis3-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python 2.7 backport of the "dis" module from Python 3.5+

%prep
%setup -q -n dis3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
