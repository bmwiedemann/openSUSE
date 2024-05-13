#
# spec file for package oculante
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


%bcond_without test
Name:           oculante
Version:        0.8.21
Release:        0
Summary:        A minimalistic crossplatform image viewer written in rust
License:        MIT
URL:            https://github.com/woelper/oculante
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc >= 13
BuildRequires:  gtk3-devel
BuildRequires:  libheif-devel
BuildRequires:  nasm
ExclusiveArch:  x86_64 aarch64

%description
Oculante's vision is to be a fast, unobtrusive, portable image viewer with
wide image format support, offering image analysis and basic editing
tools.

%prep
%autosetup -a1 -p1

%build
%{cargo_build} --features 'heif'

%install
install -Dpm755 target/release/%{name} -t %{buildroot}%{_bindir}
install -Dpm644 res/%{name}.png -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm644 res/%{name}.desktop -t %{buildroot}%{_datadir}/applications

%check
%if %{with test}
%{cargo_test} -- --skip=tests::net --skip=bench
%endif

%files
%license LICENSE*
%doc README* CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
