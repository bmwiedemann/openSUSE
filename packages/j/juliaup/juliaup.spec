#
# spec file for package juliaup
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


# We will keep this for now
%global oldest_supported_julia_version 0.7.0
%global latest_julia_version 1.11.1

Name:           juliaup
Version:        1.17.10
Release:        0
Summary:        Julia installer and version multiplexer
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND ISC AND MIT AND MPL-2.0 AND MIT
Group:          Development/Languages/Other
URL:            https://github.com/JuliaLang/juliaup
Source0:        https://github.com/JuliaLang/juliaup/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
Requires:       ca-certificates
Requires:       git
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
ExclusiveArch:  %{rust_tier1_arches}

%description
A cross-platform installer for the Julia programming language.

The installer also bundles a full Julia version manager called juliaup.
One can use juliaup to install specific Julia versions, it alerts users
when new Julia versions are released and provides a convenient Julia
release channel abstraction.

%prep
%autosetup -a1 -p1

%build
%{cargo_build} --no-default-features -F binjulialauncher

%install
%{cargo_install} --no-default-features -F binjulialauncher

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/julia %{buildroot}%{_bindir}/julia

%post
%{_sbindir}/update-alternatives --install %{_bindir}/julia \
    julia %{_bindir}/julialauncher 10

%postun
if [ ! -f %{_bindir}/julialauncher ] ; then
    %{_sbindir}/update-alternatives --remove julia %{_bindir}/julialauncher
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/juliaup
%{_bindir}/julialauncher
%ghost %{_bindir}/julia
%ghost %{_sysconfdir}/alternatives/julia

%changelog
