#
# spec file for package rust
#
# Copyright (c) 2021 SUSE LLC
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


%global version_suffix 1.58
%global version_current 1.58.0

%define obsolete_rust_versioned() \
Obsoletes:      %{1}1.57%{?2:-%{2}} \
Obsoletes:      %{1}1.56%{?2:-%{2}} \
Obsoletes:      %{1}1.55%{?2:-%{2}} \
Obsoletes:      %{1}1.54%{?2:-%{2}} \
Obsoletes:      %{1}1.53%{?2:-%{2}}

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
speed, and concurrency. It maintains these goals without having a
garbage collector, making it a useful language for a number of use
cases other languages are not good at: embedding in other languages,
programs with specific space and time requirements, and writing
low-level code, like device drivers and operating systems. It improves
on current languages targeting this space by having a number of
compile-time safety checks that produce no runtime overhead, while
eliminating all data races. Rust also aims to achieve "zero-cost
abstractions", even though some of these abstractions feel like those
of a high-level language. Even then, Rust still allows precise control
like a low-level language would.

%package -n cargo
Summary:        The Rust package manager
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       cargo%{version_suffix}
Requires:       rust = %{version}
%obsolete_rust_versioned cargo

%description -n cargo
Cargo downloads dependencies of Rust projects and compiles it.

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
