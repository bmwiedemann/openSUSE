#
# spec file for package tut
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


Name:           tut
Version:        1.0.20
Release:        0
Summary:        A TUI for Mastodon with vim inspired keys
License:        MIT
Group:          Productivity/Networking/Web/Frontends
URL:            https://tut.anv.nu
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
# some modules require go 1.18+
BuildRequires:  golang(API) >= 1.18

%description
tut is a TUI for Mastodon with vim inspired keys. TUI is an acronym for text-based user interface, so tut runs in your terminal.

%prep
%autosetup -a 1

%build
%ifarch ppc64
go build \
   -mod=vendor \
   -tags extended
%else
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie
%endif

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
