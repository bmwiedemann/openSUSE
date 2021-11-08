#
# spec file for package python-dataclasses
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


%define skip_python2 1
%define skip_python37 1
%define skip_python38 1
%define skip_python39 1
%define skip_python310 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dataclasses
Version:        0.8
Release:        0
Summary:        A backport of the dataclasses module for Python 3.6
License:        Apache-2.0
URL:            https://github.com/ericvsmith/dataclasses
Source:         https://files.pythonhosted.org/packages/source/d/dataclasses/dataclasses-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is an implementation of PEP 557, Data Classes. It is a backport for Python 3.6.

%prep
%setup -q -n dataclasses-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test_dataclasses.py -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
