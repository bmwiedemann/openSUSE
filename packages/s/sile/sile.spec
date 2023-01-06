#
# spec file for package sile
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without  tests
Name:           sile
Version:        0.14.7
Release:        0
Summary:        Simon’s Improved Layout Engine
Group:          Productivity/Publishing
License:        MIT
URL:            https://sile-typesetter.org/
Source0:        https://github.com/sile-typesetter/sile/releases/download/v%{version}/sile-%{version}.tar.xz
Source1:        sile-rpmlintrc
Source2:        LICENSE

# Lua modules
Requires:       lua54
BuildRequires:  lua54-bit32
BuildRequires:  lua54-devel
Requires:       lua54-bit32
BuildRequires:  lua54-cassowary
Requires:       lua54-cassowary
Requires:       lua54-cldr
BuildRequires:  lua54-cliargs
Requires:       lua54-cliargs
BuildRequires:  lua54-cosmo
Requires:       lua54-cosmo
BuildRequires:  lua54-luaexpat
Requires:       lua54-luaexpat
BuildRequires:  lua54-luafilesystem
Requires:       lua54-luafilesystem
BuildRequires:  lua54-fluent
Requires:       lua54-fluent
BuildRequires:  lua54-linenoise
Requires:       lua54-linenoise
BuildRequires:  lua54-loadkit
Requires:       lua54-loadkit
Requires:       lua54-lpeg
Requires:       lua54-luaepnf
BuildRequires:  lua54-luarepl
Requires:       lua54-luarepl
BuildRequires:  lua54-luautf8
Requires:       lua54-luautf8
Requires:       lua54-penlight
BuildRequires:  lua54-luasec
Requires:       lua54-luasec
Requires:       lua54-luasocket
BuildRequires:  lua54-vstruct
Requires:       lua54-vstruct
BuildRequires:  lua54-zlib
# Without this Requires, lua54-zlib isn't counted as a dependency
Requires:       lua54-zlib

# Other Dependencies
%if %{with tests}
BuildRequires:  poppler-tools
BuildRequires:  sil-gentium-fonts
%endif
BuildRequires:  automake
BuildRequires:  fontconfig-devel
Requires:       fontconfig
BuildRequires:  freetype2-devel
Requires:       freetype2
BuildRequires:  fdupes
BuildRequires:  gcc-objc
BuildRequires:  git-core
Requires:       git-core
BuildRequires:  glibc-devel
Requires:       glibc
BuildRequires:  harfbuzz-devel
BuildRequires:  libicu-devel
Requires:       icu
BuildRequires:  libpng16-compat-devel
BuildRequires:  zlib-devel
# Default font for SILE
# Without this, you have to specify the font every time you write a new .sil
Recommends:     sil-gentium-fonts
# Default font for math package
Suggests:       libertinus-fonts
# Default font for tate enabled classes
Suggests:       noto-sans-cjk-fonts
# Default mono font
Suggests:       hack-fonts

%description
SILE is a typesetting system; its job is to produce beautiful printed documents.
Conceptually, SILE is similar to TeX—from which it borrows some concepts and even
syntax and algorithms—but the similarities end there. Rather than being a
derivative of the TeX family SILE is a new typesetting and layout engine written
from the ground up using modern technologies and borrowing some ideas from
graphical systems such as InDesign.

%package -n libtexpdf0
Summary:        A PDF library extracted from TeX's dvipdfmx
Group:          Productivity/Publishing
License:        GPL-2.0-or-later

%description -n libtexpdf0
A PDF library extracted from TeX's dvipdfmx. Used in software such as SILE.
This package contains the shared library for libtexpdf.

%package -n libtexpdf-devel
Summary:        Development files for libtexpdf
Group:          Productivity/Publishing
License:        GPL-2.0-or-later
Requires:       libtexpdf0 = %{version}

%description -n libtexpdf-devel
A PDF library extracted from TeX's dvipdfmx. Used in software such as SILE.
This package contains the development files for libtexpdf.

%prep
%autosetup -p1
cp %{SOURCE2} .

%build
%configure --disable-static --with-system-luarocks
%make_build all

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}

%if %{with tests}
%check
make check
%endif

%ldconfig_scriptlets -n libtexpdf0
%ldconfig_scriptlets -n libtexpdf-devel

%files
%license %{_datadir}/licenses/sile/LICENSE
%doc %{_datadir}/doc/sile/*
%dir %{_datadir}/doc/sile
%dir %{_datadir}/licenses/sile
%{_bindir}/sile
%{_datadir}/sile
%{_libdir}/sile
%{_mandir}/man1/sile.1.gz

%files -n libtexpdf0
%license LICENSE
%{_libdir}/libtexpdf.so.0*

%files -n libtexpdf-devel
%{_includedir}/libtexpdf
%{_libdir}/libtexpdf.so

%changelog
