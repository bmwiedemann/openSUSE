#
# spec file for package python-entrypoints
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


%{?sle15_python_module_pythons}
Name:           python-entrypoints
Version:        0.4
Release:        0
Summary:        Discover and load entry points from installed packages
License:        MIT
URL:            https://github.com/takluyver/entrypoints
Source:         https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support flit-core >= 4
Patch0:         support-flit-core-4.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Entry points are a way for Python packages to advertise objects with
some common interface. The most common examples are console_scripts
entry points, which define shell commands by identifying a Python
function to run.

Groups of entry points, such as console_scripts, point to objects with
similar interfaces. An application might use a group to find its
plugins, or multiple groups if it has different kinds of plugins.

%prep
%autosetup -p1 -n entrypoints-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/entrypoints.py
%pycache_only %{python_sitelib}/__pycache__/entrypoints*.pyc
%{python_sitelib}/entrypoints-%{version}.dist-info

%changelog
