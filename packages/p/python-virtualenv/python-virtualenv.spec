#
# spec file for package python-virtualenv
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-virtualenv%{psuffix}
Version:        20.26.3
Release:        0
Summary:        Virtual Python Environment builder
License:        MIT
URL:            https://virtualenv.pypa.io/
# SourceRepository: https://github.com/pypa/virtualenv
Source:         https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
%if !%{with test}
# Don't install the build requirements during testing, see setuptools_scm comment below
BuildRequires:  %{python_module hatch-vcs >= 0.3}
BuildRequires:  %{python_module hatchling >= 1.17.1}
BuildRequires:  fdupes
%else
# Conflict with setuptools_scm giving a warning, https://github.com/pypa/virtualenv/issues/2668
BuildConflicts: %{python_module setuptools_scm}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module flaky >= 3.7}
BuildRequires:  %{python_module packaging >= 23.1}
BuildRequires:  %{python_module pytest >= 7.4}
BuildRequires:  %{python_module pytest-env >= 0.8.2}
BuildRequires:  %{python_module pytest-mock >= 3.11.1}
BuildRequires:  %{python_module pytest-timeout >= 2.1}
BuildRequires:  %{python_module setuptools >= 68}
BuildRequires:  %{python_module time-machine >= 2.10}
BuildRequires:  %{python_module virtualenv = %{version}}
%endif
Requires:       (python-distlib >= 0.3.7 with python-distlib < 1)
Requires:       (python-filelock >= 3.12.2 with python-filelock < 4)
Requires:       (python-platformdirs >= 3.9.1 with python-platformdirs < 5)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata >= 6.6
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

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/virtualenv
%endif

%if %{with test}
%check
# online tests downloads from pypi
donttest="test_seed_link_via_app_data"
# fails on python312 because it cannot find setuptools and wheel https://virtualenv.pypa.io/en/latest/changelog.html#features-20-23-0
python312_extratest=" or test_can_build_c_extensions"
%pytest -k "not ($donttest ${$python_extratest})"
# test the special case with the bundles (for all flavors)
export VIRTUALENV_SETUPTOOLS=bundle
export VIRTUALENV_WHEEL=bundle
%pytest -k "${python312_extratest:4}"
%endif

%post
%python_install_alternative virtualenv

%postun
%python_uninstall_alternative virtualenv

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/virtualenv
%{python_sitelib}/virtualenv-%{version}*-info
%python_alternative %{_bindir}/virtualenv
%endif

%changelog
