#
# spec file for package curlie
#
# Copyright (c) 2023 SUSE LLC
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


%define goipath github.com/rs/curlie
Name:           curlie
Version:        1.7.1
Release:        0
Summary:        a frontend to curl that adds the ease of use of httpie
License:        MIT
URL:            https://github.com/rs/curlie
Source0:        https://github.com/rs/curlie/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-UPSTREAM upgrade-go-version-and-x-sys-to-latest.patch  -- based on commit 9fcb3a0
Patch0:         upgrade-go-version-and-x-sys-to-latest.patch
BuildRequires:  go >= 1.20
BuildRequires:  golang-packaging
BuildRequires:  libunistring-devel

%description
If you like the interface of HTTPie but miss the features of curl, curlie is what you are searching for. Curlie is a frontend to curl that adds the ease of use of httpie, without compromising on features and performance. All curl options are exposed with syntax sugar and output formatting inspired from httpie.

%prep
%autosetup -D -a 1

%build
GOFLAGS="-buildmode=pie" go build -mod vendor -o %{name} .

%install
install -Dm 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
