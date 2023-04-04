#
# spec file for package vkbasalt
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


%define __builder ninja
Name:           vkbasalt
Version:        0.3.2.9
Release:        0
Summary:        Vulkan post processing layer
License:        Zlib
URL:            https://github.com/DadSchoorse/vkBasalt
Source0:        https://github.com/DadSchoorse/vkBasalt/archive/v%{version}.tar.gz#/vkBasalt-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  glslang-devel
BuildRequires:  libX11-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  vulkan-headers
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%endif

%description
vkBasalt is a Vulkan post processing layer to enhance the visual graphics of games.

%prep
%setup -q -n vkBasalt-%{version}

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-11"
export CXX="g++-11"
%else
export CC="gcc-12"
export CXX="g++-12"
%endif
%meson
%meson_build

%install
%meson_install

# Configuration file
install -Dpm0644 config/vkBasalt.conf -t %{buildroot}%{_sysconfdir}/

%files
%license LICENSE
%doc README.md
%{_libdir}/libvkbasalt.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/implicit_layer.d
%{_datadir}/vulkan/implicit_layer.d/vkBasalt.json
%config(noreplace) %{_sysconfdir}/vkBasalt.conf

%changelog
