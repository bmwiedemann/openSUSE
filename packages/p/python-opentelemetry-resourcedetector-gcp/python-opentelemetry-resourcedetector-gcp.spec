#
# spec file for package python-opentelemetry-resourcedetector-gcp
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
Name:           python-opentelemetry-resourcedetector-gcp
Version:        1.9.0a0
Release:        0
Summary:        Google Cloud resource detector for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-resourcedetector-gcp
Source:         https://files.pythonhosted.org/packages/source/o/opentelemetry-resourcedetector-gcp/opentelemetry_resourcedetector_gcp-%{version}.tar.gz
BuildRequires:  %{python_module opentelemetry-api >= 1.0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-api >= 1.0
Requires:       python-opentelemetry-sdk >= 1.0
Requires:       python-requests >= 2.24
Requires:       python-typing_extensions >= 4.0
BuildArch:      noarch
%python_subpackages

%description
This library provides support for detecting GCP resources like GCE, GKE, etc.

%prep
%setup -q -n opentelemetry_resourcedetector_gcp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --snapshot-update

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/opentelemetry
%exclude %{python_sitelib}/opentelemetry/py.typed
%{python_sitelib}/opentelemetry/resourcedetector
%{python_sitelib}/opentelemetry_resourcedetector_gcp-%{version}.dist-info

%changelog
