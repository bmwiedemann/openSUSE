#
# spec file for package dpkg
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


Name:           dpkg
Version:        1.19.0.5
Release:        0
Summary:        Debian package management system
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            http://www.debian.org
Source0:        http://ftp.de.debian.org/debian/pool/main/d/dpkg/dpkg_%{version}.tar.xz
Source3:        sensible-editor
# PATCH-FIX-OPENSUSE replace debian with opensuse. replace macros. update-alternatives temp directories' path and name from dpkg* to rpm*.
Patch1:         update-alternatives-suse.patch
# PATCH-FIX-SUSE: tar of Leap 42.{2,3} does not recognize --sort=name, --clamp-mtime options
Patch2:         drop-tar-option.patch
Patch3:         ncurses-fix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gpg2
BuildRequires:  libbz2-devel
BuildRequires:  libmd-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  po4a
BuildRequires:  update-alternatives
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Strict)
Requires:       cpio
Requires:       make
Requires:       patch
Requires:       update-alternatives
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
%patch1 -p1
%if 0%{?suse_version} == 1315
%patch2 -p1
%endif
%patch3 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fvi
export CFLAGS="%{optflags}"
%configure \
    --disable-silent-rules \
    --with-libselinux \
    --localstatedir=%{_localstatedir}/lib \
    --with-admindir=%{_localstatedir}/lib/dpkg

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

make %{?_smp_mflags}

%install
%make_install

# remove update-alternatives stuff (included in separate package)
rm -rf %{buildroot}%{_sysconfdir}/alternatives
rm -rf %{buildroot}%{_localstatedir}/lib/dpkg/alternatives
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
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}

%check
make %{?_smp_mflags} check

%post
cd %{_localstatedir}/lib/dpkg
for f in diversions statoverride status ; do
    [ ! -f $f ] && touch $f
done
exit 0

%files lang -f %{name}.lang
%{_mandir}/??/man*/*

%files
%license COPYING
%doc ABOUT-NLS AUTHORS doc/triggers.txt NEWS README* THANKS TODO debian/changelog
%{_mandir}/man*/*
%exclude %{_mandir}/man*/update-alternatives*
%dir %{_sysconfdir}/dpkg
%config(noreplace) %{_sysconfdir}/dpkg/*
%{_bindir}/*
%{_sbindir}/*
%{_libexecdir}/dpkg
%{_datadir}/dpkg
%{_localstatedir}/lib/dpkg
%{perl_vendorlib}/Dpkg
%{perl_vendorlib}/Dpkg.pm
%{perl_vendorlib}/Dselect
%{perl_vendorlib}/Dselect/Ftp.pm

%files devel
%{_libdir}/libdpkg.a
%{_libdir}/libdpkg.la
%{_libdir}/pkgconfig/libdpkg.pc
%{_includedir}/dpkg

%changelog
