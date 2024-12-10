#
# spec file for package cosmic-ext-dirstat
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


Name:           cosmic-ext-dirstat
Version:        0.1.0+git20241120.bab06c8
Release:        0
Summary:        KDirStat-esque disk usage analyzer using libcosmic
License:        GPL-3.0-only
URL:            https://github.com/Koranir/cosmic-dirstat
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)

%description
A WIP KDirStat-esque GUI to analyze disk usage with.
Currently Linux only.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 ./target/release/cosmic-dirstat %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
