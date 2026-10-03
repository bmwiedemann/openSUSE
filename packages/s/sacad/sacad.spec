#
# spec file for package sacad
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           sacad
Version:        3.0.3
Release:        0
Summary:        Search and download music album covers
License:        MPL-2.0
URL:            https://github.com/desbma/sacad
Source:         https://github.com/desbma/sacad/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.79
ExclusiveArch:  %{rust_arches}

%description
SACAD is a multi platform command line tool to download album covers
without manual intervention, ideal for integration in scripts, audio
players, etc.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build} --all-features
# generate man pages
./target/release/sacad_gen_extras gen-man-pages .

%install
for f in sacad sacad_r; do
  install -D -m 0755 "target/release/$f" "%{buildroot}%{_bindir}/$f"
  install -D -m 0644 "$f.1" "%{buildroot}/%{_mandir}/man1/$f.1"
done

#%%check
# disabled - tests require an internet connection

%files
%license LICENSE
%doc README.md
%{_bindir}/sacad
%{_bindir}/sacad_r
%{_mandir}/man1/sacad.1%{?ext_man}
%{_mandir}/man1/sacad_r.1%{?ext_man}

%changelog
