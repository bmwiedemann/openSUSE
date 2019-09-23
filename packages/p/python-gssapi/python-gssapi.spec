#
# spec file for package python-gssapi
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
Name:           python-gssapi
Version:        1.6.1
Release:        0
Summary:        A Python interface to RFC 2743/2744 (plus common extensions)
License:        ISC
Group:          Development/Languages/Python
URL:            https://pythongssapi.github.io/python-gssapi/stable/
Source:         https://files.pythonhosted.org/packages/source/g/gssapi/gssapi-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  krb5-devel
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       python-six
%ifpython2
BuildRequires:  python2-enum34
Requires:       python2-enum34
%endif
%python_subpackages

%description
Python-GSSAPI provides both low-level and high level wrappers around the GSSAPI
C libraries. While it focuses on the Kerberos mechanism, it should also be
usable with other GSSAPI mechanisms.

%prep
%setup -q -n gssapi-%{version}

%build
export CFLAGS="%{optflags} -DHAS_GSSAPI_EXT_H -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# requires 'MIT Kerberos installation'

%files %{python_files}
%{python_sitearch}/gssapi*
%doc README.rst
%license LICENSE.txt

%changelog
