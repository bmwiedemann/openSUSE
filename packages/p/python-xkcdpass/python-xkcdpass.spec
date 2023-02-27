#
# spec file for package python-xkcdpass
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1

Name:           python-xkcdpass
Version:        1.19.3
Release:        0
Summary:        A flexible and scriptable password generator which generates strong passphrases
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/redacted/XKCD-password-generator
Source:         https://files.pythonhosted.org/packages/source/x/xkcdpass/xkcdpass-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
# gh#redacted/XKCD-password-generator#138
pytest_python310_ignore="not test_entropy_printout_valid_input"
pytest_python311_ignore="not test_entropy_printout_valid_input"
%pytest -k "${pytest_$python_ignore}"

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
