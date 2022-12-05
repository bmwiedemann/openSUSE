#
# spec file for package tllist
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


Name:           tllist
Version:        1.1.0
Release:        0
Summary:        A C header file only implementation of a typed linked list
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://codeberg.org/dnkl/tllist
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson

%description
tllist is a Typed Linked List C header file only library implemented using pre-processor macros.

%package devel
Summary:        A C header file only implementation of a typed linked list
Group:          Development/Libraries/C and C++

%description devel
tllist is a Typed Linked List C header file only library implemented using pre-processor macros.

%prep
%autosetup -n %{name}

%build
%meson
%meson_build

%install
%meson_install

%files devel
%license LICENSE
%doc README.md
%{_datadir}/doc/%{name}/
%{_includedir}/tllist.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
