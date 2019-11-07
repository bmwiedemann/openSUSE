#
# spec file for package mpclient
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.33
Release:        0
Summary:        A minimalist command line interface to MPD
License:        GPL-2.0-or-later
URL:            https://www.musicpd.org
Source0:        https://www.musicpd.org/download/mpc/0/mpc-%{version}.tar.xz
BuildRequires:  meson >= 0.47.2
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(libmpdclient)

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
rm -r %{buildroot}%{_datadir}/doc

%check
%meson_test

%files
%license COPYING
%doc NEWS README.rst
%config %{_datadir}/bash-completion/completions/%{name}
%{_bindir}/{mpc,mpd-*}
%{_mandir}/man1/mpc.1%{?ext_man}

%changelog
