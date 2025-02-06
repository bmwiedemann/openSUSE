#
# spec file for package python-grpc-google-iam-v1
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
Name:           python-grpc-google-iam-v1
Version:        0.14.0
Release:        0
Summary:        GRPC library for the google-iam-v1 service
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/python-grpc-google-iam-v1
Source:         https://files.pythonhosted.org/packages/source/g/grpc_google_iam_v1/grpc_google_iam_v1-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-googleapis-common-protos >= 1.56.0
Requires:       python-grpcio >= 1.44.0
Requires:       python-protobuf >= 3.20.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module googleapis-common-protos >= 1.56.0}
BuildRequires:  %{python_module grpcio >= 1.44.0}
# /SECTION
%python_subpackages

%description
GRPC library for the google-iam-v1 service

%prep
%setup -q -n grpc_google_iam_v1-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests included in source tarball

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/iam/
%{python_sitelib}/grpc_google_iam_v1-%{version}.dist-info

%changelog
