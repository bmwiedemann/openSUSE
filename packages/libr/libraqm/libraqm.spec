#
# spec file for package libraqm
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


%define sover 0
Name:           libraqm
Version:        0.10.1
Release:        0
Summary:        Complex Textlayout Library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/HOST-Oman/libraqm
Source:         https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.xz
BuildRequires:  freetype2-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(harfbuzz) >= 1.7.2

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package -n %{name}%{sover}
Summary:        Complex Textlayout Library
Group:          System/Libraries
# The license and the generic %%doc files were moved to the library subpackage
Conflicts:      libraqm-doc < 0.7.2

%description -n %{name}%{sover}
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package doc
Summary:        Libraqm documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation files for raqm.

%package devel
Summary:        Complex Textlayout Library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%prep
%autosetup -n raqm-%{version} -p1

%build
%meson -Ddocs=true
%meson_build

%install
%meson_install

%check
# python 3.6 is too old for running tests
%if 0%{?suse_version} > 1500
export LC_ALL=C.utf8
%meson_test
%endif

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libraqm.so.*

%files devel
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files doc
%{_datadir}/gtk-doc/html/raqm

%changelog
