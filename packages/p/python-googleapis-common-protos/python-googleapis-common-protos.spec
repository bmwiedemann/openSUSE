#
# spec file for package python-googleapis-common-protos
#
# Copyright (c) 2024 SUSE LLC
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


%define modname googleapis-common-protos
%define pkgname %{lua:pname,_ = string.gsub(rpm.expand('%modname'), '-' , '_');print(pname)}
%{?sle15_python_module_pythons}
Name:           python-googleapis-common-protos
Version:        1.63.2
Release:        0
Summary:        Common protobufs used in Google APIs
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/python-api-common-protos
Source:         https://files.pythonhosted.org/packages/source/g/googleapis-common-protos/googleapis-common-protos-%{version}.tar.gz
Source1:        test_google_api_error_reason.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module protobuf >= 3.20.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-protobuf >= 3.20.2
Recommends:     python-grpcio >= 1.0.0
BuildArch:      noarch
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-googleapis-common-protos < %{version}
%endif
%python_subpackages

%description
googleapis-common-protos contains the python classes generated from the common
protos in the googleapis_ repository.

%prep
%autosetup -p1 -n %{modname}-%{version}

install -p -D -t tests/unit %{SOURCE1}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/google
%{python_sitelib}/google/type
%{python_sitelib}/google/longrunning
%{python_sitelib}/google/rpc
%{python_sitelib}/google/logging
%{python_sitelib}/google/api
%{python_sitelib}/google/gapic
%{python_sitelib}/google/cloud
%{python_sitelib}/%{pkgname}-%{version}*-info

%changelog
