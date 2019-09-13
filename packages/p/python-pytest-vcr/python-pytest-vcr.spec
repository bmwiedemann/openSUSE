#
# spec file for package python-pytest-vcr
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
Name:           python-pytest-vcr
Version:        1.0.2
Release:        0
Summary:        Plugin for managing VCR.py cassettes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ktosiek/pytest-vcr
Source:         https://github.com/ktosiek/pytest-vcr/archive/%{version}.tar.gz#/pytest-vcr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.6.0
Requires:       python-vcrpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.0}
BuildRequires:  %{python_module vcrpy}
# /SECTION
%python_subpackages

%description
Plugin for managing VCR.py cassettes.

%prep
%setup -q -n pytest-vcr-%{version}
# https://github.com/ktosiek/pytest-vcr/issues/27
sed -i '/pytest.config/d' tests/test_vcr.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
