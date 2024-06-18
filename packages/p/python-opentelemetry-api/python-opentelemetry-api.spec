#
# spec file for package python-opentelemetry-api
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


%{?sle15_python_module_pythons}
Name:           python-opentelemetry-api
Version:        1.25.0
Release:        0
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/master/opentelemetry-api
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-api/opentelemetry_api-%{version}.tar.gz
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Note: If python3-aiocontextvars is not available, the error message will
# be confusing: https://github.com/openSUSE/obs-build/issues/685
BuildRequires:  (python3-aiocontextvars if python3-base < 3.7)
BuildArch:      noarch
Requires:       python-Deprecated
Requires:       python-importlib-metadata
%if %{python_version_nodots} < 37
Requires:       python-aiocontextvars
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
OpenTelemetry Python API

%prep
%setup -q -n opentelemetry_api-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# ignore some tests because we don't have opentelemetry.test module
# gh#open-telemetry/opentelemetry-python#2263
%pytest --ignore tests/util/test_once.py --ignore tests/logs/test_logger_provider.py --ignore tests/logs/test_proxy.py --ignore tests/metrics/test_meter_provider.py --ignore tests/trace/test_globals.py --ignore tests/trace/test_proxy.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/opentelemetry
%{python_sitelib}/opentelemetry_api-%{version}*-info

%changelog
