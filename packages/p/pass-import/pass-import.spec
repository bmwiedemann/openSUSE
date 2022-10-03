#
# spec file for package pass-import
#
# Copyright (c) 2022 SUSE LLC
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
Version:        3.3
Release:        0
Summary:        A pass extension for importing data from most of the existing password manager
License:        GPL-3.0-only
URL:            https://github.com/roddhjav/pass-import
Source:         https://github.com/roddhjav/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  password-store
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-setuptools
BuildRequires:  python3-pypandoc
BuildRequires:  python3-requests
BuildRequires:  python3-zxcvbn
BuildRequires:  zsh
Requires:       python3-PyYAML
Suggests:       python3-cryptography
Suggests:       python3-defusedxml
Suggests:       python3-file-magic
Suggests:       python3-pykeepass
Suggests:       python3-secretstorage
BuildArch:      noarch
# We don't have pandoc for these platforms
ExcludeArch:    %{ix86}

%description
A pass extension for importing data from most of the existing password manager.

%prep
%autosetup -p1 -n pass-import-%{version}

sed -i 's|#!\s*%{_bindir}/env|#!%{_bindir}/bash|' import.bash
sed -i '1{\@^#!%{_bindir}/env python@d}' pass_import/__main__.py

%build
%python3_build

%install
%python3_install
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
