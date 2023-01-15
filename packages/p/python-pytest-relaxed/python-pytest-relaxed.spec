#
# spec file for package python-pytest-relaxed
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


Name:           python-pytest-relaxed
Version:        2.0.0
Release:        0
Summary:        Relaxed test discovery/organization for pytest
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/pytest-relaxed
Source:         https://files.pythonhosted.org/packages/source/p/pytest-relaxed/pytest-relaxed-%{version}.tar.gz
BuildRequires:  %{python_module decorator >= 4}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4
Requires:       python-pytest >= 7
BuildArch:      noarch
%python_subpackages

%description
Relaxed test discovery/organization plugin for pytest from python-paramiko author

%prep
%autosetup -p1 -n pytest-relaxed-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_relaxed
%{python_sitelib}/pytest_relaxed-%{version}*-info

%changelog
