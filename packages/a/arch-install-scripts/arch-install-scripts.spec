#
# spec file for package arch-install-scripts
#
# Copyright (c) 2022 Bruno Pitrus <brunopitrus@hotmail.com>
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


Name:           arch-install-scripts
Version:        28
Release:        0
Summary:        Scripts aimed at automating some menial installation/recovery tasks
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://github.com/archlinux/arch-install-scripts
Source0:        https://github.com/archlinux/arch-install-scripts/archive/refs/tags/v%{version}.tar.gz
Patch0:         Do_not_build_Arch-specific_scripts.patch
BuildRequires:  asciidoc
BuildRequires:  m4
Requires:       awk
Requires:       bash >= 4.1
Requires:       coreutils >= 8.15
Requires:       util-linux >= 2.23
Requires:       util-linux-systemd >= 2.23
BuildArch:      noarch

%description
This package provides helper scripts originating in Arch Linux that are useful during manual installation and recovery of any Linux distro.

* genfstab: Automatically generate an fstab file
* arch-chroot: Set up bind mounts and chroot into the target system

%prep
%setup -q
%autopatch

#preserve original file dates
sed -i 's/install -/install -p -/' Makefile

#Remove an Arch-specific script that is useless on other distros and requires a working pacman install
find . -name 'pacstrap*' -delete

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%check
%make_build check

%files
%license COPYING
%{_bindir}/arch-chroot
%{_bindir}/genfstab
%{_datadir}/bash-completion/completions/arch-chroot
%{_datadir}/bash-completion/completions/genfstab
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_archinstallscripts
%{_mandir}/man8/arch-chroot.8%{?ext_man}
%{_mandir}/man8/genfstab.8%{?ext_man}

%changelog
