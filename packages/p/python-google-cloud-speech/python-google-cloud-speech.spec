#
# spec file for package python-google-cloud-speech
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
Name:           python-google-cloud-speech
Version:        2.36.0
Release:        0
Summary:        Google Cloud Speech API client library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-speech/google_cloud_speech-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module grpcio >= 1.33.2 if %python-base < 3.14}
BuildRequires:  %{python_module grpcio >= 1.75.1 if %python-base >= 3.14}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 3.20.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %python_version_nodots < 314
Requires:       python-grpcio >= 1.33.2
%else
Requires:       python-grpcio >= 1.75.1
%endif
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 3.20.2
BuildArch:      noarch
%python_subpackages

%description
Cloud Speech API converts audio to text by applying neural network models.

%prep
%autosetup -p1 -n google_cloud_speech-%{version}
# remove tests needing credentials to google services
#rm tests/system/gapic/v1/test_system_speech_v1.py
#rm tests/system/gapic/v1p1beta1/test_system_speech_v1p1beta1.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not test_list_phrase_set"

%files %{python_files}
%exclude %{_bindir}/*.py
%license LICENSE
%doc README.rst
%{python_sitelib}/google/cloud/speech
%{python_sitelib}/google/cloud/speech_v1*
%{python_sitelib}/google/cloud/speech_v2
%{python_sitelib}/google_cloud_speech-%{version}.dist-info

%changelog
