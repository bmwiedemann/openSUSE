#
# spec file for package compiz-plugins-extra
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _rev    d941a41bbfcf3e4475e01fd00da37c85
Name:           compiz-plugins-extra
Version:        0.8.16
Release:        0
Summary:        OpenGL window and compositing manager community extra plugins
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/compiz/compiz-plugins-extra
Source:         https://gitlab.com/compiz/compiz-plugins-extra/uploads/%{_rev}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE dimstar@opensuse.org -- Define some sane standards for the extra plugins.
Patch0:         compiz-plugins-extra-defaults.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcop) < 0.9
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(compiz-animation) < 0.9
BuildRequires:  pkgconfig(compiz-cube) < 0.9
BuildRequires:  pkgconfig(compiz-mousepoll) < 0.9
BuildRequires:  pkgconfig(compiz-scale) < 0.9
BuildRequires:  pkgconfig(compiz-text) < 0.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libnotify)
Requires:       compiz < 0.9
Requires:       compiz-plugins-main < 0.9
Recommends:     %{name}-lang
Provides:       compiz-fusion-plugins-extra = %{version}
Obsoletes:      compiz-fusion-plugins-extra < %{version}
ExcludeArch:    s390 s390x

%description
This package contains the community extra Compiz compositing
manager plugins.

Contains: addhelper crashhandler extrawm firepaint goto-viewport
mswitch scalefilter splash bench cubereflex fadedesktop gears group
mblur reflex showdesktop trailfocus.

%lang_package

%package devel
Summary:        OpenGL window and compositing manager community extra plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(bcop) < 0.9
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(compiz) < 0.9
Requires:       pkgconfig(compiz-animation) < 0.9
Requires:       pkgconfig(compiz-cube) < 0.9
Requires:       pkgconfig(compiz-mousepoll) < 0.9
Requires:       pkgconfig(compiz-scale) < 0.9
Requires:       pkgconfig(compiz-text) < 0.9
Requires:       pkgconfig(gl)
Requires:       pkgconfig(libnotify)
Provides:       compiz-fusion-plugins-extra-devel = %{version}
Obsoletes:      compiz-fusion-plugins-extra-devel < %{version}

%description devel
This package contains the community extra Compiz compositing
manager plugins.

This package contain development files required for developing
other plugins.

%prep
%setup -q
%patch0 -p1

%if 0%{?suse_version} < 1500 && !(0%{?sle_version} > 120100 && 0%{?is_opensuse})
# Workaround /usr/@DATADIRNAME@/locale/.
rm -r m4/
%endif

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/compiz/*
%{_datadir}/compiz/*

%files lang -f %{name}.lang

%files devel
%{_includedir}/compiz/compiz-*.h
%{_libdir}/pkgconfig/compiz-*.pc

%changelog
