#
# spec file for package rust-srpm-macros
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Red Hat, Inc., Raleigh, North Carolina, United States of America.
# Copyright (c) 2017, 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org>.
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


Name:           rust-srpm-macros
Version:        15
Release:        0
Summary:        RPM macros for building Rust source packages
License:        MIT
Group:          Development/Languages/Rust
URL:            https://pagure.io/fedora-rust/rust2rpm
Source0:        https://releases.pagure.org/fedora-rust/rust2rpm/rust2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
This package provides the RPM macros for building usable Source RPMs
of Rust packages.

%prep
%autosetup -n rust2rpm-%{version} -p1

# Target arch is i586 on these distributions
sed -e "s/i686/i586 i686/" -i data/macros.rust-srpm
# Work around bugs in ppc64* arch setup in SUSE rpm
sed -e "s/ppc64 ppc64le/ppc64 powerpc64 ppc64le powerpc64le/" -i data/macros.rust-srpm
# Add armv6hl to supported arches
sed -e "s/armv7hl/armv6hl armv7hl/" -i data/macros.rust-srpm

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmconfigdir}/macros.d data/macros.rust-srpm

%files
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.rust-srpm

%changelog
