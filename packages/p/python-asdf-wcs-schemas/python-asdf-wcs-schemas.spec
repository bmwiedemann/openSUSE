#
# spec file for package python-asdf-wcs-schemas
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           python-asdf-wcs-schemas%{psuffix}
Version:        0.5.0
Release:        0
Summary:        ASDF WCS Schemas
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/asdf-wcs-schemas
Source:         https://files.pythonhosted.org/packages/source/a/asdf-wcs-schemas/asdf_wcs_schemas-%{version}.tar.gz
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf-coordinates-schemas >= 0.4.0
Requires:       python-asdf-standard >= 1.1.0
Requires:       python-asdf-transform-schemas >= 0.6.0
%if %{with test}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module asdf-astropy}
BuildRequires:  %{python_module asdf-wcs-schemas = %{version}}
BuildRequires:  %{python_module pytest >= 4.6.0}
%endif
BuildArch:      noarch
Provides:       python-asdf_wcs_schemas = %{version}-%{release}
%python_subpackages

%description
provides ASDF schemas for validating WCS tags.
Users should not need to install this directly;
instead, install an implementation package such
as gwcs, which includes asdf-wcs-schemas as a
dependency.

%prep
%setup -q -n asdf_wcs_schemas-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_wcs_schemas
%{python_sitelib}/asdf_wcs_schemas-%{version}.dist-info
%endif

%changelog
