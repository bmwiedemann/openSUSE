#
# spec file for package python-pyutf8
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyutf8
Version:        0.1.1
Release:        0
Summary:        Extension for dealing with valid and invalid UTF-8 strings
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/etrepum/pyutf8
Source:         https://files.pythonhosted.org/packages/source/p/pyutf8/pyutf8-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Extension for dealing with valid and invalid UTF-8 strings

%prep
%setup -q -n pyutf8-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
