#
# spec file for package eglexternalplatform
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           eglexternalplatform
Version:        1.2.1
Release:        0
Summary:        The EGL External Platform interface
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/NVIDIA/eglexternalplatform
Source0:        https://github.com/NVIDIA/eglexternalplatform/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson

%description
A work-in-progress specification of the EGL External Platform interface.

%package devel
Summary:        The EGL External Platform interface
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel
This is a work-in-progress specification of the EGL External Platform interface
for writing EGL platforms and their interactions with window systems on
top of existing low-level EGL platform implementations. This keeps window system
implementation specifics out of EGL drivers by using application-facing
EGL functions.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

%files devel
%license COPYING
%doc README.md
%{_datadir}/pkgconfig/eglexternalplatform.pc
%{_includedir}/*.h

%changelog
