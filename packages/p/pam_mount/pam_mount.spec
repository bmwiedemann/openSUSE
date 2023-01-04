#
# spec file for package pam_mount
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


Name:           pam_mount
%define lname   libcryptmount0
Version:        2.19
Release:        0
Summary:        A PAM Module that can Mount Volumes for a User Session
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://inai.de/projects/pam_mount/

Source:         http://downloads.sf.net/pam-mount/%name-%version.tar.xz
Source9:        http://downloads.sf.net/pam-mount/%name-%version.tar.asc
Source1:        convert_pam_mount_conf.pl
Source2:        convert_keyhash.pl
Source3:        pam_mount.tmpfiles
Source5:        baselibs.conf
Source6:        %name.keyring
Patch1:         pam_mount-0.47-enable-logout-kill.dif
Patch3:         bsc1153630-prevent-systemd-from-calling-pam_mount.patch
BuildRequires:  fdupes
BuildRequires:  libtool
# LOOP64 support:
BuildRequires:  linux-glibc-devel >= 2.6
BuildRequires:  man
BuildRequires:  pam-devel >= 0.99
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-Writer
BuildRequires:  pkgconfig >= 0.19
BuildRequires:  xz
BuildRequires:  pkgconfig(libHX) >= 3.12.1
BuildRequires:  pkgconfig(libcrypto) >= 0.9.7
BuildRequires:  pkgconfig(libcryptsetup) >= 1.1.2
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(mount) >= 2.20

Requires(post): coreutils
Requires(post): perl-XML-Writer
Requires(post): perl-XML-Parser
# -EBUSY bugs fixed (libdevmapper):
Requires:       device-mapper >= 1.02.48
Requires:       fd0ssh
Requires:       ofl
# for mount(8) and mount.cifs:
Requires:       util-linux >= 2.20
Suggests:       cifs-mount

%description
This module is aimed at environments with central file servers that a
user wishes to mount on login and unmount on logout, such as
(semi-)diskless stations where many users can logon.

The module also supports mounting local filesystems of any kind the
normal mount utility supports, with extra code to make sure certain
volumes are set up properly because often they need more than just a
mount call, such as encrypted volumes. This includes SMB/CIFS, FUSE,
dm-crypt and LUKS.

%package -n %lname
Summary:        Library to mount crypto images and handle key files
Group:          System/Libraries

%description -n %lname
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.

%package -n libcryptmount-devel
Summary:        Development files for libcryptmount
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libcryptmount-devel
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.

%prep
%autosetup -p1

%build
%configure --disable-static --with-slibdir="/%_lib" \
	--includedir="%_includedir/libcryptmount" \
	--with-slibdir=%{_pam_libdir} \
	%{?_with_selinux:--with-selinux}
%make_build

%install
%make_install
b="%buildroot"
# Remove static and libtool version
rm -f $b%{_pam_moduledir}/*.{a,la} "$b/%_libdir"/*.la
#install the docs
mkdir -p "$b/%_docdir/%name/examples"
cp -a doc/bugs.txt doc/news.rst LICENSE* doc/faq.txt doc/todo.txt doc/options.txt "$b/%_docdir/%name/"
install -m 755 %SOURCE1 "$b/%_docdir/%name/examples/"
install -m 755 %SOURCE2 "$b/%_docdir/%name/examples/"
%if 0%{?suse_version} < 1550
mkdir -p "$b/sbin"
ln -s /usr/sbin/mount.crypt "$b/sbin"
ln -s /usr/sbin/umount.crypt "$b/sbin"
ln -s /usr/sbin/mount.crypt_LUKS "$b/sbin"
ln -s /usr/sbin/umount.crypt_LUKS "$b/sbin"
%endif
install -Dm0644 %SOURCE3 "$b/%_tmpfilesdir/%name.conf"
%fdupes %buildroot/%_prefix

%post
%tmpfiles_create %_tmpfilesdir/%name.conf
if [ -e etc/security/pam_mount.conf ]
then
        cp etc/security/pam_mount.conf.xml %_docdir/%name/examples/
	%_docdir/%name/examples/convert_pam_mount_conf.pl \
	-i etc/security/pam_mount.conf -o etc/security/pam_mount.conf.xml
fi
if [ "$1" -gt 1 ]
then
	for v in `rpm -q --queryformat "%%VERSION " %name`; do
		if echo "$v" | grep -E "^0\." - ; then
			%_docdir/%name/examples/convert_keyhash.pl \
			-i etc/security/pam_mount.conf.xml
			break;
		fi
	done
fi

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_docdir/%name
%{_pam_moduledir}/pam_mount*.so
%_tmpfilesdir/%name.conf
%_sbindir/mount.*
%_sbindir/umount.*
%_sbindir/pmvarrun
%_sbindir/pmt-ehd
%if 0%{?suse_version} < 1550
/sbin/*mount*
%endif
%config(noreplace) %_sysconfdir/security/pam_mount.conf.xml
%doc %_mandir/man5/pam_mount.conf.5.gz
%doc %_mandir/man8/*.8.gz
%if 0%{?_with_selinux:1}
%policy %_sysconfdir/selinux/strict/src/policy/macros/%{name}_macros.te
%policy %_sysconfdir/selinux/strict/src/policy/file_contexts/misc/%name.fc
%endif

%files -n %lname
%_libdir/libcryptmount.so.0*

%files -n libcryptmount-devel
%_includedir/libcryptmount/
%_libdir/pkgconfig/*.pc
%_libdir/libcryptmount.so

%changelog
