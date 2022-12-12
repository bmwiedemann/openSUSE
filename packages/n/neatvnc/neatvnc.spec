#
# spec file for package neatvnc
#
# Copyright (c) 2022 SUSE LLC
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


%define libsoname libneatvnc0

Name:           neatvnc
Version:        0.5.4
Release:        0
Summary:        A VNC server library
License:        ISC
Group:          System/GUI/Other
URL:            https://github.com/any1/neatvnc
Source0:        %url/archive/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aml)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(zlib)

%description
This is a VNC server library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %libsoname = %{version}

%description    devel
Development files and headers for %{name}.

%package -n     %libsoname
Summary:        A VNC server library
Group:          System/Libraries

%description -n %libsoname
A VNC server library.

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %libsoname

%files devel
%license COPYING
%doc README.md
%{_includedir}/neatvnc.h
%{_libdir}/libneatvnc.so
%{_libdir}/pkgconfig/neatvnc.pc

%files -n %libsoname
%{_libdir}/libneatvnc.so.*

%changelog
