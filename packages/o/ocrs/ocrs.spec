#
# spec file for package ocrs
#
# Copyright (c) 2024 mantarimay
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


%ifarch s390x
%bcond_with test
%else
%bcond_without test
%endif
Name:           ocrs
Version:        0.8.0
Release:        0
Summary:        A modern OCR engine written in Rust
License:        Apache-2.0 AND MIT
URL:            https://github.com/robertknight/ocrs
Source0:        %{url}/archive/ocrs-v%{version}/ocrs-ocrs-v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
ocrs is CLI tool for extracting text from images, also known as OCR
(Optical Character Recognition).

%prep
%autosetup -n ocrs-ocrs-v%{version} -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/ocrs -t %{buildroot}%{_bindir}

%check
%if %{with test}
%{cargo_test}
%endif

%files
%license LICEN*
%doc README* CHANGELOG.md
%{_bindir}/ocrs

%changelog
