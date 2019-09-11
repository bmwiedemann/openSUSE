#
# spec file for package python-flake8-bugbear
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flake8-bugbear
Version:        19.3.0
Release:        0
Summary:        A plugin for flake8 finding likely bugs and design problems in your program
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/flake8-bugbear
Source:         https://files.pythonhosted.org/packages/source/f/flake8-bugbear/flake8-bugbear-%{version}.tar.gz
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module flake8 >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A plugin for Flake8 finding likely bugs and design problems in your
program.  Contains warnings that don't belong in pyflakes and
pycodestyle.

%prep
%setup -q -n flake8-bugbear-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
