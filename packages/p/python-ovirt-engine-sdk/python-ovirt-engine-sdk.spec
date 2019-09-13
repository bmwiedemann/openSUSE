#
# spec file for package python-ovirt-engine-sdk
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
Name:           python-ovirt-engine-sdk
Version:        4.3.0
Release:        0
Summary:        Python SDK for oVirt Engine API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://ovirt.org/
Source:         https://files.pythonhosted.org/packages/source/o/ovirt-engine-sdk-python/ovirt-engine-sdk-python-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.adoc
%license LICENSE.txt
%{python_sitearch}/*

%changelog
