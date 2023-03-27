#
# spec file for package aerc
#
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
Version:        0.14.0
Release:        0
Summary:        An email client for your terminal
License:        MIT
Group:          Productivity/Networking/Email/Clients
URL:            https://aerc-mail.org/
Source:         %{name}-0.14.0.tar.gz
Patch0:         fix-script-interpreter.patch
Patch1:         fix-english-typos.patch
Patch2:         filters-install-location.patch
BuildRequires:  scdoc
BuildRequires:  go
BuildRequires:  make
BuildRequires:  notmuch-devel

%description
aerc is an email client that runs in your terminal. It's highly
efficient and extensible, perfect for the discerning hacker.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%if "%{_arch}" == "ppc64"
    %make_build PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}
%else
    GOFLAGS="-buildmode=pie -tags=notmuch" %make_build PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}
%endif
strip %{name}
strip wrap

%install
%if "%{_arch}" == "ppc64"
    %make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}
%else
    GOFLAGS="-buildmode=pie -tags=notmuch" %make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}
%endif

%files
%license LICENSE
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man1/aerc.1.gz
%{_mandir}/man1/aerc-search.1.gz
%{_mandir}/man5/aerc-accounts.5.gz
%{_mandir}/man5/aerc-binds.5.gz
%{_mandir}/man5/aerc-config.5.gz
%{_mandir}/man5/aerc-imap.5.gz
%{_mandir}/man5/aerc-maildir.5.gz
%{_mandir}/man5/aerc-sendmail.5.gz
%{_mandir}/man5/aerc-notmuch.5.gz
%{_mandir}/man5/aerc-smtp.5.gz
%{_mandir}/man7/aerc-tutorial.7.gz
%{_mandir}/man7/aerc-templates.7.gz
%{_mandir}/man7/aerc-stylesets.7.gz

%changelog
