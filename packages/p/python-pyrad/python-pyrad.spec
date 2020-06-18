#
# spec file for package python-pyrad
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
Name:           python-pyrad
Version:        2.3
Release:        0
Summary:        RADIUS tools
License:        BSD-3-Clause
URL:            https://github.com/pyradius/pyrad
Source0:        https://github.com/pyradius/pyrad/archive/%{version}.tar.gz
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
pyrad is an implementation of a RADIUS client/server as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

%prep
%setup -q -n pyrad-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v -s pyrad/tests/*.py

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
