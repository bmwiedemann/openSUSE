#
# spec file for package python-redfish
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-redfish
Version:        3.1.8
Release:        0
Summary:        Redfish Python Library
License:        BSD-3-Clause
URL:            https://github.com/DMTF/python-redfish-library
Source:         https://github.com/DMTF/python-redfish-library/archive/%{version}.tar.gz#/redfish-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpatch
Requires:       python-jsonpath-rw
Requires:       python-jsonpointer
Requires:       python-requests
Requires:       python-requests-toolbelt
Requires:       python-requests-unixsocket
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module jsonpath-rw}
BuildRequires:  %{python_module jsonpointer}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
The Redfish library performs the basic HTTPS operations GET, POST,
PUT, PATCH and DELETE on resources using the HATEOAS (Hypermedia as
the Engine of Application State) Redfish architecture.

%prep
%autosetup -p1 -n %{name}-library-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.md
%doc README.rst CHANGELOG.md
%{python_sitelib}/redfish*

%changelog
