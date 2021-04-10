#
# spec file for package WSL-DistroLauncher
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


Name:           WSL-DistroLauncher
# no official release yet
Version:        0.0.1+git20200306.f858909
Release:        0
Summary:        Windows Subsystem for Linux distro launcher
License:        MIT
URL:            https://github.com/openSUSE/WSL-DistroLauncher

Source:         WSL-DistroLauncher-%{version}.tar.xz
Source1:        icon.ico

Patch0:         0001-Cross-compiling-the-launcher.patch
Patch1:         0002-replace-wscanf_s-seems-not-defined-in-mingw.patch
Patch2:         0003-SUSE-adjustments.patch
Patch3:         0004-refactor-QueryUid-to-be-reusable.patch
Patch4:         0005-Run-yast2-firstboot-instead-of-useradd.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  mingw64-filesystem

# XXX: that's a bit nasty. Launcher should probably be made run
# time configurable when packing the appx
%if 0%{?is_opensuse}
BuildRequires:  openSUSE-release
%else
BuildRequires:  sles-release
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw64_package_header_debug
BuildArch:      noarch

%description
Windows application shipped within the WSL applications in the
Windows Store. This application is initializing and launching
the distribution.

%_mingw64_debug_package

%prep
%autosetup -p1

cp %{S:1} DistroLauncher/icon.ico

%build
autoreconf -fi
if [ -e /usr/lib/os-release ]; then
	. /usr/lib/os-release
else
	. /etc/os-release
fi
# During prerelease phases, parens around RC etc. in PRETTY_NAME
# are not properly escaped if passed to mingw configure step.
# Bash substitution requires two steps:
# 1. Keep only alphanumeric characters and spaces
PRETTY_NAME_ALPHANUM="${PRETTY_NAME//[^a-zA-Z0-9- ]/}"
# 2. Replace spaces with hyphen
DISTRO_ID="${PRETTY_NAME_ALPHANUM// /-}"
%{_mingw64_configure} --with-windmc=%{_mingw64_windmc} \
                      --with-windres=%{_mingw64_windres} \
                      --with-distro-id="$DISTRO_ID" \
                      --with-distro-name="$PRETTY_NAME" \
                      --with-distro-icon="icon.ico"
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md
%license COPYING
%{_mingw64_bindir}/DistroLauncher.exe

%changelog
