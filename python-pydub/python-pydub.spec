#
# spec file for package python-pydub
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
Name:           python-pydub
Version:        0.23.1
Release:        0
Summary:        Audio manipulation with Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jiaaro/pydub
Source:         https://github.com/jiaaro/pydub/archive/v%{version}.tar.gz#/pydub-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Skip-tests-that-use-unavailable-codecs.patch
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ffmpeg
BuildRequires:  python-rpm-macros
Recommends:     python-scipy
Recommends:     python-simpleaudio
Requires:       ffmpeg
BuildArch:      noarch

%python_subpackages

%description
A Python module to manipulate audio with a high level interface.

%prep
%setup -q -n pydub-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
