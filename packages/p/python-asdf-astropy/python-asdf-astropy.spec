#
# spec file for package python-asdf_astropy
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
Name:           python-asdf-astropy
Version:        0.1.2
Release:        0
Summary:        ASDF serialization support for astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/asdf-astropy
Source:         https://files.pythonhosted.org/packages/source/a/asdf-astropy/asdf_astropy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module asdf >= 2.8.0}
BuildRequires:  %{python_module asdf-coordinates-schemas}
BuildRequires:  %{python_module asdf-transform-schemas}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging >= 16.0}
BuildRequires:  %{python_module importlib_resources >= 3 if %python-base < 3.9}
BuildRequires:  fdupes
Requires:       python-asdf >= 2.8.0
Requires:       python-asdf-coordinates-schemas
Requires:       python-asdf-transform-schemas
Requires:       python-astropy
Requires:       python-numpy
Requires:       python-packaging >= 16.0
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib_resources >= 3
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-astropy}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
ASDF serialization support for astropy

%prep
%setup -q -n asdf_astropy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/asdf_astropy
%{python_sitelib}/asdf_astropy-%{version}*-info

%changelog
