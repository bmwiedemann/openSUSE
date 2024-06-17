#
# spec file for package girara
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


%define libname libgirara-gtk3
%define so_ver  4
Name:           girara
Version:        0.4.4
Release:        0
Summary:        Graphical user interface library
License:        Zlib
URL:            https://pwmt.org/projects/girara
Source0:        %{url}/download/girara-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pango) >= 1.14

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism. Currently based on GTK+,
it provides an interface that focuses on three main
components: A so-called view widget that represents the actual
application (e.g. a website (browser), an image (image viewer) or the
document (document viewer)), an input bar that is used to execute
commands of the application and the status bar which provides the user
with current information. girara was designed to replace and enhance
the user interface that is used by zathura and jumanji and other
features that those applications share.

%package -n %{libname}-%{so_ver}
Summary:        A graphical user interface library

%description -n %{libname}-%{so_ver}
girara is a library that implements a user interface that focuses on
simplicity and minimalism. Currently based on GTK+,
it provides an interface that focuses on three main
components: A so-called view widget that represents the actual
application (e.g. a website (browser), an image (image viewer) or the
document (document viewer)), an input bar that is used to execute
commands of the application and the status bar which provides the user
with current information. girara was designed to replace and enhance
the user interface that is used by zathura and jumanji and other
features that those applications share.

%package devel
Summary:        Header files for the girara library
Requires:       %{libname}-%{so_ver} = %{version}-%{release}

%description devel
Header files for the girara user interface library.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install

%find_lang %{libname}-%{so_ver}
find %{buildroot} -name '*.*a' -delete -print

%post -n %{libname}-%{so_ver} -p /sbin/ldconfig

%postun	-n %{libname}-%{so_ver} -p /sbin/ldconfig

%files -n %{libname}-%{so_ver} -f %{libname}-%{so_ver}.lang
%license LICENSE
%doc README.md
%{_libdir}/libgirara-gtk3.so.*

%files devel
%{_libdir}/libgirara-gtk3.so
%{_includedir}/girara
%{_libdir}/pkgconfig/girara-gtk3.pc

%changelog
