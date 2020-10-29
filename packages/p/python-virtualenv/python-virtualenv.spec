#
# spec file for package python-virtualenv
#
# Copyright (c) 2020 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-virtualenv%{psuffix}
Version:        20.0.33
Release:        0
Summary:        Virtual Python Environment builder
License:        MIT
URL:            http://www.virtualenv.org/
Source:         https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 41.0.0}
BuildRequires:  %{python_module setuptools_scm >= 2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.3
Requires:       python-distlib >= 0.3.1
Requires:       python-filelock >= 3.0.0
Requires:       python-importlib-metadata >= 0.12
Requires:       python-importlib_resources >= 1.0
Requires:       python-setuptools
Requires:       python-six >= 1.9.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-contextlib2 >= 0.6.0
Requires:       python-pathlib2 >= 2.3.3
%endif
%if %{with test}
BuildRequires:  %{python_module coverage >= 4.5.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module flaky >= 3}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module pytest-env >= 0.6.2}
BuildRequires:  %{python_module pytest-freezegun >= 0.4.1}
BuildRequires:  %{python_module pytest-mock >= 2.0.0}
BuildRequires:  %{python_module pytest-timeout >= 1.3.4}
BuildRequires:  %{python_module virtualenv >= %{version}}
BuildRequires:  fish
BuildRequires:  python3-xonsh >= 0.9.13
BuildRequires:  tcsh
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
%setup -q -n virtualenv-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/virtualenv
%endif

%check
%if %{with test}
export LANG="en_US.UTF8"
# test_seed_link_via_app_data - online tests downloads from pypi
%pytest -k 'not test_seed_link_via_app_data'
%endif

%if !%{with test}
%post
%python_install_alternative virtualenv

%postun
%python_uninstall_alternative virtualenv

%files %{python_files}
%license LICENSE
%doc README.md docs/changelog.rst
%{python_sitelib}/virtualenv*
%python_alternative %{_bindir}/virtualenv
%endif

%changelog
