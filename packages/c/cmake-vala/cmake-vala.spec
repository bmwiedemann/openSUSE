#
# spec file for package cmake-vala
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cmake-vala
Version:        3
Release:        0
Summary:        Vala CMake modules
License:        BSD-3-Clause
URL:            https://gitlab.com/vala-panel-project/cmake-vala
Source:         https://gitlab.com/vala-panel-project/cmake-vala/-/archive/r%{version}/%{name}-r%{version}.tar.bz2
BuildRequires:  cmake >= 3.3

%description
This is a set of CMake modules: Translations, GSettings, and Vala
modules.

%package -n vala-cmake-modules
Summary:        Vala CMake modules

%description -n vala-cmake-modules
This is a set of CMake modules: Translations, GSettings, and Vala
modules.

%prep
%setup -q -n %{name}-r%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n vala-cmake-modules
%license LICENSE
%doc README.md README.Vala.rst
%{_datadir}/VCM/

%changelog
