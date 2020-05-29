#
# spec file for package guile
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# define the name used for versioning libs and directories.
%define guilemaj    3
%define guilemin    0
%define guilevers   %{guilemaj}.%{guilemin}
%define libgver     1
%define gsuff       %{guilemaj}_%{guilemin}-%{libgver}
Name:           guile
Version:        %{guilevers}.2
Release:        0
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        GFDL-1.3-only AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Scheme
URL:            https://www.gnu.org/software/guile/
Source0:        https://ftp.gnu.org/gnu/guile/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/guile/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=guile&download=1#/%{name}.keyring
Source3:        guile-rpmlintrc
# Fix the resulting /usr/lib64/pkgconfig/guile-3.0.pc
Patch0:         guile-3.0-gc_pkgconfig_private.patch
# The out-of-memory test is flaky, so disable it
Patch1:         disable-test-out-of-memory.patch
Patch2:		gcc10-x86-disable-one-test.patch
BuildRequires:  gmp-devel
BuildRequires:  libffi-devel
BuildRequires:  libltdl-devel
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(bdw-gc)
Requires(pre):  fileutils
Requires(pre):  sh-utils

%description
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%package -n libguile-%{gsuff}
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        GFDL-1.3-only AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Scheme
Requires:       %{name}-modules-%{guilemaj}_%{guilemin} >= %{version}
# workaround for bnc#948804
Requires:       glibc-locale

%description -n libguile-%{gsuff}
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package modules-%{guilemaj}_%{guilemin}
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        GFDL-1.3-only AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Scheme

%description modules-%{guilemaj}_%{guilemin}
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains guile modules.

%package devel
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        LGPL-2.1-or-later
Group:          Development/Languages/Scheme
Requires:       gmp-devel
# following Requires needed because /usr/bin/guile-config needs /usr/bin/guile
Requires:       guile = %{version}
Requires:       libffi-devel
Requires:       libguile-%{gsuff} = %{version}
Requires:       libunistring-devel
Requires:       ncurses-devel
Requires:       readline-devel
Requires:       pkgconfig(bdw-gc)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# remove broken prebuilt objects
rm -r prebuilt/32-bit-big-endian

%build
%configure \
  --disable-static \
  --with-pic \
  --with-threads \
  --disable-silent-rules
# do sequential build for reproducible .go files = https://issues.guix.gnu.org/issue/20272 - boo#1102408
make

%check
LD_LIBRARY_PATH="." make %{?_smp_mflags} check

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/guile/site
find %{buildroot} -type f -name "*.la" -delete -print
# bug #874028
mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}
mv %{buildroot}%{_libdir}/libguile*-gdb.scm %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info --info-dir=%{_infodir} %{_infodir}/r5rs.info%{ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/r5rs.info%{ext_info}

%pre
# Remove obsolete files (< SuSE Linux 10.2)
rm -f var/adm/SuSEconfig/md5%{_datadir}/guile/*/slibcat
rm -f usr/share/guile/site/slibcat.SuSEconfig

%post -n libguile-%{gsuff} -p /sbin/ldconfig
%postun -n libguile-%{gsuff} -p /sbin/ldconfig

%files
%doc ABOUT-NLS AUTHORS ChangeLog GUILE-VERSION HACKING
%doc NEWS README THANKS
%{_bindir}/guile-tools
%{_bindir}/guild
%{_bindir}/guile
%{_mandir}/man1/guile.1%{ext_man}

%files -n libguile-%{gsuff}
%license LICENSE COPYING*
%{_libdir}/libguile-%{guilevers}.so.%{libgver}*

%files modules-%{guilemaj}_%{guilemin}
%{_libdir}/%{name}
# Own usr/share/guile/site; side effect of not doing so is slib failing to install correctly.
%{_datadir}/%{name}

%files devel
%{_bindir}/guile-snarf
%{_bindir}/guile-config
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/%{guilevers}
%{_includedir}/%{name}/%{guilevers}/*
%{_datadir}/aclocal/guile.m4
%{_infodir}/%{name}.info%{ext_info}
%{_infodir}/%{name}.info-[0-9]%{ext_info}
%{_infodir}/%{name}.info-1[0-9]%{ext_info}
%{_infodir}/r5rs.info%{ext_info}
%{_libdir}/libguile-%{guilevers}.so
%{_libdir}/pkgconfig/guile-%{guilevers}.pc
# bug #874028
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{_libdir}
%{_datadir}/gdb/auto-load/%{_libdir}/libguile*-gdb.scm

%changelog
