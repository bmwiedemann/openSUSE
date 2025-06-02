#
# spec file for package python-ovirt-engine-sdk
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-ovirt-engine-sdk
Version:        4.4.9
Release:        0
Summary:        Python SDK for oVirt Engine API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://ovirt.org/
Source:         https://files.pythonhosted.org/packages/source/o/ovirt-engine-sdk-python/ovirt-engine-sdk-python-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       python-pycurl >= 7.19.0
Requires:       python-six
%python_subpackages

%description
Python SDK for oVirt Engine API

%prep
%setup -q -n ovirt-engine-sdk-python-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.adoc
%license LICENSE.txt
%{python_sitearch}/ovirtsdk4
%{python_sitearch}/ovirt_engine_sdk_python-%{version}*-info

%changelog
