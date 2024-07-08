#
# spec file for package phraze
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


Name:           phraze
Version:        0.3.10
Release:        0
Summary:        Generate random passphrases
License:        MPL-2.0
URL:            https://github.com/sts10/phraze
Source0:        phraze-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Generate random passphrases

%prep
%autosetup -a1 -n phraze-%{version}
mkdir -p .cargo

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/phraze
%license LICENSE.txt
%doc CHANGELOG.markdown

%changelog

