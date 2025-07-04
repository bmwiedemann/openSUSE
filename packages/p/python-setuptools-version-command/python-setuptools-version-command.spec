#
# spec file for package python-setuptools-version-command
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


%define info_version 2.2
Name:           python-setuptools-version-command
Version:        99.9
Release:        0
Summary:        Adds a command to dynamically get the version from the VCS of choice
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/j0057/setuptools-version-command
Source:         https://github.com/j0057/setuptools-version-command/archive/%{version}.tar.gz#/setuptools-version-command-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Adds a command to dynamically get the version from the VCS of choice.

%prep
%setup -q -n setuptools-version-command-%{version}
rm setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/setuptools_version_command.py
%pycache_only %{python_sitelib}/__pycache__/setuptools_version_command*
%{python_sitelib}/setuptools[-_]version[-_]command-%{info_version}*-info

%changelog
