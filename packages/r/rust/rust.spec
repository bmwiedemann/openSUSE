#
# spec file for package rust
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 William Brown <william@blackhats.net.au>
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


%global version_suffix 1.79
%global version_current 1.79.0

%define obsolete_rust_versioned() \
Obsoletes:      %{1}1.78%{?2:-%{2}} \
Obsoletes:      %{1}1.77%{?2:-%{2}} \
Obsoletes:      %{1}1.76%{?2:-%{2}} \
Obsoletes:      %{1}1.75%{?2:-%{2}} \
Obsoletes:      %{1}1.74%{?2:-%{2}} \
Obsoletes:      %{1}1.73%{?2:-%{2}} \
Obsoletes:      %{1}1.72%{?2:-%{2}} \
Obsoletes:      %{1}1.71%{?2:-%{2}} \
Obsoletes:      %{1}1.70%{?2:-%{2}} \
Obsoletes:      %{1}1.69%{?2:-%{2}} \
Obsoletes:      %{1}1.68%{?2:-%{2}} \
Obsoletes:      %{1}1.67%{?2:-%{2}} \
Obsoletes:      %{1}1.66%{?2:-%{2}} \
Obsoletes:      %{1}1.65%{?2:-%{2}} \
Obsoletes:      %{1}1.64%{?2:-%{2}} \
Obsoletes:      %{1}1.63%{?2:-%{2}} \
Obsoletes:      %{1}1.62%{?2:-%{2}}

# === rust arch support tiers ===
# https://doc.rust-lang.org/nightly/rustc/platform-support.html
# tl;dr only aarch64, x86_64 and i686 are guaranteed to work.
#
# armv6/7, s390x, ppc[64[le]], riscv are all "guaranteed to build" only
# but may not always work.
#

Name:           rust
Version:        %{version_current}
Release:        0
Summary:        A systems programming language
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
URL:            https://www.rust-lang.org
Source:         README
Source99:       %{name}-rpmlintrc
Requires:       rust%{version_suffix}
%obsolete_rust_versioned rust

%description
Rust is a systems programming language focused on three goals: safety,
speed, and concurrency.

⚠️  This is the Rust toolchain intended for build pipelines. If you
want to install Rust for a development environment, you should install
'rustup' instead.

%package -n cargo
Summary:        The Rust package manager
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       cargo%{version_suffix}
Requires:       rust = %{version}
Provides:       rust+cargo = %{version}
%obsolete_rust_versioned cargo

%description -n cargo
Cargo downloads dependencies of Rust projects and compiles it.

⚠️  This is the Rust toolchain intended for build pipelines. If you
want to install Rust for a development environment, you should install
'rustup' instead.

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/rust/README
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/cargo/README

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/rust

%files -n cargo
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/cargo

%changelog
