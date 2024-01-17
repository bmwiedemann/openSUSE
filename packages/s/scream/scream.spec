#
# spec file for package scream
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


Name:           scream
Version:        4.0
Release:        0
Summary:        Receiver for Scream virtual devices
License:        MS-PL
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/duncanthrax/scream
Source:         https://github.com/duncanthrax/scream/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  alsa-devel
BuildRequires:  pulseaudio-devel

%description
Scream is a virtual device driver for Windows that provides a discrete sound device.

This package contains the Linux receiver.

%prep
%autosetup

%build
pushd Receivers/unix
%cmake
%cmake_build
popd

%install
pushd Receivers/unix
%cmake_install
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/scream

%changelog
