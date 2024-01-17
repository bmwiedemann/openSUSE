#
# spec file for package squirrel
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


### Upstream doesn't version the library and changes ABI
### bump this version on every version update or check that it should remain
### Re-run %%setup (quilt setup) after each update
%define sover 1001

# Disable LTO optimizations
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%define tarver 3_2
Name:           squirrel
Version:        3.2
Release:        0
Summary:        A high level imperative/OO programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://squirrel-lang.org/
Source:         https://downloads.sourceforge.net/squirrel/squirrel_%{tarver}_stable.tar.gz
Source1:        squirrel-config.cmake.in
Source10:       sover.patch.in
Source11:       squirrel.rpmlintrc
Patch1:         c++11.patch
# Generated from S:10 in %%prep, so update that if patch no longer applies
Patch10:        sover.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed

%description
Squirrel is a programming language featuring higher-order functions,
classes, inheritance, delegation, tail recursion, generators,
cooperative threads, exception handling, reference counting, garbage
collection on demand, and a C-like syntax.

%package        -n libsquirrel%{sover}
Summary:        Development files for %{name}

%description -n libsquirrel%{sover}
This package contains runtime library for Squirrel

%package        devel
Summary:        Development files for %{name}
Requires:       libsquirrel%{sover} = %{version}

%description devel
This package contains everything to embed the Squirrel engine in
your own application.

%package        doc
Summary:        Documentation for %{name}
Supplements:    %{name} = %{version}
BuildArch:      noarch

%description doc
Documentation files for squirrel.

%package        examples
Summary:        Example scripts for %{name}
Suggests:       %{name} = %{version}
BuildArch:      noarch

%description examples
Example scripts to show squirrel usage.

%prep
%setup -q -n squirrel3
sed -e 's,1000,%{sover},g' < %{_sourcedir}/sover.patch.in > %{_sourcedir}/sover.patch
%patch1 -p1
%patch10 -p1
cp %SOURCE1 .

%build
%cmake \
    -DDISABLE_STATIC=1 \
    -DLONG_OUTPUT_NAMES=1
make %{?_smp_mflags}

%install
%cmake_install
# compat link for older distros
%if %suse_version < 1599
ln -s /usr/bin/squirrel3 %{buildroot}%{_bindir}/sqrl
%endif

%post -n libsquirrel%{sover} -p /sbin/ldconfig
%postun -n libsquirrel%{sover} -p /sbin/ldconfig

%files
%{_bindir}/squirrel3
%if %suse_version < 1599
%{_bindir}/sqrl
%endif

%files -n libsquirrel%{sover}
%license COPYRIGHT
%{_libdir}/*.so.%{sover}
%{_libdir}/*.so.%{sover}.*

%files devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/squirrel
%{_includedir}/sq*.h
%{_libdir}/*.so
%{_libdir}/cmake/squirrel/*

%files doc
%license COPYRIGHT
%doc README HISTORY
%doc doc/*

%files examples
%license COPYRIGHT
%doc samples/*

%changelog
