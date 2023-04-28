#
# spec file for package typst
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           typst
Version:        0.3.0
Release:        0
Summary:        A new markup-based typesetting system that is powerful and easy to learn
License:        Apache-2.0
URL:            https://github.com/typst/typst
Source0:        https://github.com/typst/typst/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  git

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

%prep
%autosetup -p1 -a1 -n typst-%{version}
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

# Build-process needs the whole git-repo in order to parse out the
# build-hash. We download the tarballs from github, which doesn't
# contain it. So we have to manually set the hash for now.
sed -i "s/_TYPST_HASH_/%{build_hash}/" cli/build.rs

%build
export GEN_ARTIFACTS=%{_builddir}/%{name}-%{version}/artifacts
mkdir -p $GEN_ARTIFACTS
cd cli
RUSTFLAGS=%{rustflags} %{cargo_build}

%check
%{cargo_test}

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}

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

%changelog
