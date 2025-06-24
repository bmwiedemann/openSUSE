#
# spec file for package sptlrx
#
# Copyright (c) 2025 mantarimay
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


Name:           sptlrx
Version:        1.2.3
Release:        0
Summary:        Synchronized lyrics in your terminal
License:        MIT
URL:            https://github.com/raitonoberu/sptlrx
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
An application for a variety of different music players that displays
lyrics on the terminal to your favorite songs while they're playing.
Compatible with Spotify, MPD, Mopidy, MPRIS, and browsers.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -Dm0755 %{name} -t %{buildroot}%{_bindir}
install -Dm0644 man/%{name}.5 -t %{buildroot}%{_datadir}/man/man5

./%{name} completion bash > "%{name}.bash"
./%{name} completion fish > "%{name}.fish"
./%{name} completion zsh > "_%{name}"

install -Dm644 %{name}.bash -t \
    %{buildroot}%{_datadir}/bash-completion/completions
install -Dm644 %{name}.fish -t \
    %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 _%{name} -t \
    %{buildroot}%{_datadir}/zsh/site-functions
    
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/man/man5/%{name}*
%{_datadir}/bash-completion/completions
%{_datadir}/fish
%{_datadir}/zsh

%changelog
