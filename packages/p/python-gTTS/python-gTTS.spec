#
# spec file for package python-gTTS
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


Name:           python-gTTS
Version:        2.3.1
Release:        0
Summary:        Python module to create MP3 files from spoken text via the Google TTS API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pndurette/gTTS
Source:         https://github.com/pndurette/gTTS/archive/refs/tags/v%{version}.tar.gz#/gTTS-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module gTTS-token >= 1.1.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 3.9}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sphinx-click}
BuildRequires:  %{python_module sphinx_mdinclude}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-click
Requires:       python-gTTS-token >= 1.1.3
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
gTTS is a Python interface for Google's Text to Speech API. An MP3
file may be created with the gTTS module or the gtts-cli command line
utility. It allows unlimited lengths to be spoken by tokenizing long
sentences where the speech would naturally pause.

%prep
%autosetup -p1 -n gTTS-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gtts-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are sadly mostly online
%pytest -k 'not net'

%post
%python_install_alternative gtts-cli

%postun
%python_uninstall_alternative gtts-cli

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/gtts-cli
%{python_sitelib}/gtts
%{python_sitelib}/gTTS-%{version}*-info

%changelog
