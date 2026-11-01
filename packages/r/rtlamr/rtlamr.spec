#
# spec file for package rtlamr
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2019-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           rtlamr
Version:        0.9.6
Release:        0
Summary:        SDR receiver for Itron ERT compatible smart meters
# Legal-Review-Notice: aggregate licence of the statically linked binary.
# Tagged AGPL-3.0-only although rtlamr's own headers grant "version 3 or (at
#   your option) any later version": the vendored github.com/bemasher/rtltcp
#   grants no or-later upgrade (its sources carry no licence header and its
#   repo ships the stock AGPLv3 text), so -or-later would overstate the
#   aggregate. Please confirm the rtltcp revision's status.
# BSD-3-Clause: in-tree r900/gf (Go Authors, r900/gf/LICENSE), imported by
#   r900.
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/bemasher/rtlamr
Source:         https://github.com/bemasher/rtlamr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.21

%description
An rtl-sdr receiver for Itron ERT compatible smart meters operating
in the 900MHz ISM band.

%prep
%autosetup -p1 -a1
# Notices for the BSD-licensed code compiled in (see Legal-Review-Notice)
cp r900/gf/LICENSE LICENSE.r900-gf

%build
# -trimpath: keep the build root out of the binary (reproducible builds); it
# also drops the debugsource package, which is useless for Go anyway
go build \
    -mod=vendor \
    -buildmode=pie \
    -trimpath

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
go test -mod=vendor ./...

%files
%license LICENSE LICENSE.r900-gf
%doc README.md
%{_bindir}/rtlamr

%changelog
