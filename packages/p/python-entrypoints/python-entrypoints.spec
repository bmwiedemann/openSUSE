#
# spec file for package python-entrypoints
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
Name:           python-entrypoints
Version:        0.3
Release:        0
Summary:        Discover and load entry points from installed packages
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/takluyver/entrypoints
Source:         https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  %{python_module devel}
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-configparser
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
pushd tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test_entrypoints.py
}
popd
%endif

%files %{python_files}
%license LICENSE
%{python_sitelib}/entrypoints.py*
%pycache_only %{python_sitelib}/__pycache__/entrypoints*.py*
%{python_sitelib}/entrypoints-%{version}-py*.egg-info

%changelog
