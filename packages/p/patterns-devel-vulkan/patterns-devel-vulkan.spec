#
# spec file for package patterns-devel-vulkan
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with betatest

Name:           patterns-devel-vulkan
Version:        20221115
Release:        0
Summary:        Patterns for Installation (Vulkan devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Vulkan development pattern.

################################################################################

%package devel_vulkan
%pattern_development
Summary:        Vulkan Development
Group:          Metapackages
Provides:       pattern() = devel_vulkan
Provides:       pattern-icon() = pattern-vulkan-devel
Provides:       pattern-order() = 3500
Provides:       pattern-visible()

Recommends:     shaderc
Recommends:     vulkan-devel 
Recommends:     vulkan-tools 
Recommends:     vulkan-validationlayers 
Suggests:       gcc-c++
Suggests:       glm-devel
Suggests:       libglfw-devel
Suggests:       libvulkan_intel 
Suggests:       libvulkan_radeon
Suggests:       libXi-devel
Suggests:       libXxf86vm-devel

%description devel_vulkan
Tools and libraries for software development using Vulkan.

%files devel_vulkan
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_vulkan.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern devel_vulkan to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_vulkan.txt

%changelog
