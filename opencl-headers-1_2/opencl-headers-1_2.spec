#
# spec file for package opencl-headers-1_2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define opencl_version 1.2
%define date 20150303

Name:           opencl-headers-1_2
Version:        %{opencl_version}_%{date}
Release:        0
Summary:        OpenCL (Open Computing Language) headers
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.khronos.org/registry/cl/
Source:         %{name}-%{version}.tar.bz2
Source1:        get-tarball.sh
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      opencl-headers

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides the official Khronos Group OpenCL headers needed to
compile programs that use OpenCL.

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 755 %{buildroot}%{_includedir}/CL
install -m644 *.h* %{buildroot}%{_includedir}/CL

%files
%defattr(-,root,root)
%dir %{_includedir}/CL
%{_includedir}/CL/*.h*

%changelog
