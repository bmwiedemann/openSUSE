#
# spec file for package oci-registry
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


Name:           oci-registry
Version:        0.4.5
Release:        0
Summary:        OCI Registry with filesystem and S3 storage back-ends
License:        MIT
URL:            https://github.com/mcronce/oci-registry
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd

# error: failed to run custom build command for `ring v0.16.20`
#   thread 'main' panicked at /home/abuild/rpmbuild/BUILD/oci-registry-v0.4.5/vendor/ring-0.16.20/build.rs:358:10:
#   called `Option::unwrap()` on a `None` value
ExcludeArch:    ppc64le s390x

%description
oci-registry is an implementation of the OCI Registry spec with filesystem and
S3 storage back-ends.

Features
- Pull-through cache for any registry, not just docker.io
  - This includes private, authenticated registries. This means that you can
    create an unauthenticated mirror of a private registry and expose it to the
    Internet. Easily. Don't do that.
- Two storage back-ends
  - S3
  - Local filesystem
- Small footprint; in my test system, the official registry uses approximately
  130 MiB of memory to mirror docker.io; five replicas of oci-registry combined
  use approximately 60 MiB to mirror everything in example.yaml, plus one private
  registry. CPU is negligible for both.

Limitations
- Pushing is not currently implemented; oci-registry only supports being a
  pull-through cache (a mirror) at this time. Push support is planned.
- Authentication is not currently implemented, but is planned
- Only SHA256 content hashes are supported, but supporting other schemes is
  planned
- Connecting to oci-registry with TLS (https) is not supported and support will
  not be added.
  - Using nginx as a TLS termination proxy is easy, well-supported, and
    well-documented; if you require TLS between the client and oci-registry,
    that is the recommended configuration
  - Connecting to upstream registries with TLS is supported, recommended, and
    usually required.
- If two clients request the same blob simultaneously, it will be downloaded
  from upstream twice in parallel instead of having the later request wait for
  the download to finish, then serve it from cache. There are no data corruption
  issues, but it is suboptimal. No fix is currently planned, but I'm open to one.
- Has not yet had the OCI distribution spec conformance test suite run against
  it; only manual compatibility testing with docker and containerd has been
  performed. This is planned after push support is implemented.

%prep
%autosetup -a 1 -p 1
mkdir -p .cargo

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/oci-registry

%changelog
