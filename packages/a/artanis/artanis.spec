#
# spec file for package artanis
#
# Copyright (c) 2026 SUSE LLC
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


%define _buildshell /bin/bash
Name:           artanis
Version:        1.3.0
Release:        0
Summary:        Web application framework for Guile Scheme
# Legal-Review-Notice: BSD-3-Clause is the bundled artanis/irregex.scm
License:        BSD-3-Clause AND GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gnu.org/software/artanis/
Source0:        https://ftp.gnu.org/gnu/artanis/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/artanis/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
BuildRequires:  glibc-locale
BuildRequires:  guile-curl
BuildRequires:  guile-json
BuildRequires:  guile-redis
BuildRequires:  make
BuildRequires:  mozilla-nss
BuildRequires:  pkgconfig
BuildRequires:  util-linux
BuildRequires:  valkey
BuildRequires:  pkgconfig(guile-3.0)
Requires:       guile >= 3.0
Requires:       guile-curl
Requires:       guile-dbi
Requires:       guile-json
Requires:       guile-redis
Requires:       mozilla-nss
Suggests:       guile-fibers

%description
GNU Artanis is a web application framework for Guile Scheme. It provides
routing, MVC, database access (through guile-dbi), caching (through
guile-redis), templating, and a high-concurrency async server core.

%prep
%autosetup -p1
rm etc/artanis/.gitkeep

%build
%configure
# upstream recipes are prefixed with $(V), so V=1 breaks them;
# parallel jobs race on artanis/version.scm
%make_build -j1 V=

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}/bin/art %{buildroot}%{_bindir}/art
install -Dm0644 build-aux/show-artanis-cmds.sh \
  %{buildroot}%{_datadir}/bash-completion/completions/art

%check
valkey-server --bind 127.0.0.1 --port 6379 --save '' &
for i in $(seq 50); do valkey-cli ping && break; sleep 0.2; done
# i18n tests expect a date in a UTC+8/+9 zone
TZ=JST-9 make test 2>&1 | tee test.log
ret=${PIPESTATUS[0]}
valkey-cli shutdown nosave
test $ret -eq 0
# make test keeps only the last file's status; crashes print Backtrace
if grep -E 'FAIL|ERROR|UPASS|UNRESOLVED|Backtrace' test.log; then exit 1; fi

%files
%license COPYING COPYING.LESSER
%doc NEWS README.md SECURITY_WARNING THANKS
%{_bindir}/art
%dir %{_sysconfdir}/artanis
%config(noreplace) %{_sysconfdir}/artanis/artanis.conf
%config(noreplace) %{_sysconfdir}/artanis/plugins.scm
%dir %{_sysconfdir}/artanis/pages
%config(noreplace) %{_sysconfdir}/artanis/pages/*
%{_datadir}/guile/site/3.0/artanis
%{_libdir}/guile/3.0/site-ccache/artanis
%{_datadir}/bash-completion/completions/art

%changelog
