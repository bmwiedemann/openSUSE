#
# spec file for package cpu-x
#
# Copyright (c) 2024 SUSE LLC
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


%define src_name CPU-X-%version
Name:           cpu-x
Version:        5.0.4
Release:        0
Summary:        Hardware overview utility
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/TheTumultuousUnicornOfDarkness/CPU-X
Source:         https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/archive/refs/tags/v%version.tar.gz
Patch1:         no-no-pie.patch
%if 0%{suse_version} < 1599
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%endif
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.12
BuildRequires:  gettext-tools
%ifarch %ix86 x86_64
BuildRequires:  nasm
%endif
BuildRequires:  opencl-headers
BuildRequires:  (pkgconfig(libproc2) or pkgconfig(libprocps))
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libcpuid) >= 0.6.0
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(vulkan)
# https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/issues/105
Provides:       bundled(bandwidth) = 1.5.1
Provides:       bundled(dmidecode) = 3.5.20230314

%description
CPU-X is a software that gathers information about CPU, motherboard
and peripherals. It is similar to CPU-Z (Windows) and can be used in
graphical mode by using GTK or in text-based mode by using NCurses. A
dump mode is present from command line.

%package bash-completion
Summary:        Bash completion for %name
Group:          System/Shells
Supplements:    (%name and bash-completion)
BuildArch:      noarch

%description bash-completion
Shell completion definitions from %name for %name.

%package fish-completion
Summary:        Bash completion for %name
Group:          System/Shells
Supplements:    (%name and fish)
BuildArch:      noarch

%description fish-completion
Shell completion definitions from %name for %name.

%package zsh-completion
Summary:        Bash completion for %name
Group:          System/Shells
Supplements:    (%name and zsh)
BuildArch:      noarch

%description zsh-completion
Shell completion definitions from %name for %name.

%lang_package

%prep
%autosetup -p1 -n %src_name

%build
%if 0%{suse_version} < 1599
export CC=gcc-12 CXX=g++-12
%endif
%cmake -DWITH_OPENCL=1
%cmake_build

%install
%cmake_install
rm -Rf "%buildroot/%_datadir/polkit-1"
%find_lang %name

%check
for dir in awk grep ; do pushd tests/$dir && ./test_regex.sh && popd ; done

%files
%_bindir/cpu-x
%_libexecdir/cpu-x*
%_datadir/applications/*.desktop
%_datadir/cpu-x/
%_datadir/icons/*
%_datadir/glib-2.0/
%_datadir/metainfo/
%license COPYING

%files bash-completion
%_datadir/bash-completion/

%files fish-completion
%_datadir/fish/

%files lang -f %name.lang

%files zsh-completion
%_datadir/zsh/

%changelog
