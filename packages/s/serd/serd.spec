#
# spec file for package serd
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1600
%define with_docs 1
%endif

%define sover 0
Name:           serd
Version:        0.32.2
Release:        0
Summary:        A lightweight C library for RDF syntax
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://drobilla.net/software/serd.html
Source0:        https://download.drobilla.net/serd-%{version}.tar.xz
Source1:        baselibs.conf
Patch0:         001-serd-docdir.patch
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
%if %{with docs}
BuildRequires:  %{python_module sphinxygen}
BuildRequires:  doxygen
BuildRequires:  mandoc-bin
BuildRequires:  python3-Sphinx
%endif

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
%autopatch -p0
#Convert all file headers to python3
for i in `grep -rl "%{_bindir}/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
%meson \
%if %{without docs}
    -Ddocs=disabled
%endif
%meson_build

%install
%meson_install

%fdupes -s %{buildroot}%{_docdir}

%post -n libserd-0-%{sover} -p /sbin/ldconfig
%postun -n libserd-0-%{sover} -p /sbin/ldconfig

%files -n serdi
%attr(0755,root,root) %{_bindir}/serdi
%if %{with docs}
%{_mandir}/man1/serdi.1%{?ext_man}
%endif

%files -n libserd-0-%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libserd-0.so.%{sover}*

%files devel
%if %{with docs}
%doc %{_docdir}/serd-0
%endif
%{_libdir}/libserd-0.so
%{_includedir}/serd-0/
%{_libdir}/pkgconfig/serd-0.pc

%changelog
