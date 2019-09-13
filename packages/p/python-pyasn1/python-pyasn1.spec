#
# spec file for package python-pyasn1
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
%define         oldpython python
Name:           python-pyasn1
Version:        0.4.5
Release:        0
Summary:        ASN.1 types and codecs
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/etingof/pyasn1
Source:         https://files.pythonhosted.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-asn1 < 0.2.3
Provides:       %{oldpython}-asn1 = %{version}
%endif
%python_subpackages

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP) but
then generalized to be suitable for a wide range of protocols based on ASN.1
specification.

%prep
%setup -q -n pyasn1-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.md TODO.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
