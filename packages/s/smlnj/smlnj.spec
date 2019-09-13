#
# spec file for package smlnj
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           smlnj
Version:        110.81
Release:        0
Summary:        Standard ML of New Jersey
License:        BSD-3-Clause
Group:          Development/Languages/Other
Url:            http://www.smlnj.org/
Source:         smlnj-%{version}.tar.bz2
Source1:        pack_new_version.sh
Patch1:         MLRISC.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} ppc

%description
SML/NJ is an interactive compiler for the Standard ML Programming
Language (1997 Revision).

%prep
%setup -q
tar -xzf config.tgz

mkdir base
cd base
tar -xzf ../runtime.tgz
tar -xzf ../MLRISC.tgz
cd MLRISC

%patch1

%build
CFLAGS="%{optflags}" config/install.sh

%install
mkdir -p %{buildroot}%{_libdir}/smlnj
cp -a bin lib %{buildroot}%{_libdir}/smlnj
mkdir -p %{buildroot}%{_bindir}
for f in %{buildroot}%{_libdir}/smlnj/bin/*; do
  sed -i -e "s,$PWD,%{_libdir}/smlnj," $f
  ln -sf ${f#%{buildroot}} %{buildroot}%{_bindir}
done
for f in %{buildroot}%{_libdir}/smlnj/bin/.*-sml; do
  sed -i -e "s,$PWD,%{_libdir}/smlnj," $f
done

%files
%defattr(-, root, root)
%doc %{version}-* HISTORY
%{_bindir}/*
%{_libdir}/smlnj

%changelog
