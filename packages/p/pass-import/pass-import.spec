#
# spec file for package pass-import
#
# Copyright (c) 2024 SUSE LLC
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


Name:           pass-import
Version:        3.4
Release:        0
Summary:        A pass extension for importing data from most of the existing password manager
License:        GPL-3.0-only
URL:            https://github.com/roddhjav/pass-import
Source:         https://github.com/roddhjav/pass-import/releases/download/v3.4/pass-import-3.4.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  password-store
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-pip
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-zxcvbn
BuildRequires:  zsh
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-zxcvbn
Suggests:       python3-cryptography
Suggests:       python3-defusedxml
Suggests:       python3-file-magic
Suggests:       python3-pykeepass
Suggests:       python3-secretstorage
BuildArch:      noarch

%description
A pass extension for importing data from most of the existing password manager.

%prep
%autosetup -p1 -n pass-import-%{version}

sed -i 's|#!\s*%{_bindir}/env|#!%{_bindir}/bash|' import.bash
sed -i '1{\@^#!%{_bindir}/env python@d}' pass_import/__main__.py

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
# gh#roddhjav/pass-import#198
install -D -t %{buildroot}%{_usr}/lib/password-store/extensions \
    %{buildroot}%{python3_sitelib}%{_usr}/lib/password-store/extensions/import.bash
rm -rf %{buildroot}%{python3_sitelib}%{_usr}
install -D -m 0644 -t %{buildroot}%{_datadir}/zsh/site-functions/ \
    share/zsh/site-functions/*
install -D -m 0644 -t %{buildroot}%{_datadir}/bash-completion/completions/ \
    share/bash-completion/completions/*
install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ \
    share/man/man1/*.1*
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc README.md
%license LICENSE
%{_bindir}/pimport
%{python3_sitelib}/pass_import
%{python3_sitelib}/pass_import-%{version}*-info
%{_mandir}/man1/pass-import.1%{?ext_man}
%{_mandir}/man1/pimport.1%{?ext_man}
%{_datadir}/zsh/site-functions/_pass-import
%{_datadir}/zsh/site-functions/_pimport
%{_datadir}/bash-completion/completions/pass-import
%{_datadir}/bash-completion/completions/pimport
# temporarily until change is included in password-store
%dir %{_prefix}/lib/password-store
%dir %{_prefix}/lib/password-store/extensions
%{_prefix}/lib/password-store/extensions/import.bash

%changelog
