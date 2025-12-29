#
# spec file for package age
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2021-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           age
Version:        1.3.0
Release:        0
Summary:        A file encryption tool
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://github.com/FiloSottile/age
#Git-Clone:     https://github.com/FiloSottile/age.git
Source:         https://github.com/FiloSottile/age/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

%description
Age features small explicit keys, no config options, and UNIX-style
composability.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} filippo.io/age
%{gobuild} -mod=vendor ...

%install
%{goinstall}
install -Dm 0644 -t %{buildroot}%{_mandir}/man1/ doc/*.1

%check
# disable test for now since it needs dependencies that are not vendored yet
#%%gotest filippo.io/age ...

%files
%license LICENSE
%doc README.md doc/*.1.html
%{_bindir}/age
%{_bindir}/age-keygen
%{_bindir}/age-inspect
%{_bindir}/age-plugin-batchpass
%{_bindir}/age-plugin-pq
%{_bindir}/age-plugin-tag
%{_bindir}/age-plugin-tagpq
%{_bindir}/age-plugin-tagtest
%{_mandir}/man1/age-keygen.1%{?ext_man}
%{_mandir}/man1/age.1%{?ext_man}
%{_mandir}/man1/age-inspect.1%{?ext_man}
%{_mandir}/man1/age-plugin-batchpass.1%{?ext_man}

%changelog
