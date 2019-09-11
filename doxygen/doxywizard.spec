#
# spec file for package doxywizard
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           doxywizard
Version:        1.8.15
Release:        0
Summary:        Graphical User Interface for Doxygen
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Tools/Doc Generators
Url:            http://www.doxygen.nl/
Source:         http://doxygen.nl/files/doxygen-%{version}.src.tar.gz
Source1:        doxywizard.desktop
# PATCH-FIX-UPSTREAM: add missing returns to non-void functions
Patch3:         vhdlparser-no-return.patch
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.12
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
Requires:       doxygen = %{version}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%if 0%{?suse_version} > 1230 && 0%{?suse_version} != 1315
# for make tests
BuildRequires:  libxml2-tools
BuildRequires:  texlive-bibtex
%endif

%description
Doxywizard is a graphical front-end to read/edit/write doxygen
configuration files.

%prep
%setup -q -n doxygen-%{version}
%patch3 -p1

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake \
    -Dbuild_wizard=ON \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now"
%make_jobs

%if 0%{?suse_version} > 1230 && 0%{?suse_version} != 1315
%check
export LANG=C.UTF-8
# testing doxygen package here to avoid build
# cycle between latex and doxygen
pushd build
make tests %{?_smp_mflags}
popd
%endif

%install
%cmake_install
rm %{buildroot}%{_bindir}/doxygen
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 doc/doxywizard.1 %{buildroot}%{_mandir}/man1/
%suse_update_desktop_file -i doxywizard Development Documentation

%files
%attr(755,root,root) %{_bindir}/doxywizard
%{_datadir}/applications/doxywizard.desktop
%{_mandir}/man1/doxywizard.1%{ext_man}

%changelog
