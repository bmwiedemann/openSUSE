#
# spec file for package chezscheme
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


%define chezscheme ChezScheme
%define srcext     tar.zst

Name:           chezscheme
Summary:        A superset of the R6RS Scheme language
Version:        10.1.0
Release:        0
License:        Apache-2.0 AND BSD-2-Clause AND GPL-2.0-only AND Zlib AND SUSE-GPL-2.0-with-linking-exception
Group:          Development/Languages/Scheme
Source0:        %{chezscheme}-v%{version}.%{srcext}
URL:            https://cisco.github.io/ChezScheme/
BuildRequires:  fdupes
BuildRequires:  libX11-devel
BuildRequires:  liblz4-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel

%description
Chez Scheme is an implementation of the Revised6 Report on Scheme (R6RS) with numerous language and programming environment extensions.

%package petite
Summary:        Faster interpret version of ChezScheme
Group:          Development/Languages/Scheme

%description petite
Petite Chez Scheme is a complete Scheme system that is fully compatible with Chez Scheme but uses a fast interpreter in place of the compiler.

%prep
cd %{_builddir}
%setup -q -n %{chezscheme}-v%{version}
# use system libs
rm -r lz4 zlib

# Patch the Makefile
# sed -i 's/-Werror//' ./c/Mf-ta6le
# Patch the expeditor.c
sed -i 's/xlocale\.h/locale.h/' ./c/expeditor.c

%build
# from https://src.fedoraproject.org/rpms/chez-scheme/blob/rawhide/f/chez-scheme.spec
case %{_arch} in
     x86_64) MACHINE=-m=ta6le ;;
     i686) MACHINE=-m=ti3le ;;
     aarch64) MACHINE=-m=tarm64le ;;
     riscv64) MACHINE=-m=trv64le ;;
     *) MACHINE=--pb ;;
esac

./configure --installprefix=/usr  --temproot=%{buildroot} --threads $MACHINE  ZLIB=-lz LZ4=-llz4

%make_build

%install
%makeinstall

# de-duplicate scheme-script.boot and scheme.boot
br_s_script=$(find %{buildroot} -name scheme-script.boot)
s_boot=$(cd %{buildroot} && find usr -name scheme.boot)
rm "$br_s_script"
ln -s "/$s_boot" "$br_s_script"

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/scheme.1*
%{_bindir}/scheme
%{_bindir}/scheme-script
/usr/lib/csv%{version}

%files petite
%defattr(-,root,root)
%{_bindir}/petite
%doc %{_mandir}/man1/petite.1*

%changelog
