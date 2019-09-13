#
# spec file for package bitlbee
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define daemon_piddir /run/%{name}
Name:           bitlbee
Version:        3.5.1
Release:        0
Summary:        IRC to other Chat Networks Gateway
License:        GPL-2.0-only
Group:          Productivity/Networking/IRC
URL:            http://www.bitlbee.org/
Source:         http://get.bitlbee.org/src/bitlbee-%{version}.tar.gz
Source2:        %{name}.service-suse.in
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-base
%endif
BuildRequires:  util-linux-systemd
BuildRequires:  w3m
BuildRequires:  xmlto
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libotr) >= 4.0.0
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
Requires(pre):  shadow

%description
BitlBee is a gateway between instant messaging and an IRC client.
With it, one's IRC client program can be reused and no extra IM program
will need to run.

This package comes with support for MSN, Jabber, Oscar and Yahoo, as well as
enabled flood protection.

%package doc
Summary:        IRC to other Chat Networks Gateway (User Guide)
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}

%description doc
BitlBee is a gateway between instant messaging and an IRC client.
With it, one's IRC client program can be reused and no extra IM program
will need to run.

This package contains the user guide:
  %{_docdir}/%{name}/user-guide

%package devel
Summary:        IRC to other Chat Networks Gateway (Devel files)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
BitlBee is a gateway between instant messaging and an IRC client.
With it, one's IRC client program can be reused and no extra IM program
will need to run.

This package contains development files for external plugins.

%prep
%setup -q

# make it verbose!
find . -name Makefile -exec sed -i.orig 's|@$(CC)|$(CC)|;s|@$(LD)|$(LD)|' {} +

%build
# not autoconf - cannot use %%configure
%if 0%{?suse_version} >= 1500
PYTHON=python3 \
%endif
CFLAGS="%{optflags} -fno-strict-aliasing" \
CXXFLAGS="%{optflags} -fno-strict-aliasing" \
./configure \
    --prefix="%{_prefix}" \
    --bindir="%{_sbindir}" \
    --etcdir="%{_sysconfdir}/%{name}" \
    --mandir="%{_mandir}" \
    --pcdir="%{_libdir}/pkgconfig" \
    --datadir="%{_datadir}/%{name}" \
    --plugindir="%{_libdir}/%{name}" \
    --pidfile="%{daemon_piddir}/%{name}.pid" \
    --config="%{_localstatedir}/lib/%{name}" \
    --ipcsocket="%{daemon_piddir}/%{name}.sock" \
    --purple=1 \
    --otr=1 \
    --msn=1 \
    --jabber=1 \
    --twitter=1 \
    --oscar=1 \
    --yahoo=1 \
    --sipe=1 \
    --debug=0 \
    --strip=0 \
    --gcov=0 \
    --flood=0 \
    --plugins=1 \
    --ssl=gnutls

make %{?_smp_mflags}

%install
install -d "%{buildroot}%{_mandir}/man1"
install -d "%{buildroot}%{_mandir}/man8"
install -d "%{buildroot}%{_sysconfdir}/bitlbee"
install -d "%{buildroot}%{_localstatedir}/lib/bitlbee"

make DESTDIR=%{buildroot} -C doc
make DESTDIR=%{buildroot} install install-etc
make DESTDIR=%{buildroot} install-dev

%fdupes -s

install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}

install -d "%{buildroot}%{_docdir}/%{name}"
LM="$PWD/%{name}.lang"
echo -n > "$LM"
for f in COPYING doc/AUTHORS doc/CHANGES doc/CREDITS doc/FAQ doc/README; do
    b="${f##*/}"
    install -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$b"
    echo "%doc %{_docdir}/%{name}/$b" >>"$LM"
done

pushd doc/user-guide
make user-guide.html user-guide.txt
popd
install -d "%{buildroot}%{_docdir}/%{name}/user-guide"
cp -a doc/user-guide/*.{txt,html} "%{buildroot}%{_docdir}/%{name}/user-guide/"


%pre
getent passwd bitlbee >/dev/null || useradd -r -U -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "user for %{name}" bitlbee
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files -f %{name}.lang
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%attr(0750,root,bitlbee) %dir %{_sysconfdir}/bitlbee
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%config(noreplace) %attr(0640,root,bitlbee) %{_sysconfdir}/bitlbee/bitlbee.conf
%config(noreplace) %attr(0640,root,bitlbee) %{_sysconfdir}/bitlbee/motd.txt
%{_sbindir}/bitlbee
%{_datadir}/bitlbee
%{_mandir}/man5/bitlbee.conf.5%{ext_man}
%{_mandir}/man8/bitlbee.8%{ext_man}
%attr(0750,bitlbee,bitlbee) %dir %{_localstatedir}/lib/bitlbee

%files doc
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/user-guide

%files devel
%defattr(-,root,root)
%{_includedir}/bitlbee/
%{_libdir}/pkgconfig/bitlbee.pc

%changelog
