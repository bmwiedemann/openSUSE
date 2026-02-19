#
# spec file for package ssh-pairing
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


Name:           ssh-pairing
Version:        0.3
Release:        0
Summary:        Passwordless SSH key exchange through pairing
License:        GPL-2.0-or-later
URL:            https://github.com/Vogtinator/ssh-pairing
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssh)
Requires:       dialog
Requires:       hostname
Requires:       /usr/bin/ssh-keygen

%description
This tool allows to use pairing (like bluetooth, kde connect, ...) for exchanging public SSH keys, basically as alternative to ssh-copy-id.
With this, setting up SSH authentication is more user friendly, as the user's public key does not need to be transferred to the server manually.
It is arguably also more secure, as no passwords are involved, not even temporarily just to be able to ssh-copy-id.
This tool is design to be used as part of some CLI or TUI, but can also be used manually.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_sbindir}/ssh-pairing
%{_sbindir}/ssh-pairing-server

%changelog
