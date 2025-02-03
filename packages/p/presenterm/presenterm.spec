#
# spec file for package presenterm
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


Name:           presenterm
Version:        0.10.0+0
Release:        0
Summary:        A terminal slideshow tool
License:        BSD-2-Clause
URL:            https://github.com/mfontanini/presenterm
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
A terminal slideshow tool.

%prep
%autosetup -p1 -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/%{name}

%changelog
