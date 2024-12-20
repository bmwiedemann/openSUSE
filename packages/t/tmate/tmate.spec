#
# spec file for package tmate
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


Name:           tmate
Version:        2.4.0
Release:        0
Summary:        Instant terminal sharing
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://tmate.io
Source:         https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libssh) >= 0.6.1
BuildRequires:  (pkgconfig(msgpack-c) >= 3.0.0 or pkgconfig(msgpack) >= 3.0.0)
BuildRequires:  pkgconfig(tinfo)

%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
./autogen.sh
# msgpack has changed name but tmate is not yet updated.
# Overrides like MSGPACK_CFLAGS need to be non-empty for configure.ac to
# recognize it as an override, therefore there is an extra space in case
# pkgconfig returns that no extra are cflags needed.
%configure MSGPACK_CFLAGS=" $(pkg-config msgpack-c --cflags)" \
	MSGPACK_LIBS="$(pkg-config msgpack-c --libs)"
%make_build

%install
%make_install

%files
%doc CHANGES FAQ README-tmux README.md
%license COPYING
%{_bindir}/tmate
%{_mandir}/man1/tmate.1%{?ext_man}

%changelog
