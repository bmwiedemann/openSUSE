#
# spec file for package guile1
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


%define binpref guile1
Name:           guile1
Version:        1.8.8
Release:        0
Summary:        GNU's Ubiquitous Intelligent Language for Extension
License:        LGPL-2.1-or-later
Group:          Development/Languages/Scheme
URL:            https://www.gnu.org/software/guile/
#https://github.com/texmacs/guile/archive/texmacs.zip
Source0:        https://ftp.gnu.org/gnu/guile/guile-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/guile/guile-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch1:         guile-64bit.patch
Patch2:         guile-1.6.10-mktemp.patch
Patch3:         guile-popen-test.patch
Patch5:         guile-gcc.patch
Patch6:         guile-automake-1.13.patch
Patch7:         guile-socket-test.patch
# fix failures with texinfo 5.2
Patch8:         guile-texinfo.patch
Patch9:         guile1-CVE-2016-8605.patch
# PATCH-FIX-OPENSUSE (version is obsolete upstream / from 2010)
Patch10:        reproducible.patch
Patch11:        guile1-fix-texinfo-default-utf8.patch
BuildRequires:  automake
BuildRequires:  gc-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  readline-devel
# Require the library packages, at least current version. The *.so symlinks are in the main package (due to dlopen(), so without the requires, it would be dangling symlinks.
Requires:       libguile-srfi-srfi-1-v-3-3 >= %{version}
Requires:       libguile-srfi-srfi-13-14-v-3-3 >= %{version}
Requires:       libguile-srfi-srfi-4-v-3-3 >= %{version}
Requires:       libguile-srfi-srfi-60-v-2-2 >= %{version}
Requires:       libguile17 >= %{version}
Requires:       libguilereadline-v-17-17 >= %{version}
PreReq:         %{install_info_prereq}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         fileutils
PreReq:         sh-utils
Conflicts:      slib < 3a5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
%if 0%{?suse_version} >= 1230
BuildRequires:  makeinfo
%endif

%description
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs.

%package -n libguile17
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguile17
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguile-srfi-srfi-1-v-3-3
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguile-srfi-srfi-1-v-3-3
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguile-srfi-srfi-4-v-3-3
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguile-srfi-srfi-4-v-3-3
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguile-srfi-srfi-13-14-v-3-3
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguile-srfi-srfi-13-14-v-3-3
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguile-srfi-srfi-60-v-2-2
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguile-srfi-srfi-60-v-2-2
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguilereadline-v-17-17
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme

%description -n libguilereadline-v-17-17
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the shared libraries.

%package -n libguile1-devel
Summary:        GNU's Ubiquitous Intelligent Language for Extension
Group:          Development/Languages/Scheme
Requires:       gmp-devel
Requires:       guile1
Requires:       libguile-srfi-srfi-1-v-3-3 = %{version}-%{release}
Requires:       libguile-srfi-srfi-13-14-v-3-3 = %{version}-%{release}
Requires:       libguile-srfi-srfi-4-v-3-3 = %{version}-%{release}
Requires:       libguile-srfi-srfi-60-v-2-2 = %{version}-%{release}
Requires:       libguile17 = %{version}-%{release}
Requires:       libguilereadline-v-17-17 = %{version}-%{release}
Requires:       libltdl-devel
Requires:       ncurses-devel
Requires:       readline-devel

%description -n libguile1-devel
This is Guile, a portable, embeddable Scheme implementation written in
C. Guile provides a machine independent execution platform that can be
linked in as a library when building extensible programs. This package
contains the files necessary to link against the guile libraries.

%prep
%setup -q -n guile-%{version}
%patch1
%patch2
%patch3
%patch5
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11
# guile-1.8.1: The code is not so good for -Werror (unused results of write()).
sed -i s/-Werror// configure.in configure

%build
%define _lto_cflags %{nil}
# NOTE: GCC 10 succeeds in rewriting a
#particular tail call into jumps. This avoids stack frames from the
#recursive call which the check relies on. Funnily enough, a comment
#says: "If the code could be inlined, that might cause the test to give
#an incorrect answer." - indeed.
# As a result the guile executable causes a segfault when built with -02
export CFLAGS="`echo %optflags|tr 02 00`"
echo $CFLAGS
sed -i "s:GUILE_:GUILE1_:" guile-config/guile.m4
sed -i "s:guile:guile1:" guile-config/guile.m4
# automake 1.13: do not run test simultaneously
find -name Makefile.am | xargs sed -i 's/\(^AUTOMAKE_OPTIONS.*$\)/\1 serial-tests/'
autoreconf -fi
# FIXME: Following files are apparently compiled without RPM_OPT_FLAGS:
# gen-scmconfig.c,c-tokenize.c
%configure \
	--disable-static \
	--with-pic \
	--with-threads \
	--program-transform-name="s:guile:%{binpref}:"
make --trace %{?_smp_mflags}

%check
# 47 of 11930 tests are failing now
make check || :

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}%{_datadir}/guile/site
rm -r %{buildroot}%{_infodir}
# conflict with guile2
mv %{buildroot}%{_datadir}/aclocal/guile{,1}.m4
# use /usr/bin/guile1 instead of /usr/bin/guile
sed -i "s:${GUILE-guile}:${GUILE-guile1}:" %{buildroot}%{_datadir}/guile/1.8/scripts/*
sed -i "s:%{_bindir}/guile:%{_bindir}/guile1:" %{buildroot}%{_bindir}/guile1-config

%post -n libguile-srfi-srfi-1-v-3-3 -p /sbin/ldconfig

%postun -n libguile-srfi-srfi-1-v-3-3 -p /sbin/ldconfig

%files -n libguile-srfi-srfi-1-v-3-3
%defattr(-,root,root)
%{_libdir}/libguile-srfi-srfi-1-v-3.so.3*

%post -n libguile-srfi-srfi-4-v-3-3 -p /sbin/ldconfig

%postun -n libguile-srfi-srfi-4-v-3-3 -p /sbin/ldconfig

%files -n libguile-srfi-srfi-4-v-3-3
%defattr(-,root,root)
%{_libdir}/libguile-srfi-srfi-4-v-3.so.3*

%post -n libguile-srfi-srfi-13-14-v-3-3 -p /sbin/ldconfig

%postun -n libguile-srfi-srfi-13-14-v-3-3 -p /sbin/ldconfig

%files -n libguile-srfi-srfi-13-14-v-3-3
%defattr(-,root,root)
%{_libdir}/libguile-srfi-srfi-13-14-v-3.so.3*

%post -n libguile-srfi-srfi-60-v-2-2 -p /sbin/ldconfig

%postun -n libguile-srfi-srfi-60-v-2-2 -p /sbin/ldconfig

%files -n libguile-srfi-srfi-60-v-2-2
%defattr(-,root,root)
%{_libdir}/libguile-srfi-srfi-60-v-2.so.2*

%post -n libguile17 -p /sbin/ldconfig

%postun -n libguile17 -p /sbin/ldconfig

%files -n libguile17
%defattr(-,root,root)
%{_libdir}/libguile.so.17*

%post -n libguilereadline-v-17-17 -p /sbin/ldconfig

%postun -n libguilereadline-v-17-17 -p /sbin/ldconfig

%files -n libguilereadline-v-17-17
%defattr(-,root,root)
%{_libdir}/libguilereadline-v-17.so.17*

%pre
# Remove obsolete files (< SuSE Linux 10.2)
rm -f var/adm/SuSEconfig/md5%{_datadir}/guile/*/slibcat
rm -f usr/share/guile/site/slibcat.SuSEconfig

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog* GUILE-VERSION HACKING
%doc NEWS README THANKS
%license LICENSE COPYING*
%{_bindir}/*
%dir %{_datadir}/guile
%{_datadir}/guile/1.8
%dir %{_datadir}/guile/site
%{_mandir}/man1/%{binpref}.1.gz
# please leave *.so files here [bnc#772490]
%{_libdir}/libguile*.so

%files -n libguile1-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libguile*.la
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/guile1.m4

%changelog
