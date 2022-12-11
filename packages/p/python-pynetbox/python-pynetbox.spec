#
# spec file for package python-pynetbox
#
# Copyright (c) 2022 SUSE LLC
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
%define         skip_python2 1
Name:           python-pynetbox
Version:        7.0.0
Release:        0
Summary:        NetBox API client library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/digitalocean/pynetbox
Source:         https://files.pythonhosted.org/packages/source/p/pynetbox/pynetbox-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-netaddr
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
%python_subpackages

%description
Python API client library for NetBox.

%prep
%setup -q -n pynetbox-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove testsuite from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%pytest tests/unit

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/*

%changelog
