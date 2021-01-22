#
# spec file for package sord
#
# Copyright (c) 2021 SUSE LLC
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
Name:           sord
Version:        0.16.8
Release:        0
Summary:        Utilities to work with RDF data
License:        ISC
Group:          Productivity/File utilities
URL:            https://drobilla.net/software/sord/
Source0:        http://download.drobilla.net/sord-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(serd-0) >= 0.22.4

%description
Utilities to work with RDF data.
Sord is a lightweight C library for storing RDF data in memory.

%package        -n libsord-0-%{sover}
Summary:        A lightweight C library for storing RDF data in memory
Group:          System/Libraries

%description    -n libsord-0-%{sover}
A lightweight C library for storing RDF data in memory.
http://drobilla.net/software/sord/

%package        devel
Summary:        Development files for libsord
Group:          Development/Libraries/C and C++
Requires:       libsord-0-%{sover} = %{version}
Provides:       libsord-0-devel = %{version}
Obsoletes:      libsord-0-devel < %{version}

%description    devel
Development files for libsord.
Sord is a lightweight C library for storing RDF data in memory.

%prep
%setup -q

%build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
python3 ./waf configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --docdir=%{_defaultdocdir} \
  --test \
  --docs
# waf only understands -j, so do not use smp_mflags
python3 ./waf build -v %{?_smp_mflags}

%install
python3 ./waf install --destdir=%{?buildroot}
rm -rf %{buildroot}%{_docdir}/sord-0/html

%check
python3 ./waf test

%post -n libsord-0-%{sover} -p /sbin/ldconfig
%postun -n libsord-0-%{sover} -p /sbin/ldconfig

%files
%attr(0755,root,root) %{_bindir}/sordi
%attr(0755,root,root) %{_bindir}/sord_validate
%{_mandir}/man1/sordi.1%{?ext_man}
%{_mandir}/man1/sord_validate.1%{?ext_man}

%files -n libsord-0-%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libsord-0.so.%{sover}*

%files devel
%{_mandir}/man3/sord.3%{?ext_man}
%{_libdir}/libsord-0.so
%{_includedir}/sord-0/
%{_libdir}/pkgconfig/sord-0.pc

%changelog
