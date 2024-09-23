#
# spec file for package libacm
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libacm
%define lname   libacm-1_3
%define commit  110a8a03806c2a4e00b772a32f17b7207060000f
Version:        1.3+g7.110a8a0
Release:        0
Summary:        Decoder for ACM audio files
License:        MIT AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/markokr/libacm
Source:         https://github.com/markokr/libacm/archive/%commit.tar.gz
Patch1:         shared.patch
Patch2:         autoconf-leap.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(ao)
BuildRequires:  xz

%description
Decoder library for InterPlay ACM audio files.

%package -n %lname
Summary:        Decoder for ACM audio files
Group:          System/Libraries
License:        MIT

%description -n %lname
Decoder library for InterPlay ACM audio files.
ACM is a slightly compressed variant of PCM.

%package devel
Summary:        Development for libacm, an audio decoder library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
License:        MIT

%description devel
Decoder library for InterPlay ACM audio files.
This subpackage contains the header files for libacm.

%prep
%autosetup -p1 -n %name-%commit
./autogen.sh

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libacm-1.3.so

%files devel
%_bindir/acmtool
%_includedir/*.h
%_libdir/libacm.so
%license COPYING

%changelog
