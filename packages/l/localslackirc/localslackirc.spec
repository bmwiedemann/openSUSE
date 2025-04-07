#
# spec file for package localslackirc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           localslackirc
Version:        1.33+git.1739989938.1a93818
Release:        0
Summary:        IRC gateway for slack and rocket.chat
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/ltworf/%{name}
# Source0:        https://github.com/ltworf/%%{name}/releases/download/%%{version}/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source3:        %{name}.sysconfig
Patch0:         0001-Replace-shebang-to-force-python3.patch
Patch1:         localslackirc-handle-removal-exception.patch
BuildRequires:  python3-typedload >= 2.6
BuildRequires:  python3-emoji >= 2
# BuildRequires:  python3-types-emoji
BuildRequires:  python3-websockets
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-pytest
Requires:       python3-typedload >= 2.6
Requires:       python3-websockets
BuildArch:      noarch
%{?systemd_requires}

%description
IRC gateway for slack, running on localhost for one user. This project is a replacement for slack's IRC gateway that they dropped.

One instance of localslackirc connects to one slack account and one IRC client, passing the messages between the two.

localslackirc also supports Rocket.Chat.

%prep
%autosetup -p1

sed -i -e '1{/#!/s/env //}' lsi-cli.py lsi-getconf

%build
%make_build

%install
sed -i -e 's@%{_datadir}/%{name}/@%{python3_sitelib}/%{name}/@g' \
       -e 's@\.\./share/@%{python3_sitelib}/@' Makefile
DESTDIR=%{buildroot}
%make_install

# Install systemd unit
install -d %{buildroot}%{_unitdir}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}%{_sbindir}
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Install man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1/
install -m 0644 man/*.1 %{buildroot}%{_mandir}/man1/

# Install doc files
install -d -m 0755 %{buildroot}%{_docdir}/%{name}

%check
%python3_pytest

%pre
%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket
%{fillup_only -n %{name}}

%preun
%service_del_preun %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%license LICENSE
%doc CHANGELOG README.md
%dir %{_sysconfdir}/%{name}.d
%config %{_sysconfdir}/%{name}.d/example
%{_bindir}/localslackirc
%{_bindir}/lsi-getconf
%{_bindir}/lsi-send
%{_bindir}/lsi-write
%{_mandir}/man1/*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%{_fillupdir}/sysconfig.%{name}
%{_sbindir}/rc%{name}
%{python3_sitelib}/%{name}*
%exclude %{_datadir}/doc/%{name}/*

%changelog
