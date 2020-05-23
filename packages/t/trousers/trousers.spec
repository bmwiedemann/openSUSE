#
# spec file for package trousers
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


%define tpmstatedir %{_localstatedir}/lib/tpm
Name:           trousers
Version:        0.3.14
Release:        0
Summary:        TSS (TCG Software Stack) access daemon for a TPM chip
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            http://trousers.sourceforge.net/
Source0:        http://downloads.sf.net/trousers/%{name}-%{version}.tar.gz
Source1:        tcsd.service
Source2:        baselibs.conf
Source3:        91-trousers.rules
Patch0:         fix-lto.patch
Patch1:         bsc1164472.patch
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  udev
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The trousers package provides a TSS implementation through the help of
a user-space daemon, the tcsd, and a library  Trousers aims to be
compliant to the 1.1b and 1.2 TSS specifications as available from the
Trusted Computing website http://www.trustedcomputinggroup.org/.

The package needs the /dev/tpm device file to be present on your
system. It is a character device file major 10 minor 224, 0600 tss:tss.

%package devel
Summary:        TSS (TCG Software Stack) access daemon for a TPM chip
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libopenssl-devel
Requires:       libtspi1 = %{version}
Requires:       trousers = %{version}

%description devel
The trousers package provides a TSS implementation through the help of
a user-space daemon, the tcsd, and a library  Trousers aims to be
compliant to the 1.1b and 1.2 TSS specifications as available from the
Trusted Computing website http://www.trustedcomputinggroup.org/.

The package needs the /dev/tpm device file to be present on your
system. It is a character device file major 10 minor 224, 0600 tss:tss.

%package -n libtspi1
Summary:        TSS (TCG Software Stack) access daemon for a TPM chip
Group:          Productivity/Security
Requires:       trousers

%description -n libtspi1
The trousers package provides a TSS implementation through the help of
a user-space daemon, the tcsd, and a library  Trousers aims to be
compliant to the 1.1b and 1.2 TSS specifications as available from the
Trusted Computing website http://www.trustedcomputinggroup.org/.

The package needs the /dev/tpm device file to be present on your
system. It is a character device file major 10 minor 224, 0600 tss:tss.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
    CC=gcc
CFLAGS="%{optflags} -Wall -fno-strict-aliasing -fgnu89-inline -ffat-lto-objects"
 SHARE=%{_prefix}/share
   DOC=%{_defaultdocdir}
export CC CFLAGS
autoreconf -i -f
%configure --libdir=/%{_lib} --disable-static --with-pic --with-gui=none
make %{?_smp_mflags}

%install
%define trousers_data %{buildroot}%{_datadir}/%{name}
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/tcsd.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rctcsd
# these files can be used to fake trousers ownership of a TPM if the ownership
# was already taken by some other stack. they are sample files.
mkdir -p %{trousers_data}
cp -a dist/system.data* %{trousers_data}

mkdir -p %{buildroot}%{_libdir}
ln -s -v /%{_lib}/$(readlink %{buildroot}/%{_lib}/libtspi.so) %{buildroot}%{_libdir}/libtspi.so
rm -v %{buildroot}/%{_lib}/libtspi.{so,la}
mv -v %{buildroot}/%{_lib}/*.a %{buildroot}%{_libdir}

# we want to run tcsd as tss user right away. therefore we need to install a
# suitable udev rule file. this conflicts somewhat with tpm2-0-tss, but both
# rules files are compatible at the moment. trousers has a lower priority than
# tpm2-0-tss in case both should be installed. The tss user is shared between
# both packages anyways already.
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}

%pre
%service_add_pre tcsd.service

%post
%service_add_post tcsd.service
%_bindir/udevadm trigger -s tpm || :

# bsc#1164472: adjust potential root ownership to allow tcsd to open the file
# as unprivileged user. Be careful not to follow a symlink target.
system_data=%{tpmstatedir}/system.data

if [ -e "${system_data}" ]; then
	chown --no-dereference tss:tss %{tpmstatedir}/system.data
fi

%postun
%service_del_postun tcsd.service

%preun
%service_del_preun tcsd.service

%post -n libtspi1 -p /sbin/ldconfig

%postun -n libtspi1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config(noreplace) %attr(640,root,tss) %{_sysconfdir}/tcsd.conf
%doc README README.selinux AUTHORS ChangeLog LICENSE NICETOHAVES TODO doc/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_datadir}/%{name}
%{_sbindir}/tcsd
%{_sbindir}/rctcsd
%{_unitdir}/tcsd.service
%{_udevrulesdir}/91-trousers.rules

%files devel
%defattr(-,root,root)
%{_includedir}/trousers
%{_includedir}/tss
%{_mandir}/man3/*
%{_libdir}/*.so
#only available in static form
%{_libdir}/libtddl.a

%files -n libtspi1
%defattr(-,root,root)
/%{_lib}/*.so.*

%changelog
