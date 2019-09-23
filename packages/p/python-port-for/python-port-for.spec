#
# spec file for package python-port-for
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-port-for
Version:        0.4
Release:        0
License:        MIT
Summary:        Utility that helps with local TCP ports managment
Url:            https://github.com/kmike/port-for/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/port_for/port-for-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch

%python_subpackages

%description
port-for is a command-line utility and a python library that
helps with local TCP ports management.

It can find an unused TCP localhost port and remember the association::

    $ sudo port-for foo
    37987

This can be useful when you are installing a stack of software
with multiple parts needing port numbers.

There are several rules port-for is trying to follow to find and
return a new unused port:

1) Port must be unused: port-for checks this by trying to connect
   to the port and to bind to it.

2) Port must be IANA unassigned and otherwise not well-known:
   this is acheived by maintaining unassigned ports list
   (parsed from IANA and Wikipedia).

3) Port shouldn't be inside ephemeral port range.
   This is important because ports from ephemeral port range can
   be assigned temporary by OS (e.g. by machine's IP stack) and
   this may prevent service restart in some circumstances.
   ``port-for`` doesn't return ports from ephemeral port ranges
   configured at the current machine.

4) Other heuristics are also applied: ``port-for`` tries to return
   a port from larger port ranges; it also doesn't return ports that are
   too close to well-known ports.

%prep
%setup -q -n port-for-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -f %{buildroot}%{$python_sitelib}/port_for/tests.py* %{buildroot}%{$python_sitelib}/port_for/__pycache__/tests.*
%python_clone -a %{buildroot}%{_bindir}/port-for
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest --doctest-modules port_for/utils.py port_for/tests.py

%post
%python_install_alternative port-for

%postun
%python_uninstall_alternative port-for

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/port-for


%changelog
