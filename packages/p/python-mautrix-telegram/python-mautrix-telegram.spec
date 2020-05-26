#
# spec file for package python-mautrix-telegram
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
# Python2 is not supported
%define skip_python2 1
Name:           python-mautrix-telegram
Version:        0.7.2
Release:        0
Summary:        A Matrix-Telegram hybrid puppeting/relaybot bridge
License:        AGPL-3.0-only
URL:            https://github.com/tulir/mautrix-telegram
Source0:        https://files.pythonhosted.org/packages/source/m/mautrix-telegram/mautrix-telegram-%{version}.tar.gz
Source1:        mautrix-telegram.service
# https://github.com/tulir/mautrix-telegram/issues/454
Source99:       https://raw.githubusercontent.com/tulir/mautrix-telegram/master/LICENSE
Patch0:         fix-test.patch
Patch1:         fix-install-files.patch
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
Requires:       python-SQLAlchemy >= 1.2.3
Requires:       python-Telethon >= 1.10
Requires:       python-aiohttp >= 3.0.1
Requires:       python-alembic >= 1.0.0
Requires:       python-commonmark >= 0.8.1
Requires:       python-mautrix >= 0.4.0
Requires:       python-python-magic >= 0.4.15
Requires:       python-ruamel.yaml >= 0.15.35
Requires:       python-telethon-session-sqlalchemy >= 0.2.14
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Brotli
Recommends:     python-Pillow >= 4.3.0
Recommends:     python-aiodns
Recommends:     python-cchardet
Recommends:     python-cryptg >= 0.1
Recommends:     python-moviepy >= 1.0
Recommends:     python-prometheus_client >= 0.6.0
Recommends:     python-psycopg2-binary >= 2
Provides:       mautrix-telegram-impl = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy >= 1.2.3}
BuildRequires:  %{python_module Telethon >= 1.10}
BuildRequires:  %{python_module aiohttp >= 3.0.1}
BuildRequires:  %{python_module alembic >= 1.0.0}
BuildRequires:  %{python_module commonmark >= 0.8.1}
BuildRequires:  %{python_module mautrix >= 0.4.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-magic >= 0.4.15}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.35}
BuildRequires:  %{python_module telethon-session-sqlalchemy >= 0.2.14}
# /SECTION
%python_subpackages

%description
A Matrix-Telegram hybrid puppeting/relaybot bridge.

%package -n mautrix-telegram-server
Summary:        A Matrix-Telegram bridge server
Requires:       mautrix-telegram-impl >= %{version}

%description -n mautrix-telegram-server
A Matrix-Telegram hybrid puppeting/relaybot bridge bridge server.

%prep
%setup -q -n mautrix-telegram-%{version}
%autopatch -p1
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mautrix-telegram
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcmautrix-telegram
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-telegram.service

%pre -n mautrix-telegram-server
%service_add_pre mautrix-telegram.service

%post -n mautrix-telegram-server
%service_add_post mautrix-telegram.service

%preun -n mautrix-telegram-server
%service_del_preun mautrix-telegram.service

%postun -n mautrix-telegram-server
%service_del_postun mautrix-telegram.service

%check
%pytest

%post
%python_install_alternative mautrix-telegram

%postun
%python_uninstall_alternative mautrix-telegram

%files -n mautrix-telegram-server
%{_sysconfdir}/mautrix-telegram/
%config %{_sysconfdir}/mautrix-telegram/example-config.yaml
%{_sysconfdir}/alembic
%config(noreplace) %{_sysconfdir}/alembic/alembic.ini
%{_sbindir}/rcmautrix-telegram
%{_unitdir}/mautrix-telegram.service
%{_datadir}/alembic
%{_datadir}/alembic/env.py
%{_datadir}/alembic/versions

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/mautrix-telegram
%{python_sitelib}/*

%changelog
