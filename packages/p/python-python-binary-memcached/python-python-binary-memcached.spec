#
# spec file for package python-python-binary-memcached
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-python-binary-memcached
Version:        0.31.2
Release:        0
Summary:        Access memcached via its binary protocol with SASL auth support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaysonsantos/python-binary-memcached
Source:         https://files.pythonhosted.org/packages/source/p/python-binary-memcached/python-binary-memcached-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-uhashring
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module uhashring}
# /SECTION
%python_subpackages

%description
A pure python module to access memcached via its binary protocol with SASL auth support

%prep
%setup -q -n python-binary-memcached-%{version}

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
