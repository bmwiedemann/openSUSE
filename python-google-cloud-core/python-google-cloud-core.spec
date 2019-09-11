#
# spec file for package python-google-cloud-core
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
Name:           python-google-cloud-core
Version:        1.0.0
Release:        0
Summary:        Google Cloud API client core library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-core/google-cloud-core-%{version}.tar.gz
BuildRequires:  %{python_module grpcio}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.11.0
Recommends:     python-grpcio >= 1.8.2
BuildArch:      noarch
%ifpython2
BuildRequires:  python2-futures
%endif
# SECTION test requirements
BuildRequires:  %{python_module google-api-core >= 0.1.1}
# /SECTION
%ifpython2
Requires:       python-futures >= 3.2.0
%endif
%python_subpackages

%description
Core Helpers for Google Cloud Python Client Library
This library is not meant to stand-alone. Instead it defines
common helpers (e.g. base ``Client`` classes) used by all of the
``google-cloud-*`` packages.

%prep
%setup -q -n google-cloud-core-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
