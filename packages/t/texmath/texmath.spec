#
# spec file for package texmath
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


%global pkg_name texmath
%bcond_with tests
Name:           %{pkg_name}
Version:        0.12.0.3
Release:        0
Summary:        Conversion between formats used to represent mathematics
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-xml-devel
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-utf8-string-devel
%endif

%description
The texmath library provides functions to read and write TeX math, presentation
MathML, and OMML (Office Math Markup Language, used in Microsoft Office).
Support is also included for converting math formats to Gnu eqn and to pandoc's
native format (allowing conversion, via pandoc, to a variety of different
markup formats). The TeX reader supports basic LaTeX and AMS extensions, and it
can parse and apply LaTeX macros. (See <http://johnmacfarlane.net/texmath here>
for a live demo of bidirectional conversion between LaTeX and MathML.)

The package also includes several utility modules which may be useful for
anyone looking to manipulate either TeX math or MathML. For example, a copy of
the MathML operator dictionary is included.

Use the 'executable' flag to install a standalone executable, 'texmath', that
by default reads a LaTeX formula from 'stdin' and writes MathML to 'stdout'.
With flags all the functionality exposed by 'Text.TeXMath' can be accessed
through this executable. (Use the '--help' flag for a description of all
functionality)

The 'texmath' executable can also be used as a CGI script, when renamed as
'texmath-cgi'. It will expect query parameters for 'from', 'to', 'input', and
optionally 'inline', and return a JSON object with either 'error' and a message
or 'success' and the converted result.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup

%build
%define cabal_configure_options -fexecutable
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc README.markdown changelog
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc README.markdown changelog

%changelog
