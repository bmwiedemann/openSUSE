#
# spec file for package python-limnoria
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


%define skip_python2 1
%define appname limnoria
%define srcver 2022-09-27
Name:           python-limnoria
Version:        2022.11.10
Release:        0
Summary:        A modified version of Supybot (an IRC bot and framework)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ProgVal/Limnoria
Source:         https://github.com/ProgVal/Limnoria/archive/master-%{srcver}.tar.gz#/%{appname}-%{version}.tar.gz
# full python for sqlite3 module
BuildRequires:  %pythons
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-gnupg}
BuildRequires:  %{python_module pytz if %python-base < 3.9}
# pyxmpp2-scram not available, the code actually covers the non-availability
#BuildRequires:  %%{python_module pyxmpp2-scram}
BuildRequires:  %{python_module setuptools}
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
#Requires:       python-pyxmpp2-scram
%if 0%{?python_version_nodots} < 39
Requires:       python-pytz
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       Supybot = %{version}
Obsoletes:      Supybot < 1.0
BuildArch:      noarch
%python_subpackages

%description
Limnoria is a Python IRC bot with a plugin API. It is equipped with
an ACL system for specifying user permissions with per-command
granularity. Numerous plugins are included.

%prep
%setup -q -n Limnoria-master-%{srcver}
sed -i "1,4{/\/usr\/bin\/python/d}" plugins/Debug/plugin.py
sed -i "1,4{/\/usr\/bin\/env/d}" plugins/SedRegex/constants.py
chmod -x supybot/plugins/*/locales/fi.po

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/supybot/
%python_clone -a %{buildroot}%{_mandir}/man1/supybot.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-adduser.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-botchk.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-plugin-create.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-plugin-doc.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-test.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-wizard.1
%python_clone -a %{buildroot}%{_mandir}/man1/supybot-reset-password.1
%python_clone -a %{buildroot}%{_bindir}/supybot
%python_clone -a %{buildroot}%{_bindir}/supybot-adduser
%python_clone -a %{buildroot}%{_bindir}/supybot-botchk
%python_clone -a %{buildroot}%{_bindir}/supybot-plugin-create
%python_clone -a %{buildroot}%{_bindir}/supybot-plugin-doc
%python_clone -a %{buildroot}%{_bindir}/supybot-reset-password
%python_clone -a %{buildroot}%{_bindir}/supybot-test
%python_clone -a %{buildroot}%{_bindir}/supybot-wizard

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
}

%postun
%{python_uninstall_alternative supybot}

%files %{python_files}
%doc README.md CONTRIBUTING.md
%license LICENSE.md
%python_alternative %{_bindir}/supybot
%python_alternative %{_bindir}/supybot-adduser
%python_alternative %{_bindir}/supybot-botchk
%python_alternative %{_bindir}/supybot-plugin-create
%python_alternative %{_bindir}/supybot-plugin-doc
%python_alternative %{_bindir}/supybot-reset-password
%python_alternative %{_bindir}/supybot-test
%python_alternative %{_bindir}/supybot-wizard
%{python_sitelib}/supybot/
%{python_sitelib}/limnoria-*.egg-info
%python_alternative %{_mandir}/man1/supybot.1
%python_alternative %{_mandir}/man1/supybot-adduser.1
%python_alternative %{_mandir}/man1/supybot-botchk.1
%python_alternative %{_mandir}/man1/supybot-plugin-create.1
%python_alternative %{_mandir}/man1/supybot-plugin-doc.1
%python_alternative %{_mandir}/man1/supybot-reset-password.1
%python_alternative %{_mandir}/man1/supybot-test.1
%python_alternative %{_mandir}/man1/supybot-wizard.1

%changelog
