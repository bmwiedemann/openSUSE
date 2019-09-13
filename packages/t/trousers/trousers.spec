#
# spec file for package trousers
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define tpmstatedir %{_localstatedir}/lib/tpm
Name:           trousers
Version:        0.3.14
Release:        0
Summary:        TSS (TCG Software Stack) access daemon for a TPM chip
License:        BSD-3-Clause
Group:          Productivity/Security
Url:            http://trousers.sourceforge.net/
Source0:        http://downloads.sf.net/trousers/%{name}-%{version}.tar.gz
Source1:        tcsd.service
Source2:        baselibs.conf
Patch0:         fix-lto.patch
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
# for 'stat' for the hack in %pretrans
BuildRequires:  coreutils
Requires(pre):  shadow
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
%define trousers_state %{buildroot}%{tpmstatedir}
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{trousers_state}
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

%pre
%_bindir/getent group tss >/dev/null || %{_sbindir}/groupadd -g 98 tss || :
%_bindir/getent passwd tss >/dev/null || \
	%{_sbindir}/useradd -u 98 -o -g tss -s /bin/false -c "TSS daemon" \
	-d %{tpmstatedir} tss || :
%service_add_pre tcsd.service

%pretrans
# this scriplet and the counterpart in %posttrans work around a packaging bug
# that was present in all trousers packages since around 2008.
# /var/lib/tpm/system.data.* was wrongly packaged as runtime state data
# instead of package resource data in /usr/share. After removal of these files
# from packaging, during updating they will be deleted. Since users could have
# created their own versions of the files already (by taking ownership of a
# TPM) we want to keep those files in place.
#
# to achieve this we use the ownership of /var/lib/tpm as an indicator.
# Versions that still wrongly package those files also had the ownership of
# the directory wrong. Therefore if the directory is not owned by the tss user
# we apply a backup and restore logic.
[ ! -d "%{tpmstatedir}" ] && exit 0
OWNER=`/usr/bin/stat -c "%U" "%{tpmstatedir}"`
[ "$OWNER" = "tss" ] && exit 0
for data in system.data.auth system.data.noauth; do
	file="%{tpmstatedir}/${data}"
	[ ! -e "$file" ] && continue
	cp -p $file ${file}.rpmsave
	echo "saving backup of $file"
done

%post
%service_add_post tcsd.service

%posttrans
# see pretrans for an explanation of this
for data in system.data.auth system.data.noauth; do
	file="%{tpmstatedir}/${data}"
	# nothing to restore here
	[ ! -e "${file}.rpmsave" ] && continue
	# for some reason the to-be-restored file already exists? ignore.
	[ -e "${file}" ] && continue
	# restore the original file
	echo "restoring backup of $file"
	mv ${file}.rpmsave ${file}
	chown tss:tss "${file}"
done

%postun
%service_del_postun tcsd.service

%preun
%service_del_preun tcsd.service

%post -n libtspi1 -p /sbin/ldconfig

%postun -n libtspi1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config(noreplace) %attr(600,tss,tss) %{_sysconfdir}/tcsd.conf
%doc README README.selinux AUTHORS ChangeLog LICENSE NICETOHAVES TODO doc/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%attr(750,tss,tss) %{tpmstatedir}
%{_datadir}/%{name}
%{_sbindir}/tcsd
%{_sbindir}/rctcsd
%{_unitdir}/tcsd.service

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
