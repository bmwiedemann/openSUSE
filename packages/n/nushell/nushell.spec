#
# spec file for package nushell
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


Name:           nushell
Version:        0.102.0
Release:        0
Summary:        A new type of shell
License:        MIT
URL:            https://www.nushell.sh/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Patch0:         reproducible.patch
BuildRequires:  cargo-packaging
BuildRequires:  git
BuildRequires:  zstd
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
ExclusiveArch:  %{rust_tier1_arches}

%description
A modern shell written in Rust.

%package plugin_custom_values
Summary:        Plugin nu_plugin_custom_values for %{name}
Requires:       %{name} = %{version}

%description plugin_custom_values
%{summary}.

%package plugin_example
Summary:        Plugin nu_plugin_example for %{name}
Requires:       %{name} = %{version}

%description plugin_example
%{summary}.

%package plugin_formats
Summary:        Plugin nu_plugin_formats for %{name}
Requires:       %{name} = %{version}

%description plugin_formats
%{summary}.

%package plugin_gstat
Summary:        Plugin nu_plugin_gstat for %{name}
Requires:       %{name} = %{version}

%description plugin_gstat
%{summary}.

%package plugin_inc
Summary:        Plugin nu_plugin_inc for %{name}
Requires:       %{name} = %{version}

%description plugin_inc
%{summary}.

%package plugin_polars
Summary:        Plugin nu_plugin_polars for %{name}
Requires:       %{name} = %{version}

%description plugin_polars
%{summary}.

%package plugin_query
Summary:        Plugin nu_plugin_query for %{name}
Requires:       %{name} = %{version}

%description plugin_query
%{summary}.

%package plugin_stress_internals
Summary:        Plugin nu_plugin_stress_internals for %{name}
Requires:       %{name} = %{version}

%description plugin_stress_internals
%{summary}.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
pushd crates/nu_plugin_custom_values
%{cargo_install}
popd
pushd crates/nu_plugin_example
%{cargo_install}
popd
pushd crates/nu_plugin_formats
%{cargo_install}
popd
pushd crates/nu_plugin_gstat
%{cargo_install}
popd
pushd crates/nu_plugin_inc
%{cargo_install}
popd
pushd crates/nu_plugin_polars
%{cargo_install}
popd
pushd crates/nu_plugin_query
%{cargo_install}
popd
pushd crates/nu_plugin_stress_internals
%{cargo_install}
popd
%{cargo_install}

install -d %{buildroot}/%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/nu
%{_datadir}/%{name}/

%files plugin_custom_values
%{_bindir}/nu_plugin_custom_values

%files plugin_example
%{_bindir}/nu_plugin_example

%files plugin_formats
%{_bindir}/nu_plugin_formats

%files plugin_gstat
%{_bindir}/nu_plugin_gstat

%files plugin_inc
%{_bindir}/nu_plugin_inc

%files plugin_polars
%{_bindir}/nu_plugin_polars

%files plugin_query
%{_bindir}/nu_plugin_query

%files plugin_stress_internals
%{_bindir}/nu_plugin_stress_internals

%changelog
