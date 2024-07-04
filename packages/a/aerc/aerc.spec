#
# spec file for package aerc
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Hannes Braun
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


Name:           aerc
Version:        0.18.0
Release:        0
Summary:        An email client for terminals
License:        MIT
Group:          Productivity/Networking/Email/Clients
URL:            https://aerc-mail.org/
Source0:        https://git.sr.ht/~rjarry/aerc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         fix-script-interpreter.patch
BuildRequires:  gcc
BuildRequires:  golang-packaging
BuildRequires:  make
BuildRequires:  notmuch-devel >= 0.37
BuildRequires:  scdoc
BuildRequires:  zstd
Recommends:     dante
Recommends:     w3m

%description
aerc is an email client that runs in terminals.

%prep
%autosetup -p1 -a1

%build
# Need for cache writes
export HOME=${PWD}

%if "%{_arch}" == "ppc64"
    export GOFLAGS=""
%else
    export GOFLAGS="-buildmode=pie -tags=notmuch"
%endif
%make_build CC=cc DATE="$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)"

%install
%make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}

%check
%gotest ./...
LC_ALL=C.UTF-8 ./filters/test.sh

%files
%license LICENSE
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_bindir}/carddav-query
%{_libexecdir}/%{name}
%{_mandir}/man1/aerc.1.gz
%{_mandir}/man1/aerc-search.1.gz
%{_mandir}/man1/carddav-query.1.gz
%{_mandir}/man5/aerc-accounts.5.gz
%{_mandir}/man5/aerc-binds.5.gz
%{_mandir}/man5/aerc-config.5.gz
%{_mandir}/man5/aerc-imap.5.gz
%{_mandir}/man5/aerc-jmap.5.gz
%{_mandir}/man5/aerc-maildir.5.gz
%{_mandir}/man5/aerc-sendmail.5.gz
%{_mandir}/man5/aerc-notmuch.5.gz
%{_mandir}/man5/aerc-smtp.5.gz
%{_mandir}/man7/aerc-patch.7.gz
%{_mandir}/man7/aerc-tutorial.7.gz
%{_mandir}/man7/aerc-templates.7.gz
%{_mandir}/man7/aerc-stylesets.7.gz

%changelog
