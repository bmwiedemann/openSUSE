#
# spec file for package goipp
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


%define         import_path github.com/OpenPrinting/goipp
Name:           goipp
Version:        1.2.0
Release:        0
Summary:        Implementation of the IPP core protocol in pure GO
License:        BSD-2-Clause
URL:            https://github.com/OpenPrinting/goipp
Source:         %{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
BuildArch:      noarch

%{go_provides}

%description
The goipp library is fairly complete implementation of IPP core protocol in pure Go.
Essentially, it is IPP messages parser/composer. Transport is not implemented
here, because Go standard library has an excellent built-in HTTP client,
and it doesn't make a lot of sense to wrap it here.

High-level requests, like "print a file" are also not implemented,
only the low-level stuff.

%prep
%autosetup
%goprep %{import_path}

%build
%gobuild

%install
%gosrc

%check
%gotest %{import_path}

%files
%license LICENSE
%doc README.md
%{go_contribsrcdir}/github.com

%changelog
