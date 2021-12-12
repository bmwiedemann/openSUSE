#
# spec file for package python-edgegrid-python
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-edgegrid-python
Version:        1.2.1
Release:        0
Summary:        Client authentication protocol for python-requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/akamai-open/AkamaiOPEN-edgegrid-python
Source:         https://files.pythonhosted.org/packages/source/e/edgegrid-python/edgegrid-python-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ndg-httpsclient
Requires:       python-pyOpenSSL >= 19.0.0
Requires:       python-pyasn1
Requires:       python-requests >= 2.3.0
Requires:       python-urllib3
BuildArch:      noarch

%python_subpackages

%description
Client authentication protocol for python-requests

%prep
%setup -q -n edgegrid-python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
