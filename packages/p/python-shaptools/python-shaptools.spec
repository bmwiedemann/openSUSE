#
# spec file for package python-shaptools
#
# Copyright (c) 2019 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%if 0%{?suse_version} < 1500
%bcond_with test
%else
%bcond_without test
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-shaptools
Version:        0.3.10+git.1601275579.c59c61d
Release:        0
Summary:        Python tools to interact with SAP HANA utilities
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/SUSE/shaptools
Source:         %{name}-%{version}.tar.gz
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
API to expose SAP HANA functionalities

%prep
%setup -q -n %{name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# do not install tests
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests

%if %{with test}
%check
%pytest tests
%endif

%files %{python_files}
%if 0%{?sle_version:1} && 0%{?sle_version} < 120300
%doc README.md LICENSE
%else
%doc README.md
%license LICENSE
%endif
%{python_sitelib}/*
%python3_only %{_bindir}/shapcli

%changelog
