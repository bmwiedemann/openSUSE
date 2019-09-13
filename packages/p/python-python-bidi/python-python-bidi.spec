#
# spec file for package python-python-bidi
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
Name:           python-python-bidi
Version:        0.4.2
Release:        0
Summary:        BiDi layout algorithm
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/MeirKriheli/python-bidi
Source:         https://files.pythonhosted.org/packages/source/p/python-bidi/python-bidi-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A pure python implementation of the BiDi layout algorithm.

%prep
%setup -q -n python-bidi-%{version}
sed -i -e '/^#!\//, 1d' bidi/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license COPYING COPYING.LESSER
%python3_only %{_bindir}/pybidi
%{python_sitelib}/*

%changelog
