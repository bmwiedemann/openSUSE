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

Name:           python-poetry-plugin-export%{psuffix}
Version:        1.2.0
Release:        0
Summary:        Poetry plugin to export the dependencies to various formats
License:        MIT
URL:            https://python-poetry.org/
Source:         https://files.pythonhosted.org/packages/source/p/poetry-plugin-export/poetry_plugin_export-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.3.0}
# No buildtime requirement of poetry: avoid build dep cycles!
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module poetry-plugin-export = %{version}}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  fdupes
Requires:       python-poetry >= 1.2.2
Requires:       python-poetry-core >= 1.3.0
Provides:       python-poetry_plugin_export = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Poetry plugin to export the dependencies to various formats

%prep
%setup -q -n poetry_plugin_export-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/poetry_plugin_export
%{python_sitelib}/poetry_plugin_export-%{version}*-info
%endif

%changelog
