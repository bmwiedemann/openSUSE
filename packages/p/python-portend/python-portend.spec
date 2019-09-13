#
# spec file for package python-portend
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
Name:           python-portend
Version:        2.5
Release:        0
Summary:        TCP port monitoring utilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/portend
Source:         https://files.pythonhosted.org/packages/source/p/portend/portend-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tempora}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tempora
BuildArch:      noarch
%python_subpackages

%description
Use portend to monitor TCP ports for bound or unbound states.

The portend may also be executed directly. If the function succeeds, it
returns nothing and exits with a status of 0. If it fails, it prints a
message and exits with a status of 1. For example::

Portend also exposes a ``find_available_local_port`` for identifying
a suitable port for binding locally::

%prep
%setup -q -n portend-%{version}
# do not require cov/xdist/etc
sed -i -e '/addopts/d' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest test_portend.py

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
