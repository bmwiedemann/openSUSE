#
# spec file for package sd-mux-ctrl
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sd-mux-ctrl
Version:        0.0~git20200217.9dd189d
Release:        0
Summary:        Control software for sd-mux devices
License:        Apache-2.0
Group:          Development/Tools
URL:            https://wiki.tizen.org/SD_MUX
Source0:        sd-mux-%{version}.tar.xz
BuildRequires:  cmake >= 2.8.3
BuildRequires:  libftdi1-devel >= 1.4
BuildRequires:  popt-devel
BuildRequires:  gcc-c++

%description
Tool for controlling multiple sd-mux devices (SD_MUX, SDWIRE, etc.).

%prep
%setup -q -n sd-mux-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
# Man pages
mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 doc/man/%{name}.1 %{buildroot}%{_mandir}/man1
# Bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install etc/bash_completion.d/%{name} %{buildroot}%{_datadir}/bash-completion/completions/

%files
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/*

%changelog
