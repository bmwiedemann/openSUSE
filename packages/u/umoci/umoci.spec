#
# spec file for package umoci
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


# Project name when using go tooling.
%define project github.com/opencontainers/umoci

Name:           umoci
Version:        0.5.0
Release:        0
Summary:        Open Container Image manipulation tool
License:        Apache-2.0
Group:          System/Management
URL:            https://umo.ci
Source0:        https://github.com/opencontainers/umoci/releases/download/v%{version}/umoci.tar.xz#/%{name}-%{version}.tar.xz
Source1:        https://github.com/opencontainers/umoci/releases/download/v%{version}/umoci.tar.xz.asc#/%{name}-%{version}.tar.xz.asc
Source2:        https://umo.ci/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  go >= 1.23
BuildRequires:  go-go-md2man
ExcludeArch:    s390

%description
umoci modifies Open Container images. umoci is a manipulation tool for OCI
images. In particular, it is a more complete alternative to oci-image-tools
provided by the OCI.

%prep
%setup -q

%build
export VERSION="$(cat ./VERSION)"
if [ "$VERSION" != "%{version}" ]; then
  # Append "_suse" if the version is not an upstream one.
  VERSION="%{version}_suse"
fi
# Build umoci and docs.
make VERSION="$VERSION" umoci docs

# Make sure that our keyring copy is identical to upstream.
our_keyring=$(sha256sum <"%{SOURCE2}")
src_keyring=$(sha256sum <umoci.keyring)
if [ "$our_keyring" != "$src_keyring" ]; then
	echo "keyring file doesn't match upstream"
	diff -u "%{SOURCE2}" umoci.keyring
	exit 1
fi

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Install all of the docs.
for file in doc/man/*.1; do
  install -D -m 0644 $file "%{buildroot}/%{_mandir}/man1/$(basename $file)"
done

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md doc/*
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/umoci*

%changelog
