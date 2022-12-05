#
# spec file for package mutt
#
# Copyright (c) 2022 SUSE LLC
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


%global         _sysconfdir %{_sysconfdir}
%bcond_with    mutt_openssl
%bcond_without mutt_gnutls
Name:           mutt
Version:        2.2.9
Release:        0
Summary:        Mail Program
# ftp://ftp.mutt.org/mutt/devel/
# https:///bitbucket.org/mutt/mutt/downloads/%%name-%%version.tar.gz
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            http://www.mutt.org
Source0:        https://bitbucket.org/mutt/mutt/downloads/mutt-%{version}.tar.gz
Source1:        Signature_conversion
Source2:        README.alternates
Source3:        mutt.png
Source4:        mutt.desktop
Source5:        skel.muttrc
Source6:        mutt_oauth2.py-3.6
Source7:        mutt_oauth2.py.README
Source8:        backports-datetime-fromisoformat-1.0.0.tar.gz
Source9:        mutt.mailcap
Source10:       https://bitbucket.org/mutt/mutt/downloads/mutt-%{version}.tar.gz.asc
Source11:       mutt.keyring
Patch0:         %{name}-1.13.3.dif
# http://www.spinnaker.de/mutt/compressed/
Patch2:         %{name}-1.5.9i-pgpewrap.diff
Patch3:         %{name}-1.5.20-sendgroupreplyto.diff
Patch4:         %{name}-1.5.15-wrapcolumn.diff
Patch7:         mutt-1.6.1-opennfs.dif
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
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-gssapi
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  hunspell
BuildRequires:  iso_ent
BuildRequires:  libgpgme-devel
BuildRequires:  libxslt-tools
BuildRequires:  opensp
BuildRequires:  pkgconfig
BuildRequires:  w3m
BuildRequires:  pkgconfig(gssrpc)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libsasl2)
%if 0%{suse_version} >= 1500
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif
Requires:       glibc-locale
Requires(post): %{_bindir}/cat
Requires(post): %{_bindir}/mkdir
Requires(postun):%{_bindir}/rm
Requires(pre):  %{_bindir}/grep
Requires(pre):  %{_bindir}/zcat
Recommends:     hunspell
Recommends:     mutt-doc
Recommends:     mutt-lang
Recommends:     urlscan
Recommends:     urlview
Recommends:     w3m
%if %{with mutt_openssl}
BuildRequires:  pkgconfig(openssl)
%endif
%if %{with mutt_gnutls}
BuildRequires:  pkgconfig(gnutls)
%endif
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
%if 0%{?suse_version} > 1130
Requires(post): shared-mime-info
Requires(postun):shared-mime-info
%endif

%description
A very powerful mail user agent. It supports (among other nice things)
highlighting, threading, and PGP. It takes some time to get used to,
however. This version is based on NeoMutt, that is it includes many
enhancements.

%package doc
Summary:        Additional Documentation about Mutt
Group:          Documentation/Other
Requires:       %{name} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
Recommends:     perl(Expect)
Provides:       %{name}:%{_docdir}/%{name}/COPYRIGHT
BuildArch:      noarch

%description doc
Some extend documentation about mutt together with muttrc examples
for different environments and requirements.

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Languages for Mutt
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       mutt:%{_datadir}/locale/en_GB/LC_MESSAGES/mutt.mo
BuildArch:      noarch

%description lang
Provides translations to the package mutt.

%prep
%setup -q -n mutt-%{version}
%patch0  -b .p0
%patch2  -b .pgpewrap
%patch3  -b .sendgroupreplyto
%patch4  -b .wrapcolumn
%patch7  -b .opennfs
%patch11  -b .listreply
%patch12  -b .pgp_verbose_mtime
%patch15  -b .widechar.sidebar
%patch16  -b .crlf
%patch18  -b .mailcap
%patch19  -b .cvw2014.9116
%patch20  -b .imap
%patch21  -b .quit

cp %{SOURCE2} .

%build
%if %{with mutt_gnutls}
echo 'set ssl_ca_certificates_file="%{_sysconfdir}/ssl/ca-bundle.pem"' >> doc/Muttrc.head
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
CFLAGS="-Wall %{optflags} -I. -D_GNU_SOURCE"
cflags -fno-strict-aliasing		CFLAGS
cflags -fstack-protector		CFLAGS
cflags -fPIE				CFLAGS
cflags -g3				CFLAGS
cflags -pipe				CFLAGS
cflags -Wl,--as-needed			LDFLAGS
cflags -Wl,-O2				LDFLAGS
cflags -pie				LDFLAGS
export CC CFLAGS LDFLAGS
export SENDMAIL=%{_sbindir}/sendmail
export ISPELL=%{_bindir}/hunspell
export PATH="%{_prefix}/lib/mit/bin:$PATH"
export KRB5CFGPATH="$(type -p krb5-config)"
$KRB5CFGPATH --cflags gssapi
$KRB5CFGPATH --libs gssapi
$KRB5CFGPATH --version
%configure \
	--with-docdir=%{_docdir}/%{name} \
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
	--enable-debug \
%if 0%{?suse_version} > 1315
	--with-idn2
%else
	--with-idn
%endif
%make_build -C doc clean
%make_build
%make_build -C doc

%install
%make_install
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}
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
   %find_lang %{name}
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
install -D -m 644 %{SOURCE9} %{buildroot}%{_datadir}/%{name}/mailcap
rm -vf %{buildroot}%{_docdir}/%{name}/manual.txt
install -D -m 644 doc/manual.txt.gz %{buildroot}%{_docdir}/%{name}/

sed -rn '/Command formats for gpg/,$p' %{SOURCE5} >> %{buildroot}%{_sysconfdir}/Muttrc

%if 0%{?suse_version}
%suse_update_desktop_file mutt
%endif

%if 0%{suse_version} >= 1500
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 755 %{SOURCE6} %{buildroot}%{_docdir}/%{name}/mutt_oauth2.py
install -m 644 %{SOURCE7} %{buildroot}%{_docdir}/%{name}/mutt_oauth2.py.README
%if %{?pkg_vcmp:%{pkg_vcmp python3-base < 3.7.0}}%{!?pkg_vcmp:0}
tar xf %{SOURCE8}
pushd backports-datetime-fromisoformat-1.0.0
    python3 setup.py install --root %{buildroot}
popd
%endif
%endif

%pre
if test $1 -gt 1 -a -e %{_docdir}/%{name}/manual.txt.gz
then
    zcat %{_docdir}/%{name}/manual.txt.gz |  grep -F 'version %{version}' > /run/mutt-version || :
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
%config(noreplace) %{_sysconfdir}/skel/.muttrc
%config(noreplace) %{_sysconfdir}/Muttrc
%{_bindir}/mutt
%{_bindir}/pgpewrap
%{_bindir}/mutt_pgpring
%{_bindir}/smime_keys
%{_bindir}/Signature_conversion
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/mutt.png
%{_mandir}/man1/mutt.1%{?ext_man}
%{_mandir}/man1/*pgp*.1%{?ext_man}
%{_mandir}/man1/smime_keys.1%{?ext_man}
%{_mandir}/man5/mmdf_mutt.5%{?ext_man}
%{_mandir}/man5/muttrc.5%{?ext_man}
%{_mandir}/man5/mbox_mutt.5%{?ext_man}
%dir %{_datadir}/mutt/
%{_datadir}/mutt/mailcap
%dir %doc %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/manual.txt.gz
%if 0%{suse_version} >= 1500
%{_docdir}/%{name}/mutt_oauth2.py
%{_docdir}/%{name}/mutt_oauth2.py.README
%if %{?pkg_vcmp:%{pkg_vcmp python3-base < 3.7.0}}%{!?pkg_vcmp:0}
%{python3_sitearch}/backports
%{python3_sitearch}/backports_datetime_fromisoformat-1.0.0-py3.6.egg-info
%endif
%endif

%files doc
%doc %{_docdir}/%{name}/COPYRIGHT
%doc %{_docdir}/%{name}/ChangeLog
%doc %{_docdir}/%{name}/GPL
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/*.txt
%dir %doc %{_docdir}/%{name}/samples/
%doc %{_docdir}/%{name}/samples/*.rc
%doc %{_docdir}/%{name}/samples/ca-bundle.crt
%doc %{_docdir}/%{name}/samples/colors.*
%doc %{_docdir}/%{name}/samples/markdown2html
%doc %{_docdir}/%{name}/samples/mutt_oauth2.py
%doc %{_docdir}/%{name}/samples/mutt_oauth2.py.README
%doc %{_docdir}/%{name}/samples/mutt_xtitle
%doc %{_docdir}/%{name}/samples/sample.*
%doc %{_docdir}/%{name}/samples/smime_keys_test.pl
%doc %{_docdir}/%{name}/samples/bgedit-detectgui.sh
%doc %{_docdir}/%{name}/samples/bgedit-screen-tmux.sh
%dir %doc %{_docdir}/%{name}/samples/iconv/
%doc %{_docdir}/%{name}/samples/iconv/*.rc
%{_infodir}/*.gz

%files lang -f %{name}.lang

%changelog
