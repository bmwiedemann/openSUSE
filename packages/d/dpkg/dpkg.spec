#
# spec file for package dpkg
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           dpkg
Version:        1.22.22
Release:        0
Summary:        Debian package management system
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://tracker.debian.org/pkg/%{name}
Source0:        https://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%{version}.tar.xz
Source1:        sensible-editor
Source2:        dpkg.tmpfiles
# PATCH-FIX-SUSE: tar of Leap 42.{2,3} does not recognize --sort=name, --clamp-mtime options
Patch2:         drop-tar-option.patch
Patch3:         ncurses-fix.patch
Patch4:         openssl.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gpg2
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl >= 5.28.1
BuildRequires:  po4a >= 0.59
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Strict)
Requires:       cpio
Requires:       make
Requires:       patch
Requires:       perl(Date::Parse)
Requires(post): coreutils
Recommends:     perl(File::FcntlLock)
Provides:       deb = %{version}
Obsoletes:      deb < %{version}
Provides:       dpkg-dev = %{version}
Provides:       dpkg-doc = %{version}
Provides:       dselect = %{version}
%{perl_requires}

%description
This package contains tools for working with Debian packages. It makes
it possible to create and extract Debian packages. If Alien is
installed, the packages can be converted to RPMs.

This package contains the following Debian packages: dpkg, dselect,
dpkg-doc, dpkg-dev.

%package devel
Summary:        Development files for dpkg
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libmd-devel
Provides:       deb-devel = %{version}
Obsoletes:      deb-devel < %{version}

%description devel
Libraries and header files for dpkg.

%lang_package

%prep
%setup -q
%if 0%{?suse_version} == 1315
%patch -P 2 -p1
%endif
%patch -P 3 -p1
%patch -P 4 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fvi
export CFLAGS="%{?build_cflags:%build_cflags}%{?!build_cflags:%optflags}"
%configure \
    --disable-silent-rules \
    --with-libselinux \
    --localstatedir=%{_localstatedir}/lib \
    --with-admindir=%{_localstatedir}/lib/dpkg \
    --docdir=%{_docdir}/%{name}

# configure somehow does not detect architecture correctly in OBS (bnc#469337), so
# let's do an awful hack and fix it in config.h
# XXX: who knows if this works on s390? :)

%define debarch %{_arch}
%ifarch x86_64
%define debarch amd64
%endif
%ifarch %{ix86}
%define debarch i386
%endif
%ifarch ppc powerpc
%define debarch powerpc
%endif
%ifarch ppc64 powerpc64
%define debarch ppc64
%endif
sed -i 's/^#define ARCHITECTURE ""/#define ARCHITECTURE "%{debarch}"/' config.h

%make_build

%install
%make_install

# tmpfiles: install snippet
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/dpkg.conf

# tmpfiles: remove directory structure that will be created by systemd-tmpfiles
rm -rf %{buildroot}%{_localstatedir}/lib/dpkg

# remove update-alternatives stuff (included in separate package)
rm -rf %{buildroot}%{_sysconfdir}/alternatives
rm -rf %{buildroot}%{_bindir}/update-alternatives
rm -rf %{buildroot}%{_sbindir}/update-alternatives
rm -rf %{buildroot}%{_mandir}/man8/update-alternatives.8
rm -rf %{buildroot}%{_mandir}/*/man8/update-alternatives.8
rm -rf %{buildroot}%{_datadir}/polkit-1/actions/org.dpkg.pkexec.update-alternatives.policy

# locales
%find_lang %{name}
%find_lang dselect
%find_lang dpkg-dev
cat dselect.lang dpkg-dev.lang >> %{name}.lang

# extras
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}

%check
%make_build check

%post
%tmpfiles_create dpkg.conf
exit 0

%files lang -f %{name}.lang
%{_mandir}/??/man*/*

%files
%license COPYING
%{_docdir}/%{name}
%{_mandir}/man*/*
%exclude %{_mandir}/man*/update-alternatives*
%dir %{_sysconfdir}/dpkg
%config(noreplace) %{_sysconfdir}/dpkg/*
%{_bindir}/dpkg
%{_bindir}/dpkg-architecture
%{_bindir}/dpkg-buildapi
%{_bindir}/dpkg-buildflags
%{_bindir}/dpkg-buildpackage
%{_bindir}/dpkg-buildtree
%{_bindir}/dpkg-checkbuilddeps
%{_bindir}/dpkg-deb
%{_bindir}/dpkg-distaddfile
%{_bindir}/dpkg-divert
%{_bindir}/dpkg-genbuildinfo
%{_bindir}/dpkg-genchanges
%{_bindir}/dpkg-gencontrol
%{_bindir}/dpkg-gensymbols
%{_bindir}/dpkg-maintscript-helper
%{_bindir}/dpkg-mergechangelogs
%{_bindir}/dpkg-name
%{_bindir}/dpkg-parsechangelog
%{_bindir}/dpkg-query
%{_bindir}/dpkg-realpath
%{_bindir}/dpkg-scanpackages
%{_bindir}/dpkg-scansources
%{_bindir}/dpkg-shlibdeps
%{_bindir}/dpkg-source
%{_bindir}/dpkg-split
%{_bindir}/dpkg-statoverride
%{_bindir}/dpkg-trigger
%{_bindir}/dpkg-vendor
%{_bindir}/dselect
%{_bindir}/sensible-editor
%{_sbindir}/start-stop-daemon
%{_libexecdir}/dpkg
%{_datadir}/dpkg
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_dpkg-parsechangelog
%{perl_vendorlib}/Dpkg
%{perl_vendorlib}/Dpkg.pm
%{perl_vendorlib}/Dselect
%{_tmpfilesdir}/dpkg.conf
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/info
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/methods
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/methods/file
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/methods/ftp
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/methods/media
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/methods/mnt
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/parts
%ghost %attr(755,root,root) %dir %{_localstatedir}/lib/dpkg/updates

%files devel
%{_datadir}/aclocal/*.m4
%{_libdir}/libdpkg.a
%{_libdir}/libdpkg.la
%{_libdir}/pkgconfig/libdpkg.pc
%{_includedir}/dpkg

%changelog
