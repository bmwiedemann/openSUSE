#
# spec file for package python-opentelemetry-instrumentation
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
Name:           python-opentelemetry-instrumentation
Version:        0.50b0
Release:        0
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-instrumentation
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-instrumentation/opentelemetry_instrumentation-%{version}.tar.gz
BuildRequires:  %{python_module packaging >= 18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module opentelemetry-api >= 1.4}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wrapt >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-opentelemetry-api >= 1.4
Requires:       python-wrapt >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

%prep
%setup -q -n opentelemetry_instrumentation-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/opentelemetry-instrument
%python_clone -a %{buildroot}%{_bindir}/opentelemetry-bootstrap
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests disabled because they're not shipped with the sources
#%%check
#%%pytest

%post
%python_install_alternative opentelemetry-instrument opentelemetry-bootstrap

%postun
%python_uninstall_alternative opentelemetry-instrument

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/opentelemetry-instrument
%python_alternative %{_bindir}/opentelemetry-bootstrap
%{python_sitelib}/opentelemetry/instrumentation
%{python_sitelib}/opentelemetry_instrumentation-%{version}.dist-info

%changelog
