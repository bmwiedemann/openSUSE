#
# spec file for package sad
#
# Copyright (c) 2022 SUSE LLC
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


Name:           sad
Version:        0.4.22
Release:        0
Summary:        CLI search and replace batch file editing tool
URL:            https://github.com/ms-jpq/sad
License:        (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND MIT AND (Artistic-2.0 OR CC0-1.0) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND MPL-2.0+ AND Zlib AND zlib-acknowledgement AND Apache-2.0
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
Recommends:     fzf

%description
Basically sad is a Batch File Edit tool.
It will show you a really nice diff of proposed changes before you commit them.
Unlike sed, you can double check before you fat finger your edit.

%prep
%autosetup -a1
mkdir -p .cargo

# replacing the toml provided by sad
cp %{SOURCE2} .cargo/config.toml

%build
%{cargo_build}

%install
%{cargo_install}

%if %{with check}
%check
%{cargo_test}
%endif

%files
%license LICENSE
%doc README.md RELEASE_NOTES.md
%{_bindir}/sad

%changelog
