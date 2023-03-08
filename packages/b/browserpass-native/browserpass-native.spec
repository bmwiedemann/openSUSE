#
# spec file for package browserpass-native
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


Name:           browserpass-native
Version:        3.1.0
Release:        0
Summary:        Native application for the browserpass browser extension
License:        ISC
URL:            https://github.com/browserpass/browserpass-native
Source:         https://github.com/browserpass/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.14
ExcludeArch:    ppc64
Recommends:     password-store

%description
This is a host application for browserpass browser extension providing it
access to your password store. The communication is handled through Native
Messaging API.

%prep
%setup -qa1

%build
export GOFLAGS="-mod=vendor"
%make_build browserpass

%check
export GOFLAGS=-mod=vendor
make test

%install
make configure
%make_install

rm -rf %{buildroot}/usr/share/{doc,licenses}

%files
%license LICENSE
%doc README.md
%{_bindir}/browserpass
%{_prefix}/lib/browserpass

%changelog
