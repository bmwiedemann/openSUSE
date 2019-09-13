#
# spec file for package linux32
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           linux32
Version:        1.0
Release:        0
Summary:        32-Bit Emulation Utility for x86-64
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            http://ftp.x86-64.org/pub/linux/tools/linux32/
Source2:        %{name}.desktop
Source3:        konsole-linux32-24.png
Source4:        konsole-linux32-32.png
Source5:        konsole-linux32-48.png
Source6:        konsole-linux32-64.png
Source7:        konsole-linux32-128.png
Source8:        konsole-linux32-256.png
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       util-linux >= 2.16
Recommends:     xterm-bin
ExclusiveArch:  x86_64

%description
This is a small tool for 32-bit emulation in Linux/x86-64. It allows
you to execute programs that need a uname -m of i386 with uname
emulation. The uname -m is inherited by all child programs, but does
not affect the current shell or processes above it in the process
hierarchy.

%prep

%build

%install
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/konsole-linux32.png
install -D -m 644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/konsole-linux32.png
install -D -m 644 %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/konsole-linux32.png
install -D -m 644 %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/konsole-linux32.png
install -D -m 644 %{SOURCE7} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/konsole-linux32.png
install -D -m 644 %{SOURCE8} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/konsole-linux32.png
%suse_update_desktop_file -i %{name}

%files
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/konsole-linux32.png

%changelog
