#
# spec file for package girara
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


%define libname libgirara
%define so_ver  5
%if 0%{?suse_version} == 1600
%bcond_without gcc15
%endif
Name:           girara
Version:        2026.07.07
Release:        0
Summary:        Graphical user interface library
License:        Zlib
URL:            https://pwmt.org/projects/girara
Source0:        %{url}/download/girara-%{version}.tar.xz
Source1:        %{url}/download/girara-%{version}.tar.xz.asc
Source2:        girara.keyring
BuildRequires:  c_compiler
BuildRequires:  meson >= 1.5
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.72
BuildRequires:  pkgconfig(glib-2.0) >= 2.72
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72
%if %{with gcc15}
BuildRequires:  gcc15
%endif

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

%package -n %{libname}%{so_ver}
Summary:        A graphical user interface library

%description -n %{libname}%{so_ver}
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
Requires:       %{libname}%{so_ver} = %{version}-%{release}

%description devel
Header files for the girara user interface library.

%package        devel-doc
Summary:        Documentation for girara-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildArch:      noarch

%description    devel-doc
Doxygen generated documentations for girara-devel.

%prep
%autosetup -p1

%build
%{?with_gcc15:export CC=gcc-15}
%meson
%meson_build

%install
%meson_install
install -dm 0755 %{buildroot}%{_docdir}/girara-devel-doxygen/
cp -a %{_vpath_builddir}/doc/html %{buildroot}%{_docdir}/girara-devel-doxygen/
%fdupes -s %{buildroot}%{_docdir}/girara-devel-doxygen/

%check
%meson_test

%ldconfig_scriptlets -n %{libname}%{so_ver}

%files -n %{libname}%{so_ver}
%{_libdir}/libgirara.so.%{so_ver}*

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libgirara.so
%{_includedir}/girara
%{_libdir}/pkgconfig/girara.pc

%files devel-doc
%{_docdir}/girara-devel-doxygen

%changelog
