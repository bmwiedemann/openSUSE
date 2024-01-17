#
# spec file for package slang
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


Name:           slang
Version:        2.3.3
Release:        0
Summary:        Programming Library and Embeddable Extension Language
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.jedsoft.org/
Source0:        http://www.jedsoft.org/releases/slang/slang-%{version}.tar.bz2
Source1:        http://www.jedsoft.org/releases/slang/slang-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         slang.patch
Patch1:         slang-autoconf.patch
Patch2:         slang-fsuid.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1210
BuildRequires:  oniguruma-devel >= 5.9.0
%endif
BuildRequires:  libpng-devel

%description
S-Lang is a programming library for creating multi-platform software.
It provides display/screen management, keyboard input, keymaps, etc.
Another feature is the interpreter for the S-Lang extension language
which can be embedded into an application to make it extensible. With
slsh, a standalone interpreter is available as well.

%package slsh
Summary:        Interpreter for S-Lang Scripts
Group:          Development/Languages/Other
Provides:       slang = %{version}
Obsoletes:      slang <= 2.1.1

%description slsh
slsh is a standalone interpreter of the S-Lang language. It can be used to
execute scripts, or be run interactively.

%package -n libslang2
Summary:        Programming Library and Embeddable Extension Language
Group:          System/Libraries

%description -n libslang2
S-Lang is a programming library for creating multi-platform software.
It provides display/screen management, keyboard input, keymaps, etc.
Another feature is the interpreter for the S-Lang extension language
which can be embedded into an application to make it extensible. With
slsh, a standalone interpreter is available as well.

%package devel
Summary:        Programming Library and Embeddable Extension Language - Development Package
Group:          Development/Languages/C and C++
Requires:       libslang2 = %{version}
Provides:       slang:%{_includedir}/slang.h

%description devel
S-Lang is a programming library for creating multi-platform software.
It provides display/screen management, keyboard input, keymaps, etc.
Another feature is the interpreter for the S-Lang extension language
which can be embedded into an application to make it extensible. With
slsh, a standalone interpreter is available as well.

This package contains all necessary include files and libraries needed to
develop applications that require it.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# %%global _lto_cflags %%{_lto_cflags} -ffat-lto-objects
mv autoconf/configure.ac .
mv autoconf/aclocal.m4 autoconf/acinclude.m4
#autoheader -I autoconf
aclocal -I autoconf --output=autoconf/aclocal.m4
autoconf -I autoconf
export CFLAGS="%{optflags} -fno-strict-aliasing -fstack-protector"
export ELF_CFLAGS="$CFLAGS"
%configure \
    --docdir=%{_docdir}/slang-devel \
    --with-pcre \
    --with-z
#    --with-onig
# parallel make still broken in 2.2.2
make --jobs 1
# make  static --jobs 1

%install
make DESTDIR=%{buildroot} install
# install-static

rm -rf %{buildroot}%{_datadir}/doc/

%check
%ifnarch i586
%ifnarch s390
%ifnarch s390x
make check
%endif
%endif
%endif

%post -n libslang2 -p /sbin/ldconfig

%postun -n libslang2 -p /sbin/ldconfig

%files slsh
%doc COPYING slsh/README
%doc slsh/doc/html/
%config(noreplace) %{_sysconfdir}/slsh.rc
%{_bindir}/slsh
%{_libdir}/slang/
%{_datadir}/slsh/
%{_mandir}/man1/slsh.1*

%files -n libslang2
%{_libdir}/libslang.so.*

%files devel
%doc changes.txt NEWS README UPGRADE.txt demo/ examples/
%doc doc/grammar.txt doc/text/
%license COPYING
%{_includedir}/*
%{_libdir}/pkgconfig/slang.pc
# %%{_libdir}/libslang.a
%{_libdir}/libslang.so

%changelog
