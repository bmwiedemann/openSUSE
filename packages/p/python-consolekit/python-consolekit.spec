#
# spec file for package python-consolekit
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
Name:           python-consolekit%{psuffix}
Version:        1.7.1
Release:        0
Summary:        Additional utilities for click
License:        MIT
URL:            https://github.com/domdfcoding/consolekit
Source:         https://github.com/domdfcoding/consolekit/archive/refs/tags/v%{version}.tar.gz#/consolekit-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module consolekit = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 7.1.2
Requires:       python-deprecation-alias >= 0.1.1
Requires:       python-domdf-python-tools >= 3.8.0
Requires:       python-mistletoe >= 0.7.2
Requires:       python-typing-extensions >= 3.10.0.0
Suggests:       python-psutil >= 5.8.0
Suggests:       python-coincidence >= 0.1.0
Suggests:       python-pytest >= 6.0.0
Suggests:       python-pytest-regressions >= 2.0.2
BuildArch:      noarch
%python_subpackages

%description
Additional utilities for click.

%prep
%autosetup -p1 -n consolekit-%{version}

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
%{python_sitelib}/consolekit
%{python_sitelib}/consolekit-%{version}.dist-info
%endif

%changelog
