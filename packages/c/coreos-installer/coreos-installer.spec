#
# spec file for package coreos-installer
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


Name:           coreos-installer
Version:        0.23.0
Release:        0
Summary:        Installer for CoreOS disk images
License:        Apache-2.0
URL:            https://github.com/openshift/coreos-installer
Source0:        coreos-installer-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.76
BuildRequires:  cargo-packaging
BuildRequires:  gnupg
BuildRequires:  libzstd-devel
BuildRequires:  openssl-devel

%description
coreos-installer is a program to assist with installing Fedora CoreOS (FCOS) and
Red Hat Enterprise Linux CoreOS (RHCOS). It can do the following:

* Install the operating system to a target disk, optionally customizing it with
  an Ignition config or first-boot kernel parameters (coreos-installer install)
* Download and verify an operating system image for various cloud,
  virtualization, or bare metal platforms (coreos-installer download)
* List Fedora CoreOS images available for download
  (coreos-installer list-stream)
* Embed an Ignition config in a live ISO image to customize the running system
  that boots from it (coreos-installer iso ignition)
* Wrap an Ignition config in an initrd image that can be appended to the live
* PXE initramfs to customize the running system that boots from it
  (coreos-installer pxe ignition)

The options available for each subcommand are available in the Command Line
Reference or via the --help option.

Take a look at the [Getting Started
Guide](https://github.com/coreos/coreos-installer/blob/main/docs/getting-started.md)
for more information regarding how to download and use coreos-installer.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build} --features docgen,rdcore

PROFILE=release docs/_cmd.sh
PROFILE=release docs/_config-file.sh
./target/release/coreos-installer pack man -C man
./target/release/coreos-installer pack example-config >> example-config.yaml

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -d -m 0755 %{buildroot}%{_mandir}/man8/
for manpage in man/coreos-installer*
do
    install -m 0644 "${manpage}" %{buildroot}%{_mandir}/man8/
done

%check
%{cargo_test}

%files
%doc README.md example-config.yaml
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/coreos-installer*

%changelog
