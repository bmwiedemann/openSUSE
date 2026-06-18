#
# spec file for package falcosecurity-container-plugin
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


Name:           falcosecurity-container-plugin
Version:        0.7.1
Release:        0
Summary:        Falcosecurity plugin providing container metadata
License:        Apache-2.0
URL:            https://github.com/falcosecurity/plugins/tree/main/plugins/container
# Source0/Source1 are produced by _service (obs_scm + go_modules):
Source0:        container-plugin-%{version}.tar
Source1:        vendor.tar.gz
# the plugins/container subtree ships no LICENSE (it lives at the monorepo root)
Source2:        LICENSE
# Redirect the cmake FetchContent modules (fmt/reflex/plugin-sdk-cpp/btrfs)
# to the system copies so the build works offline:
Patch0:         container-plugin-use-system-deps.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go >= 1.25
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(fmt)
BuildRequires:  libbtrfs-devel
BuildRequires:  libcap-devel
BuildRequires:  cmake(Reflex)
BuildRequires:  plugin-sdk-cpp-devel

%description
The container plugin enriches Falco/libsinsp events with container metadata
(id, name, image, labels, ...) gathered from the local container runtimes
(Docker, containerd, CRI-O, Podman). It is loaded as a shared-object plugin
(libcontainer.so) by the falcosecurity libs (the system libsinsp) and by
sysdig; the plugin itself links only the header-only plugin SDK, not libsinsp.

%prep
%autosetup -p1 -n container-plugin-%{version}
# vendored Go modules for go-worker/ (Source1)
tar -C go-worker -xf %{SOURCE1}
# LICENSE lives at the monorepo root, not in the subtree
cp -a %{SOURCE2} .

%build
export GOFLAGS=-mod=vendor
export GOPROXY=off
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/.gocache
%define __builder ninja
# ENABLE_TESTS pulls in a from-source libsinsp (sinsp_test_support); keep it OFF
# so the plugin builds against the system stack only.
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DENABLE_TESTS=OFF
%cmake_build

%install
# the plugin's CMakeLists installs nothing; place the .so in the plugins dir
install -D -m 0755 build/libcontainer.so \
  %{buildroot}%{_libdir}/falcosecurity/plugins/libcontainer.so

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/falcosecurity
%dir %{_libdir}/falcosecurity/plugins
%{_libdir}/falcosecurity/plugins/libcontainer.so

%changelog
