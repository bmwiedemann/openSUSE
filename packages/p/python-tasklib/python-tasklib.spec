#
# spec file for package python-tasklib
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


Name:           python-tasklib
Version:        2.5.1
Release:        0
Summary:        Python Task Warrior library
License:        BSD-3-Clause
URL:            https://github.com/robgolding/tasklib
Source:         https://files.pythonhosted.org/packages/source/t/tasklib/tasklib-%{version}.tar.gz
Patch0:         disable-windows-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  taskwarrior >= 2.4.0
Requires:       python-pytz
Requires:       python-tzlocal
Requires:       taskwarrior >= 2.4.0
BuildArch:      noarch
%python_subpackages

%description
Tasklib is a Python library for interacting with taskwarrior
databases, using a queryset API similar to that of Django's ORM.

%prep
%autosetup -p1 -n tasklib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%python_exec -m unittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tasklib
%{python_sitelib}/tasklib-%{version}.dist-info

%changelog
