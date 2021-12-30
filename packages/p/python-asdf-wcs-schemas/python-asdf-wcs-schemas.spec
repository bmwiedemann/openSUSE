#
# spec file for package python-asdf_wcs_schemas
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-asdf-wcs-schemas
Version:        0.1.1
Release:        0
Summary:        ASDF WCS Schemas
License:        BSD-3-Clause
URL:            https://github.com/spacetelescope/asdf-wcs-schemas
Source:         https://files.pythonhosted.org/packages/source/a/asdf-wcs-schemas/asdf_wcs_schemas-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module importlib_resources >= 3 if %python-base < 3.9}
BuildRequires:  fdupes
Requires:       python-asdf >= 2.8.0
%if %python_version_nodots < 39
Requires:       python-importlib_resources >= 3
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.6.0}
BuildRequires:  %{python_module pytest-openfiles >= 0.5.0}
# /SECTION
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/asdf_wcs_schemas
%{python_sitelib}/asdf_wcs_schemas-%{version}*-info

%changelog
