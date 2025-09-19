#
# spec file for package neomutt
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        20250905
Release:        0
Summary:        A command line mail reader (or MUA), a fork of Mutt with added features
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://neomutt.org
Source:         https://github.com/neomutt/neomutt/archive/%{version}.tar.gz
Source2:        https://github.com/neomutt/neomutt/releases/download/%{version}/%{version}.tar.gz.sig
Source3:        https://flatcap.org/id/richard.russon.neomutt.asc#/%{name}.keyring
# NOTE: This archive version needs to be updated manually every time the services
# are re-run and the upstream version of the neomutt-test-files repo has changed
Source4:	neomutt-test-files-git20241201.7404f44.tar.gz
# PATCH-FIX-UPSTREAM 0001-test-fix-build-for-re-entrant-ncurses.patch https://github.com/neomutt/neomutt/pull/4668 TODO: This has been fixed upstream and should be in the next release
Patch1:		https://github.com/neomutt/neomutt/pull/4668.patch#/0001-test-fix-build-for-re-entrant-ncurses.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  libdb-4_8-devel
BuildRequires:  libtool
BuildRequires:  notmuch-devel
BuildRequires:  pkgconfig
BuildRequires:  tcl
BuildRequires:  w3m
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(kyotocabinet)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Recommends:     cyrus-sasl-plain
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
%autosetup -p1

%build
export CC=gcc
%configure \
	--autocrypt		        	\
	--docdir=%{_docdir}/neomutt	        \
	--gnutls		        	\
	--gpgme			        	\
	--gss				        \
	--kyotocabinet			        \
	--lmdb				        \
	--lua				        \
	--lz4				        \
	--notmuch		        	\
	--pcre2				        \
	--sasl				        \
	--sqlite			        \
	--with-mailpath=%{_localstatedir}/mail	\
	--zlib                                  \
	--zstd

%make_build

%install
%make_install

%find_lang neomutt

# Remove MacOS-specific files
rm -rf %{buildroot}%{_datadir}/%{name}/account-command/macos-keychain/

# Fix Python interpreter path
# https://en.opensuse.org/openSUSE:Packaging_Python#Dependency_on_/usr/bin/python3
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/oauth2/*

%check
export NEOMUTT_TEST_DIR="$PWD/neomutt-test-files"
mkdir -p "$NEOMUTT_TEST_DIR"
tar -xvf %{SOURCE4} -C "$NEOMUTT_TEST_DIR" --strip-components 1
pushd "$NEOMUTT_TEST_DIR"
./setup.sh
popd
%make_build test

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
%doc %{_datadir}/%{name}/account-command/README.md
%{_datadir}/%{name}/account-command/gpg-json/credentials.sh
%doc %{_datadir}/%{name}/account-command/gpg-json/README.md

%files contrib
%dir %{_datadir}/%{name}/oauth2/
%dir %{_datadir}/%{name}/vim-keys/
%{_datadir}/%{name}/oauth2/mutt_oauth2.py
%doc %{_datadir}/%{name}/oauth2/README.md
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
