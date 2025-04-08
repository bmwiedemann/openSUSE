#
# spec file for package nyaa
#
# Copyright (c) 2025 mantarimay
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
Name:           nyaa
Version:        0.9.1
Release:        0
Summary:        A tui tool for browsing and downloading torrents
License:        GPL-3.0-or-later
URL:            https://github.com/Beastwick18/nyaa
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel

%description
A simple cli tool for browsing and downloading Anime torrents from nyaa.si.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%if %{with test}
%check
%{cargo_test}
%endif

%files
%license LICEN*
%doc README* docs
%{_bindir}/%{name}

%changelog
