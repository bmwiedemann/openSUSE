#
# spec file for package python-slumber
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
Name:           python-slumber
Version:        0.7.1
Release:        0
Summary:        Object Orientated Interface to ReSTful APIs
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/samgiles/slumber
# https://github.com/samgiles/slumber/issues/43
Source:         https://github.com/samgiles/slumber/archive/%{version}.tar.gz
# https://github.com/samgiles/slumber/issues/151
Patch0:         python-slumber-disable-test_yaml_get_serializer-subtest.patch
# https://github.com/samgiles/slumber/pull/153
Patch1:         python-slumber-no-unittest2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires:       python-requests
Suggests:       python-PyYAML
Suggests:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
Slumber is a python library that provides a convenient yet powerful object
orientated interface to ReSTful APIs. It acts as a wrapper around the
excellent requests library and abstracts away the handling of urls, serialization,
and processing requests.

%prep
%setup -q -n slumber-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst docs/*
%{python_sitelib}/*

%changelog
