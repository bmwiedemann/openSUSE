#
# spec file for package python-python-gnupg
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
%define         oldpython python
Name:           python-python-gnupg
Version:        0.4.6
Release:        0
Summary:        A wrapper for the GNU Privacy Guard (GPG or GnuPG)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://pythonhosted.org/python-gnupg/index.html
Source:         https://files.pythonhosted.org/packages/source/p/python-gnupg/python-gnupg-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gpg2
BuildRequires:  python-rpm-macros
Requires:       gpg2
Obsoletes:      python-gnupg < %{version}
Provides:       python-gnupg = %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-gnupg < %{version}
Provides:       %{oldpython}-gnupg = %{version}
%endif
%python_subpackages

%description
This module allows access to GnuPG's key management,
encryption and signature functionality from Python programs.

%prep
%setup -q -n python-gnupg-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export NO_EXTERNAL_TESTS=true
%pytest test_gnupg.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
