#
# spec file for package libostree
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define _dracutmodulesdir %(pkg-config --variable dracutmodulesdir dracut)
%define libversion 1
%define soversion  1
%bcond_without     composefs
%bcond_without     ed25519
%bcond_with        tests
Name:           libostree
Version:        2025.2
Release:        0
Summary:        Git for operating system binaries
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/ostreedev/ostree
Source:         https://github.com/ostreedev/ostree/releases/download/v%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE ostree-grub2-location.patch boo#974714 dimstar@opensuse.org -- Fix path to grub-mkconfig_lib
Patch0:         ostree-grub2-location.patch
BuildRequires:  bison
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gobject-introspection-devel >= 1.34.0
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(fuse3) >= 3.1.1
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gpgme) >= 1.8.0
BuildRequires:  pkgconfig(libarchive) >= 2.8.0
BuildRequires:  pkgconfig(libcurl) >= 7.29.0
BuildRequires:  pkgconfig(liblzma) >= 5.0.5
# Using libcurl requires Soup for tests
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount) >= 2.23.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# Package was renamed from ostree to libostree with version 2017.2
Provides:       ostree = %{version}
Obsoletes:      ostree < %{version}
%if %{with tests}
BuildRequires:  gjs
%endif
%if %{with ed25519}
BuildRequires:  pkgconfig(openssl)
%endif
%if %{with composefs}
BuildRequires:  pkgconfig(composefs)
%endif

%description
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%package -n libostree-%{libversion}-%{soversion}
Summary:        Git for operating system binaries
Group:          System/Libraries

%description -n libostree-%{libversion}-%{soversion}
OSTree is a tool for managing bootable, immutable, versioned
filesystem trees. While it takes over some of the roles of tradtional
"package managers" like dpkg and rpm, it is not a package system; nor
is it a tool for managing full disk images. Instead, it sits between
those levels, offering a blend of the advantages (and disadvantages)
of both.

%package -n typelib-1_0-OSTree-%{soversion}_0
Summary:        Git for operating system binaries  -- GObject bindings
Group:          System/Libraries

%description -n typelib-1_0-OSTree-%{soversion}_0
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
BuildArch:      noarch
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
Requires:       libostree-%{libversion}-%{soversion} = %{version}
Requires:       typelib-1_0-OSTree-%{soversion}_0 = %{version}
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
%configure \
%if %{with composefs}
	--with-composefs \
%endif
	--with-dracut \
%if %{with ed25519}
	--with-openssl \
%endif
	--with-curl \
	--without-soup \
	--with-soup3 \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libostree-%{libversion}-%{soversion}

%pre
%service_add_pre ostree-prepare-root.service
%service_add_pre ostree-remount.service
%service_add_pre ostree-finalize-staged.service
%service_add_pre ostree-finalize-staged-hold.service
%service_add_pre ostree-boot-complete.service

%preun
%service_del_preun ostree-prepare-root.service
%service_del_preun ostree-remount.service
%service_del_preun ostree-finalize-staged.service
%service_del_preun ostree-finalize-staged-hold.service
%service_del_preun ostree-boot-complete.service

%post
%service_add_post ostree-prepare-root.service
%service_add_post ostree-remount.service
%service_add_post ostree-finalize-staged.service
%service_add_post ostree-finalize-staged-hold.service
%service_add_post ostree-boot-complete.service
%tmpfiles_create %{_tmpfilesdir}/ostree-tmpfiles.conf

%postun
%service_del_postun ostree-prepare-root.service
%service_del_postun ostree-remount.service
%service_del_postun ostree-finalize-staged.service
%service_del_postun ostree-finalize-staged-hold.service
%service_del_postun ostree-boot-complete.service

%files
%license COPYING
%doc README.md
%{_mandir}/man1/ostree*.1%{?ext_man}
%{_mandir}/man5/ostree.repo*.5%{?ext_man}
%{_mandir}/man1/rofiles-fuse.1%{?ext_man}
%{_mandir}/man8/ostree-state-overlay@.service.8%{?ext_man}
%{_bindir}/ostree
%{_bindir}/rofiles-fuse
%{_datadir}/bash-completion/completions/ostree
%dir %{_prefix}/lib/ostree
%dir %{_libexecdir}/libostree
%{_prefix}/lib/ostree/ostree-prepare-root
%{_prefix}/lib/ostree/ostree-remount
%{_dracutmodulesdir}/98ostree/
%{_unitdir}/ostree-prepare-root.service
%{_unitdir}/ostree-remount.service
%{_unitdir}/ostree-finalize-staged.service
%{_unitdir}/ostree-finalize-staged-hold.service
%{_unitdir}/ostree-boot-complete.service
%{_unitdir}/ostree-state-overlay@.service
%dir %{_sysconfdir}/dracut.conf.d
%config %{_sysconfdir}/dracut.conf.d/ostree.conf
%{_datadir}/ostree/
%{_systemdgeneratordir}/ostree-system-generator
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/ostree-tmpfiles.conf
# /run/ostree is generated though ostree-tmpfiles.conf
%ghost /run/ostree
%exclude %{_sysconfdir}/grub.d/*ostree
%exclude %{_libexecdir}/libostree/grub2*

%files -n libostree-%{libversion}-%{soversion}
%license COPYING
%{_libdir}/libostree-%{libversion}.so.%{soversion}*

%files -n typelib-1_0-OSTree-%{soversion}_0
%license COPYING
%{_libdir}/girepository-1.0/OSTree-%{soversion}.0.typelib

%files devel
%license COPYING
%{_includedir}/ostree-%{libversion}/
%{_libdir}/libostree-%{libversion}.so
%{_libdir}/pkgconfig/ostree-%{libversion}.pc
%{_datadir}/gir-1.0/OSTree-%{soversion}.0.gir

%ifnarch s390 s390x %{arm}
%files grub2
%license COPYING
%dir %{_sysconfdir}/grub.d/
%config %{_sysconfdir}/grub.d/*ostree
%{_libexecdir}/libostree/grub2*
%endif

%changelog
