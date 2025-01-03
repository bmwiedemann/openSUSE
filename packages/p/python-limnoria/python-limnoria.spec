#
# spec file for package python-limnoria
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-limnoria
Version:        2024.10.19
Release:        0
Summary:        A modified version of Supybot (an IRC bot and framework)
License:        BSD-3-Clause
URL:            https://github.com/ProgVal/Limnoria
Source:         https://files.pythonhosted.org/packages/source/l/limnoria/limnoria-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Skip Fediverse webfinger tests that don't seem to mock correctly
Patch0:         skip-fediverse-profile-tests.patch
# full python for sqlite3 module
BuildRequires:  %pythons
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-gnupg}
BuildRequires:  %{python_module pytzdata}
# pyxmpp2-scram not available, the code actually covers the non-availability
#BuildRequires:  %%{python_module pyxmpp2-scram}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  coreutils-systemd
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
Requires:       procps
Requires:       python
Requires:       python-PySocks
Requires:       python-chardet
Requires:       python-cryptography
Requires:       python-ecdsa
Requires:       python-feedparser
Requires:       python-python-dateutil
Requires:       python-python-gnupg
Requires:       python-pytzdata
#Requires:       python-pyxmpp2-scram
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       Supybot = %{version}
Obsoletes:      Supybot < 1.0
BuildArch:      noarch
%python_subpackages

%description
Limnoria is a Python IRC bot with a plugin API. It is equipped with
an ACL system for specifying user permissions with per-command
granularity. Numerous plugins are included.

%prep
%autosetup -p1 -n limnoria-%{version}
sed -i "1,4{/\/usr\/bin\/python/d}" plugins/Debug/plugin.py
sed -i "1,4{/\/usr\/bin\/env/d}" plugins/SedRegex/constants.py

sed -Ei "1{\@^#!/usr/bin/env python3@d}" src/scripts/limnoria_*.py

%build
# Get SOURCE_DATE_EPOCH corresponding to pyproject.toml in sources
export SOURCE_DATE_EPOCH=`date -r pyproject.toml +"%s"`
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/supybot/
for ex in supybot limnoria
do
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-adduser.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-botchk.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-plugin-create.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-plugin-doc.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-test.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-wizard.1
  %python_clone -a %{buildroot}%{_mandir}/man1/${ex}-reset-password.1
  %python_clone -a %{buildroot}%{_bindir}/${ex}
  %python_clone -a %{buildroot}%{_bindir}/${ex}-adduser
  %python_clone -a %{buildroot}%{_bindir}/${ex}-botchk
  %python_clone -a %{buildroot}%{_bindir}/${ex}-plugin-create
  %python_clone -a %{buildroot}%{_bindir}/${ex}-plugin-doc
  %python_clone -a %{buildroot}%{_bindir}/${ex}-reset-password
  %python_clone -a %{buildroot}%{_bindir}/${ex}-test
  %python_clone -a %{buildroot}%{_bindir}/${ex}-wizard
done

%fdupes %{buildroot}%{_mandir}/man1/

%check
%{python_expand export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{$python_sitelib}/
# Status plugin cannot read cpuinfo in obs environment
%{buildroot}%{_bindir}/supybot-test-%{$python_bin_suffix} -c -v --plugins-dir=%{buildroot}%{$python_sitelib}/supybot/plugins/ --no-network
}

%post
%{python_install_alternative supybot supybot-adduser supybot-botchk
  supybot-plugin-create supybot-plugin-doc supybot-reset-password supybot-test supybot-wizard
  supybot.1 supybot-adduser.1 supybot-botchk.1 supybot-plugin-create.1
  supybot-plugin-doc.1 supybot-reset-password.1 supybot-test.1 supybot-wizard.1
  limnoria limnoria-adduser limnoria-botchk
  limnoria-plugin-create limnoria-plugin-doc limnoria-reset-password limnoria-test limnoria-wizard
  limnoria.1 limnoria-adduser.1 limnoria-botchk.1 limnoria-plugin-create.1
  limnoria-plugin-doc.1 limnoria-reset-password.1 limnoria-test.1 limnoria-wizard.1
}

%postun
%{python_uninstall_alternative supybot limnoria}

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/limnoria
%python_alternative %{_bindir}/limnoria-adduser
%python_alternative %{_bindir}/limnoria-botchk
%python_alternative %{_bindir}/limnoria-plugin-create
%python_alternative %{_bindir}/limnoria-plugin-doc
%python_alternative %{_bindir}/limnoria-reset-password
%python_alternative %{_bindir}/limnoria-test
%python_alternative %{_bindir}/limnoria-wizard
%python_alternative %{_bindir}/supybot
%python_alternative %{_bindir}/supybot-adduser
%python_alternative %{_bindir}/supybot-botchk
%python_alternative %{_bindir}/supybot-plugin-create
%python_alternative %{_bindir}/supybot-plugin-doc
%python_alternative %{_bindir}/supybot-reset-password
%python_alternative %{_bindir}/supybot-test
%python_alternative %{_bindir}/supybot-wizard
%python_alternative %{_mandir}/man1/limnoria.1
%python_alternative %{_mandir}/man1/limnoria-adduser.1
%python_alternative %{_mandir}/man1/limnoria-botchk.1
%python_alternative %{_mandir}/man1/limnoria-plugin-create.1
%python_alternative %{_mandir}/man1/limnoria-plugin-doc.1
%python_alternative %{_mandir}/man1/limnoria-reset-password.1
%python_alternative %{_mandir}/man1/limnoria-test.1
%python_alternative %{_mandir}/man1/limnoria-wizard.1
%python_alternative %{_mandir}/man1/supybot.1
%python_alternative %{_mandir}/man1/supybot-adduser.1
%python_alternative %{_mandir}/man1/supybot-botchk.1
%python_alternative %{_mandir}/man1/supybot-plugin-create.1
%python_alternative %{_mandir}/man1/supybot-plugin-doc.1
%python_alternative %{_mandir}/man1/supybot-reset-password.1
%python_alternative %{_mandir}/man1/supybot-test.1
%python_alternative %{_mandir}/man1/supybot-wizard.1
%{python_sitelib}/supybot/
%{python_sitelib}/limnoria-%{version}*.*-info

%changelog
