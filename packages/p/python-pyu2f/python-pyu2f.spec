#
# spec file for package python-pyu2f
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
Name:           python-pyu2f
Version:        0.1.5a
Release:        0
Summary:        U2F host library for interacting with a U2F device over USB
License:        Apache-2.0
URL:            https://github.com/google/pyu2f/
Source:         https://github.com/google/pyu2f/archive/refs/tags/%{version}.tar.gz#/pyu2f-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/google/pyu2f/pull/32 fix DeprecationWarning for logging and fake_filesystem
Patch:          fix-deprecation-warning.patch
# https://github.com/google/pyu2f/issues/34
Patch1:         python-pyu2f-no-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pyfakefs >= 2.4}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
U2F host library for interacting with a U2F device over USB.

%prep
%autosetup -p1 -n pyu2f-%{version}
sed -i 's/import mock/from unittest import mock/' pyu2f/tests/*_test.py pyu2f/tests/hid/*_test.py

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
