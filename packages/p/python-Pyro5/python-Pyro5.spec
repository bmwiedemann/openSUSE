#
# spec file for package python-Pyro5
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


Name:           python-Pyro5
Version:        5.14
Release:        0
Summary:        Distributed object middleware for Python (RPC)
License:        MIT
URL:            https://github.com/irmen/Pyro5
Source:         https://files.pythonhosted.org/packages/source/P/Pyro5/Pyro5-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#irmen/Pyro5#76
Patch0:         add-network-marker.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-serpent >= 1.41
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     ca-certificates
Recommends:     python-cloudpickle >= 0.4.0
Recommends:     python-dill >= 0.2.6
Recommends:     python-msgpack-python >= 0.5.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  sqlite3
BuildRequires:  %{python_module cloudpickle >= 0.4.0}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module dill >= 0.2.6}
BuildRequires:  %{python_module msgpack-python >= 0.5.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module serpent >= 1.41}
BuildRequires:  ca-certificates
# /SECTION
%python_subpackages

%description
Pyro means PYthon Remote Objects.

It is a library for building applications in which objects can talk
to each other over the network. One can use normal Python method
calls, with almost every possible parameter and return value type,
and Pyro takes care of locating the right object on the right system
to execute the method. It also provides a set of features that enable
building distributed applications. Pyro is a pure Python library and
runs on many different platforms and Python versions.

%prep
%autosetup -p1 -n Pyro5-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyro5-check-config
%python_clone -a %{buildroot}%{_bindir}/pyro5-echoserver
%python_clone -a %{buildroot}%{_bindir}/pyro5-httpgateway
%python_clone -a %{buildroot}%{_bindir}/pyro5-ns
%python_clone -a %{buildroot}%{_bindir}/pyro5-nsc

%check
%pytest -m "not network"

%post
%{python_install_alternative pyro5-check-config pyro5-echoserver pyro5-httpgateway pyro5-ns pyro5-nsc}

%postun
%python_uninstall_alternative pyro5-check-config

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/pyro5-check-config
%python_alternative %{_bindir}/pyro5-echoserver
%python_alternative %{_bindir}/pyro5-httpgateway
%python_alternative %{_bindir}/pyro5-ns
%python_alternative %{_bindir}/pyro5-nsc
%{python_sitelib}/Pyro5
%{python_sitelib}/Pyro5-%{version}*-info

%changelog
