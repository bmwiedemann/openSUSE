#
# spec file for package replay-sorcery
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


Name:           replay-sorcery
Version:        0.5.0
Release:        0
Summary:        Instant replay solution for Linux
License:        GPL-3.0-only
URL:            https://github.com/matanui159/ReplaySorcery
Source0:        ReplaySorcery-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  ffmpeg-4-libavcodec-devel
BuildRequires:  ffmpeg-4-libavdevice-devel
BuildRequires:  ffmpeg-4-libavfilter-devel
BuildRequires:  ffmpeg-4-libavformat-devel
BuildRequires:  ffmpeg-4-libavutil-devel
BuildRequires:  gcc-c++
BuildRequires:  libpulse-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(x11)
Requires(post): permissions
%{?systemd_requires}

%description
This program will constantly record the screen without using too much
computer resources and, at the press of a key combination, will save
the last 30 seconds.

%prep
%autosetup -n ReplaySorcery-%{version} -p1

%build
%cmake -DRS_SETID:BOOL=OFF
%cmake_build

%install
%cmake_install

%verifyscript
%verify_permissions -e %{_bindir}/%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%if 0%{?set_permissions:1}
    %set_permissions %{_bindir}/%{name}
%else
    %run_permissions
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_prefix}%{_sysconfdir}/%{name}.conf
%{_prefix}/lib/systemd/user/%{name}.service

%changelog
