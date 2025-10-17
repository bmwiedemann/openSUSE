#
# spec file for package python-google-cloud-audit-log
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
Name:           python-google-cloud-audit-log
Version:        0.4.0
Release:        0
Summary:        Google Cloud Audit Protos
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-audit-log
Source:         https://files.pythonhosted.org/packages/source/g/google_cloud_audit_log/google_cloud_audit_log-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module googleapis-common-protos >= 1.56.2}
BuildRequires:  %{python_module protobuf >= 3.20.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-googleapis-common-protos >= 1.56.2
Requires:       python-protobuf >= 3.20.2
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Audit Protos

%prep
%autosetup -p1 -n google_cloud_audit_log-%{version}

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
%exclude %{python_sitelib}/docs
%{python_sitelib}/google/cloud/audit
%{python_sitelib}/google_cloud_audit_log-%{version}.dist-info

%changelog
