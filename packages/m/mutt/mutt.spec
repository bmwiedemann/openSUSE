#
# spec file for package mutt
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


%bcond_with    mutt_openssl
%bcond_without mutt_gnutls

Name:           mutt
%if %{with mutt_openssl}
BuildRequires:  pkgconfig(openssl)
%endif
%if %{with mutt_gnutls}
BuildRequires:  pkgconfig(gnutls)
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-gssapi
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  hunspell
BuildRequires:  iso_ent
BuildRequires:  libgpgme-devel
BuildRequires:  libxslt-tools
BuildRequires:  opensp
BuildRequires:  pkgconfig(gssrpc)
BuildRequires:  pkgconfig(krb5)
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(kyotocabinet)
%else
BuildRequires:  libkyotocabinet-devel
%endif
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(libidn2)
%else
BuildRequires:  pkgconfig(libidn)
%endif
BuildRequires:  pkgconfig(libsasl2)
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(ncurses)
%else
BuildRequires:  ncurses-devel
%endif
%if 0%{?suse_version} > 1130
BuildRequires:  pkgconfig(shared-mime-info)
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  w3m
URL:            http://www.mutt.org
Requires(postun): /usr/bin/rm
Requires(post): /usr/bin/mkdir
Requires(post): /usr/bin/cat
Requires(pre):  /usr/bin/zcat
Requires(pre):  /usr/bin/grep
Recommends:     hunspell
Provides:       muttssl
Obsoletes:      muttssl
Recommends:     mutt-doc
Recommends:     mutt-lang
Recommends:     urlscan
Recommends:     urlview
Recommends:     w3m
%if 0%{?suse_version} > 1130
Requires(post):   shared-mime-info
Requires(postun): shared-mime-info
%endif
Version:        1.14.4
Release:        0
Summary:        Mail Program
# ftp://ftp.mutt.org/mutt/devel/
# https:///bitbucket.org/mutt/mutt/downloads/%%name-%%version.tar.gz
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
Source0:        https://bitbucket.org/mutt/mutt/downloads/mutt-%version.tar.gz
Source1:        Signature_conversion
Source2:        README.alternates
Source3:        mutt.png
Source4:        mutt.desktop
Source5:        skel.muttrc
Source9:        mutt.mailcap
Patch0:         %name-1.13.3.dif
# http://www.spinnaker.de/mutt/compressed/
Patch2:         %name-1.5.9i-pgpewrap.diff
Patch3:         %name-1.5.20-sendgroupreplyto.diff
Patch4:         %name-1.5.15-wrapcolumn.diff
Patch7:         mutt-1.6.1-opennfs.dif
Patch9:         bug-676388-largefile.patch
# http://www.wolfermann.org/mutt.html
Patch11:        aw.listreply.diff
Patch12:        patch-1.5.24.vk.pgp_verbose_mime
# PATCH-FIX-OPENSUSE: bnc#813498 - mutt crashes in fgetwc in text_enriched_handler
Patch15:        widechar.sidebar.dif
# PATCH-FIX-OPENSUSE: Be able to read signed/encrypted messsages even with CRLF
Patch16:        mutt-1.5.23-carriage-return.path
# PATCH-FIX-OPENSUSE bnc#899712 - fallback mailcap for e.g text/html
Patch18:        mutt-1.5.21-mailcap.diff
# PATCH-FIX-SUSE: bsc#907453 - CVE-2014-9116: mutt: heap-based buffer overflow in mutt_substrdup()
Patch19:        bsc907453-CVE-2014-9116-jessie.patch
# PATCH-ENHANCE-SUSE: allow to list current imap folders
Patch20:        mutt-1.10.1-imap.patch
# PATCH-ENHANCE-SUSE: boo#1156477 - Mutt has an option to ask before quitting on ^C but quits immediately on ^4
Patch21:        mutt-Fix-SIGQUIT-handling.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir %{_sysconfdir}

%description
A very powerful mail user agent. It supports (among other nice things)
highlighting, threading, and PGP. It takes some time to get used to,
however. This version is based on NeoMutt, that is it includes many
enhancements.

%package doc
Summary:        Additional Documentation about Mutt
Group:          Documentation/Other
Requires:       %{name} = %{version}
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
Recommends:     perl(Expect)
Provides:       %{name}:%{_docdir}/%name/COPYRIGHT
BuildArch:      noarch

%description doc
Some extend documentation about mutt together with muttrc examples
for different environments and requirements.

%package lang
Summary:        Languages for Mutt
Group:          System/Localization
Provides:       mutt:/usr/share/locale/en_GB/LC_MESSAGES/mutt.mo
Requires:       %{name} = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package mutt.

%prep
%setup -q -n mutt-%version
%patch0 -p0 -b .p0
%patch2 -p0 -b .pgpewrap
%patch3 -p0 -b .sendgroupreplyto
%patch4 -p0 -b .wrapcolumn
%patch7 -p0 -b .opennfs
%patch9 -p0 -b .largefile
%patch11 -p0 -b .listreply
%patch12 -p0 -b .pgp_verbose_mtime
%patch15 -p0 -b .widechar.sidebar
%patch16 -p0 -b .crlf
%patch18 -p0 -b .mailcap
%patch19 -p0 -b .cvw2014.9116
%patch20 -p0 -b .imap
%patch21 -p0 -b .quit

cp %{S:2} .

%build
%if %{with mutt_gnutls}
echo 'set ssl_ca_certificates_file="/etc/ssl/ca-bundle.pem"' >> doc/Muttrc.head
%endif
autoreconf -fi
  cflags ()
  {
    local flag=$1; shift
    local var=$1; shift
    test -n "${flag}" -a -n "${var}" || return
    case "${!var}" in
    *${flag}*) return
    esac
    set -o noclobber
    case "$flag" in
    -Wl,*)
	if echo 'int main () { return 0; }' | \
	    ${CC:-gcc} -Werror $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
	    eval $var=\${$var:+\$$var\ }$flag
	fi
	;;
    *)
	if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	    eval $var=\${$var:+\$$var\ }$flag
	fi
    esac
    set +o noclobber
  }
CC=gcc
CFLAGS="-Wall $RPM_OPT_FLAGS -I. -D_GNU_SOURCE"
cflags -fno-strict-aliasing		CFLAGS
cflags -fstack-protector		CFLAGS
cflags -fPIE				CFLAGS
cflags -g3				CFLAGS
cflags -pipe				CFLAGS
cflags -Wl,--as-needed			LDFLAGS
cflags -Wl,-O2				LDFLAGS
cflags -pie				LDFLAGS
export CC CFLAGS LDFLAGS
export SENDMAIL=/usr/sbin/sendmail
export ISPELL=/usr/bin/hunspell
export PATH="/usr/lib/mit/bin:$PATH"
export KRB5CFGPATH="$(type -p krb5-config)"
$KRB5CFGPATH --cflags gssapi
$KRB5CFGPATH --libs gssapi
$KRB5CFGPATH --version
%configure \
	--with-docdir=%{_docdir}/%name \
%if %{with mutt_openssl}
	--without-gnutls \
	--with-ssl=%{_prefix} \
%endif
%if %{with mutt_gnutls}
	--without-ssl \
	--with-gnutls=%{_prefix} \
%endif
	--enable-imap \
	--enable-pop \
	--enable-pgp \
	--enable-gpgme \
	--enable-nfs-fix \
	--enable-mailtool \
	--enable-compressed \
	--enable-sidebar \
	--disable-external-dotlock \
	--with-kyotocabinet \
	--with-sasl=%{_prefix} \
	--with-gss=%{_prefix} \
	--with-curses=%{_prefix} \
	--enable-smtp \
	--enable-hcache \
	--with-regex \
%if 0%{?suse_version} > 1315
	--with-idn2
%else
	--with-idn
%endif
make -C doc clean
make
make -C doc

%install
make install DESTDIR=%{buildroot}
install -m 755 %{S:1} %{buildroot}%{_bindir}
gzip -n -9 doc/manu*.txt
rm -f contrib/Makefile*
# datadir not automatically created:
mkdir -p %{buildroot}%{_datadir}/mutt
# INSTALL file should be removed:
rm -rf %{buildroot}%{_docdir}/%{name}/INSTALL
# mbox/mmdf manual page conflicts with the one from tin, so rename it
mv %{buildroot}%{_mandir}/man5/mbox.5 \
   %{buildroot}%{_mandir}/man5/mbox_mutt.5
mv %{buildroot}%{_mandir}/man5/mmdf.5 \
   %{buildroot}%{_mandir}/man5/mmdf_mutt.5
   %find_lang %name
# We get mime.types from aaa_base
rm -f %{buildroot}%{_sysconfdir}/mime.types
# Mutt BTS is gone
rm -f %{buildroot}%{_mandir}/man1/{flea*,muttbug*}
rm -f %{buildroot}%{_bindir}/{flea,muttbug}
rm -f %{buildroot}%{_sysconfdir}/Muttrc.dist
rm -f %{buildroot}%{_sysconfdir}/mime.types.dist
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/applications/
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/skel/.muttrc
install -D -m 644 %{SOURCE9} %{buildroot}%{_datadir}/%name/mailcap
rm -vf %{buildroot}%{_docdir}/%name/manual.txt
install -D -m 644 doc/manual.txt.gz %{buildroot}%{_docdir}/%name/

%if 0%{?suse_version}
%suse_update_desktop_file mutt
%endif

%pre
if test $1 -gt 1 -a -e %{_docdir}/%name/manual.txt.gz
then
    zcat %{_docdir}/%name/manual.txt.gz |  grep -F 'version %{version}' > /run/mutt-version || :
fi

%post
%mime_database_post
if test -f /run/mutt-version -a ! -s /run/mutt-version
then
    mkdir -p %{_localstatedir}/adm/update-messages
    cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-notify <<-'EOF'
	With %{name}-%{version} some variables and the behaviour changes:
	   $send_multipart_alternative changes to run in batch mode on ask-yes.
	   $write_bcc changes to default off
	EOF
fi

%postun
%mime_database_postun
rm -f %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-notify

%post doc
%install_info --info-dir=%{_infodir} "%{_infodir}/mutt.info.gz"

%preun doc
%install_info_delete --info-dir=%{_infodir} "%{_infodir}/mutt.info.gz"

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/skel/.muttrc
%config(noreplace) %{_sysconfdir}/Muttrc
%{_bindir}/mutt
%{_bindir}/pgpewrap
%{_bindir}/mutt_pgpring
%{_bindir}/smime_keys
%{_bindir}/Signature_conversion
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/mutt.png
%{_mandir}/man1/mutt.1%{ext_man}
%{_mandir}/man1/*pgp*.1%{ext_man}
%{_mandir}/man1/smime_keys.1%{ext_man}
%{_mandir}/man5/mmdf_mutt.5%{ext_man}
%{_mandir}/man5/muttrc.5%{ext_man}
%{_mandir}/man5/mbox_mutt.5%{ext_man}
%dir %{_datadir}/mutt/
%{_datadir}/mutt/mailcap
%dir %doc %{_docdir}/%name/
%doc %{_docdir}/%name/manual.txt.gz

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%name/COPYRIGHT
%doc %{_docdir}/%name/ChangeLog
%doc %{_docdir}/%name/GPL
%doc %{_docdir}/%name/NEWS
%doc %{_docdir}/%name/README*
%doc %{_docdir}/%name/TODO
%doc %{_docdir}/%name/*.html
%doc %{_docdir}/%name/*.txt
%dir %doc %{_docdir}/%name/samples/
%doc %{_docdir}/%name/samples/*.rc
%doc %{_docdir}/%name/samples/ca-bundle.crt
%doc %{_docdir}/%name/samples/colors.*
%doc %{_docdir}/%name/samples/markdown2html
%doc %{_docdir}/%name/samples/mutt_xtitle
%doc %{_docdir}/%name/samples/sample.*
%doc %{_docdir}/%name/samples/smime_keys_test.pl
%doc %{_docdir}/%name/samples/bgedit-detectgui.sh
%doc %{_docdir}/%name/samples/bgedit-screen-tmux.sh
%dir %doc %{_docdir}/%name/samples/iconv/
%doc %{_docdir}/%name/samples/iconv/*.rc
%doc %{_infodir}/*.gz

%files lang -f %name.lang
%defattr(-,root,root)

%changelog
