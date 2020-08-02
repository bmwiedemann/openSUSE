#
# spec file for package python-coreapi
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
Name:           python-coreapi
Version:        2.3.3
Release:        0
Summary:        Python client library for Core API
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/core-api/python-client
Source:         https://github.com/core-api/python-client/archive/%{version}.tar.gz#/coreapi-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/core-api/python-client/master/LICENSE.md
Patch0:         same-bsd.patch
BuildRequires:  %{python_module coreschema}
BuildRequires:  %{python_module itypes}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module uritemplate}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coreschema
Requires:       python-itypes
Requires:       python-requests
Requires:       python-uritemplate
BuildArch:      noarch
%python_subpackages

%description
Python client library for Core API, a format-independent Document Object Model
for representing Web APIs.

%prep
%setup -q -n python-client-%{version}
cp %{SOURCE1} .
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/coreapi/
%{python_sitelib}/coreapi-%{version}-py*.egg-info

%changelog
