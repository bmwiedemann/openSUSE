#
# spec file for package python-gTTS-token
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-gTTS-token
Version:        1.1.3
Release:        0
Summary:        Python module for calculating a token to run the Google text-to-speech engine
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/boudewijn26/gTTS-token
Source:         https://files.pythonhosted.org/packages/source/g/gTTS-token/gTTS-token-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-requests
BuildArch:      noarch

%python_subpackages

%description
gTTS-token (Google Text to Speech token) is a Python implementation
of the token validation required by Google Translate when making
a request to its API.

%prep
%setup -q -n gTTS-token-%{version}
dos2unix README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
