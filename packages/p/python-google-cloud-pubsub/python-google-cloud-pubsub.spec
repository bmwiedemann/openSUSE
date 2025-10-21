#
# spec file for package python-google-cloud-pubsub
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-google-cloud-pubsub
Version:        2.31.1
Release:        0
Summary:        Google Cloud Pub/Sub API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-pubsub
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-pubsub/google_cloud_pubsub-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module google-api-core >= 1.34.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module grpc-google-iam-v1 >= 0.12.4}
BuildRequires:  %{python_module grpcio >= 1.51.3}
BuildRequires:  %{python_module grpcio-status >= 1.33.2}
BuildRequires:  %{python_module opentelemetry-api >= 1.27.0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.27.0}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module proto-plus >= 1.22.2}
BuildRequires:  %{python_module proto-plus >= 1.25.0}
BuildRequires:  %{python_module protobuf >= 3.20.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-grpcio >= 1.51.3
Requires:       python-grpcio-status >= 1.33.2
Requires:       python-opentelemetry-api >= 1.27.0
Requires:       python-opentelemetry-sdk >= 1.27.0
Requires:       python-proto-plus >= 1.22.0
Requires:       python-proto-plus >= 1.22.2
Requires:       python-proto-plus >= 1.25.0
Requires:       python-protobuf >= 3.20.2
Suggests:       python-libcst >= 0.3.10
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Pub/Sub API client library

%prep
%autosetup -p1 -n google_cloud_pubsub-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fixup_pubsub_v1_keywords.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%%pytest

%post
%python_install_alternative fixup_pubsub_v1_keywords.py

%postun
%python_uninstall_alternative fixup_pubsub_v1_keywords.py

%files %{python_files}
%python_alternative %{_bindir}/fixup_pubsub_v1_keywords.py
%{python_sitelib}/google/pubsub
%{python_sitelib}/google/cloud/pubsub
%{python_sitelib}/google/pubsub_v1
%{python_sitelib}/google/cloud/pubsub_v1
%{python_sitelib}/google_cloud_pubsub-%{version}.dist-info

%changelog
