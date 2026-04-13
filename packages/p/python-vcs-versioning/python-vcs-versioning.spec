#
# spec file for package python-vcs-versioning
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if !%{with test}
%{?pythons_for_pypi}
%endif
Name:           python-vcs-versioning%{psuffix}
Version:        1.1.1
Release:        0
Summary:        the blessed package to manage your versions by vcs metadata
License:        MIT
URL:            https://github.com/pypa/setuptools-scm
Source:         https://files.pythonhosted.org/packages/source/v/vcs_versioning/vcs_versioning-%{version}.tar.gz
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 20
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module vcs-versioning >= %{version}}
%endif
%python_subpackages

%description
the blessed package to manage your versions by vcs metadata

%prep
%autosetup -p1 -n vcs_versioning-%{version}

%build
%pyproject_wheel

%if %{with test}
%check
%pytest --ignore testing_vcs/test_file_finders.py --ignore testing_vcs/test_git.py

%else

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vcs-versioning
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative vcs-versioning

%postun
%python_uninstall_alternative vcs-versioning

%files %{python_files}
%license LICENSE.txt
%python_alternative %{_bindir}/vcs-versioning
%{python_sitelib}/vcs_versioning
%{python_sitelib}/vcs_versioning-%{version}.dist-info
%endif

%changelog
