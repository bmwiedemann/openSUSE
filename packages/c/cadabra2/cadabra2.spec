#
# spec file for package cadabra2
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


Name:           cadabra2
Version:        2.3.0
Release:        0
Summary:        A computer algebra system for solving problems in field theory
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://cadabra.science/
Source0:        https://github.com/kpeeters/cadabra2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-gtk.appdata.xml
# PATCH-FIX-UPSTREAM -- https://github.com/kpeeters/cadabra2/commit/4df3e7cba29a9bb25a70badbc9de8aeef3693933 (gh#kpeeters/cadabra2#202)
Patch2:         Fix-linking-of-cadabra-module.patch
# PATCH-FIX-UPSTREAM cadabra2-python-modules-location.patch gh#kpeeters/cadabra2#203 badshah400@gmail.com -- Move python modules to standard python modules path
Patch3:         cadabra2-python-modules-location.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libuuid-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-sympy
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(sqlite3)
Recommends:     %{name}-doc
Recommends:     %{name}-examples

%description
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory. It has extensive
functionality for tensor computer algebra, tensor polynomial
simplification including multi-term symmetries, fermions and
anti-commuting variables, Clifford algebras and Fierz transformations,
implicit coordinate dependence, multiple index types and many more.
The input format is a subset of TeX. Both a command-line and a
graphical interface are available.

Key features of Cadabra2:
- Input and output using TeX notation.
- Designed for field-theory problems, with handling of anti-commuting
  and non-commuting objects without special notations for their
  products, gamma matrix algebra, Fierz identities, Dirac conjugation,
  vielbeine, flat and curved, covariant and contravariant indices,
  implicit dependence of tensors on coordinates, partial and covariant
  derivatives...
- Powerful tensor simplification algorithms, not just for mono-term
  symmetries but also for multi-terms symmetries like the Bianchi
  identity, or dimensionally-dependent symmetries like the Schouten
  identity.

%package gui
Summary:        GUI for cadabra2: computer algebra system for problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Obsoletes:      cadabra < 2.0
Provides:       cadabra = %{version}

%description gui
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides the GUI for %{name} and it's desktop menu integration.

%package examples
Summary:        A computer algebra system for solving problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description examples
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides examples for %{name}.

%package doc
Summary:        A computer algebra system for solving problems in field theory
Group:          Documentation/HTML
Obsoletes:      cadabra-doc < 2.0
Provides:       cadabra-doc = %{version}

%description doc
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides html documentation for %{name}.

%prep
%setup -q
%patch2 -p1
%patch3 -p1
rm examples/.gitignore
# Remove timestamps from Doxygen HTML files
echo "HTML_TIMESTAMP = NO" >> config/Doxyfile
# REMOVE HASHBANG FROM NON-EXEC SCRIPT
sed -i "1{/#!\/usr\/bin\/env python/d}" libs/appdirs/cdb_appdirs.py

%build
%cmake \
  -DCMAKE_MANDIR:PATH=%{_mandir} \
  -DINSTALL_LATEX_DIR:PATH=%{_datadir}/texmf \
  -DENABLE_FRONTEND:BOOL=ON \
  -DENABLE_SYSTEM_JSONPP:BOOL=ON \
  -DENABLE_MATHEMATICA:BOOL=OFF \
  -DBUILD_TESTS:BOOL=ON

%cmake_build
cd ..
make %{?_smp_mflags} doc

%install
%cmake_install

%suse_update_desktop_file cadabra2-gtk

# INSTALL APPDATA TO /usr/share/metainfo
install -D -m0644 %{S:1} %{buildroot}%{_datadir}/metainfo/%{name}-gtk.appdata.xml

# Replace "/usr/bin/env python3" hashbang by "/usr/bin/python3"
sed -E -i "s|^#!/usr/bin/env python3|#!/usr/bin/python3|" %{buildroot}%{_bindir}/cadabra2

mkdir -p %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/
ln %{buildroot}%{_datadir}/cadabra2/latex/* %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.rst
%license doc/license.txt
%{_bindir}/cadabra2cadabra
%{_bindir}/cadabra2latex
%{_bindir}/cadabra-server
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}python
%{_bindir}/%{name}html
%{_datadir}/%{name}/
%{_datadir}/texmf
%{python3_sitearch}/*
%{_mandir}/man1/cadabra*.1%{?ext_man}

%files gui
%{_bindir}/%{name}-gtk
%{_datadir}/icons/hicolor/*/apps/cadabra2-gtk.*
%{_datadir}/applications/cadabra2-gtk.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml

%files examples
%doc examples/

%files doc
%doc doxygen/html

%changelog
