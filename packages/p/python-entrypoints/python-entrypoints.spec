#
# spec file for package python-entrypoints
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


%{?sle15_python_module_pythons}
Name:           python-entrypoints
Version:        0.4
Release:        0
Summary:        Discover and load entry points from installed packages
License:        MIT
URL:            https://github.com/takluyver/entrypoints
Source:         https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-configparser >= 3.5
%endif
%ifpython2
Requires:       python-configparser >= 3.5
%endif
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
%setup -q -n entrypoints-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/entrypoints.py*
%pycache_only %{python_sitelib}/__pycache__/entrypoints*.py*
%{python_sitelib}/entrypoints-%{version}.dist-info

%changelog
