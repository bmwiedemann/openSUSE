#
# spec file for package ecryptfs-utils
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


%if 0%{?suse_version} < 1550
%define sbindir /sbin
%else
%define sbindir %{_sbindir}
%endif

%define lname   libecryptfs1
Name:           ecryptfs-utils
Version:        111
Release:        0
Summary:        Userspace Utilities for ecryptfs
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://ecryptfs.org/
Source0:        https://launchpad.net/ecryptfs/trunk/%{version}/+download/ecryptfs-utils_%{version}.orig.tar.gz
Source1:        baselibs.conf
Source2:        ecryptfs-mount-private.png
# PATCH-FIX-OPENSUSE fix for systemd and no UUID in fstab
Patch0:         ecryptfs-setup-swap-SuSE.patch
# PATCH-FIX-OPENSUSE build with -fpie/-pie
Patch1:         ecryptfs-utils-src-utils-Makefile.patch
Patch2:         ecryptfs-utils-openssl11.patch
Patch3:         ecryptfs-usrmerge.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  keyutils-devel
BuildRequires:  keyutils-libs
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  mozilla-nss-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-config
BuildRequires:  pam-devel
BuildRequires:  pkcs11-helper-devel
BuildRequires:  pkg-config
#BuildRequires:  python3-devel
#BuildRequires:  swig
BuildRequires:  trousers-devel
BuildRequires:  update-desktop-files
Requires(pre):  pam-config
Requires(pre):  permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A stacked cryptographic filesystem for Linux.

%package -n %{lname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{lname}
A stacked cryptographic filesystem for Linux.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}

%description devel
A stacked cryptographic filesystem for Linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
export RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing"
autoreconf -fiv
%configure \
	rootsbindir=%{sbindir} \
	--docdir=%{_defaultdocdir}/%{name} \
	--disable-static \
	--disable-pywrap \
	--enable-tspi \
	--enable-pkcs11-helper \
	--with-pamdir=%{_pamdir}
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}/%{_datadir}/applications
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/ecryptfs-mount-private.png
printf "Encoding=UTF-8\n" >>%{buildroot}/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
printf "Encoding=UTF-8\n" >>%{buildroot}/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
printf "Icon=%{_datadir}/%{name}/ecryptfs-mount-private.png\n" >>%{buildroot}/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
printf "Icon=%{_datadir}/%{name}/ecryptfs-mount-private.png\n" >>%{buildroot}/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
sed -i 's|^_||' %{buildroot}/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
sed -i 's|^_||' %{buildroot}/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
mv %{buildroot}/%{_datadir}/%{name}/ecryptfs-setup-private.desktop %{buildroot}/%{_datadir}/applications
%suse_update_desktop_file %{buildroot}/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
%suse_update_desktop_file -r ecryptfs-setup-private System Security
%find_lang %{name}
# replace duplicate files by symlinks
%fdupes -s %{buildroot}
# do not ship .la files
find %{buildroot} -type f -name "*.la" -delete -print

#we need ecryptfs kernel module
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d/
echo -e "# ecryptfs module is needed before ecryptfs mount, so mount helper can \n# check for file name encryption support\necryptfs" >%{buildroot}%{_prefix}/lib/modules-load.d/ecryptfs.conf

%verifyscript
%verify_permissions -e %{sbindir}/mount.ecryptfs_private

%post
%set_permissions %{sbindir}/mount.ecryptfs_private
%{_sbindir}/pam-config -a --ecryptfs
%desktop_database_post

%post -n %{lname} -p /sbin/ldconfig

%postun
if [ "$1" -eq 0 ]; then
	%{_sbindir}/pam-config -d --ecryptfs
fi
%desktop_database_postun

%postun -n %{lname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING NEWS README THANKS doc/ecryptfs-faq.html
%{_docdir}/%{name}
%{_bindir}/*
%{sbindir}/mount.ecryptfs
%{sbindir}/umount.ecryptfs
%{sbindir}/umount.ecryptfs_private
%verify(not mode) %{sbindir}/mount.ecryptfs_private
%{_mandir}/man1/*ecryptfs*
%{_mandir}/man7/ecryptfs*
%{_mandir}/man8/*ecryptfs*
%{_libdir}/ecryptfs*
%{_datadir}/ecryptfs-utils
%{_pamdir}/pam_ecryptfs.so
#{python_sitelib}/ecryptfs-utils
#{python_sitearch}/ecryptfs-utils
%{_datadir}/applications/*.desktop
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/*

%files -n %{lname}
%defattr(-, root, root)
%{_libdir}/libecryptfs.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/ecryptfs.h
%{_libdir}/libecryptfs.so
%{_libdir}/pkgconfig/libecryptfs.pc

%changelog
