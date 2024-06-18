#
# spec file for package python-opentelemetry-sdk
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
Name:           python-opentelemetry-sdk
Version:        1.25.0
Release:        0
Summary:        OpenTelemetry Python SDK
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-sdk/opentelemetry_sdk-%{version}.tar.gz
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-api == %{version}}
BuildRequires:  %{python_module opentelemetry-semantic-conventions == 0.44b0}
BuildRequires:  %{python_module opentelemetry-test-utils == 0.44b0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 3.7.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-api == %{version}
Requires:       python-opentelemetry-semantic-conventions == 0.44b0
Requires:       python-typing-extensions >= 3.7.4
BuildArch:      noarch
%python_subpackages

%description
OpenTelemetry Python SDK for the OpenTelemetry Project <https://opentelemetry.io/>

%prep
%autosetup -p1 -n opentelemetry_sdk-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rvf tests/performance tests/trace/test_trace.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/opentelemetry/sdk
%{python_sitelib}/opentelemetry_sdk-%{version}.dist-info

%changelog
