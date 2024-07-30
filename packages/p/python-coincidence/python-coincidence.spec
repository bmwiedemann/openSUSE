#
# spec file for package python-coincidence
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
Name:           python-coincidence%{psuffix}
Version:        0.6.6
Release:        0
Summary:        Helper functions for pytest
License:        MIT
URL:            https://github.com/python-coincidence/coincidence
Source:         https://github.com/python-coincidence/coincidence/archive/refs/tags/v%{version}.tar.gz#/coincidence-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module whey}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence = %{version}}
BuildRequires:  %{python_module pytest >= 6.2.0}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module toml}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-domdf-python-tools >= 2.8.0
Requires:       python-pytest >= 6.2.0
Requires:       python-pytest-regressions >= 2.0.2
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
%python_subpackages

%description
Helper functions for pytest.

%prep
%autosetup -p1 -n coincidence-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/coincidence
%{python_sitelib}/coincidence-%{version}.dist-info
%endif

%changelog
