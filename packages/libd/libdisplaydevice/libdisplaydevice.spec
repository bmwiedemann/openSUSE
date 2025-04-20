#
# spec file for package libdisplaydevice
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover 0_0_0
Name:           libdisplaydevice
Version:        2025.115.133852
Release:        0
Summary:        C++ library to modify display devices
License:        AGPL-3.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/LizardByte/libdisplaydevice
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         soversion.patch
BuildRequires:  boost-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.24
BuildRequires:  ninja
BuildRequires:  patchelf
BuildRequires:  pkgconfig(nlohmann_json)

%description
libdisplaydevice is a WIP library that provides a common interface for
interacting with display devices. It is intended to be used by applications
that need to interact with displays, such as screen capture software, remote
desktop software, and video players.

As of right now, this is only a dummy library

%package -n %{name}%{sover}
Summary:        C++ library to modify display devices

%description -n %{name}%{sover}
libdisplaydevice is a WIP library that provides a common interface for
interacting with display devices. It is intended to be used by applications
that need to interact with displays, such as screen capture software, remote
desktop software, and video players.

%prep
%autosetup -p1

%build
%cmake -DBUILD_DOCS=false -DBUILD_TESTS=false
%cmake_build

%install
install -D build/src/common/lib%{name}_common.so.0.0.0 %{buildroot}%{_libdir}/%{name}_common.so.0.0.0

#fix soname
patchelf --set-soname %{name}_common.so.0.0.0 %{buildroot}%{_libdir}/%{name}_common.so.0.0.0

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/%{name}_common.so.0.0.0

%changelog
