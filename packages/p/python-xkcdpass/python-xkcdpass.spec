#
# spec file for package python-xkcdpass
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.19.2
Release:        0
Summary:        A flexible and scriptable password generator which generates strong passphrases
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/redacted/XKCD-password-generator
Source:         https://files.pythonhosted.org/packages/a3/46/c86f1c11abe2679c3d7e7e9a8f1dc2d4d400ef0273e2ab35fe7a09e8d9f7/xkcdpass-1.19.2.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
A flexible and scriptable password generator which generates strong passphrases,
inspired by XKCD 936 (https://xkcd.com/936/)

%prep
%setup -q -n xkcdpass-%{version}
# Remove the shebang
sed -i -e '1d' xkcdpass/xkcd_password.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/xkcdpass
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative xkcdpass

%postun
%python_uninstall_alternative xkcdpass

%files %{python_files}
%license LICENSE*
%doc README.rst
%python_alternative %{_bindir}/xkcdpass
%{python_sitelib}/xkcdpass
%{python_sitelib}/xkcdpass-%{version}*-info

%changelog
