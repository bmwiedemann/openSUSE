#
# spec file for package python-audiogrep
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


%bcond_without libalternatives
Name:           python-audiogrep
Version:        0.1.5
Release:        0
Summary:        Python package to create audio supercuts
License:        MIT
Group:          Development/Languages/Python
URL:            https://antiboredom.github.io/audiogrep
Source:         https://files.pythonhosted.org/packages/source/a/audiogrep/audiogrep-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       ffmpeg
Requires:       pocketsphinx
Requires:       python-pydub
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pydub}
# /SECTION
%python_subpackages

%description
Audiogrep transcribes audio files and then creates "audio supercuts"
based on search phrases.

%prep
%setup -q -n audiogrep-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/audiogrep
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative audiogrep

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/audiogrep
%{python_sitelib}/audiogrep
%{python_sitelib}/audiogrep-%{version}*-info

%changelog
