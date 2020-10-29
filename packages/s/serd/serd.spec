#
# spec file for package serd
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


%define sover 0
Name:           serd
Version:        0.30.6
Release:        0
Summary:        A lightweight C library for RDF syntax
License:        ISC
Group:          Development/Libraries/C and C++
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/serd-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  python3-base

%description
A lightweight C library for RDF syntax  which supports reading and writing Turtle and NTriples.

%package        -n serdi
Summary:        Read and write RDF syntax
Group:          Productivity/Text/Editors

%description    -n serdi
Read and write RDF syntax.

%package        -n libserd-0-%{sover}
Summary:        A lightweight C library for RDF syntax
Group:          System/Libraries

%description    -n libserd-0-%{sover}
A lightweight C library for RDF syntax which supports reading and writing Turtle and NTriples.

%package        devel
Summary:        Development files for libserd
Group:          Development/Libraries/C and C++
Requires:       libserd-0-%{sover} = %{version}
Provides:       libserd-0-devel = %{version}
Obsoletes:      libserd-0-devel < %{version}

%description    devel
Development files for libserd.

%prep
%setup -q
#Convert all file headers to python3
for i in `grep -rl "%{_bindir}/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
export CFLAGS='%{optflags} -std=gnu99'
export CXXFLAGS='%{optflags}'
./waf configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --docdir=%{_defaultdocdir} \
  --test \
  --docs

./waf build -v %{?_smp_mflags}

%install
./waf install --destdir=%{?buildroot}
rm -rf %{buildroot}%{_docdir}/serd-0/html

%check
./waf test

%post -n libserd-0-%{sover} -p /sbin/ldconfig
%postun -n libserd-0-%{sover} -p /sbin/ldconfig

%files -n serdi
%attr(0755,root,root) %{_bindir}/serdi
%{_mandir}/man1/serdi.1%{?ext_man}

%files -n libserd-0-%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libserd-0.so.%{sover}*

%files devel
%{_libdir}/libserd-0.so
%{_includedir}/serd-0/
%{_libdir}/pkgconfig/serd-0.pc
%{_mandir}/man3/serd.3%{?ext_man}

%changelog
