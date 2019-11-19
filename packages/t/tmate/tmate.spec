#
# spec file for package tmate
#
# Copyright (c) 2019 SUSE LLC.
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
URL:            https://www.tmate.io
Source:         https://github.com/tmate-io/tmate/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libevent-devel
BuildRequires:  libmsgpack-devel >= 1.1.0
BuildRequires:  libmsgpackc-devel >= 1.1.0
BuildRequires:  libopenssl-devel
BuildRequires:  libssh-devel >= 0.6.1
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tmate is a fork of tmux providing an instant pairing solution.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc CHANGES FAQ README-tmux README.md
%license COPYING
%{_bindir}/tmate
%{_mandir}/man1/tmate.1*

%changelog
