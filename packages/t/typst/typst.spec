#
# spec file for package typst
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

%if 0%{?sle_version} && 0%{?sle_version} < 160000
# We have to use the same gcc-version that Rust was being built with
%define force_gcc_version 12
%endif

Name:           typst
Version:        0.11.1
Release:        0
Summary:        A new markup-based typesetting system that is powerful and easy to learn
License:        Apache-2.0
URL:            https://github.com/typst/typst
Source0:        https://github.com/typst/typst/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  git
BuildRequires:  openssl-devel
Recommends:     hayagriva

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package -n     hayagriva
Summary:        Standalone CLI of built-in bibliography management tool
Supplements:    %{name}

%description -n hayagriva
Standalone CLI of the built-in bibliography management library used in typst.

%prep
%autosetup -p1 -a1 -n typst-%{version}

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
export TYPST_VERSION=%{version}
export GEN_ARTIFACTS=%{_builddir}/%{name}-%{version}/artifacts
mkdir -p $GEN_ARTIFACTS
RUSTFLAGS=%{rustflags} %{cargo_build} --workspace

# Building hayagriva

# Tiny hack to be able to build it from inside the vendor-dir,
# otherwise it would complain about not being a member of the
# top-level typst-workspace
echo "[workspace]" >> vendor/hayagriva/Cargo.toml
# hayagriva is older, so typst might use newer dot-dependencies.
# We tell hayagriva to use the newer ones, if available.
cargo update --offline --manifest-path=vendor/hayagriva/Cargo.toml
# We may have updated hayagriva's Cargo.lock-file.
# So we have to tell typst, not to worry about hash-mismatches.
# (Matters in the check-section below)
echo "[patch.crates-io.hayagriva]" >> Cargo.toml
echo "path = \"vendor/hayagriva\"" >> Cargo.toml
RUSTFLAGS=%{rustflags} %{cargo_build} --manifest-path=vendor/hayagriva/Cargo.toml

%check
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%{cargo_test} --workspace

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/hayagriva

# Shell completions
install -Dm644 -T %{_builddir}/%{name}-%{version}/artifacts/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 -T %{_builddir}/%{name}-%{version}/artifacts/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# copy man-pages
mkdir -p %{buildroot}%{_mandir}/man1/
cp -L  %{_builddir}/%{name}-%{version}/artifacts/*.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md
%{_bindir}/typst
%{_mandir}/*/*

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files -n hayagriva
%license vendor/hayagriva/LICENSE*
%doc vendor/hayagriva/README.md vendor/hayagriva/docs/*
%{_bindir}/hayagriva

%changelog
