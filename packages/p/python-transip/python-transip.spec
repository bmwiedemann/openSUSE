#
# spec file for package python-transip
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
Name:           python-transip
Version:        2.0.0
Release:        0
Summary:        TransIP API Connector
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/benkonrath/transip-api
Source:         https://github.com/benkonrath/transip-api/archive/v%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module suds-jurko}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-requests
Requires:       python-suds-jurko
BuildArch:      noarch
%python_subpackages

%description
This library implements part of the TransIP API in Python.

%prep
%setup -q -n transip-api-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# testConstructor needs network connection
%python_expand nosetests-%{$python_bin_suffix} -e "test_constructor" -e "testConstructor"

%files %{python_files}
%license LICENSE
%{python_sitelib}/*
%python3_only %{_bindir}/transip-api

%changelog
