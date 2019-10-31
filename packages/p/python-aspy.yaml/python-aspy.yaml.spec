#
# spec file for package python-aspy.yaml
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
Name:           python-aspy.yaml
Version:        1.3.0
Release:        0
Summary:        A few extensions to pyyaml
License:        MIT
URL:            https://github.com/asottile/aspy.yaml
Source:         https://github.com/asottile/aspy.yaml/archive/v%{version}.tar.gz#/aspy.yaml-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
%python_subpackages

%description
A few extensions to pyyaml.

%prep
%setup -q -n aspy.yaml-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/asottile/aspy.yaml/issues/35
%pytest -k 'not test_ordered_dump_plain_dict_py36_plus'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
