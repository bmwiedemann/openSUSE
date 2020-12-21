#
# spec file for package python-xkcdpass
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
%define skip_python2 1

Name:           python-xkcdpass
Version:        1.17.6
Release:        0
Summary:        A flexible and scriptable password generator which generates strong passphrases
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/redacted/XKCD-password-generator
Source:         https://files.pythonhosted.org/packages/cc/3a/065130b94cb57cbbd7057e4627cc15bcb16bb9f9d9ef6290e8138273b7a6/xkcdpass-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python3-base
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
A flexible and scriptable password generator which generates strong passphrases,
inspired by XKCD 936 (https://xkcd.com/936/)

%prep
%setup -q -n xkcdpass-%{version}

%build
%{python_build}

%check
%{pytest}

%install
%{python_install}

# Remove the shebang
sed -i -e '1d' %{buildroot}%{python_sitelib}/xkcdpass/xkcd_password.py

%fdupes %{buildroot}%{python_sitelib}

%files %{python_files}
%license LICENSE*
%doc README.rst
%{_bindir}/xkcdpass
%{python_sitelib}/*

%changelog
