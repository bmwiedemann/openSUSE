#
# spec file for package python-atpublic
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-atpublic
Version:        2.1.1
Release:        0
Summary:        @public decorator for populating __all__
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://public.readthedocs.io/
Source:         https://gitlab.com/warsaw/public/-/archive/%{version}/public-%{version}.tar.gz#/atpublic-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
public -- @public for populating __all__.

%prep
%setup -q -n public-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc docs/NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
