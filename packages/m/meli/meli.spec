#
# spec file for package meli
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


%if "@BUILD_FLAVOR@%{nil}" == "debug-tracing"
%define debug_tracing_mode 1
%endif

%if 0%{?debug_tracing_mode}
Name:           meli-with-debug-tracing
%else
Name:           meli
%endif
Version:        0.8.10
Release:        0
Summary:        Terminal email client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://meli-email.org/

Source0:        https://github.com/meli/meli/archive/refs/tags/v%{version}.tar.gz#/meli-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         release-profile.patch
Patch1:         0001-Revert-accounts-cancel-any-previous-mailbox-fetches.patch
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-glib-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libopenssl-devel
BuildRequires:  mandoc-bin
BuildRequires:  sqlite3-devel
%if 0%{?debug_tracing_mode}
Provides:       meli
Conflicts:      meli
%endif

%description
Terminal email client with support for multiple accounts and Maildir / mbox / notmuch / IMAP / JMAP.

%prep
%autosetup -a1 -p1 -n meli-%{version}

%build
%if 0%{?debug_tracing_mode}
%{cargo_build} -F debug-tracing,imap-trace
%endif
%{cargo_build}

%install
mkdir -p %{buildroot}%{_bindir}

%if 0%{?debug_tracing_mode}
cp target/release/meli %{buildroot}%{_bindir}/meli_with_debug_tracing
%else
cp target/release/meli %{buildroot}%{_bindir}
%endif

install -Dm644 meli/docs/meli.1 %{buildroot}%{_mandir}/man1/meli.1
install -Dm644 meli/docs/meli.conf.5 %{buildroot}%{_mandir}/man5/meli.conf.5
install -Dm644 meli/docs/meli-themes.5 %{buildroot}%{_mandir}/man5/meli-themes.5

%files
%license COPYING
%doc CHANGELOG.md README.md
%if 0%{?debug_tracing_mode}
%{_bindir}/meli_with_debug_tracing
%else
%{_bindir}/meli
%endif
%{_mandir}/man1/meli.1%{?ext_man}
%{_mandir}/man5/meli-themes.5%{?ext_man}
%{_mandir}/man5/meli.conf.5%{?ext_man}

%changelog
