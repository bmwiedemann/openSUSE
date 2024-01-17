#
# spec file for package firectl
#
# Copyright (c) 2022 SUSE LLC
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


# Use hardening ldflags.

Name:           firectl
Version:        0.2.0
Release:        0
Summary:        Command-line tool to run Firecracker microVMs
License:        Apache-2.0
Group:          System/Emulators/PC
URL:            https://firecracker-microvm.github.io/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  git
BuildRequires:  golang-packaging
BuildRequires:  sed
BuildRequires:  golang(API) >= 1.12
ExclusiveArch:  x86_64 aarch64

%description
Firectl is a command-line tool to run Firecracker microVMs.

%prep
%setup -q -a1

# Copying the file elsewhere is required, because rpm build for aarch64
# tries to change all the config.guess files found in BUILD with
# some arch specific stuff.

%build
# This should eventually migrate to distro policy
# Enable optimization, debuginfo, and link hardening.
sed -i -e 's|go build|go build -mod vendor -buildmode=pie|g' Makefile
make %{name}

%install
# remove spurious files
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 firectl %{buildroot}%{_bindir}/firectl

%files
%license LICENSE
%doc README.md
%{_bindir}/firectl

%changelog
