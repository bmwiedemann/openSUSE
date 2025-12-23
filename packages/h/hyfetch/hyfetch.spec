#
# spec file for package hyfetch
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           hyfetch
Version:        2.0.5
Release:        0
Summary:        Customizable Linux System Information Script
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/hykilpikonna/HyFetch
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Patch0:         fix-shebang.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
Recommends:     maim
Recommends:     w3m-inline-image
# Replaces Python packages that used to provide /usr/bin/hyfetch
Obsoletes:      python311-hyfetch  < %{version}
Obsoletes:      python312-hyfetch  < %{version}
Obsoletes:      python313-hyfetch  < %{version}
Conflicts:      python311-hyfetch
Conflicts:      python312-hyfetch
Conflicts:      python313-hyfetch

%description
HyFetch is a command line script to display information about your
Linux system, such as amount of installed packages, OS and kernel
version, active GTK theme, CPU info, and used/available memory.
It is a fork of neofetch, and adds pride flag coloration to the OS logo.

%package -n neowofetch
# version as reported by neowofetch --version
Version:        8.0.5
Summary:        CLI system information tool written in BASH
BuildArch:      noarch
Provides:       neofetch = %{version}
Obsoletes:      neofetch < %{version}

%description -n neowofetch
Displays information about the system next to an image, the OS logo, or any
ASCII file of choice. The main purpose of Neofetch is to be used in
screenshots to show other users what OS/Distro is running, what Theme/Icons
are being used, etc.

Customizable through the use of command line flags or the user config file.
There are over 50 config options to mess around with and there's the `print_info()
function and friends which let you add your own custom info.

This is the forked version that is maintained together with hyfetch

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
%{cargo_install -p crates/hyfetch}
install -m 0755 %{_builddir}/%{name}-%{VERSION}/neofetch %{buildroot}%{_bindir}/neowofetch
ln -s %{_bindir}/neowofetch %{buildroot}%{_bindir}/neofetch

%check
[ "$(%{buildroot}%{_bindir}/neofetch --version)" == "Neofetch %{version}" ] || (
    echo "Neofetch version does not match the RPM version - please update"
    exit 1
)

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE.md

%files -n neowofetch
%{_bindir}/neofetch
%{_bindir}/neowofetch

%changelog
