#
# spec file for package ghc-lukko
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name lukko
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.1.3
Release:        0
Summary:        File locking
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-singleton-bool-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
This package provides access to platform dependent file locking APIs:

*
<https://www.gnu.org/software/libc/manual/html_node/Open-File-Description-Locks.html
Open file descriptor locking> on Linux ("Lukko.OFD") * BSD-style 'flock(2)'
locks on UNIX platforms ("Lukko.FLock") * Windows locking via
<https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-lockfilee
LockFileEx> ("Lukko.Windows") * No-op locking, which throws exceptions
("Lukko.NoOp") * "Lukko" module exports the best option for the target platform
with uniform API.

There are alternative file locking packages:

* "GHC.IO.Handle.Lock" in 'base >= 4.10' is good enough for most use cases.
However, uses only 'Handle's so these locks cannot be used for intra-process
locking. (You should use e.g. 'MVar' in addition).

* <https://hackage.haskell.org/package/filelock filelock> doesn't support OFD
locking.

/Lukko/ means lock in Finnish.

Submodules "Lukko.OFD", "Lukko.Windows" etc are available based on following
conditions.

' if os(windows) cpp-options: -DHAS_WINDOWS_LOCK

elif (os(linux) && flag(ofd-locking)) cpp-options: -DHAS_OFD_LOCKING
cpp-options: -DHAS_FLOCK

elif !(os(solaris) || os(aix)) cpp-options: -DHAS_FLOCK '

"Lukko.FLock" is available on not (Windows or Solaris or AIX).
"Lukko.NoOp" is always available.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%license LICENSE.GPLv2
%license LICENSE.GPLv3

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
