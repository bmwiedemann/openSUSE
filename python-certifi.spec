#
# spec file for package python-certifi
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
Name:           python-certifi
Version:        2020.4.5.1
Release:        0
Summary:        Python package for providing Mozilla's CA Bundle
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/certifi/python-certifi
Source:         https://files.pythonhosted.org/packages/source/c/certifi/certifi-%{version}.tar.gz
# PATCH-FIX-SUSE -- prefer SUSE certificates (only for use on SUSE platforms)
Patch0:         python-certifi-shipped-requests-cabundle.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
BuildArch:      noarch
%python_subpackages

%description
This installable Python package contains a CA Bundle that you can reference
in your Python code. This is useful for verifying HTTP requests, for example.

This is the same CA Bundle which ships with the Requests codebase, and is
derived from Mozilla Firefox's canonical set.

%prep
%setup -q -n certifi-%{version}
%if 0%{?suse_version}
%patch0 -p1
%endif

%build
%python_build

%install
%python_install

%{python_expand chmod +x %{buildroot}%{$python_sitelib}/certifi/core.py
 sed -i "s|#!%{_bindir}/env python|#!%__$python|" %{buildroot}/%{$python_sitelib}/certifi/core.py
 %if 0%{?suse_version}
 rm %{buildroot}%{$python_sitelib}/certifi/cacert.pem
 %endif
}

%python_expand $python -m compileall %{buildroot}%{$python_sitelib}/certifi/
%python_expand $python -O -m compileall %{buildroot}%{$python_sitelib}/certifi/

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests found

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/certifi/
%{python_sitelib}/certifi-%{version}-py*.egg-info

%changelog
