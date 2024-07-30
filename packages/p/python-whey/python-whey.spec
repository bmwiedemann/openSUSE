#
# spec file for package python-whey
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
Name:           python-whey%{psuffix}
Version:        0.1.1
Release:        0
Summary:        A simple Python wheel builder for simple projects
License:        MIT
URL:            https://github.com/repo-helper/whey
Source:         https://github.com/repo-helper/whey/archive/refs/tags/v%{version}.tar.gz#/whey-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel >= 0.34.2}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module pyproject-examples}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module re-assert}
BuildRequires:  %{python_module whey = %{version}}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 22.2.0
Requires:       python-click >= 7.1.2
Requires:       python-consolekit >= 1.4.1
Requires:       python-dist-meta >= 0.1.0
Requires:       python-dom-toml >= 2.0.0
Requires:       python-domdf-python-tools >= 2.8.0
Requires:       python-handy-archives >= 0.2.0
Requires:       python-natsort >= 7.1.1
Requires:       python-packaging >= 20.9
Requires:       python-pyproject-parser >= 0.11.0
Requires:       python-shippinglabel >= 0.16.0
Suggests:       python-docutils >= 0.16
Suggests:       python-editables >= 0.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A simple Python wheel builder for simple projects.

%prep
%autosetup -p1 -n whey-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/whey
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if !%{with test}
%post
%python_install_alternative whey

%postun
%python_uninstall_alternative whey
%endif

%check
%if %{with test}
# test_show_builders requires two whey modules that are not packaged
# test_build_success requires that the module is built exactly when the tests are run
%pytest --ignore tests/test_utils.py -k 'not (test_show_builders or test_build_success)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/whey
%{python_sitelib}/whey
%{python_sitelib}/whey-%{version}.dist-info
%endif

%changelog
