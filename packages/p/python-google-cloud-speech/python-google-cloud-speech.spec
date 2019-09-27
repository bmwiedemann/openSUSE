#
# spec file for package python-google-cloud-speech
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-cloud-speech
Version:        1.2.0
Release:        0
Summary:        Google Cloud Speech API client library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-speech/google-cloud-speech-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.14.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.14.0
BuildArch:      noarch
%python_subpackages

%description
Cloud Speech API converts audio to text by applying neural network models.

%prep
%setup -q -n google-cloud-speech-%{version}
# remove tests needing credentials to google services
rm tests/system/gapic/v1/test_system_speech_v1.py
rm tests/system/gapic/v1p1beta1/test_system_speech_v1p1beta1.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
