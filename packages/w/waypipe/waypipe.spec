#
# spec file for package waypipe
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           waypipe
Version:        0.11.0
Release:        0
Summary:        Proxy for Wayland clients
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Servers
URL:            https://mstoeckl.com/notes/gsoc/blog.html
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  meson >= 0.56.0
BuildRequires:  rust-bindgen >= 0.66.0
BuildRequires:  shaderc
BuildRequires:  pkgconfig(gbm) >= 11.0.0
BuildRequires:  pkgconfig(libavcodec) >= 61.19.100
BuildRequires:  pkgconfig(libavutil) >= 59.39.100
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(liblz4) >= 1.7.0
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libzstd) >= 0.4.6
BuildRequires:  pkgconfig(scdoc) >= 1.9.4
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
waypipe is a proxy for Wayland clients. It forwards Wayland messages
and serializes changes to shared memory buffers over a single socket.
This makes application forwarding similar to `ssh -X` feasible.

Waypipe needs to be run on both ends of a socket connection. It
emulates shared files between the different systems on each end of
the connection, using twin file copies to quickly identify file
changes.

It supports both shared-memory and DMABUFs. Performance on a local
network is kind of acceptable for terminals and relatively static
applications, but games are often unplayable due to FPS drop from the
delay needed to send a screenful of data over the network.

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/waypipe
%_mandir/man*/waypipe*
%license LICENSE.*
%doc README*

%changelog
