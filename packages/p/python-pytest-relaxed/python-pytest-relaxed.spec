#
# spec file for package python-pytest-relaxed
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pytest-relaxed
Version:        1.1.5
Release:        0
Summary:        Relaxed test discovery/organization for pytest
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/pytest-relaxed
Source:         https://files.pythonhosted.org/packages/source/p/pytest-relaxed/pytest-relaxed-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest-relaxed-pr10.patch -- gh#bitprophet/pytest-relaxed#10
Patch0:         pytest-relaxed-pr10.patch
# PATCH-FIX-UPSTREAM pytest-6.1-and-7.patch -- gh#bitprophet/pytest-relaxed#21 + gh#s-t-e-v-e-n-k/pytest-relaxed#1
Patch1:         pytest-6.1-and-7.patch
BuildRequires:  %{python_module decorator >= 4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4
Requires:       python-pytest
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Relaxed test discovery/organization plugin for pytest from python-paramiko author

%prep
%autosetup -p1 -n pytest-relaxed-%{version}
# do not hardcode deps
sed -i setup.py \
    -e 's:pytest>=3,<5:pytest>=3:' \
    -e 's:decorator>=4,<5:decorator>=4:'

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_relaxed
%{python_sitelib}/pytest_relaxed-%{version}*-info

%changelog
