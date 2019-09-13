#
# spec file for package gnokii
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnokii
Version:        0.6.31
Release:        0
Summary:        Nokia Connectivity Program
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
Url:            http://www.gnokii.org/
Source:         http://www.gnokii.org/download/gnokii/%{name}-%{version}.tar.bz2
Source1:        xgnokii.desktop
Source2:        gnokii.xpm
Source3:        README.SUSE
# PATCH-FIX-UPSTREAM gnokii-xgnokii.patch dimstar@opensuse.org -- Fix typo which results in xgnokii not being built and installed.
Patch0:         gnokii-xgnokii.patch
# PATCH-FIX-UPSTREAM gnokii-suid_flags.patch bnc#743142 vuntz@opensuse.org -- Respect SUID_CFLAGS/SUID_LDFLAGS; sent upstream by mail on 2012-02-24
Patch1:         gnokii-suid_flags.patch
# PATCH-FIX-OPENSUSE gnokii-date-time.patch crrodriguez@opensuse.org -- Do not include __DATE__ or __TIME__ in resulting binaries.
Patch2:         gnokii-date-time.patch
# PATCH-FIX-UPSTREAM invalid-cast.patch https://savannah.nongnu.org/patch/index.php?8685 schwab@suse.de -- Fix invalid cast
Patch3:         invalid-cast.patch
BuildRequires:  bluez-devel
BuildRequires:  coreutils
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1210
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
%endif
BuildRequires:  libical-devel
# Needed for patch0 and patch1
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  mysql-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  perl-XML-Parser
%if 0%{?suse_version} > 1501
BuildRequires:  postgresql-server-devel
%else
BuildRequires:  postgresql-devel
%endif
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
PreReq:         permissions
Requires:       bluez
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
gnokii is a package of programs for communicating with a Nokia cellular
phone in Linux. Read the READMEs in /usr/share/doc/packages/gnokii to
find out which models are supported.

%package -n xgnokii
Summary:        Nokia Connectivity Program
Group:          Hardware/Mobile
Requires:       gnokii
Requires:       gtk2
Provides:       gnokii:/usr/share/xgnokii

%description -n xgnokii
xgnokii is an X Window System front-end for gnokii. gnokii has to be
installed as well.

%package smsd
Summary:        Nokia Connectivity Program
Group:          Hardware/Mobile
Requires:       gnokii
Provides:       gnokii:/usr/share/smsd

%description smsd
gnokii is a package of programs for communicating with a Nokia cellular
phone in Linux. Please read the READMEs in
/usr/share/doc/packages/gnokii to find out which models are supported.

%package devel
Summary:        Nokia Connectivity Program
Group:          Hardware/Mobile
Requires:       %{name} = %{version}
Requires:       %{name}-smsd = %{version}

%description devel
gnokii is a package of programs for communicating with a Nokia cellular
phone in Linux. Please read the READMEs in
/usr/share/doc/packages/gnokii to find out which models are supported.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Needed by patch0 and patch1
autoreconf -fi
export CFLAGS="%{optflags} -fgnu89-inline -D_GNU_SOURCE -fPIC -Wall -Wno-unused -fstack-protector -fno-strict-aliasing -fPIE"
export LDFLAGS="$LDFLAGS -pie"
export SUID_CFLAGS="-fPIE"
export SUID_LDFLAGS="-pie"
%configure \
    --enable-nls \
    --enable-security \
    --disable-static \
    --with-x
make %{?jobs:-j%jobs}
make -C smsd %{?jobs:-j%jobs}

%install
cp %{S:3} .
%makeinstall
make DESTDIR=%{buildroot} -C smsd install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/smsd/*.la
mkdir -p %{buildroot}%{_sysconfdir}
sed "s:/usr/local/sbin:%{_sbindir}:g" Docs/sample/gnokiirc > %{buildroot}%{_sysconfdir}/gnokiirc
chmod +x %{buildroot}%{_bindir}/sendsms
%find_lang %{name} %{?no_lang_C}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/gnokii.xpm
%suse_update_desktop_file -i xgnokii Utility TelephonyTools Calendar ContactManagement Office GTK
# prepare documentation
find Docs -name 'Makefile.*' -exec rm -f {} \;
rm -rf Docs/man %{buildroot}%{_datadir}/doc/%{name}
chmod -x Docs/gnokii.nol
mv Docs/sample Docs/examples

%post
/sbin/ldconfig
%set_permissions %{_sbindir}/mgnokiidev

%verifyscript
%verify_permissions -e %{_sbindir}/mgnokiidev

%postun -p /sbin/ldconfig

%if 0%{?suse_version} > 1130

%post -n xgnokii
%desktop_database_post
%endif

%if 0%{?suse_version} > 1130

%postun -n xgnokii
%desktop_database_postun
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/gnokiirc
%doc COPYING COPYRIGHT ChangeLog MAINTAINERS TODO Docs/*
%doc %{_mandir}/man1/gnokii*
%doc %{_mandir}/man8/gnokiid*
%doc %{_mandir}/man8/mgnokiidev*
%{_bindir}/gnokii
%{_bindir}/gnokiid
%{_libdir}/*.so.*
%verify(not mode) %attr(0755, root, uucp) %{_sbindir}/mgnokiidev

%files -n xgnokii
%defattr(-,root,root)
%doc %{_mandir}/man1/xgnokii*
%{_bindir}/xgnokii
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files smsd
%defattr(-,root,root)
%doc %{_mandir}/man1/sendsms*
%doc %{_mandir}/man8/smsd*
%{_bindir}/sendsms
%{_bindir}/smsd
%dir %{_libdir}/smsd
%{_libdir}/smsd/libsmsd_file.so
%{_libdir}/smsd/libsmsd_mysql.so
%{_libdir}/smsd/libsmsd_pq.so
%{_libdir}/smsd/libsmsd_sqlite.so

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/gnokii.h
%{_includedir}/gnokii/

%files lang -f %{name}.lang

%changelog
