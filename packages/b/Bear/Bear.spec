#
# spec file for package Bear
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without  tests

Name:           Bear
Version:        4.2.1
Release:        0
Summary:        Tool that generates a compilation database for clang tooling
License:        GPL-3.0-or-later
URL:            https://github.com/rizsotto/Bear
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  lld
%if %{with tests}
#BuildRequires:  ccache
BuildRequires:  fakeroot
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  valgrind
%endif
ExclusiveArch:  %{rust_tier1_arches}

%description
Build ear produces compilation database in JSON format. This database
describes how single compilation unit should be processed and can be
used by Clang tooling.

%prep
%autosetup -a1 -p1

%build
export INTERCEPT_LIBDIR=%{_lib}
%{cargo_build}
./target/release/generate-completions target/release/completions

%install
#%%{cargo_install}
DESTDIR=%{buildroot} PREFIX=%{_prefix} INTERCEPT_LIBDIR=%{_lib} ./scripts/install.sh
chmod 0755 %{buildroot}%{_libexecdir}/bear/%{_lib}/libexec.so
rm -r %{buildroot}%{_datadir}/{doc,elvish}

%if %{with tests}
%check
export INTERCEPT_LIBDIR=%{_lib}
# Several cases fail if ccache wrappers are in the PATH
cc_path=$(command -v gcc)
if [ "$cc_path" != "${cc_path%%/ccache*}" ]; then
    cc_path=$(dirname "$cc_path")
    export PATH="${PATH%"$cc_path:"*}${PATH##*"$cc_path:"}"
fi
unset cc_path
#%%{cargo_test}
cargo build --offline
cargo test
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/bear
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/bear
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/bear.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bear
%dir %{_libexecdir}/bear
%dir %{_libexecdir}/bear/bin
%dir %{_libexecdir}/bear/%{_lib}
%{_libexecdir}/bear/bin/bear-driver
%{_libexecdir}/bear/bin/bear-wrapper
%{_libexecdir}/bear/%{_lib}/libexec.so
%{_mandir}/man1/bear.1%{?ext_man}

%changelog
