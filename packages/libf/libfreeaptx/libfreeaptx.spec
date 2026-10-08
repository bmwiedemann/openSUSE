#
# spec file for package libfreeaptx
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           libfreeaptx
%define lname   libfreeaptx0
Version:        0.2.2
Release:        0
Summary:        Open Source implementation of Audio Processing Technology codec (aptX)
License:        LGPL-2.0-or-later
URL:            https://github.com/regularhunter/libfreeaptx
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf

BuildRequires:  c_compiler
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  sed

%description
This is Open Source implementation of Audio Processing Technology codec (aptX)
derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec is
mainly used in Bluetooth A2DP profile.

%package     -n %lname
Summary:        Shared libraries for %{name}

%description -n %lname
This is Open Source implementation of Audio Processing Technology codec (aptX)
derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec is
mainly used in Bluetooth A2DP profile.
This package contains the shared library files.

%package        devel
Summary:        Development files for %{name}
Requires:       %lname = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Encoder and decoder utilities for %{name}
Requires:       %lname = %{version}

%description    tools
The %{name}-tools package contains openaptxenc encoder and openaptxdec decoder
command-line utilities.

%prep
%autosetup -p1

sed -i s/"^PREFIX =.*"/"PREFIX = \/usr"/ Makefile
sed -i s/"^LIBDIR = .*"/"LIBDIR = %{_lib}"/ Makefile

%build
%make_build CC=gcc

%install
%make_install

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/freeaptx.h
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/freeaptxenc
%{_bindir}/freeaptxdec

%changelog
