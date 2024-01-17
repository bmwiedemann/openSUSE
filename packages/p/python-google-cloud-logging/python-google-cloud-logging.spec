#
# spec file for package python-google-cloud-logging
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.9.0
Release:        0
Summary:        Stackdriver Logging API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-logging
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-logging/google-cloud-logging-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 1.33.2}
BuildRequires:  %{python_module google-cloud-appengine-logging >= 0.1.0}
BuildRequires:  %{python_module google-cloud-audit-log >= 0.1.0}
BuildRequires:  %{python_module google-cloud-core >= 2.0.0}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.12.4}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.33.2
Requires:       python-google-cloud-appengine-logging >= 0.1.0
Requires:       python-google-cloud-audit-log >= 0.1.0
Requires:       python-google-cloud-core >= 2.0.0
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.19.5
Suggests:       python-proto-plus >= 1.22.2
BuildArch:      noarch
%python_subpackages

%description
Stackdriver Logging API client library

%prep
%autosetup -p1 -n google-cloud-logging-%{version}

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
