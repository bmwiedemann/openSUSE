#
# spec file for package wxhexeditor
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


%bcond_with gcc6
%define _name   wxHexEditor
%define _rev    3f34976552e4d8f62c260b60825b7d0faf064ff2

Name:           wxhexeditor
Version:        0.24
Release:        0
Summary:        A free HEX editor / disk editor
# Program is statically linked to udis86 which is BSD-2-Clause
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/EUA/wxHexEditor
Source:         https://github.com/EUA/wxHexEditor/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE wxhexeditor-0.23-mhash.patch lazy.kent@opensuse.org -- Use system mhash library.
Patch0:         %{name}-0.23-mhash.patch
# PATCH-FIX-OPENSUSE wxhexeditor-remove-debug.patch zaitor@opensuse.org -- Remove debug msg that include nonsense.
Patch1:         wxhexeditor-remove-debug.patch
# PATCH-FIX-UPSTREAM wxhexeditor-fixdesktopfile.patch davejplater@gmail.com -- Fix desktop file
Patch2:         wxhexeditor-fixdesktopfile.patch
# PATCH-FIX-UPSTREAM - https://github.com/EUA/wxHexEditor/issues/90
Patch3:         wxhexeditor-fix-arm.patch
%if %{with gcc6}
%if 0%{?sle_version} >= 120200
#!BuildIgnore:  libgcc_s1
BuildRequires:  cpp6
BuildRequires:  gcc6
BuildRequires:  gcc6-c++
%endif
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mhash-devel
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
Recommends:     %{name}-lang

%description
wxHexEditor is a hex editor that is capable of handling very large
files. It supports files up to 2^64 bytes. It can also act as a
disk editor.
Features:
 * Small footprint on RAM;
 * Raw Disk Access (on POSIX systems);
 * Does not create temporary files.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
rm -rf mhash
%patch0 -p0
%patch1 -p0
%patch2
%patch3 -p1
chmod -x docs/*
cp -v udis86/LICENSE LICENSE-udis86
cp -v docs/GPL.txt .

%build
%if %{with gcc6}
%if 0%{?sle_version} >= 120200
export CC=gcc-6
export CPP=cpp-6
export CXX=g++-6
%endif
%endif
make %{?_smp_mflags} V=1 \
%if 0%{?suse_version} > 1320
  PYTHON='%{_bindir}/python3' \
%endif
  CFLAGS='%{optflags}'   \
  CXXFLAGS='%{optflags}'

%install
%make_install PREFIX=%{_prefix}
%find_lang %{_name} %{?no_lang_C}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc docs/Change.log README.md
%license GPL.txt LICENSE-udis86
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.png

%files lang -f %{_name}.lang
%defattr(-,root,root)

%changelog
