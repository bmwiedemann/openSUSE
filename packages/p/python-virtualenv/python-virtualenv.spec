#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# there is no platformdirs for python2 on any of the target distributions
%define skip_python2 1
Name:           python-virtualenv%{psuffix}
Version:        20.16.7
Release:        0
Summary:        Virtual Python Environment builder
License:        MIT
URL:            http://www.virtualenv.org/
Source:         https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildRequires:  %{python_module distlib >= 0.3.1}
BuildRequires:  %{python_module filelock >= 3.0.0}
BuildRequires:  %{python_module importlib-metadata >= 0.12 if %python-base < 3.8}
BuildRequires:  %{python_module importlib_resources >= 1.0 if %python-base < 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 41.0.0}
BuildRequires:  %{python_module setuptools_scm >= 2}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports.entry_points_selectable >= 1.0.4
Requires:       python-distlib >= 0.3.1
Requires:       python-filelock >= 3.0.0
Requires:       python-platformdirs >= 2
Requires:       python-setuptools
Requires:       python-six >= 1.9.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata >= 0.12
%endif
%if 0%{python_version_nodots} < 37
Requires:       python-importlib_resources >= 1.0
%endif
%ifpython2
Requires:       python-contextlib2 >= 0.6.0
Requires:       python-pathlib2 >= 2.3.3
%endif
%if %{with test}
BuildRequires:  %{python_module backports.entry_points_selectable >= 1.0.4}
BuildRequires:  %{python_module flaky >= 3}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module platformdirs >= 2}
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module pytest-env >= 0.6.2}
BuildRequires:  %{python_module pytest-freezegun >= 0.4.1}
BuildRequires:  %{python_module pytest-mock >= 2.0.0}
BuildRequires:  %{python_module pytest-timeout >= 1.3.4}
BuildRequires:  ca-certificates
%endif
%python_subpackages

%description
virtualenv is a tool to create isolated Python environments.
The basic problem being addressed is one of dependencies and versions, and
indirectly permissions. Imagine you have an application that needs version 1
of LibFoo, but another application requires version 2.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you cant install packages into the global site-packages
directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that
has its own installation directories, that doesnt share libraries with other
virtualenv environments (and optionally doesnt use the globally installed
libraries either).

%prep
%autosetup -p1 -n virtualenv-%{version}

# Dependencies on all those shells are too cumbersome.
rm -r tests/unit/activation

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/virtualenv
%endif

%check
%if %{with test}
export LANG="en_US.UTF8"
export PIP_CERT="%{_sysconfdir}/ssl/ca-bundle.pem"
export PYTHONPATH=$PWD/src
# online tests downloads from pypi
donttest="test_seed_link_via_app_data"
# gh#pypa/virtualenv!2431
donttest+=" or test_py_pyc_missing"
%pytest -k "not ($donttest)"
%endif

%if !%{with test}
%post
%python_install_alternative virtualenv

%postun
%python_uninstall_alternative virtualenv

%files %{python_files}
%license LICENSE
%doc README.md docs/changelog.rst
%{python_sitelib}/virtualenv
%{python_sitelib}/virtualenv-%{version}*-info
%python_alternative %{_bindir}/virtualenv
%endif

%changelog
