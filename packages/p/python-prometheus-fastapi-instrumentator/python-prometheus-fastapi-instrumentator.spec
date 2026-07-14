#
# spec file for package python-prometheus-fastapi-instrumentator
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-prometheus-fastapi-instrumentator
Version:        8.0.2
Release:        0
Summary:        Instrument a FastAPI app with Prometheus metrics
License:        ISC
URL:            https://github.com/trallnag/prometheus-fastapi-instrumentator
Source:         https://files.pythonhosted.org/packages/source/p/prometheus_fastapi_instrumentator/prometheus_fastapi_instrumentator-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 2.0}
BuildRequires:  %{python_module prometheus_client >= 0.8.0}
BuildRequires:  %{python_module starlette >= 1.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-prometheus-client >= 0.8.0
Requires:       python-starlette >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
A configurable and modular Prometheus instrumentator for FastAPI and
Starlette applications. It exposes request metrics such as latency,
size and count, and lets you add custom metrics.

%prep
%autosetup -p1 -n prometheus_fastapi_instrumentator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The PyPI sdist ships no test suite (tests live only in the upstream
# git repository), so run an import smoke test instead of %%pytest.
%python_expand PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import prometheus_fastapi_instrumentator"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/prometheus_fastapi_instrumentator
%{python_sitelib}/prometheus_fastapi_instrumentator-%{version}.dist-info

%changelog
