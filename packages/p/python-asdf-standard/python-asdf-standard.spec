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

Name:           python-asdf-standard%{psuffix}
Version:        1.0.3
Release:        0
Summary:        The ASDF Standard schemas
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/asdf-standard
Source:         https://files.pythonhosted.org/packages/source/a/asdf-standard/asdf_standard-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module importlib_resources >= 3 if %python-base < 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %python_version_nodots < 39
Requires:       python-importlib_resources >= 3
%endif
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module asdf-standard = %{version}}
BuildRequires:  %{python_module astropy >= 5.0.4}
BuildRequires:  %{python_module gwcs}
BuildRequires:  %{python_module packaging >= 16.0}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
Provides:       python-asdf_standard = %{version}-%{release}
%python_subpackages

%description
The ASDF Standard schemas

%prep
%setup -q -n asdf_standard-%{version}
sed -i "/addopts = '--color=yes'/d" pyproject.toml

%if !%{with test}
%build
%pyproject_wheel
%endif

%if !%{with test}
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
%{python_sitelib}/asdf_standard
%{python_sitelib}/asdf_standard-%{version}*-info
%endif

%changelog
