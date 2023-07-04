#
# spec file for package vsgExamples
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


%define addprofile 1

Name:           vsgExamples
Version:        1.0.5
Release:        0
Summary:        3D graphics toolkit
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://github.com/vsg-dev/vsgExamples
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  cmake(vsg)
BuildRequires:  cmake(vsgImGui)
BuildRequires:  cmake(vsgXchange)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)

%description
Example programs that test and illustrate how to use the VulkanSceneGraph and optional add-on libraries

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%install
%cmake_install

%if %addprofile
# setup VSG_FILE_PATH
prjdatadir=%_datadir/%name
profiledir=%_sysconfdir/profile.d
mkdir -p %buildroot/$profiledir
cat << EOF > %buildroot/$profiledir/%{name}.sh
export VSG_FILE_PATH=$prjdatadir:\${VSG_FILE_PATH+\$VSG_FILE_PATH}
EOF
%endif

%fdupes %buildroot/$prjdatadir

%files
%defattr(-,root,root)
%{_bindir}/vsg*
%dir %_datadir/%name
%_datadir/%name
%if %addprofile
%config %_sysconfdir/profile.d/vsgExamples.sh
%endif

%changelog
