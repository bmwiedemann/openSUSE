#
# spec file for package python-pydub
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pydub
Version:        0.25.1
Release:        0
Summary:        Audio manipulation with Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jiaaro/pydub
Source:         https://github.com/jiaaro/pydub/archive/v%{version}.tar.gz#/pydub-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ffmpeg
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module scipy if (%python-base without python36-base)}
Recommends:     python-scipy
Recommends:     python-simpleaudio
Requires:       ffmpeg
BuildArch:      noarch

%python_subpackages

%description
A Python module to manipulate audio with a high level interface.

%prep
%setup -q -n pydub-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v test.test

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
