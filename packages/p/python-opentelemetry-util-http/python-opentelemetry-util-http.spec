#
# spec file for package python-opentelemetry-util-http
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-opentelemetry-util-http
Version:        0.50b0
Release:        0
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-util-http
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry_util_http/opentelemetry_util_http-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-api = 1.29.0
Requires:       python-opentelemetry-instrumentation == %{version}
Requires:       python-opentelemetry-sdk = 1.29.0
Requires:       python-opentelemetry-semantic-conventions == %{version}
Requires:       python-wrapt >= 1.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-api = 1.29.0}
BuildRequires:  %{python_module opentelemetry-instrumentation == %{version}}
BuildRequires:  %{python_module opentelemetry-sdk = 1.29.0}
BuildRequires:  %{python_module opentelemetry-semantic-conventions == %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils == %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wrapt >= 1.0.0}
# /SECTION
%python_subpackages

%description
Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

%prep
%setup -q -n opentelemetry_util_http-%{version}

%build
%pyproject_wheel

%install
install -m 644 %{SOURCE1} %{_builddir}/opentelemetry_util_http-%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/opentelemetry/util/http
%{python_sitelib}/opentelemetry_util_http-%{version}.dist-info

%changelog
