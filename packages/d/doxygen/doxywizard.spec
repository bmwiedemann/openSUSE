#
# spec file for package doxywizard
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


Name:           doxywizard
Version:        1.14.0
Release:        0
Summary:        Graphical User Interface for Doxygen
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later
Group:          Development/Tools/Doc Generators
URL:            https://www.doxygen.nl/
Source:         https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz
Source1:        doxywizard.desktop
BuildRequires:  bison
BuildRequires:  cmake >= 3.14
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
Requires:       doxygen = %{version}
# for make tests
BuildRequires:  libxml2-tools
BuildRequires:  texlive-bibtex

%description
Doxywizard is a graphical front-end to read/edit/write doxygen
configuration files.

%prep
%autosetup -p1 -n doxygen-%{version}

%build
%cmake \
    -Dbuild_wizard=ON \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_STATIC_LIBS=ON
%cmake_build

%check
export LANG=C.UTF-8
# testing doxygen package here to avoid build
# cycle between latex and doxygen
%ctest

%install
%cmake_install
rm %{buildroot}%{_bindir}/doxygen
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 doc/doxywizard.1 %{buildroot}%{_mandir}/man1/
rm %{buildroot}%{_mandir}/man1/doxygen.1
%suse_update_desktop_file -i doxywizard Development Documentation

%files
%attr(755,root,root) %{_bindir}/doxywizard
%{_datadir}/applications/doxywizard.desktop
%{_mandir}/man1/doxywizard.1%{?ext_man}

%changelog
