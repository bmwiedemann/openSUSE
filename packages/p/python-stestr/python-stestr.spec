#
# spec file
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
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-stestr%{psuffix}
Version:        4.1.0
Release:        0
Summary:        A parallel Python test runner built around subunit
License:        Apache-2.0
URL:            https://github.com/mtreinish/stestr
Source:         https://files.pythonhosted.org/packages/source/s/stestr/stestr-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10.0
Requires:       python-cliff >= 2.8.0
Requires:       python-dbm
Requires:       python-fixtures >= 3.0.0
Requires:       python-pbr >= 2.0.0
Requires:       python-python-subunit >= 1.4.0
Requires:       python-testtools >= 2.2.0
Requires:       python-tomlkit >= 0.11.6
Requires:       python-voluptuous >= 0.8.9
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module ddt >= 1.0.1}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module stestr = %{version}}
%endif
%if !0%{?_no_weakdeps}
Recommends:     python-SQLAlchemy
Recommends:     python-subunit2sql >= 1.8.0
%endif
%python_subpackages

%description
stestr is parallel Python test runner designed to execute unittest test suites
using multiple processes to split up execution of a test suite. It also will
store a history of all test runs to help in debugging failures and optimizing
the scheduler to improve speed. To accomplish this goal it uses the subunit
protocol to facilitate streaming and storing results from multiple workers.

stestr originally started as a fork of the testrepository project. But, instead
of being an interface for any test runner that used subunit, like testrepository,
stestr concentrated on being a dedicated test runner for python projects. While
stestr was originally forked from testrepository it is not backwards compatible
with testrepository. At a high level the basic concepts of operation are shared
between the two projects but the actual usage is not exactly the same.

%prep
%autosetup -p1 -n stestr-%{version}

%if %{with test}
%check
export LC_ALL="en_US.UTF8"
%pytest stestr/tests -v -k 'not test_empty_with_pretty_out'
%endif

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/stestr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative stestr

%postun
%python_uninstall_alternative stestr

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/stestr
%{python_sitelib}/stestr
%{python_sitelib}/stestr-%{version}.dist-info
%endif

%changelog
