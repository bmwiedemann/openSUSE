#
# spec file for package conmon
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


Name:           conmon
Version:        2.2.1
Release:        0
Summary:        An OCI container runtime monitor
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers/conmon
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  go-go-md2man
BuildRequires:  pkgconfig
BuildRequires:  golang(API) >= 1.20
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)

%description
Conmon is a monitoring program and communication tool between a
container manager (like podman or CRI-O) and an OCI runtime (like
runc or crun) for a single container.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%set_build_flags
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/conmon*.8%{?ext_man}

%changelog
