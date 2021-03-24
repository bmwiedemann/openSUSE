#
# spec file for package python-limnoria
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


%define skip_python2 1
%define appname limnoria
%define srcver 2020-12-07
Name:           python-limnoria
Version:        2021.03.17
Release:        0
Summary:        A modified version of Supybot (an IRC bot and framework)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ProgVal/Limnoria
Source:         https://github.com/ProgVal/Limnoria/archive/master-%{srcver}.tar.gz#/%{appname}-%{version}.tar.gz
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-gnupg}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PySocks
Requires:       python-SQLAlchemy
Requires:       python-chardet
Requires:       python-ecdsa
Requires:       python-feedparser
Requires:       python-python-dateutil
Requires:       python-python-gnupg
Requires:       python-pytz
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
%python_exec test/test.py
}

%post
%{python_install_alternative supybot supybot-adduser supybot-botchk
  supybot-plugin-create supybot-plugin-doc supybot-reset-password supybot-test supybot-wizard
  supybot.1 supybot-adduser.1 supybot-botchk.1 supybot-plugin-create.1
  supybot-plugin-doc.1 supybot-test.1 supybot-wizard.1
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
%python_alternative %{_mandir}/man1/supybot-test.1
%python_alternative %{_mandir}/man1/supybot-wizard.1

%changelog
