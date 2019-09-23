#
# spec file for package python-h11
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
Name:           python-h11
Version:        0.9.0
Release:        0
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/11
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-hyper/h11
Source:         https://files.pythonhosted.org/packages/source/h/h11/h11-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest < 5}
# /SECTION
%python_subpackages

%description
This is a little HTTP/1.1 library written from scratch in Python,
heavily inspired by hyper-h2 <https://hyper-h2.readthedocs.io>

%prep
%setup -q -n h11-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
