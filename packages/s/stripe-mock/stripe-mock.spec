#
# spec file for package stripe-mock
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


Name:           stripe-mock
Version:        0.185.0
Release:        0
Summary:        Mock HTTP server based on the real Stripe API
License:        MIT
URL:            https://github.com/stripe/stripe-mock
Source:         https://github.com/stripe/stripe-mock/archive/refs/tags/v%{version}.tar.gz#/stripe-mock-%{version}.tar.gz
BuildRequires:  golang(API) >= 1.19

%description
stripe-mock is a mock HTTP server based on the real Stripe API. It accepts
the same requests and parameters that the Stripe API accepts, and rejects
requests whose parameters are not recognized or have incorrect types. Its
responses resemble the responses of the real Stripe API in terms of data
type; however, stripe-mock does not attempt to reproduce the behavior of
the real Stripe API at all.

%prep
%autosetup -p1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
strip %{buildroot}%{_bindir}/%{name}

%check
./%{name} --help

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
