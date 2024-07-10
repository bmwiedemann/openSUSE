#
# spec file for package python-platformdirs
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-platformdirs
Version:        4.2.2
Release:        0
Summary:        Module for determining appropriate platform-specific dirs
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source:         https://files.pythonhosted.org/packages/source/p/platformdirs/platformdirs-%{version}.tar.gz
BuildRequires:  %{python_module appdirs == 1.4.4}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling >= 0.22.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 7.4}
BuildRequires:  %{python_module pytest-cov >= 4.1}
BuildRequires:  %{python_module pytest-mock >= 3.11.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".

%prep
%autosetup -p1 -n platformdirs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/platformdirs
%{python_sitelib}/platformdirs-%{version}.dist-info

%changelog
