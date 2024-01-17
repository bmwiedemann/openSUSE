#
# spec file for package lwjgl3
#
# Copyright (c) 2021 SUSE LLC
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


Name:           lwjgl3
Version:        3.2.3
Release:        0
Summary:        Lightweight Java Game Library 3
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.lwjgl.org/
Source:         https://github.com/LWJGL/lwjgl3/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildArch:      noarch

%description
LWJGL is a Java library that enables cross-platform access to popular native APIs
useful in the development of graphics (OpenGL, Vulkan), audio (OpenAL), parallel
computing (OpenCL, CUDA) and XR (OpenVR, LibOVR) applications.

%prep
%autosetup

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc README.md

%changelog
