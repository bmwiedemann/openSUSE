#
# spec file for package fq
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
# nodebuginfo


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           fq
Version:        0.14.0
Release:        0
Summary:        CLI tool and REPL for working with binary data inspired by jq
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/wader/fq
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18

%description
fq is inspired by the well known jq tool and language and allows you to work
with binary formats the same way you would using jq. In addition it can present
data like a hex viewer, transform, slice and concatenate binary data. It also
supports nested formats and has an interactive REPL with auto-completion.

%prep
%autosetup -a 1

%build
# Build the binary.
go build \
   -mod=vendor \
   -buildmode=pie

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
