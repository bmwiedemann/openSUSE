#
# spec file for package opencl-headers
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           opencl-headers
Version:        2.2+git.20190806
Release:        0
Summary:        OpenCL (Open Computing Language) headers
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.khronos.org/registry/cl/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  xz
Conflicts:      opencl-headers-1_2
BuildArch:      noarch

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides the official Khronos Group OpenCL headers needed to
compile programs that use OpenCL.

%prep
%setup -q

%build

%install
install -d -m 0755 %{buildroot}%{_includedir}/CL
install -p -m 0644 ./CL/*.h* %{buildroot}%{_includedir}/CL

%files
%doc README.md
%license LICENSE
%dir %{_includedir}/CL
%{_includedir}/CL/*.h*

%changelog
