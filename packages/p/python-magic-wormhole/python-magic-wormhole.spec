#
# spec file for package python-magic-wormhole
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


%{?!python_module:%define python_module() %{!?skip_python2:python-%{**}} %{!?skip_python3:python3-%{**}}}
%define modname magic-wormhole
Name:           python-magic-wormhole
Version:        0.11.2
Release:        0
Summary:        Tool for transferring files through a secure channel
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/warner/magic-wormhole
Source:         https://files.pythonhosted.org/packages/source/m/magic-wormhole/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Automat}
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module hkdf}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module magic-wormhole-mailbox-server}
BuildRequires:  %{python_module magic-wormhole-transit-relay}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module spake2 >= 0.8}
BuildRequires:  %{python_module tqdm >= 4.13.0}
BuildRequires:  %{python_module txtorcon >= 0.19.3}
BuildRequires:  fdupes
Requires:       python-Automat
Requires:       python-PyNaCl
Requires:       python-click
Requires:       python-hkdf
Requires:       python-humanize
Requires:       python-magic-wormhole-mailbox-server
Requires:       python-service_identity
Requires:       python-spake2 >= 0.8
Requires:       python-tqdm >= 4.13.0
Requires:       python-txtorcon >= 0.19.3
Suggests:       python-magic-wormhole-transit-relay
Suggests:       python-mock
BuildArch:      noarch
%python_subpackages

%description
This package provides a library and a command-line tool named wormhole,
which makes it possible to get arbitrary-sized files and directories from
one computer to another. The two endpoints are identified by using identical
"wormhole codes": in general, the sending machine generates and displays
the code, which must then be typed into the receiving machine.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone %{buildroot}%{_bindir}/wormhole

%check
%pytest src/wormhole/test

%files %{python_files}
%license LICENSE
%doc NEWS.md README.md
%{_bindir}/wormhole-%{python_bin_suffix}
%python3_only %{_bindir}/wormhole
%{python_sitelib}/*

%changelog
