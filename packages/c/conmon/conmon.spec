#
# spec file for package conmon
#
# Copyright (c) 2020 SUSE LLC
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


Name:           conmon
Version:        2.0.21
Release:        0
Summary:        An OCI container runtime monitor
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers/conmon
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(libsystemd)

%description
Conmon is a monitoring program and communication tool between a
container manager (like podman or CRI-O) and an OCI runtime (like
runc or crun) for a single container.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
