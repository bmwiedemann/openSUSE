#
# spec file for package kl
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kl
Version:        0.6.1
Release:        0
Summary:        An interactive Kubernetes log viewer for your terminal
License:        MIT
URL:            https://github.com/robinovitch61/kl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.23

%description
An interactive Kubernetes log viewer for your terminal.

* View logs across multiple containers, pods, namespaces, and clusters
* Select containers interactively or auto-select by pattern matching against
  names, labels, and more
* See cluster changes in real time
* Navigate logs from multiple containers interleaved by timestamp
* Search logs by exact string or regex pattern. Show or hide surrounding
  context
* Zoom in and flip through single formatted logs one by one
* Archive and share: save logs to a local file or copy a log to your clipboard

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -tags="osusergo netgo release" \
   -ldflags="-X github.com/robinovitch61/kl/cmd.Version=v%{version}" \
   -o bin/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
