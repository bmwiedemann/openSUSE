#
# spec file for package ghc-mintty
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


%global pkg_name mintty
Name:           ghc-%{pkg_name}
Version:        0.1.2
Release:        0
Summary:        A reliable way to detect the presence of a MinTTY console on Windows
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
MinTTY is a Windows-specific terminal emulator for the widely used Cygwin and
MSYS projects, which provide Unix-like environments for Windows.
MinTTY consoles behave differently from native Windows consoles (such as
'cmd.exe' or PowerShell) in many ways, and in some cases, these differences
make it necessary to treat MinTTY consoles differently in code.

The 'mintty' library provides a simple way to detect if your code in running in
a MinTTY console on Windows. It exports 'isMinTTY', which does the right thing
90% of the time (by checking if standard error is attached to MinTTY), and it
also exports 'isMinTTYHandle' for the other 10% of the time (when you want to
check is some arbitrary handle is attached to MinTTY). As you might expect,
both of these functions will simply return 'False' on any non-Windows operating
system.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
