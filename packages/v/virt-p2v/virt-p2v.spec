#
# spec file for package virt-p2v
#
# Copyright (c) 2025 SUSE LLC
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
# needsbinariesforbuild


Name:           virt-p2v
Version:        1.42.4
Release:        0
Summary:        Tools to convert a physical machine to run on KVM
URL:            https://libguestfs.org/
License:        GPL-2.0-or-later
Group:          System/Management

# virt-p2v works only on x86_64 at the moment.  It requires porting
# to properly detect the hardware on other architectures, and furthermore
# virt-v2v requires porting too.
ExclusiveArch:  x86_64

# Source and patches.
Source0:        https://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        virt-p2v.keyring

# Basic build requirements.
BuildRequires:  gcc
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
####BuildRequires: /usr/bin/pod2text
BuildRequires:  libxml2-devel
BuildRequires:  gtk3-devel
BuildRequires:  pcre2-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(bash-completion) >= 2.0
#BuildRequires: dbus-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  m4

# Test suite requirements.
####BuildRequires: /usr/bin/qemu-nbd
BuildRequires:  qemu-tools

# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:       bundled(gnulib)


Requires:       /usr/bin/gawk
Requires:       /usr/bin/gzip

# virt-p2v-make-disk runs virt-builder:
Requires:       guestfs-tools >= 1.42

# virt-p2v-make-kickstart runs strip:
Requires:       binutils

# Migrate from the old virt-p2v-maker:
####Provides: virt-p2v-maker = 1:%{version}-%{release}
####Obsoletes: virt-p2v-maker < 1:1.41.5

# The bash completion for p2v were shipped with the others of libguestfs:
####Obsoletes: libguestfs-bash-completion < 1:1.41.5

%description
Virt-p2v converts (virtualizes) physical machines so they can be run
as virtual machines under KVM.

This package contains the tools needed to make a virt-p2v boot CD or
USB disk image which is booted on the physical machine to perform the
conversion.  You also need virt-v2v installed somewhere else to
complete the conversion.

To convert virtual machines from other hypervisors, see virt-v2v.

%prep
%autosetup -p1

%build
%configure \
  --disable-gnulib-tests
%make_build

#%check
#
#if ! make check; then
#    cat test-suite.log
#    exit 1
#fi

%install
%make_install

# Delete the development man pages.
rm %{buildroot}/%{_mandir}/man1/p2v-building.1* \
   %{buildroot}/%{_mandir}/man1/p2v-hacking.1* \
   %{buildroot}/%{_mandir}/man1/p2v-release-notes.1*

%files
%doc README
%license COPYING
%{_bindir}/virt-p2v-make-disk
%{_bindir}/virt-p2v-make-kickstart
%{_bindir}/virt-p2v-make-kiwi
%{_datadir}/bash-completion/completions/virt-*
%{_datadir}/virt-p2v
%{_libdir}/virt-p2v
%{_mandir}/man1/virt-p2v-make-disk.1*
%{_mandir}/man1/virt-p2v-make-kickstart.1*
%{_mandir}/man1/virt-p2v-make-kiwi.1*
%{_mandir}/man1/virt-p2v.1*

%changelog
