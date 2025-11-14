#
# spec file for package manga-tui
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
Name:           manga-tui
Version:        0.10.0
Release:        0
Summary:        Terminal manga reader and downloader
License:        MIT
URL:            https://github.com/josueBarretogit/manga-tui
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-devel
BuildRequires:  openssl-devel
BuildRequires:  rust >= 1.85
ExclusiveArch:  x86_64 aarch64

%description
Terminal-based manga reader and downloader with image support.

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
