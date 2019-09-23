#
# spec file for package mpclient
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           mpclient
Version:        0.30
Release:        0
Summary:        A minimalist command line interface to MPD
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://www.musicpd.org/
Source:         http://www.musicpd.org/download/mpc/0/mpc-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmpdclient) >= 2.9

%description
A client for MPD, the Music Player Daemon. mpc connects to a MPD
running on a machine via a network. Accepts input on standard input,
so can be easily used in scripts.

%prep
%setup -q -n mpc-%{version}

%build
%meson
%meson_build

%install
%meson_install
install -m 0755 contrib/mpd-pls-handler.sh %{buildroot}%{_bindir}/mpd-pls-handler
install -m 0755 contrib/mpd-m3u-handler.sh %{buildroot}%{_bindir}/mpd-m3u-handler

install -Dm 0644 contrib/mpc-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
rm -rf %{buildroot}%{_datadir}/doc

%check
%meson_test

%files
%license COPYING
%doc NEWS README.rst
%{_bindir}/*
%config %{_datadir}/bash-completion/completions/%{name}

%changelog
