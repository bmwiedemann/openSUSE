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


%global version_suffix 1.53
%global version_current 1.53.0

# Dev tools - these are needed for developers, vs building, so
# we don't always enable them. Some platforms have issues
# building these (IE RLS requires 64-bit atomics).
# As a result, we limit this to platforms that are likely used on
# desktop arches
%ifarch x86_64 aarch64
%bcond_without devtools
%else
%bcond_with devtools
%endif

# Rpm specs have a limitation that if the parent package is noarch, all child packages must
# also be noarch. Since rls is arch dependent, we MUST have all packages as arch dependent
# because of this.
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
Conflicts:      rust < %{version}
Obsoletes:      rust < %{version}

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

%package -n rust-gdb
Summary:        Gdb integration for rust binaries
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust = %{version}
Requires:       rust%{version_suffix}
Requires:       rust%{version_suffix}-gdb
Conflicts:      rust-gdb < %{version}
Obsoletes:      rust-gdb < %{version}

%if 0%{?suse_version} && 0%{?suse_version} < 1500
# Legacy SUSE-only form
Supplements:    packageand(rust:gdb)
%else
# Standard form
Supplements:    (rust and gdb)
%endif

%description -n rust-gdb
This subpackage provides pretty printers and a wrapper script for
invoking gdb on rust binaries.





# As this is masked by devtools, this is arch specific even if it has no content.
%package -n rls
Summary:        Language server for Rust lang
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rls%{version_suffix}
Requires:       rust = %{version}
Requires:       rust%{version_suffix}
Conflicts:      rls < %{version}
Obsoletes:      rls < %{version}

%description -n rls
The RLS provides a server that runs in the background, providing IDEs,
editors, and other tools with information about Rust programs. It
supports functionality such as 'goto definition', symbol search,
reformatting, and code completion, and enables renaming and
refactorings.  It can be used with an IDE such as Gnome-Builder.

%package -n cargo
Summary:        The Rust package manager
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       cargo%{version_suffix}
Requires:       rust = %{version}
Requires:       rust%{version_suffix}
Conflicts:      cargo < %{version}
Obsoletes:      cargo < %{version}

%description -n cargo
Cargo downloads dependencies of Rust projects and compiles it.

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/rust/README
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/rust-gdb/README
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/cargo/README
%if %{with devtools}
install -D -m 0644 %{S:0} %{buildroot}/usr/share/doc/packages/rls/README
%endif

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/rust

%files -n rust-gdb
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/rust-gdb

%if %{with devtools}
%files -n rls
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/rls
%endif

%files -n cargo
%defattr(-,root,root,-)
%doc /usr/share/doc/packages/cargo

%changelog
