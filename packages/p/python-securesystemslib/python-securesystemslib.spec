#
# spec file for package python-wakeonlan
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-securesystemslib
Version:        0.21.0
Release:        0
License:        MIT
Summary:        Cryptographic and general-purpose routines for Secure Systems Lab projects at NYU
Group:          Development/Languages/Python
Url:            https://github.com/secure-systems-lab/securesystemslib
Source:         securesystemslib-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

Requires: python-cryptography >= 3.3.2
Requires: python-PyNaCl
Requires: python-colorama

BuildArch:      noarch
%python_subpackages

%description
Cryptographic and general-purpose routines for Secure Systems Lab projects at NYU

%prep
%setup -q -n securesystemslib-%version

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%{python_sitelib}/*

