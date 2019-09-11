#
# spec file for package libostree
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


Name:           libostree
Version:        2019.1
Release:        0
Summary:        Git for operating system binaries
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/ostreedev/ostree
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE ostree-grub2-location.patch boo#974714 dimstar@opensuse.org -- Fix path to grub-mkconfig_lib
Patch0:         ostree-grub2-location.patch

BuildRequires:  bison
BuildRequires:  gjs
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel >= 1.34.0
BuildRequires:  gpgme-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(fuse) >= 2.9.2
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.36.0
BuildRequires:  pkgconfig(libarchive) >= 2.8.0
BuildRequires:  pkgconfig(liblzma) >= 5.0.5
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.39.1
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount) >= 2-23.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# Package was renamed from ostree to libostree with version 2017.2
Provides:       ostree = %{version}
Obsoletes:      ostree < %{version}

%description
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%package -n libostree-1-1
Summary:        Git for operating system binaries
Group:          System/Libraries

%description -n libostree-1-1
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%package -n typelib-1_0-OSTree-1_0
Summary:        Git for operating system binaries  -- GObject bindings
Group:          System/Libraries

%description -n typelib-1_0-OSTree-1_0
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%ifnarch s390 s390x %{arm}
%package        grub2
Summary:        GRUB2 integration for OSTree
# Package was renamed from ostree to libostree with version 2017.2
Group:          System/Boot
Provides:       ostree-grub2 = %{version}
Obsoletes:      ostree-grub2 < %{version}
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

%description grub2
GRUB2 integration for OSTree
%endif

%package devel
Summary:        Git for operating system binaries -- Development files
# Package was renamed from ostree to libostree with version 2017.2
Group:          Development/Languages/C and C++
Requires:       libostree-1-1 = %{version}
Requires:       typelib-1_0-OSTree-1_0 = %{version}
Provides:       ostree-devel = %{version}
Obsoletes:      ostree-devel < %{version}

%description devel
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
NOCONFIGURE=1 ./autogen.sh
%configure --with-dracut
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# openSUSE rcFOO links
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcostree-prepare-root
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcostree-remount

%post -n libostree-1-1 -p /sbin/ldconfig
%postun -n libostree-1-1 -p /sbin/ldconfig
%pre
%service_add_pre ostree-prepare-root.service
%service_add_pre ostree-remount.service

%preun
%service_del_preun ostree-prepare-root.service
%service_del_preun ostree-remount.service.service

%post
%service_add_post ostree-prepare-root.service
%service_add_post ostree-remount.service
%tmpfiles_create %{_tmpfilesdir}/ostree-tmpfiles.conf

%postun
%service_del_postun ostree-prepare-root.service
%service_del_postun ostree-remount.service

%files
%license COPYING
%doc README.md
%{_mandir}/man1/ostree*.1%{?ext_man}
%{_mandir}/man5/ostree.repo*.5%{?ext_man}
%{_mandir}/man1/rofiles-fuse.1%{?ext_man}
%{_bindir}/ostree
%{_bindir}/rofiles-fuse
%{_datadir}/bash-completion/completions/ostree
%dir %{_libexecdir}/ostree
%dir %{_libexecdir}/libostree
%{_libexecdir}/ostree/ostree-prepare-root
%{_libexecdir}/ostree/ostree-remount
%{_libexecdir}/libostree/ostree-trivial-httpd
%dir %{_libexecdir}/dracut
%dir %{_libexecdir}/dracut/modules.d
%{_libexecdir}/dracut/modules.d/98ostree/
%{_unitdir}/ostree-prepare-root.service
%{_unitdir}/ostree-remount.service
%{_unitdir}/ostree-finalize-staged.service
%{_unitdir}/ostree-finalize-staged.path
%dir %{_sysconfdir}/dracut.conf.d
%{_sysconfdir}/dracut.conf.d/ostree.conf
%{_datadir}/ostree/
%{_sbindir}/rcostree-prepare-root
%{_sbindir}/rcostree-remount
%{_libexecdir}/systemd/system-generators/ostree-system-generator
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/ostree-tmpfiles.conf
%exclude %{_sysconfdir}/grub.d/*ostree
%exclude %{_libexecdir}/libostree/grub2*

%files -n libostree-1-1
%{_libdir}/libostree-1.so.*

%files -n typelib-1_0-OSTree-1_0
%{_libdir}/girepository-1.0/OSTree-1.0.typelib

%files devel
%{_includedir}/ostree-1/
%{_libdir}/libostree-1.so
%{_libdir}/pkgconfig/ostree-1.pc
%{_datadir}/gir-1.0/OSTree-1.0.gir

%ifnarch s390 s390x %{arm}
%files grub2
%dir %{_sysconfdir}/grub.d/
%{_sysconfdir}/grub.d/*ostree
%{_libexecdir}/libostree/grub2*
%endif

%changelog
