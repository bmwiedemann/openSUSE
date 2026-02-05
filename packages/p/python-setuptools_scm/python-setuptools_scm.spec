#
# spec file for package python-setuptools_scm
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
%bcond_without libalternatives
%{?pythons_for_pypi}
%{?sle15_python_module_pythons}
Name:           python-setuptools_scm%{psuffix}
Version:        9.2.2
Release:        0
Summary:        Python setuptools handler for SCM tags
License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-scm/setuptools_scm-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-packaging >= 20.0
Requires:       python-setuptools
BuildArch:      noarch
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1
%endif
%if %{with test}
# Testing requirements
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm = %{version}}
BuildRequires:  %{python_module typing-extensions if %python-base < 3.11}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  git-core
BuildRequires:  mercurial
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     git-core
%endif
%python_subpackages

%description
The setuptools_scm package handles managing one's Python package versions
in SCM metadata. It also handles file finders for the supperted SCMs.

%prep
%autosetup -p1 -n setuptools_scm-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/setuptools-scm
%endif

%if %{with test}
%check
# pip download needs network
donttest="test_pip_download or test_xmlsec_download_regression"
%pytest -rsEf -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%python_alternative %{_bindir}/setuptools-scm
%{python_sitelib}/setuptools_scm
%{python_sitelib}/setuptools_scm-%{version}*-info
%endif

%changelog
