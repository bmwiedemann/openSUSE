#
# spec file for package rage-encryption
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


%{?!rust_tier1_arches:%global rust_tier1_arches x86_64 aarch64}

Name:           rage-encryption
#               This will be set by osc services, that will run after this.
Version:        0.9.0+0
Release:        0
Summary:        Simple, modern, and secure file encryption tool
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-3-Clause AND CDDL-1.0 AND MIT
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Productivity/Security
URL:            https://github.com/str4d/rage
Source0:        rage-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
%if %{suse_version} > 1500
BuildRequires:  cargo-packaging
%endif
# Requires >1.59 for thread::available_parallelism
BuildRequires:  cargo >= 1.59
BuildRequires:  vendored_licenses_packager
# for feature mount
BuildRequires:  fuse-devel
Recommends:     pinentry
Conflicts:      rage
ExclusiveArch:  %{rust_tier1_arches}

%description
Rage is a simple, modern, and secure file encryption tool, using the age format. It features small
explicit keys, no config options, and UNIX-style composability.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          Productivity/Security
BuildArch:      noarch
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
Conflicts:      rage

%description bash-completion
Bash command line completion support for %{name}

%prep
%setup -q -a 0 -n rage-%{version}
%setup -q -n rage-%{version} -a 1 -D -T
mkdir .cargo
cp %{SOURCE2} .cargo/config
%vendored_licenses_packager_prep

%build
%define build_args --manifest-path rage/Cargo.toml --features "mount" --release %{?_smp_mflags}

%if %{suse_version} > 1500
%{cargo_build} --features "mount"
%else
cargo build %{build_args}
%endif

cargo run --example generate-completions %{build_args}
cargo run --example generate-docs %{build_args}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/rage-%{version}/target/release/rage %{buildroot}%{_bindir}/rage
install -m 0755 %{_builddir}/rage-%{version}/target/release/rage-keygen %{buildroot}%{_bindir}/rage-keygen
install -m 0755 %{_builddir}/rage-%{version}/target/release/rage-keygen %{buildroot}%{_bindir}/rage-mount

for i in "" -keygen -mount; do
  install -D -p -m 644 target/manpages/rage$i.1.gz %{buildroot}/%{_mandir}/man1/rage$i.1%{?ext_man}
  install -D -p -m 644 target/completions/rage$i.bash %{buildroot}%{_datadir}/bash-completion/completions/rage$i
done
%vendored_licenses_packager_install

%files
%{_bindir}/rage
%{_bindir}/rage-keygen
%{_bindir}/rage-mount
%doc README.md rage/CHANGELOG.md
# accept duplicates here
%license LICENSE-APACHE LICENSE-MIT
%vendored_licenses_packager_files
%{_mandir}/man1/rage*.1%{?ext_man}

%files bash-completion
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/bash-completion/completions/rage*

%changelog
