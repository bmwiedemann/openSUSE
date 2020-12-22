#
# spec file for package ghc-atomic-write
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


%global pkg_name atomic-write
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.0.7
Release:        0
Summary:        Atomically write to a file
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unix-compat-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%endif

%description
Atomically write to a file on POSIX-compliant systems while preserving
permissions.

On most Unix systems, `mv` is an atomic operation. This makes it simple to
write to a file atomically just by using the mv operation. However, this will
destroy the permissions on the original file. This library does the following
to preserve permissions while atomically writing to a file:

* If an original file exists, take those permissions and apply them to the temp
file before `mv`ing the file into place.

* If the original file does not exist, create a following with default
permissions (based on the currently-active umask).

This way, when the file is `mv`'ed into place, the permissions will be the ones
held by the original file.

This library is based on similar implementations found in common libraries in
Ruby and Python:

* <http://apidock.com/rails/File/atomic_write/class Ruby on Rails includes a
similar method called atomic_write>

*
<https://github.com/chef/chef/blob/c4631816132fcfefaba3d123a1d0dfe8bc2866bb/lib/chef/file_content_management/deploy/mv_unix.rb#L23:L71
Chef includes atomic update functionality>

* <https://github.com/sashka/atomicfile There is a python library for
atomically updating a file>

To use `atomic-write`, import the module corresponding to the type you wish to
write atomically, e.g., to write a (strict) ByteString atomically:

> import System.AtomicWrite.Writer.ByteString

Then you can use the atomicWriteFile function that accepts a `FilePath` and a
`ByteString`, e.g.:

> atomicWriteFile myFilePath myByteString.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
