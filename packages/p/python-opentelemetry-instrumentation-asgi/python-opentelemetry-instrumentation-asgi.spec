#
# spec file for package python-opentelemetry-instrumentation-asgi
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
Name:           python-opentelemetry-instrumentation-asgi%{?psuffix}
Version:        0.50b0
Release:        0
Summary:        ASGI instrumentation for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-asgi
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry_instrumentation_asgi/opentelemetry_instrumentation_asgi-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-api >= 1.12}
BuildRequires:  %{python_module opentelemetry-instrumentation == %{version}}
BuildRequires:  %{python_module opentelemetry-semantic-conventions == %{version}}
BuildRequires:  %{python_module opentelemetry-test-utils == %{version}}
BuildRequires:  %{python_module opentelemetry-util-http == %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asgiref >= 3.0
Requires:       python-opentelemetry-api >= 1.12
Requires:       python-opentelemetry-instrumentation == %{version}
Requires:       python-opentelemetry-semantic-conventions == %{version}}
Requires:       python-opentelemetry-util-http == %{version}}
BuildArch:      noarch
%python_subpackages

%description
This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through
OpenTelemetry.

%prep
%setup -q -n opentelemetry_instrumentation_asgi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/opentelemetry/instrumentation/asgi
%{python_sitelib}/opentelemetry_instrumentation_asgi-%{version}.dist-info

%changelog
