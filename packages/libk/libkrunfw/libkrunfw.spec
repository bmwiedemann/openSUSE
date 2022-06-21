#
# spec file for package libkrunfw
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libkrunfw
Version:        3.0.0
Release:        0
Summary:        A dynamic library bundling a Linux kernel in a convenient storage format
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/v%{version}.tar.gz#/libkrunfw-%{version}.tar.gz
Source1:        https://www.kernel.org/pub/linux/kernel/v5.x/linux-5.15.47.tar.xz
# libkrunfw is a plugin for us, more than a full-fledged library,
# so let's avoid setting up a SONAME etc (which upstream is now doing).
Patch1:         dont-set-soname-as-it-is-plugin-for-us.patch
ExclusiveArch:  x86_64 aarch64
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  hmaccalc
BuildRequires:  hostname
BuildRequires:  libelf-devel
BuildRequires:  net-tools
BuildRequires:  python3-pyelftools
Conflicts:      libkrunfw-devel <= 0.7
Conflicts:      libkrunfw0 <= 0.7

%description
libkrunfw is a library bundling a Linux kernel in a dynamic library in a way that can be easily consumed by libkrun.

By having the kernel bundled in a dynamic library, libkrun can leave to the linker the work of mapping the sections into the process, and then directly inject those mappings into the guest without any kind of additional work nor processing.

%prep
%autosetup -S git
mkdir tarballs
cp %{SOURCE1} tarballs/

%build
test -n "$SOURCE_DATE_EPOCH" || export SOURCE_DATE_EPOCH=`date +%s`
cat > .kernel-binary.spec.buildenv <<EOF
export KBUILD_BUILD_TIMESTAMP="$(LANG=C date -u -d "@$SOURCE_DATE_EPOCH")"
export KBUILD_BUILD_USER=geeko
export KBUILD_BUILD_HOST=buildhost
EOF
source ./.kernel-binary.spec.buildenv
%make_build
%ifarch x86_64
%make_build SEV=1
%endif

%install
source ./.kernel-binary.spec.buildenv
%make_install PREFIX=%{_prefix}
%ifarch x86_64
%make_install SEV=1 PREFIX=%{_prefix}
%endif

%files
%{_libdir}/libkrunfw.so
%ifarch x86_64
%{_libdir}/libkrunfw-sev.so
%endif

%changelog
