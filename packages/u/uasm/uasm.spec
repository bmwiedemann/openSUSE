#
# spec file for package uasm
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

Name:           uasm
Version:        2.56.2
Release:        0
Summary:        MASM-compatible assembler based on JWasm
License:        Watcom-1.0
URL:            http://www.terraspace.co.uk/%{name}.html
Source:         https://github.com/Terraspace/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:         fix-error-return-type.patch
BuildRequires:  glibc-devel

%description
MASM-compatible assembler based on JWasm

%prep
%autosetup -n UASM-%{version} -p1

%build
%make_build -f gccLinux64.mak CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install GccUnixR/%{name} -t %{buildroot}%{_bindir}

%files
%doc Readme.txt
%doc History.txt
%license License.txt
%{_bindir}/%{name}

%changelog
