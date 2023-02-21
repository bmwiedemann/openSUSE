#
# spec file for package python-Pyro4
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


# Do not support pyhon 3.11, and will never support it, it recommends
# to use Pyro5, gh#irmen/Pyro4#246
%define skip_python311 1
%bcond_without python2
Name:           python-Pyro4
Version:        4.82
Release:        0
Summary:        Distributed object middleware for Python (RPC)
License:        MIT
URL:            https://github.com/irmen/Pyro4
Source:         https://files.pythonhosted.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-serpent >= 1.27
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     ca-certificates
Recommends:     python-cloudpickle >= 0.4.0
Recommends:     python-dill >= 0.2.6
Recommends:     python-msgpack-python >= 0.5.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cloudpickle >= 0.4.0}
BuildRequires:  %{python_module dill >= 0.2.6}
BuildRequires:  %{python_module msgpack-python >= 0.5.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module serpent >= 1.27}
BuildRequires:  ca-certificates
%if %{with python2}
BuildRequires:  python-selectors34
%endif
# /SECTION
%ifpython2
Requires:       python-selectors34
%endif
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
%autosetup -p1 -n Pyro4-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyro4-check-config
%python_clone -a %{buildroot}%{_bindir}/pyro4-flameserver
%python_clone -a %{buildroot}%{_bindir}/pyro4-httpgateway
%python_clone -a %{buildroot}%{_bindir}/pyro4-ns
%python_clone -a %{buildroot}%{_bindir}/pyro4-nsc
%python_clone -a %{buildroot}%{_bindir}/pyro4-test-echoserver

%check
# socket tests require at least lo interface thus skip them
skip="testContextAndSock"
skip+=" or testGetIP or testAutoClean"
skip+=" or testBroadcast or testBCstart"
skip+=" or testStartNSfunc or testStartNSfunc"
skip+=" or testResolveWrongHmac"
skip+=" or testResolveAsymmetricHmacUsage"
skip+=" or testResolve"
skip+=" or testPyroname"
skip+=" or testLookupAndRegister"
skip+=" or testBCLookup0000"
skip+=" or testRefuseDottedNames"
skip+=" or testMulti"
skip+=" or testLookupUnixsockParsing"
skip+=" or testLookupInvalidHmac"
skip+=" or testLookupAndRegister"
skip+=" or testDaemonPyroObj"
export PYTHONPATH=${PWD}/tests/PyroTests
%pytest -rs -v -k "not ($skip)"

%post
%{python_install_alternative pyro4-check-config pyro4-flameserver pyro4-httpgateway pyro4-ns pyro4-nsc pyro4-test-echoserver}

%postun
%python_uninstall_alternative pyro4-check-config

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/pyro4-check-config
%python_alternative %{_bindir}/pyro4-flameserver
%python_alternative %{_bindir}/pyro4-httpgateway
%python_alternative %{_bindir}/pyro4-ns
%python_alternative %{_bindir}/pyro4-nsc
%python_alternative %{_bindir}/pyro4-test-echoserver
%{python_sitelib}/Pyro4
%{python_sitelib}/Pyro4-%{version}*-info

%changelog
