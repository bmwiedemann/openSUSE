#
# spec file for package python-configparser
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


# inline the 38 with the Version (based on which python the config module is from)
%if %{python3_version_nodots} >= 38
%define skip_python3 1
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-configparser%{psuffix}
Version:        4.0.2
Release:        0
Summary:        Backport of the enhanced config parser introduced in Python 3.x
License:        MIT
Group:          Development/Languages/Python
URL:            https://docs.python.org/3/library/configparser.html
Source:         https://files.pythonhosted.org/packages/source/c/configparser/configparser-%{version}.tar.gz
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module configparser >= %{version}}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  python-devel
BuildRequires:  python-pathlib2
BuildRequires:  python3-testsuite
%endif
%python_subpackages

%description
The ancient ConfigParser module available in the standard library 2.x has
seen a major update in Python 3.x. This is a backport of those changes so
that they can be used directly in Python 2.7.

%prep
%setup -q -n configparser-%{version}
rm pytest.ini

%build
export LANG=en_US.UTF-8
%python_build

%install
%if !%{with test}
export LANG=en_US.UTF-8
%python_install
%python_expand rm -f %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__*
%python_expand %fdupes %{buildroot}%{$python_sitelib}/
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/configparser.py*
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/backports/configparser/
%{python_sitelib}/configparser-%{version}-py*.egg-info
%endif

%changelog
