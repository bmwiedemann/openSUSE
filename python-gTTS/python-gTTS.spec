#
# spec file for package python-gTTS
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
Name:           python-gTTS
Version:        2.0.3
Release:        0
Summary:        Python module to create MP3 files from spoken text via the Google TTS API
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/pndurette/gTTS
Source:         https://files.pythonhosted.org/packages/source/g/gTTS/gTTS-%{version}.tar.gz
Patch0:         remove-pip-requirement.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-click
Requires:       python-gTTS-token
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
gTTS is a Python interface for Google's Text to Speech API. An MP3
file may be created with the gTTS module or the gtts-cli command line
utility. It allows unlimited lengths to be spoken by tokenizing long
sentences where the speech would naturally pause.

%prep
%setup -q -n gTTS-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.rst README.md
%license LICENSE
%python3_only %{_bindir}/gtts-cli
%{python_sitelib}/*

%changelog
