#
# spec file for package hey
#
# Copyright (c) 2021 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           hey
Version:        0.1.4
Release:        0
Summary:        HTTP load generator, ApacheBench (ab) replacement
License:        Apache-2.0
URL:            https://github.com/rakyll/hey
Source:         hey-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.13

%description
hey is a tiny program that sends some load to a web application.

hey was originally called boom and was influenced from Tarek Ziade's tool at
tarekziade/boom. Using the same name was a mistake as it resulted in cases
where binary name conflicts created confusion. To preserve the name for its
original owner, we renamed this project to hey.

%prep
%autosetup -a 1 -p 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
