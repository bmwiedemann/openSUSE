#
# spec file for package spicetify-cli
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


%define sname cli
%define binname spicetify
Name:           spicetify-cli
Version:        2.38.5
Release:        0
Summary:        Command-line tool to customize Spotify client
License:        LGPL-2.1-or-later
URL:            https://spicetify.app/
Source0:        %{sname}-%{version}.tar.zst
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.21

%description
Command-line tool to customize the official Spotify client

%prep
%autosetup -a1 -n %{sname}-%{version}

%build
go build -mod=vendor -buildmode=pie -ldflags="-X 'main.version=%{version}'"
printf "#!/bin/sh\n%{_libdir}/%{name}/%{binname} \"\$@\"" > ./shortcut

%install
install -Dm755 shortcut %{buildroot}%{_bindir}/%{binname}
install -Dm755 %{sname} %{buildroot}%{_libdir}/%{name}/%{binname}
cp -r Themes Extensions CustomApps jsHelper globals.d.ts css-map.json %{buildroot}%{_libdir}/%{name}

find %{buildroot}%{_libdir}/%{name}/ -type f -executable | grep -v %{name}/%{binname} | xargs chmod a-x

%files
%{_bindir}/%{binname}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%license LICENSE
%doc README.md

%changelog
