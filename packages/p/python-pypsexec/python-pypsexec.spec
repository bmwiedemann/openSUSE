#
# spec file for package python-pypsexec
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
Name:           python-pypsexec
Version:        0.3.0
Release:        0
Summary:        Run commands on a remote Windows host using SMB/RPC
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jborean93/pypsexec
Source:         https://github.com/jborean93/pypsexec/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module smbprotocol}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-smbprotocol
BuildArch:      noarch
%python_subpackages

%description
This library can run commands on a remote Windows host through Python.
This means that it can be run on any host with Python and does not
require any binaries to be present or a specific OS. It uses SMB/RPC to
executable commands in a similar fashion to the popular PsExec tool.

%prep
%setup -q -n pypsexec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/*

%changelog
