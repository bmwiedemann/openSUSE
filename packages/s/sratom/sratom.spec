#
# spec file for package sratom
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           sratom
Version:        0.6.20
Release:        0
Summary:        A library for serialising LV2 atoms to/from RDF
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://drobilla.net/software/sratom.html
Source0:        https://download.drobilla.net/sratom-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lv2) >= 1.18.4
BuildRequires:  pkgconfig(serd-0) >= 0.30.10
BuildRequires:  pkgconfig(sord-0) >= 0.16.16

%description
A library for serialising LV2 atoms to/from RDF, particularly the Turtle syntax.

%package        -n libsratom-0-%{sover}
Summary:        A library for serialising LV2 atoms to/from RDF
Group:          System/Libraries

%description    -n libsratom-0-%{sover}
A library for serialising LV2 atoms to/from RDF, particularly the Turtle syntax.

%package        devel
Summary:        Development files for libsratom
Group:          Development/Libraries/C and C++
Requires:       libsratom-0-%{sover} = %{version}
Provides:       libsratom-0-devel = %{version}
Obsoletes:      libsratom-0-devel < %{version}

%description    devel
Development files for libsratom.

%prep
%autosetup -p1

%build
%meson -Ddocs=disabled
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libsratom-0-%{sover}

%files -n libsratom-0-%{sover}
%license COPYING
%doc NEWS
%{_libdir}/libsratom-0.so.%{sover}*

%files devel
%license COPYING
%{_libdir}/libsratom-0.so
%{_includedir}/sratom-0/
%{_libdir}/pkgconfig/sratom-0.pc

%changelog
