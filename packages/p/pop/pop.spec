#
# spec file for package pop
#
# Copyright (c) specCURRENT_YEAR SUSE LLC
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


Name:           pop
Version:        0.2.0
Release:        0
Summary:        Program to send emails from a terminal
License:        MIT
Group:          Productivity/Networking/Email/Utilities
URL:            https://github.com/charmbracelet/pop
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18
BuildRequires:  zstd

%description
A program to send emails from a terminal.
To use pop, a RESEND_API_KEY is required, or an SMTP host needs to be
configured.

%prep
%autosetup -a1

%build
export GOWORK=off

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%check
# execute the binary as a basic check
./%{name} --help

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
