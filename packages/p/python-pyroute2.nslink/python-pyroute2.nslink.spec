#
# spec file for package python-pyroute2.nslink
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pyroute2.nslink
Version:        0.6.13
Release:        0
Summary:        Python Netlink library: the nslink
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://github.com/svinota/pyroute2
Source:         https://files.pythonhosted.org/packages/source/p/pyroute2.nslink/pyroute2.nslink-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pyroute2 is a pure Python netlink library. It requires only Python stdlib, no
3rd party libraries.

This module provides NetNS, NSPopen and RemoteSocket classes.

%prep
%setup -q -n pyroute2.nslink-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE.Apache.v2 LICENSE.GPL.v2
%{python_sitelib}/*

%changelog
