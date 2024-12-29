#
# spec file for package hare-libnotify-tools
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

%global haredir  %{_usrsrc}/hare

Name:           hare-libnotify-tools
License:        MPL-2.0
Summary:        Hare clone of the notify-send tool
URL:            https://git.sr.ht/~uncomfy/hare-libnotify
Version:        1.0.0
Release:        0
Source0:        https://git.sr.ht/~uncomfy/hare-libnotify/archive/%{version}.tar.gz
BuildRequires:  hare
BuildRequires:  make
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  hare-libnotify = %{version}
Recommends:     notification-daemon

%description
An attempt to create Hare bindings for libnotify. This contains a clone of the notify-send tool.

%prep
%autosetup -n hare-libnotify-%{version}

%build
make notify-send

%install
# Hare does not have a way to get the envs so you have to
# do this

mkdir -p %{buildroot}%{_bindir}
make notify-send

# Rename binary
mv out/bin/notify-send %{buildroot}%{_bindir}/hare-notify-send

%check
make run

%files
%{_bindir}/hare-notify-send
%license LICENSE
%doc     README.md

%changelog
