#
# spec file for package gocryptfs
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


Name:           gocryptfs
Version:        2.4.0
Release:        0
Summary:        Encrypted overlay filesystem written in Go
License:        MIT
URL:            https://nuetzlich.net/gocryptfs/
Source0:        https://github.com/rfjakob/gocryptfs/releases/download/v%{version}/%{name}_v%{version}_src-deps.tar.gz
Source1:        https://github.com/rfjakob/gocryptfs/releases/download/v%{version}/%{name}_v%{version}_src-deps.tar.gz.asc
Source2:        https://nuetzlich.net/gocryptfs-signing-key.pub#/%{name}.keyring
Source3:        %{name}.rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl)
Requires:       fuse
Requires:       util-linux-systemd
Suggests:       %{name}-doc = %{version}

%description
gocryptfs is built on top the excellent go-fuse FUSE library.
This project was inspired by EncFS and strives to fix its
security issues while providing good performance.

gocryptfs uses file-based encryption that is implemented as a
mountable FUSE filesystem. Each file in gocryptfs is stored as
one corresponding encrypted file on disk.

%package doc
Summary:        Documentation for gocryptfs
BuildArch:      noarch

%description doc
This package contains the documentation files for gocryptfs.

%prep
%autosetup -n %{name}_v%{version}_src-deps -p1

%build
export GOFLAGS="-mod=vendor -buildmode=pie -trimpath"
./build.bash

%install
%make_install

install -D -m 0755 -t %{buildroot}%{_bindir} contrib/atomicrename/atomicrename \
	contrib/findholes/findholes contrib/statfs/statfs
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 Documentation/statfs.1

rm Documentation/MANPAGE* Documentation/*.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-xray
%{_bindir}/atomicrename
%{_bindir}/findholes
%{_bindir}/statfs
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-xray.1%{?ext_man}
%{_mandir}/man1/statfs.1%{?ext_man}

%files doc
%license LICENSE
%doc Documentation/*

%changelog
