#
# spec file for package python-edgegrid-python
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-edgegrid-python
Version:        1.3.1
Release:        0
Summary:        Client authentication protocol for python-requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/akamai-open/AkamaiOPEN-edgegrid-python
Source:         https://files.pythonhosted.org/packages/source/e/edgegrid-python/edgegrid-python-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ndg-httpsclient
Requires:       python-pyOpenSSL >= 19.0.0
Requires:       python-pyasn1
Requires:       python-requests >= 2.3.0
Requires:       python-requests-toolbelt
Requires:       python-urllib3
BuildArch:      noarch

%python_subpackages

%description
Client authentication protocol for python-requests

%prep
%setup -q -n edgegrid-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/akamai
%{python_sitelib}/akamai/edgegrid
%{python_sitelib}/edgegrid_python-%{version}*.pth
%{python_sitelib}/edgegrid_python-%{version}.dist-info

%changelog
