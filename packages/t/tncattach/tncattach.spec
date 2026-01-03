#
# spec file for package tncattach
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


Name:           tncattach
Version:        20241222.c910421
Release:        0
Summary:        Attach KISS TNC devices as network interfaces in Linux
License:        MIT
URL:            https://github.com/markqvist/tncattach
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  binutils

%description
Attach KISS TNC devices as network interfaces in Linux.
This program allows you to attach TNCs or any KISS-compatible device as a
network interface. This program does not need any kernel modules, and has
no external dependencies outside the standard Linux and GNU C libraries.

%prep
%autosetup

%build
%make_build
strip tncattach

%install
%make_install PREFIX=%{_prefix}/

%files
%license LICENSE
%doc README.md
%{_bindir}/tncattach
%{_mandir}/man8/tncattach.8%{?ext_man}

%changelog
