#
# spec file for package neomutt
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


Name:           neomutt
Version:        20200821
Release:        0
Summary:        A command line mail reader (or MUA), a fork of Mutt with added features
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://neomutt.org
Source:         https://github.com/neomutt/neomutt/archive/%{version}.tar.gz
Patch0:         neomutt-sidebar-abbreviate-shorten-what-user-sees.patch
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
BuildRequires:  pkgconfig
BuildRequires:  w3m
BuildRequires:  xsltproc
BuildRequires:  zlib-devel
Recommends:     neomutt-doc
Recommends:     neomutt-lang

%description
NeoMutt is a command line mail reader based on Mutt, brings together many
new features. Can be installed in parallel with mutt.

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
%patch0 -p1

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
		--zlib

make %{?_smp_mflags}

%install
%make_install

%find_lang neomutt

%files
%config(noreplace) %{_sysconfdir}/neomuttrc
%license %{_docdir}/neomutt/LICENSE.md
%{_bindir}/neomutt
%{_mandir}/man1/neomutt.1%{?ext_man}
%{_mandir}/man5/neomuttrc.5%{?ext_man}
%dir %{_prefix}/libexec
%dir %{_prefix}/libexec/neomutt
%{_prefix}/libexec/neomutt/pgpewrap
%{_prefix}/libexec/neomutt/smime_keys
%{_mandir}/man1/pgpewrap_neomutt.1%{?ext_man}
%{_mandir}/man1/smime_keys_neomutt.1%{?ext_man}
%{_mandir}/man5/mbox_neomutt.5%{?ext_man}
%{_mandir}/man5/mmdf_neomutt.5%{?ext_man}
# this file is used from the default /etc/neomuttrc and moved from neomutt-doc
%dir %{_docdir}/neomutt
%doc %{_docdir}/neomutt/manual.txt

%files doc
%dir %{_docdir}/neomutt
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/ChangeLog.md
%doc %{_docdir}/%{name}/CODE_OF_CONDUCT.md
%doc %{_docdir}/neomutt/INSTALL.md
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/neomutt/mime.types
%doc %{_docdir}/neomutt/smime-notes.txt
%dir %doc %{_docdir}/%{name}/colorschemes/
%doc %{_docdir}/%{name}/colorschemes/*.neomuttrc
%dir %doc %{_docdir}/%{name}/keybase/
%doc %{_docdir}/%{name}/keybase/*
%dir %doc %{_docdir}/%{name}/logo/
%doc %{_docdir}/%{name}/logo/neomutt*
%dir %doc %{_docdir}/%{name}/samples/
%doc %{_docdir}/%{name}/samples/*.pl
%doc %{_docdir}/%{name}/samples/*.rc
%doc %{_docdir}/%{name}/samples/colors.*
%doc %{_docdir}/%{name}/samples/sample.*
%doc %{_docdir}/%{name}/samples/smime_keys_test.pl
%dir %doc %{_docdir}/%{name}/vim-keys/
%doc %{_docdir}/%{name}/vim-keys/*
%dir %doc %{_docdir}/%{name}/hcache-bench/
%doc %{_docdir}/%{name}/hcache-bench/README.md
%doc %{_docdir}/%{name}/hcache-bench/neomuttrc
%doc %{_docdir}/%{name}/hcache-bench/neomutt-hcache-bench.sh
%dir %doc %{_docdir}/%{name}/lua/
%doc %{_docdir}/%{name}/lua/test_lua-api_runner.neomuttrc
%doc %{_docdir}/%{name}/lua/test_lua-api_spec.lua

%files lang -f %{name}.lang

%changelog
