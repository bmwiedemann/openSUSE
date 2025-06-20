#
# spec file for package python-autopep8
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-autopep8
Version:        2.3.2
Release:        0
Summary:        Automatic generated to pep8 checked code
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hhatto/autopep8
Source:         https://files.pythonhosted.org/packages/source/a/autopep8/autopep8-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycodestyle >= 2.12}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-pycodestyle >= 2.12.0
BuildArch:      noarch
%if %{python_version_nodots} < 311
Requires:       python-tomli
%endif
%python_subpackages

%description
Autopep8 is automatic generated to pep8 checked code.
This is old style tool, wrapped pep8 via subprocess module.

%prep
%autosetup -p1 -n autopep8-%{version}
sed -i '1s/^#!.*//' autopep8.py # Remove she-bang line

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/autopep8

%check
export LANG="en_US.UTF-8"
%pytest -k 'not test_e701_with_escaped_newline_and_spaces'

%pre
# Since /usr/bin/autopep8 became ghosted to be used with update-alternatives, we have to get rid
# of the old binary resulting from the non-update-alternativies-ified package:
[ -h %{_bindir}/autopep8 ] || rm -f %{_bindir}/autopep8
# now, let's convert the old update-alternatives link to libalternatives
%python_libalternatives_reset_alternative autopep8

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/autopep8
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/autopep8.py*
%{python_sitelib}/autopep8-%{version}.dist-info

%changelog
