#
# spec file for package aide
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


Name:           aide
Version:        0.18
Release:        0
Summary:        Advanced Intrusion Detection Environment
License:        GPL-2.0-or-later
URL:            https://aide.github.io/
Source0:        https://github.com/aide/aide/releases/download/v%{version}/aide-%{version}.tar.gz
Source1:        aide.conf
Source2:        aide-cron_daily.sh
Source3:        aide-test.sh
Source4:        aide.service
Source5:        aide.service.8
Source6:        aide.timer
Source7:        aide.timer.8
Source8:        aide_service.conf
Source42:       https://github.com/aide/aide/releases/download/v%{version}/aide-%{version}.tar.gz.asc
Source43:       aide.keyring
Patch1:         aide-0.18-as-needed.patch
Patch2:         aide-xattr-in-libc.patch
Patch3:         aide-systemd.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  flex
BuildRequires:  gzip
BuildRequires:  libacl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel

%description
AIDE is an intrusion detection system that checks file integrity.

%package test
Summary:        Simple AIDE testing

%description test
Simple AIDE test script for externalized testing.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure 					\
	--with-config_file=%{_sysconfdir}/aide.conf	\
	--with-dbhmactype=md5			\
	--disable-static			\
	--enable-lfs				\
	--with-posix-acl			\
	--with-xattr				\
	--with-selinux				\
	--with-curl				\
	--with-zlib \
    --with-gcrypt \
    --without-mhash
# --enable-forced_configmd
%make_build

%install
%make_install
install -m 700 -d     %{buildroot}%{_localstatedir}/lib/aide
install -m 700 -d     %{buildroot}%{_sysconfdir}
install -m 700 -d     %{buildroot}%{_unitdir}/
install -m 700 -d     %{buildroot}%{_mandir}/man8
install -m 600 %{SOURCE1} %{buildroot}%{_sysconfdir}/aide.conf
install -m 700 %{SOURCE3} %{buildroot}%{_bindir}/
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/aide.service
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/aide.timer
install -m 644 %{SOURCE5} %{buildroot}%{_mandir}/man8/aide.service.8
install -m 644 %{SOURCE7} %{buildroot}%{_mandir}/man8/aide.timer.8
install -m 600 %{SOURCE8} %{buildroot}%{_sysconfdir}/aide_service.conf
gzip -9 %{buildroot}%{_mandir}/man8/aide.service.8
gzip -9 %{buildroot}%{_mandir}/man8/aide.timer.8
mkdir -p doc/examples%{_sysconfdir}/cron.daily/
cp -a %{SOURCE2} doc/examples%{_sysconfdir}/cron.daily/aide.sh

%post
if ! grep -q "database_in" %{_sysconfdir}/aide.conf ; then
  # with the 0.17 update some backward incompatible changes were made to the config file. Therefore, we have to adapt those parameters, otherwise the program will fail
  sed -i 's/database=/database_in=/' %{_sysconfdir}/aide.conf
  sed -i '/verbose=/d' %{_sysconfdir}/aide.conf
  sed -i 's/\t/ /g' %{_sysconfdir}/aide.conf
fi
%systemd_post %{name}.service %{name}.timer

%preun
%systemd_preun %{name}.service %{name}.timer

%postun
%systemd_postun %{name}.service %{name}.timer

%check
rm -rf %{_localstatedir}/tmp/aide-test
mkdir %{_localstatedir}/tmp/aide-test
export TESTDIR=%{_localstatedir}/tmp/aide-test
%make_build DESTDIR=$TESTDIR install
install -m 700 -d $TESTDIR%{_localstatedir}/lib/aide
install -m 700 -d $TESTDIR%{_sysconfdir}
install -m 600    %{SOURCE1} $TESTDIR%{_sysconfdir}/aide.conf.new
sed -e "s#%{_localstatedir}/lib/aide#$TESTDIR%{_localstatedir}/lib/aide#g" <$TESTDIR%{_sysconfdir}/aide.conf.new >$TESTDIR%{_sysconfdir}/aide.conf
if ! grep -q "database_in" %{_sysconfdir}/aide.conf ; then
  # with the 0.17 update some backward incompatible changes were made to the config file. Therefore, we have to adapt those parameters, otherwise the program will fail
  sed -i 's/database=/database_in=/' $TESTDIR%{_sysconfdir}/aide.conf
  sed -i '/verbose=/d' $TESTDIR%{_sysconfdir}/aide.conf
  sed -i 's/\t/ /g' $TESTDIR%{_sysconfdir}/aide.conf
fi
$TESTDIR/usr/bin/aide -D -c $TESTDIR%{_sysconfdir}/aide.conf
sleep 2
sync
sleep 2

$TESTDIR/usr/bin/aide -c $TESTDIR%{_sysconfdir}/aide.conf --init
mv $TESTDIR%{_localstatedir}/lib/aide/aide.db.new $TESTDIR%{_localstatedir}/lib/aide/aide.db
$TESTDIR/usr/bin/aide -c $TESTDIR%{_sysconfdir}/aide.conf --check --log-level=info

rm -rf $TESTDIR

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README doc/examples
%{_bindir}/aide
/%{_mandir}/man1/aide.1.gz
/%{_mandir}/man5/aide.conf.5.gz
%{_localstatedir}/lib/aide
%config(noreplace) %{_sysconfdir}/aide.conf
%config(noreplace) %{_sysconfdir}/aide_service.conf
%{_unitdir}/aide.service
%{_unitdir}/aide.timer
%{_mandir}/man8/aide.timer.8*
%{_mandir}/man8/aide.service.8*

%files test
%{_bindir}/aide-test.sh

%changelog
