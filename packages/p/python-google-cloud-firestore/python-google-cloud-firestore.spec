#
# spec file for package python-google-cloud-firestore
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
Name:           python-google-cloud-firestore
Version:        2.13.1
Release:        0
Summary:        Google Cloud Firestore API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-firestore
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-firestore/google-cloud-firestore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 1.34.0}
BuildRequires:  %{python_module google-cloud-core >= 1.4.1}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.0
Requires:       python-google-cloud-core >= 1.4.1
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.19.5
Suggests:       python-proto-plus >= 1.22.2
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Firestore API client library

%prep
%autosetup -p1 -n google-cloud-firestore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fixup_firestore_admin_v1_keywords.py
%python_clone -a %{buildroot}%{_bindir}/fixup_firestore_v1_keywords.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative fixup_firestore_admin_v1_keywords.py fixup_firestore_v1_keywords.py

%postun
%python_uninstall_alternative fixup_firestore_admin_v1_keywords.py

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/fixup_firestore_admin_v1_keywords.py
%python_alternative %{_bindir}/fixup_firestore_v1_keywords.py
%{python_sitelib}/google/cloud/firestore*
%{python_sitelib}/google_cloud_firestore-%{version}-*.pth
%{python_sitelib}/google_cloud_firestore-%{version}.dist-info

%changelog
