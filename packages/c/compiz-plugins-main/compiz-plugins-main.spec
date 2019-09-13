#
# spec file for package compiz-plugins-main
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


%define _rev    04ce73e38045e608944b5ec668820f18
Name:           compiz-plugins-main
Version:        0.8.16
Release:        0
Summary:        OpenGL window and compositing manager plugins
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/compiz/compiz-plugins-main
Source:         https://gitlab.com/compiz/compiz-plugins-main/uploads/%{_rev}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libjpeg8-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcop) >= 0.7.3
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(cairo-xlib-xrender)
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(compiz-scale) < 0.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(pangocairo)
Requires:       compiz-plugins < 0.9
Recommends:     %{name}-lang
Conflicts:      compiz-extra < %{version}
ExcludeArch:    s390 s390x

%description
This package contains the non-default Compiz compositing manager
plugins.

%lang_package

%package devel
Summary:        OpenGL window and compositing manager plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(bcop)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(cairo-xlib-xrender)
Requires:       pkgconfig(compiz) < 0.9
Requires:       pkgconfig(compiz-scale) < 0.9
Requires:       pkgconfig(gl)
Requires:       pkgconfig(pangocairo)
Provides:       compiz-fusion-plugins-main-devel = %{version}
Obsoletes:      compiz-fusion-plugins-main-devel < %{version}

%description devel
This package contains the non-default Compiz compositing manager
plugins.

%prep
%setup -q
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

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/compiz/*
%{_datadir}/compiz/*

%files lang -f %{name}.lang

%files devel
%{_includedir}/compiz/
%{_libdir}/pkgconfig/*.pc

%changelog
