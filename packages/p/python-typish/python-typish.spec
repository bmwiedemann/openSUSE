#
# spec file for package python-typish
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-typish
Version:        1.9.3
Release:        0
Summary:        Functionality for types
License:        MIT
URL:            https://github.com/ramonhagenaars/typish
Source:         https://github.com/ramonhagenaars/typish/archive/refs/tags/v%{version}.tar.gz#/typish-%{version}-gh.tar.gz
BuildRequires:  %{python_module nptyping >= 1.3.0}
# Tests
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package contains Python module Typish for type-checking.

%prep
%autosetup -p1 -n typish-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not (test_instance_of_nptyping_ndarray or test_get_origin)"

%files %{python_files}
%{python_sitelib}/typish
%{python_sitelib}/typish-%{version}.dist-info

%changelog
