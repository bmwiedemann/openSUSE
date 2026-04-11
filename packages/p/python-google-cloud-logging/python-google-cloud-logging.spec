#
# spec file for package python-google-cloud-logging
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-google-cloud-logging
Version:        3.15.0
Release:        0
Summary:        Stackdriver Logging API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-logging
Source:         https://files.pythonhosted.org/packages/source/g/google_cloud_logging/google_cloud_logging-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 2.11.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module google-cloud-appengine-logging >= 0.1.3}
BuildRequires:  %{python_module google-cloud-audit-log >= 0.3.1}
BuildRequires:  %{python_module google-cloud-core >= 2.0.0}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.12.4}
BuildRequires:  %{python_module grpcio >= 1.33.2}
BuildRequires:  %{python_module opentelemetry-api >= 1.9.0}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 4.25.8}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 2.11.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-google-cloud-appengine-logging >= 0.1.3
Requires:       python-google-cloud-audit-log >= 0.3.1
Requires:       python-google-cloud-core >= 2.0.0
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-grpcio >= 1.33.2
Requires:       python-opentelemetry-api >= 1.9.0
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 4.25.8
Suggests:       python-proto-plus >= 1.22.3
BuildArch:      noarch
%python_subpackages

%description
Stackdriver Logging API client library

%prep
%autosetup -p1 -n google_cloud_logging-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/logging*
%{python_sitelib}/google_cloud_logging-%{version}.dist-info

%changelog
