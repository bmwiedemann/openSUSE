#
# spec file for package clipman
#
# Copyright (c) 2021 SUSE LLC
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

Name:           clipman
Version:        1.5.2
Release:        0
Summary:        A clipboard manager for Wayland
License:        GPL-3.0
URL:            https://github.com/yory8/clipman
# Source0:        https://github.com/yory8/%%{name}/archive/%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/yory8/%{name}/archive/v%{version}.tar.gz
# Run go build && go mod vendor to get vendor/ subdirectory
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.12

%description
A clipboard manager for Wayland with support for
persisting copy buffers after an application exits.

%prep
%autosetup -p1 -a1

%build
export GOCACHE=$(readlink -f vendor/)
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags ""

%install
install -Dm755 clipman %{buildroot}%{_bindir}/clipman
install -Dm644 -t %{buildroot}%{_mandir}/man1/ docs/%{name}.*

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/clipman
%{_mandir}/man1/%{name}*.1%{?ext_man}
%license COPYING

%changelog
