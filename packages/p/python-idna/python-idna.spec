#
# spec file for package python-idna
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
Name:           python-idna
Version:        2.8
Release:        0
Summary:        Internationalized Domain Names in Applications (IDNA)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/kjd/idna
Source0:        https://files.pythonhosted.org/packages/source/i/idna/idna-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891
http://tools.ietf.org/html/rfc5891. This version of the protocol
is often referred to as “IDNA2008” and can produce different
results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the “encodings.idna” module that comes with the Python standard
library but currently only supports the older 2003 specification.

%prep
%setup -q -n idna-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.rst
%doc HISTORY.rst README.rst
%{python_sitelib}/*

%changelog
