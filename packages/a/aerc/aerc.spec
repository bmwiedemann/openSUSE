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
Version:        0.15.2
Release:        0
Summary:        An email client for your terminal
License:        MIT
Group:          Productivity/Networking/Email/Clients
URL:            https://aerc-mail.org/
Source:         %{name}-%{version}.tar.gz
Patch0:         fix-script-interpreter.patch
BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  make
BuildRequires:  notmuch-devel
BuildRequires:  scdoc

%description
aerc is an email client that runs in your terminal. It's highly
efficient and extensible, perfect for the discerning hacker.

%prep
%setup -q
%patch0 -p1

%build
%if "%{_arch}" == "ppc64"
    %make_build CC=cc GOFLAGS=""
%else
    %make_build CC=cc GOFLAGS="-buildmode=pie -tags=notmuch"
%endif

%install
%make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}/%{name}

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
