#
# spec file for package patterns-devel-vulkan
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with betatest
Name:           patterns-devel-vulkan
Version:        20261030
Release:        0
Summary:        Patterns for Installation (Vulkan devel)
License:        MIT
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
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
Provides:       pattern() = devel_vulkan
Provides:       pattern-icon() = pattern-vulkan-devel
Provides:       pattern-order() = 3500
Provides:       pattern-visible()
# SECTION C++ development pattern
Recommends:     pattern() = devel_C_C++
# /SECTION
# SECTION Vulkan SDK
Recommends:     shaderc
Recommends:     vulkan-devel
Recommends:     vulkan-tools
Recommends:     vulkan-validationlayers
# /SECTION
# SECTION Example and windowing dependencies
Recommends:     glfw-devel
Recommends:     glm-devel
Recommends:     libXi-devel
Recommends:     libXxf86vm-devel
# /SECTION
# SECTION Vulkan drivers (ICDs)
Recommends:     libvulkan_intel
Recommends:     libvulkan_lvp
Recommends:     libvulkan_radeon
# /SECTION
# SECTION Debugging tools
Recommends:     renderdoc
# /SECTION

%description devel_vulkan
Tools and libraries for software development using Vulkan.

%files devel_vulkan
%dir %{_docdir}/patterns
%{_docdir}/patterns/devel_vulkan.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern devel_vulkan to be installed.' > %{buildroot}/%{_defaultdocdir}/patterns/devel_vulkan.txt

%changelog
