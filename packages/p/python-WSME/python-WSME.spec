#
# spec file for package python-WSME
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-WSME
Version:        0.9.3
Release:        0
Summary:        Web Services Made Easy
License:        MIT
Group:          Development/Languages/Python
Url:            http://packages.python.org/WSME/
Source:         https://files.pythonhosted.org/packages/source/W/WSME/WSME-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements:
BuildRequires:  %{python_module WebOb >= 1.2.3}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module netaddr >= 0.7.12}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pecan}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module simplegeneric}
BuildRequires:  %{python_module six >= 1.9.0}
Requires:       python-WebOb >= 1.2.3
Requires:       python-netaddr >= 0.7.12
Requires:       python-pytz
Requires:       python-simplegeneric
Requires:       python-six >= 1.9.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Web Service Made Easy (WSME) is a way to implement webservices
in Python web applications.
It is originally a rewrite of TGWebServices
with focus on extensibility, framework-independence and improved type handling.

%prep
%setup -q -n WSME-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests -v tests/pecantest tests/rest

%files %{python_files}
%license LICENSE
%doc README.rst examples
%{python_sitelib}/*

%changelog
