#
# spec file for package python-pyosf
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
Name:           python-pyosf
Version:        1.0.5
Release:        0
Summary:        Python lib for synching with OpenScienceFramework projects
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/psychopy/pyosf
Source:         https://files.pythonhosted.org/packages/source/p/pyosf/pyosf-%{version}.zip
Source10:       https://raw.githubusercontent.com/psychopy/pyosf/v%{version}/README.md
Source11:       https://raw.githubusercontent.com/psychopy/pyosf/v%{version}/The%20MIT%20License%20%28MIT%29.md
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
The pyosf package is a pure Python library for file sync with
Open Science Framework.

This package is for synchronisation of files from the local
file space to the Open Science Framework (OSF). There is a more
complex sync package by the Center for Open Science,
who created OSF, called osf-sync.

The OSF official package is designed for continuous automated
synchronisation of many projects (à la Dropbox). The authors of pyosf
needed something simpler (for combination with PsychoPy). The pyosf
package performs basic search/login/sync operations with single
projects on OSF, but only when instructed to do so (no continuous
sync).

%prep
%setup -q -n pyosf-%{version}
cp %{SOURCE10} .
cp "%{SOURCE11}" LICENSE.md

%build
%python_build

%install
%python_install
%python_exec %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests only

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
