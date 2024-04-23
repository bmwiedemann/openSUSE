#
# spec file for package oxipng
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


Name:           oxipng
Version:        9.1.0
Release:        0
Summary:        Multithreaded lossless PNG optimizer
License:        MIT
URL:            https://github.com/shssoichiro/oxipng
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Oxipng is a multithreaded lossless PNG compression optimizer. It can be used
via a command-line interface or as a library in other Rust programs.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}
install -Dm0644 MANUAL.txt %{buildroot}%{_mandir}/man1/%{name}.1

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
