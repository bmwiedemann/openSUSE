#
# spec file for package python-python-binary-memcached
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-binary-memcached
Version:        0.31.2
Release:        0
Summary:        Access memcached via its binary protocol with SASL auth support
License:        MIT
URL:            https://github.com/jaysonsantos/python-binary-memcached
Source:         https://files.pythonhosted.org/packages/source/p/python-binary-memcached/python-binary-memcached-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  memcached
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export MEMCACHED_HOST=localhost
memcached &
pid=$!
%pytest -k 'not (SocketMemcachedTests or BinaryMemcachedTests or MemcachedTests)'
kill $pid

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/bmemcached
%{python_sitelib}/python_binary_memcached-%{version}.dist-info

%changelog
