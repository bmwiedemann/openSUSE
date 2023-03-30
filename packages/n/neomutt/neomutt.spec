#
# spec file for package neomutt
#
# Copyright (c) 2023 SUSE LLC
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


Name:           neomutt
Version:        20230322
Release:        0
Summary:        A command line mail reader (or MUA), a fork of Mutt with added features
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://neomutt.org
Source:         https://github.com/neomutt/neomutt/archive/%{version}.tar.gz
Source2:        https://github.com/neomutt/neomutt/releases/download/%{version}/%{version}.tar.gz.sig
Source3:        https://flatcap.org/id/richard.russon.neomutt.asc#/%{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gawk
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  krb5-devel
BuildRequires:  libdb-4_8-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libidn-devel
BuildRequires:  libkyotocabinet-devel
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  lua-devel
BuildRequires:  ncurses-devel
BuildRequires:  notmuch-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  w3m
BuildRequires:  xsltproc
BuildRequires:  zlib-devel
Recommends:     neomutt-doc
Recommends:     neomutt-lang

%description
NeoMutt is a command line mail reader based on Mutt, brings together many
new features. Can be installed in parallel with mutt.

%package contrib
Summary:        Contrib scripts for Neomutt
Group:          Productivity/Networking/Email/Clients
Requires:       %{name} = %{version}
Recommends:     perl
Recommends:     python3
BuildArch:      noarch

%description contrib
Examples, scripts and helpers that are distributed with Neomutt but are not
maintained by the Neomutt authors.

%package doc
Summary:        Additional documentation for neomutt
Group:          Documentation/Other
Requires:       %{name} = %{version}
#Recommends:     perl(Expect)
BuildArch:      noarch

%description doc
Documentation for NeoMutt with neomuttrc examples for different environments
and requirements.

%lang_package macro

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
./configure	--prefix=%{_prefix}			\
		--docdir=%{_docdir}/neomutt	\
		--with-mailpath=%{_localstatedir}/mail	\
		--kyotocabinet			\
		--lua				\
		--lmdb				\
		--gnutls			\
		--gpgme				\
		--notmuch			\
		--sasl				\
		--gss				\
		--idn				\
		--mixmaster			\
		--pcre2         		\
		--zlib

make %{?_smp_mflags}

%install
%make_install

%find_lang neomutt

%files
%config(noreplace) %{_sysconfdir}/neomuttrc
%license %{_docdir}/%{name}/LICENSE.md
%{_bindir}/neomutt
%{_mandir}/man1/neomutt.1%{?ext_man}
%{_mandir}/man5/neomuttrc.5%{?ext_man}
%if 0%{?suse_version} && 0%{?suse_version} < 1550
%dir %{_prefix}/libexec
%endif
%dir %{_prefix}/libexec/neomutt
%{_prefix}/libexec/neomutt/pgpewrap
%{_prefix}/libexec/neomutt/smime_keys
%{_mandir}/man1/pgpewrap_neomutt.1%{?ext_man}
%{_mandir}/man1/smime_keys_neomutt.1%{?ext_man}
%{_mandir}/man5/mbox_neomutt.5%{?ext_man}
%{_mandir}/man5/mmdf_neomutt.5%{?ext_man}
# this file is used from the default /etc/neomuttrc and moved from neomutt-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/manual.txt
# helper scripts and instructions
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/account-command/
%dir %{_datadir}/%{name}/account-command/gpg-json/
%dir %{_datadir}/%{name}/account-command/macos-keychain/
%doc %{_datadir}/%{name}/account-command/README.md
%{_datadir}/%{name}/account-command/gpg-json/credentials.sh
%doc %{_datadir}/%{name}/account-command/gpg-json/README.md
%{_datadir}/%{name}/account-command/macos-keychain/keychain.py
%doc %{_datadir}/%{name}/account-command/macos-keychain/README.md

%files contrib
%dir %{_datadir}/%{name}/oauth2/
%dir %{_datadir}/%{name}/vim-keys/
%{_datadir}/%{name}/oauth2/mutt_oauth2.py
%doc %{_datadir}/%{name}/oauth2/mutt_oauth2.py.README
%doc %{_datadir}/%{name}/vim-keys/vim-keys.rc
%doc %{_datadir}/%{name}/vim-keys/README.md

%files doc
%dir %{_docdir}/%{name}/
%dir %doc %{_datadir}/%{name}/colorschemes/
%dir %doc %{_datadir}/%{name}/logo/
%doc %{_docdir}/%{name}/AUTHORS.md
%doc %{_docdir}/%{name}/ChangeLog.md
%doc %{_docdir}/%{name}/CODE_OF_CONDUCT.md
%doc %{_datadir}/%{name}/colorschemes/*.neomuttrc
%doc %{_docdir}/%{name}/CONTRIBUTING.md
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/INSTALL.md
%doc %{_datadir}/%{name}/logo/neomutt*
%doc %{_datadir}/%{name}/mime.types
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/SECURITY.md
%doc %{_docdir}/%{name}/smime-notes.txt

%files lang -f %{name}.lang

%changelog
