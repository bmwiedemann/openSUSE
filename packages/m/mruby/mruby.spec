# vim: set sw=4 ts=4 et nu:
#
# spec file for package mruby
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%define sover 3_1_0
Name:           mruby
Version:        3.1.0
Release:        0
Summary:        Lightweight Ruby
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/mruby/mruby/
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE PATCH-FEATURE-UPSTREAM link-with-soname.patch -- Add SONAME to library
Patch0:         link-with-soname.patch
# PATCH-FIX-UPSTREAM CVE-2022-1286.patch -- boo#1198289 https://github.com/mruby/mruby/commit/b1d0296a
Patch2:         CVE-2022-1286.patch
# PATCH-FIX-UPSTREAM CVE-2022-1212.patch -- https://github.com/mruby/mruby/commit/3cf291f72224715942beaf8553e42ba8891ab3c6
Patch3:         CVE-2022-1212.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1500
BuildRequires:  %{rb_default_ruby_suffix}
%else
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rake)
%endif

%description
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard.

mruby can be linked and embedded within your application.

We provide the interpreter program "mruby" and the interactive mruby shell
"mirb" as examples.

You can also compile Ruby programs into compiled byte code using the mruby
compiler "mrbc".

The "mrbc" is also able to generate compiled byte code in a C source file.

%package devel
Summary:        Lightweight Ruby Embedded Environment
Group:          Development/Languages/Ruby
Requires:       libmruby%{sover} = %{version}
Requires:       libmruby_core%{sover} = %{version}

%description devel
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard.

This package contains the headers and static library files in order to embed
mruby into your application.

%package -n libmruby%{sover}
Summary:        Lightweight Ruby Embedded Environment
Group:          Development/Languages/Ruby
# Was wrongly used (only) on Factory until 02-2022
Obsoletes:      libmruby3 < %{version}

%description -n libmruby%{sover}
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard.

%package -n libmruby_core%{sover}
Summary:        Lightweight Ruby Embedded Environment
Group:          Development/Languages/Ruby

%description -n libmruby_core%{sover}
mruby is the lightweight implementation of the Ruby language complying to (part
of) the ISO standard.

%prep
%autosetup -p1
# Currently broken
sed -i 's|conf.enable_debug|# conf.enable_debug|' build_config/host-shared.rb

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
export MRUBY_CONFIG="host-shared"
# Needed for mruby to find its libraries before they are installed
export LD_LIBRARY_PATH="$PWD/build/host/mrbc/lib/"
rake all

%install
# Install binaries
for b in mirb mrbc mruby; do
    install -D -m 0755 "bin/${b}" "%{buildroot}%{_bindir}/${b}"
done

# Install libraries
for l in mruby mruby_core; do
	l=l"ib$l.so"
    install -D -m 0755 "build/host/lib/${l}.%{version}" "%{buildroot}%{_libdir}/$l.%{version}"
    ln -s "${l}.%{version}" "%{buildroot}%{_libdir}/${l}"
done

install -d "%{buildroot}%{_includedir}"
cp -a include/* "%{buildroot}%{_includedir}/"

%post   -p /sbin/ldconfig -n libmruby%{sover}
%post   -p /sbin/ldconfig -n libmruby_core%{sover}
%postun -p /sbin/ldconfig -n libmruby%{sover}
%postun -p /sbin/ldconfig -n libmruby_core%{sover}

%files -n libmruby%{sover}
%{_libdir}/libmruby.so.%{version}

%files -n libmruby_core%{sover}
%{_libdir}/libmruby_core.so.%{version}

%files
%doc AUTHORS CONTRIBUTING.md LEGAL NEWS README.md
%license LICENSE
%{_bindir}/mirb
%{_bindir}/mrbc
%{_bindir}/mruby
%{_bindir}/mrbc

%files devel
%{_includedir}/mr*.h
%{_includedir}/mruby
%{_libdir}/libmruby*.so

%changelog
