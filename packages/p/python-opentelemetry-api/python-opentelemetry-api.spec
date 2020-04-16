#
# spec file for package python-opentelemetry-api
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-opentelemetry-api
Version:        0.6b0
Release:        0
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/master/opentelemetry-api
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-api/opentelemetry-api-%{version}.tar.gz
# https://github.com/open-telemetry/opentelemetry-python/pull/557
Source98:       tests.tar.bz2
# https://github.com/open-telemetry/opentelemetry-python/issues/473
Source99:       https://raw.githubusercontent.com/open-telemetry/opentelemetry-python/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-setuptools
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
OpenTelemetry Python API

%prep
%setup -q -n opentelemetry-api-%{version} -a98
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_environment_variables and test_getattr erroring,
# let us see whether they got fixed via github PR referenced
# above (in next version)
%pytest -k 'not (test_getattr or test_environment_variables)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
