#
# spec file for package inn
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


Name:           inn
BuildRequires:  bison
BuildRequires:  gdbm-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  postfix
BuildRequires:  python-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(GD)
BuildRequires:  perl(MIME::Parser)
URL:            https://www.isc.org/othersoftware/#INN
Summary:        InterNetNews
License:        GPL-2.0-or-later AND BSD-4-Clause
Group:          Productivity/Networking/News/Servers
Provides:       inn_pkg
Provides:       nntp_daemon
Conflicts:      cnews nntpd mininews
PreReq:         perl permissions
PreReq:         group(uucp)
PreReq:         user(news)
PreReq:         group(news)
Requires:       perl-MIME-tools
Requires:       perl(GD)
Requires:       perl(MIME::Parser)
%{?systemd_requires}
%{?libperl_requires}
Version:        2.6.3
Release:        0
%define PatchVersion -%{version}
Source:         inn%{PatchVersion}.tar.gz
Source1:        doc-inn.tar.bz2
Source2:        pubring.pgp
Source3:        inn-emptydb.tar.gz
Source4:        inn.reg
Source5:        inn%{PatchVersion}.tar.gz.asc
Source6:        %{name}.keyring
Source7:        inn.service
Patch0:         inn-%{version}.diff
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#

%description
Rich Salz's InterNetNews news transport system.

%package devel
Requires:       %name = %version
Summary:        InterNetNews development files
Group:          Development/Languages/C and C++
Requires:       bison
Requires:       gdbm-devel
Requires:       pam-devel
Requires:       zlib-devel

%description devel
Rich Salz's InterNetNews news transport system.

This package contains the files needed to develop software depending on
inn.

%package -n mininews
Summary:        Inews - Post News from an NNTP Client
Group:          Productivity/Networking/News/Utilities
Provides:       nntp_daemon
PreReq:         permissions
PreReq:         group(uucp)
PreReq:         user(news)
PreReq:         group(news)

%description -n mininews
Rich Salz's InterNetNews news transport system.

%prep
%setup -n inn%{PatchVersion} 
%setup -n inn%{PatchVersion} -D -T -a 1 
%setup -n inn%{PatchVersion} -D -T -a 3
%patch0 -p1
cp -a $RPM_SOURCE_DIR/pubring.pgp .

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
LDFLAGS="-pie" CFLAGS="$RPM_OPT_FLAGS -pipe -fno-strict-aliasing -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -fPIE -fstack-protector -fcommon" ./configure \
		--enable-uucp-rnews \
		--enable-setgid-inews \
		--prefix=/usr/lib/news \
		--sysconfdir=/etc/news \
		--mandir=%{_mandir} \
		--disable-shared \
		--enable-tagged-hash \
		--with-perl \
		--with-zlib \
        --with-python \
        --with-openssl \
		--with-sendmail=/usr/sbin/sendmail \
		--with-news-user=news \
		--with-news-group=news \
		--with-news-master=news \
		--with-db-dir=/var/lib/news \
		--with-run-dir=/var/run/news \
		--with-log-dir=/var/log/news \
		--with-http-dir=/var/log/news/http \
		--with-spool-dir=/var/spool/news \
		--with-tmp-dir=/var/spool/news/tmp
make
cp site/inn.conf inn.conf.tmp
echo 'domain: test.com' >> inn.conf.tmp
echo "runasuser: $(id -n -u)" >> inn.conf.tmp
echo "runasgroup: $(id -n -g)" >> inn.conf.tmp
INNCONF=inn.conf.tmp expire/makedbz -f `pwd`/inn-emptydb/history -s 666666
rm -f inn.conf.tmp

%install
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/var/lib
mkdir -p %{buildroot}/var/log
mkdir -p %{buildroot}/var/spool
mkdir -p %{buildroot}%{_mandir}
#
make DESTDIR=%{buildroot} OWNER= ROWNER= install
for i in %{buildroot}%{_mandir}/*/* ; do
  if test -L "$i" ; then
    il=$(readlink "$i")
    ln -s "$il.gz" "$i.gz"
    rm -f "$i"
  else
    gzip -nf9 "$i"
  fi
done
chmod 444 %{buildroot}/usr/lib/news/lib/*.a
# those just die("BerkeleyDB support not compiled");
rm %{buildroot}/usr/lib/news/bin/ovdb_server
rm %{buildroot}/usr/lib/news/bin/ovdb_stat
ln %{buildroot}/usr/lib/news/bin/ovdb_init %{buildroot}/usr/lib/news/bin/ovdb_server
ln %{buildroot}/usr/lib/news/bin/ovdb_init %{buildroot}/usr/lib/news/bin/ovdb_stat
#
#
# 
%define installnews install -o news -g news -m
%define installnews install -m
%define installroot install -o root -g root -m
%define installroot install -m
%{installnews} 0755 	-d		%{buildroot}/var/log/news/http
%{installnews} 0644	subscriptions	%{buildroot}/etc/news
%{installnews} 0644	distributions	%{buildroot}/etc/news
%{installnews} 0644	crontab.sample	%{buildroot}/etc/news
%{installnews} 0644	profile		%{buildroot}/etc/news/.profile
%{installnews} 0755 	-d		%{buildroot}/etc/news/.pgp
%{installnews} 0600	pubring.pgp	%{buildroot}/etc/news/.pgp
%{installnews} 0644	samples/send-uucp.cf	%{buildroot}/etc/news
%{installnews} 0755 	-d		%{buildroot}/var/log/news/http
%{installnews} 0755 	-d		%{buildroot}/var/log/news/http/pics
%{installnews} 0555	convertspool	%{buildroot}/usr/lib/news/bin
%{installnews} 0755 	-d		%{buildroot}/usr/lib/news/include
%{installnews} 0755 	-d		%{buildroot}/usr/lib/news/include/inn
#
# 
#
%{installnews} 0644	inn-emptydb/*	%{buildroot}/var/lib/news
%{installnews} 0755 	-d		%{buildroot}/var/lib/news/backoff
#
# compat links
#
ln -sf bin/inews		%{buildroot}/usr/lib/news/inews
ln -sf ../lib/news/bin/inews	%{buildroot}/usr/bin/inews
ln -sf ../lib/news/bin/rnews	%{buildroot}/usr/bin/rnews
#
# other links
#
ln -sf ../innfeed.status	%{buildroot}/var/log/news/http/innfeed.status.txt
ln -sf ../inn.status		%{buildroot}/var/log/news/http/inn.status.txt
#
# 
# 
%{installnews} 0755	-d		%{buildroot}/usr/lib/systemd/system
%{installroot} 0644	%{SOURCE7}	%{buildroot}/usr/lib/systemd/system/inn.service
%{installnews} 0755	-d		%{buildroot}/usr/sbin
ln -sf service 	%{buildroot}/usr/sbin/rcinn
#
touch				%{buildroot}/var/log/news/news
touch				%{buildroot}/var/log/news/news.notice
touch				%{buildroot}/var/log/news/news.err
touch				%{buildroot}/var/log/news/news.crit
touch				%{buildroot}/var/log/news/inn.status
touch				%{buildroot}/var/log/news/innfeed.status
#
# SLP regfile
#
%{installroot} 0755	-d		%{buildroot}/etc/slp.reg.d
%{installroot} 0644	%{SOURCE4}	%{buildroot}/etc/slp.reg.d/
# /var/run/news
mkdir -p $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/
echo "d /var/run/news 0750 news news -" > %{buildroot}/usr/lib/tmpfiles.d/inn.conf

#
# build filelist
# 
%define filelist %{name}-filelist
find %{buildroot} -type d -printf "/%%P\n" | awk '
! /^\/(etc|usr\/lib|var\/lib|var\/log|var\/spool|var\/run)\/news/ { next }
$0 == "/etc/news"     { next }
$0 == "/usr/lib/news/include" { next }
$0 == "/usr/lib/news/include/inn" { next }
$0 == "/var/run/news" { next }
{ pfx="" }
$0 == "/usr/lib/news" { pfx = "%%attr(755,root,root) " }
$0 == "/var/lib/news" { pfx = "%%attr(755,news,news) " }
$0 == "/usr/lib/news/bin" { pfx = "%%attr(755,root,root) " }
$0 == "/var/spool/news" { pfx = "%%attr(775,news,news) " }
$0 == "/var/run/news" { pfx = "%ghost %%attr(750,news,news) "}
/\/news/ {
 	if (!match(pfx, /%%attr/)) pfx = "%%attr(-,news,news) " pfx
}
{ print "%dir " pfx $0 }
' > %{filelist}
find %{buildroot} ! -type d -printf "/%%P\n" | awk '
{ pfx="" }
/^\/usr\/lib\/news\/include/              { next }
/^\/usr\/lib\/news\/lib\/.*\.a/             { next }
$0 == "/usr/lib/news/bin/inews"           { pfx="%attr(2555,news,news) " }
$0 == "/usr/lib/news/bin/rnews"           { pfx="%attr(4550,news,uucp) " }
$0 == "/usr/lib/news/bin/innbind"         { pfx="%verify(not mode) %attr(4550,root,news) " }
/^\/(etc\/news|usr\/lib\/news\/bin\/filter|var\/lib\/news)\// {
	pfx="%config(noreplace) "pfx
}
/\/man\/man/ {
	pfx="%doc %attr(444,root,root) "pfx
}
/^\/var\/log\/news\/(news|inn\.status|innfeed\.status)/ {
	pfx="%ghost %attr(644,news,news) "pfx
}
/\/news\// {
 	if (!match(pfx, /%%attr/)) pfx = "%%attr(-,news,news) " pfx
}
/^\/etc\/slp\.reg\.d\// { next }
{ print pfx $0 }
' >> %{filelist}
#
# 
# 

%pre
test -f var/log/news && mv var/log/news var/log/news.bak
%service_add_pre inn.service
exit 0

%post
runuser -u news -g news touch \
    var/log/news/news.notice \
    var/log/news/news.err \
    var/log/news/news.crit \
    var/log/news/news \
    var/log/news/inn.status \
    var/log/news/innfeed.status
if test -e usr/lib/news/bin/control/version -o -e usr/lib/news/bin/inndstart ; then
    rm -f etc/news/inn.conf.OLD
    rm -f etc/news/newsfeeds.OLD
    usr/lib/news/bin/innupgrade etc/news
fi
if ! test -d /var/run/news ; then
    install -d -m 750 -o news -g news /var/run/news
fi
%set_permissions /usr/lib/news/bin/innbind /usr/lib/news/bin/inews /usr/lib/news/bin/rnews
%service_add_post inn.service
%tmpfiles_create inn.conf

%post -n mininews
%set_permissions /usr/lib/news/bin/inews /usr/lib/news/bin/rnews
%tmpfiles_create inn.conf

%verifyscript
%verify_permissions -e /usr/lib/news/bin/innbind -e /usr/lib/news/bin/inews -e /usr/lib/news/bin/rnews

%verifyscript -n mininews
%verify_permissions -e /usr/lib/news/bin/inews -e /usr/lib/news/bin/rnews

%preun
%service_del_preun inn.service

%postun
%service_del_postun inn.service

%files -f %{filelist}
%defattr(-,root,root)
%dir			/etc/slp.reg.d
%config(noreplace)	/etc/slp.reg.d/inn.reg
%doc ChangeLog NEWS INSTALL README*
%doc doc-inn/*

%files devel
%defattr(-,root,root)
/usr/lib/news/include
/usr/lib/news/lib/*.a

%files -n mininews
%defattr(-,root,root)
%config(noreplace)      /etc/news/inn.conf
%dir                    /usr/lib/news/bin
%attr(4550,news,uucp)   /usr/lib/news/bin/rnews
%attr(2555,news,news)   /usr/lib/news/bin/inews
                        /usr/bin/[ri]news
                        /usr/lib/news/[ri]news
%doc                    %{_mandir}/*/inn.conf.*
%doc                    %{_mandir}/*/[ri]news.*

%changelog
