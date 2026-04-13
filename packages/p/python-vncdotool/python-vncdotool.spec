#
# spec file for package python-vncdotool
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-vncdotool
Version:        1.3.0
Release:        0
Summary:        Command line VNC client
License:        MIT
URL:            https://github.com/sibson/vncdotool
Source:         https://files.pythonhosted.org/packages/source/v/vncdotool/vncdotool-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Pillow >= 10.0.1
Requires:       python-Twisted >= 22.10.0
Requires:       python-cryptography >= 41.0.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 10.0.1}
BuildRequires:  %{python_module Twisted >= 22.10.0}
BuildRequires:  %{python_module cryptography >= 41.0.7}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Command line VNC client.

%prep
%setup -q -n vncdotool-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vncdo
%python_clone -a %{buildroot}%{_bindir}/vncdotool
%python_clone -a %{buildroot}%{_bindir}/vnclog
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative vncdo
%python_libalternatives_reset_alternative vncdotool
%python_libalternatives_reset_alternative vnclog

%check
rm -rf tests/functional
%pytest -k 'not functional'

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/vncdo
%python_alternative %{_bindir}/vncdotool
%python_alternative %{_bindir}/vnclog
%{python_sitelib}/vncdotool
%{python_sitelib}/vncdotool-%{version}*-info

%changelog
