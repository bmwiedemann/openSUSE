#
# spec file for package python-coreapi-cli
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
Name:           python-coreapi-cli
Version:        1.0.9
Release:        0
Summary:        An interactive command line client for Core API
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/core-api/coreapi-cli
Source:         https://github.com/core-api/coreapi-cli/archive/%{version}.tar.gz
Source1:        LICENSE.md
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coreapi}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-coreapi
Requires:       python-coreschema
Requires:       python-itypes
Requires:       python-requests
Requires:       python-uritemplate
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
An interactive command line client for Core API.

%prep
%setup -q -n coreapi-cli-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

for p in coreapi ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative coreapi

%preun
%python_uninstall_alternative coreapi

%files %{python_files}
%license LICENSE.md
%python_alternative %{_bindir}/coreapi
%{python_sitelib}/*

%changelog
