#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-hatch_vcs%{psuffix}
Version:        0.3.0
Release:        0
Summary:        Hatch plugin for versioning with your preferred VCS
License:        MIT
URL:            https://github.com/ofek/hatch-vcs
Source:         https://files.pythonhosted.org/packages/source/h/hatch_vcs/hatch_vcs-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
# https://github.com/ofek/hatch-vcs/issues/8
Requires:       (python-setuptools_scm >= 6.4.0)
Requires:       python-hatchling >= 0.21.0
Provides:       python-hatch-vcs = %{version}-%{release}
BuildArch:      noarch
# SECTION build
BuildRequires:  %{python_module hatchling >= 0.21.0}
BuildRequires:  %{python_module pip}
# /SECTION
%if %{with test}
# SECTION test
BuildRequires:  %{python_module hatch_vcs = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 6.4.0}
BuildRequires:  git
# /SECTION
%endif
%python_subpackages

%description
This provides a plugin for Hatch that uses your preferred version control system (like Git) to determine project versions.

%prep
%autosetup -n hatch_vcs-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests
%endif

%if %{without test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/hatch_vcs
%{python_sitelib}/hatch_vcs-%{version}*-info
%endif

%changelog
