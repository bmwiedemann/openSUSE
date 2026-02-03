#
# spec file for package pdpmake
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           pdpmake
Version:        2.0.4
Release:        0
Summary:        Public domain POSIX make
License:        SUSE-Public-Domain
URL:            https://github.com/rmyorston/pdpmake
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
This version implements the make utility as defined in both the 2017 and 2024 POSIX standards.
The default build from source includes a number of extensions but a key feature of the program
is that it can be switched to a strictly POSIX-compliant mode at runtime

%prep
%autosetup

%build
%make_build CC=gcc CFLAGS="%{optflags} -std=c99"

%install
%make_install PREFIX=%{_prefix}

%check
%make_build test

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
