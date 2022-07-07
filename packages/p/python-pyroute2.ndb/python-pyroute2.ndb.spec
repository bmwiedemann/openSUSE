#
# spec file for package python-pyroute2.ndb
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
Name:           python-pyroute2.ndb
Version:        0.6.13
Release:        0
Summary:        Python Netlink library: NDB module
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://github.com/svinota/pyroute2
Source:         https://files.pythonhosted.org/packages/source/p/pyroute2.ndb/pyroute2.ndb-%{version}.tar.gz
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

NDB is a high-level network management module. It provides a transactional DB
with multiple sources, from local RTNL source to netns and remote systems. The
DB provides Python API and HTTP RPC (json and plain text), my run as a
standalone service or may be used as a Python module.

%prep
%setup -q -n pyroute2.ndb-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyroute2-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyroute2-cli

%postun
%python_uninstall_alternative pyroute2-cli

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE.Apache.v2 LICENSE.GPL.v2
%python_alternative %{_bindir}/pyroute2-cli
%{python_sitelib}/*

%changelog
