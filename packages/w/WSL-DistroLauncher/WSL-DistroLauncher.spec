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
Version:        0.0.1+git20200918.2ed9a93
Release:        0
Summary:        Windows Subsystem for Linux distro launcher
License:        MIT
URL:            https://github.com/openSUSE/WSL-DistroLauncher

Source:         WSL-DistroLauncher-%{version}.tar.xz
Source1:        icon.ico

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
	source /usr/lib/os-release
else
	source /etc/os-release
fi

# PRETTY_NAME is embedded in WSL launcher executable Windows resource metadata.
# Modify PRETTY_NAME for allowed characters and stable name dropping SLE prerelease.
# During SLE prerelease phases, parens around RC etc. in PRETTY_NAME
# will not not be properly escaped if passed to mingw configure step.
#
# Reuse bash substitution pattern from obs-service-kiwi_metainfo_helper.
#
# PRETTY_NAME:                     openSUSE Leap 15.3
# PRETTY_NAME_BEFORE_PAREN:        openSUSE Leap 15.3
# PRETTY_NAME_BEFORE_PAREN_DASHED: openSUSE-Leap-15.3
#
# PRETTY_NAME:                     SUSE Linux Enterprise Server 15 SP3 (Snapshot16)
# PRETTY_NAME_BEFORE_PAREN:        SUSE Linux Enterprise Server 15 SP3
# PRETTY_NAME_BEFORE_PAREN_DASHED: SUSE-Linux-Enterprise-Server-15-SP3
#
# Special case for SLE release labels e.g. RC1. Keep only up to (space) open paren.
# Provides a stable project name for third-party integrations e.g. app store submissions
PRETTY_NAME_BEFORE_PAREN="${PRETTY_NAME// (*/}"

# Attribute distro-id must not contain spaces, replace with dash
PRETTY_NAME_BEFORE_PAREN_DASHED="${PRETTY_NAME_BEFORE_PAREN//[^[:alnum:].]/-}"

%{_mingw64_configure} --with-windmc=%{_mingw64_windmc} \
                      --with-windres=%{_mingw64_windres} \
                      --with-distro-id="$PRETTY_NAME_BEFORE_PAREN_DASHED" \
                      --with-distro-name="$PRETTY_NAME_BEFORE_PAREN" \
                      --with-distro-icon="icon.ico"
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md
%license COPYING
%{_mingw64_bindir}/DistroLauncher.exe

%changelog
