#
# spec file for package python-deepdiff
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
Name:           python-deepdiff
Version:        4.2.0
Release:        0
Summary:        Deep Difference and Search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff
Source:         https://github.com/seperman/deepdiff/archive/%{version}.tar.gz
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module ordered-set}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpickle
Requires:       python-ordered-set
BuildArch:      noarch
%python_subpackages

%description
A Python module to calculate Deep Difference of dictionaries,
iterables, strings and other objects. It can search for objects
within other objects, and hash any object based on their content.

%prep
%setup -q -n deepdiff-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# murmur3 is optional, deepdiff uses sha256 instead
%pytest -k 'not TestDeepHashMurmur3'

%files %{python_files}
%license LICENSE
%doc README.md AUTHORS
%{python_sitelib}/*

%changelog
