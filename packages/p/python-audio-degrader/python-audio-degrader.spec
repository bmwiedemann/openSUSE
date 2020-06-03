#
# spec file for package python-audio-degrader
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-audio-degrader
Version:        1.2.3
Release:        0
Summary:        Tool to introduce controlled degradations to audio
License:        GPL-3.0-only
URL:            https://github.com/EliosMolina/audio_degrader
Source:         https://files.pythonhosted.org/packages/source/a/audio_degrader/audio_degrader-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-librosa >= 0.6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module librosa >= 0.6.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Audio degradation toolbox in python. It is used to apply controlled
degradations to audio.

%prep
%setup -q -n audio_degrader-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/audio_degrader
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests are not in sdist and there is no github tag for the latest release
# See https://github.com/emilio-molina/audio_degrader/pull/32
# and https://github.com/emilio-molina/audio_degrader/issues/33
# %%check
# %%pytest

%post
%python_install_alternative audio_degrader

%postun
%python_uninstall_alternative audio_degrader

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/audio_degrader
%{python_sitelib}/*

%changelog
