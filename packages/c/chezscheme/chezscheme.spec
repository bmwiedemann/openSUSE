#
# spec file for package chezscheme
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


%define chezscheme ChezScheme

Name:           chezscheme
Summary:        A superset of the R6RS Scheme language
Version:        10.1.0
Release:        0
License:        Apache-2.0 AND BSD-2-Clause AND GPL-2.0-only AND Zlib AND SUSE-GPL-2.0-with-linking-exception
Group:          Development/Languages/Scheme
Source0:        %{chezscheme}-%{version}.tar.gz
Source1:        lz4-5ff839680134437dbf4678f3d0c7b371d84f4964.zip
Source2:        nanopass-framework-scheme-68990d02573faa555ee42919d5809de03f1268a0.zip
Source3:        stex-5e4f0ca67bac448e19a24c09f12fc16d24cd6b6d.zip
Source4:        zlib-51b7f2abdade71cd9bb0e7a373ef2610ec6f9daf.zip
Source5:        zuo-ebdc0451c39c70ce88b3b6ab9ba2b8e389ec519a.zip
ExclusiveArch:  x86_64
URL:            https://cisco.github.io/ChezScheme/
BuildRequires:  fdupes
BuildRequires:  libX11-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  unzip

%description
Chez Scheme is an implementation of the Revised6 Report on Scheme (R6RS) with numerous language and programming environment extensions.

%package petite
Summary:        Faster interpret version of ChezScheme
Group:          Development/Languages/Scheme

%description petite
Petite Chez Scheme is a complete Scheme system that is fully compatible with Chez Scheme but uses a fast interpreter in place of the compiler.

%prep
cd %{_builddir}
%setup -q -n %{chezscheme}-%{version}
SUBMODULE_ARRAY=(%{S:1} %{S:2} %{S:3} %{S:4} %{S:5})
for submodule in "${SUBMODULE_ARRAY[@]}"; do
    export submodule_filename=$(basename ${submodule})
    submodule_name=$(perl -e '$submodule = $ENV{"submodule_filename"}; $submodule =~ s/(.*?)-(.*)$/$1/; print "$submodule\n";')
    rmdir ${submodule_name}
    unzip ${submodule}
    mv ${submodule_filename%.zip} ${submodule_name}
done
# Patch the Makefile
# sed -i 's/-Werror//' ./c/Mf-ta6le
# Patch the expeditor.c
sed -i 's/xlocale\.h/locale.h/' ./c/expeditor.c

%build

./configure --installprefix=/usr  --temproot=%{buildroot} --threads
%make_build

%install
%makeinstall
# Fix incorrect symlink
rm %{buildroot}/usr/lib/csv%{version}/ta6le/scheme-script.boot
ln -s "/usr/lib/csv%{version}/ta6le/scheme.boot" "%{buildroot}/usr/lib/csv%{version}/ta6le/scheme-script.boot"
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
