#
# spec file for package ftxui
#
# Copyright (c) 2023 SUSE LLC
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

%define         c_lib libftxui4_0_0
Name:           ftxui
Version:        4.0.0
Release:        0
Summary:        A C++ library for terminal based user interfaces
License:        MIT
URL:            https://github.com/ArthurSonzogni/FTXUI
Source:         https://github.com/ArthurSonzogni/FTXUI/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A C++ library for terminal based user interfaces.

%package -n     %{c_lib}
Summary:        A C++ library for terminal based user interfaces
Group:          System/Libraries
Recommends:     %{name} >= %{version}

%description -n %{c_lib}
A C++ library for terminal based user interfaces.

%package devel
Summary:        Devel files for ftxui
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description devel
Development files for ftxui.

%prep
%autosetup -n FTXUI-%{version}

%build
%cmake -DFTXUI_BUILD_EXAMPLES=OFF \
       -DFTXUI_BUILD_TESTS=OFF \
       -DFTXUI_BUILD_DOCS=OFF \
       -DFTXUI_ENABLE_INSTALL=ON

%install
%cmake_install

%ldconfig_scriptlets -n libftxui4_0_0

%files -n %{c_lib}
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libftxui-component.so.4.0.0
%{_libdir}/libftxui-dom.so.4.0.0
%{_libdir}/libftxui-screen.so.4.0.0

%files devel
%license LICENSE
%doc CHANGELOG.md README.md
%{_includedir}/ftxui/
%{_libdir}/cmake/ftxui/
%{_libdir}/libftxui-component.so
%{_libdir}/libftxui-dom.so
%{_libdir}/libftxui-screen.so

%changelog
