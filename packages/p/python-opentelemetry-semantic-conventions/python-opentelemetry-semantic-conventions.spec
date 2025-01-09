#
# spec file for package python-opentelemetry-semantic-conventions
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
Name:           python-opentelemetry-semantic-conventions
Version:        0.50b0
Release:        0
Summary:        OpenTelemetry Semantic Conventions
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-semantic-conventions/opentelemetry_semantic_conventions-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Deprecated >= 1.2.6
Requires:       python-opentelemetry-api >= 1.29.0
BuildArch:      noarch
%python_subpackages

%description
This library contains generated code for the semantic conventions
defined by the OpenTelemetry specification.

%prep
%setup -q -n opentelemetry_semantic_conventions-%{version}

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
%dir %{python_sitelib}/opentelemetry
%{python_sitelib}/opentelemetry/semconv
%{python_sitelib}/opentelemetry_semantic_conventions-%{version}.dist-info

%changelog
