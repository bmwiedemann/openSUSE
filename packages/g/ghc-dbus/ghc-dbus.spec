#
# spec file for package ghc-dbus
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


%global pkg_name dbus
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.3.9
Release:        0
Summary:        A client library for the D-Bus IPC system
License:        Apache-2.0
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-xml-types-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
%endif

%description
D-Bus is a simple, message-based protocol for inter-process communication,
which allows applications to interact with other parts of the machine and the
user's session using remote procedure calls.

D-Bus is a essential part of the modern Linux desktop, where it replaces
earlier protocols such as CORBA and DCOP.

This library is an implementation of the D-Bus protocol in Haskell. It can be
used to add D-Bus support to Haskell applications, without the awkward
interfaces common to foreign bindings.

Example: connect to the session bus, and get a list of active names.

' &#x7b;-# LANGUAGE OverloadedStrings #-&#x7d;

import Data.List (sort) import DBus import DBus.Client

main = do &#x20; client <- connectSession &#x20; &#x20; -- Request a list of
connected clients from the bus &#x20; reply <- call_ client (methodCall
"/org/freedesktop/DBus" "org.freedesktop.DBus" "ListNames") &#x20; &#x7b;
methodCallDestination = Just "org.freedesktop.DBus" &#x20; &#x7d; &#x20; &#x20;
-- org.freedesktop.DBus.ListNames() returns a single value, which is &#x20; --
a list of names (here represented as [String]) &#x20; let Just names =
fromVariant (methodReturnBody reply !! 0) &#x20; &#x20; -- Print each name on a
line, sorted so reserved names are below &#x20; -- temporary names.
&#x20; mapM_ putStrLn (sort names) '

>$ ghc --make list-names.hs >$ ./list-names >:1.0 >:1.1 >:1.10 >:1.106 >:1.109
>:1.110 >ca.desrt.dconf >org.freedesktop.DBus >org.freedesktop.Notifications
>org.freedesktop.secrets >org.gnome.ScreenSaver.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}

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
%license license.txt

%files devel -f %{name}-devel.files
%doc examples

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license license.txt

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
