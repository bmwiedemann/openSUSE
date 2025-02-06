#
# spec file for package hare-libnotify
#
# Copyright (c) 2025 SUSE LLC
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

Name:           hare-libnotify
License:        MPL-2.0
Summary:        Hare C bindings for libnotify
URL:            https://git.sr.ht/~uncomfy/hare-libnotify
Version:        1.0.0
Release:        0
Source0:        https://git.sr.ht/~uncomfy/hare-libnotify/archive/%{version}.tar.gz
Source99:       hare-libnotify-rpmlintrc
BuildRequires:  hare
BuildRequires:  make
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildArch:      noarch
Recommends:     notification-daemon
# harec cannot produce PIE compatible code
#!BuildIgnore:  gcc-PIE

%description
An attempt to create Hare bindings for libnotify.

%prep
%autosetup

%build
make

%install
# Hare does not have a way to get the envs so you have to
# do this

mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} \
     PREFIX="%{_prefix}" \
     SRCDIR=%{_usrsrc} install

make DESTDIR=%{buildroot} \
     PREFIX="%{_prefix}" \
     SRCDIR=%{_usrsrc} install-lib

# Remove binary
pushd %{buildroot}%{_bindir}
rm notify-send
popd

%check
make run

%files
%dir %{haredir}
%{haredir}/third-party
%license LICENSE
%doc     README.md

%changelog
