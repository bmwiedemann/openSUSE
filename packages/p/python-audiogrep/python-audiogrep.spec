#
# spec file for package python-audiogrep
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-audiogrep
Version:        0.1.5
Release:        0
License:        MIT
Summary:        Python package to create audio supercuts
Url:            http://antiboredom.github.io/audiogrep
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/audiogrep/audiogrep-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pydub}
# /SECTION
Requires:       ffmpeg
Requires:       pocketsphinx
Requires:       python-pydub
BuildArch:      noarch

%python_subpackages

%description
Audiogrep transcribes audio files and then creates "audio supercuts"
based on search phrases.

%prep
%setup -q -n audiogrep-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/audiogrep
%{python_sitelib}/*

%changelog
