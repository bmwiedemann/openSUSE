#
# spec file for package python-nodeenv
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
Name:           python-nodeenv
Version:        1.3.3
Release:        0
Summary:        Nodejs virtual environment builder
License:        BSD-2-Clause
URL:            https://github.com/ekalinin/nodeenv
Source:         https://github.com/ekalinin/nodeenv/archive/%{version}.tar.gz#/nodeenv-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Node.js virtual environment builder.

%prep
%setup -q -n nodeenv-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_smoke is an integration test requiring network access.
%pytest -k 'not test_smoke'

%files %{python_files}
%doc AUTHORS CHANGES README README.rst
%license LICENSE
%python3_only %{_bindir}/nodeenv
%{python_sitelib}/*

%changelog
