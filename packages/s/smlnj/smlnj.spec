#
# spec file for package smlnj
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


Name:           smlnj
Version:        110.99.3
Release:        0
Summary:        Standard ML of New Jersey
License:        BSD-3-Clause
Group:          Development/Languages/Other
URL:            https://www.smlnj.org/
Source:         smlnj-%{version}.tar.xz
Source1:        pack_new_version.sh
Source2:        urlgetter.sh
Source3:        smlnj-rpmlintrc
Patch1:         MLRISC.diff
Patch2:         smlnj-kernel-6.x.patch
BuildRequires:  gcc-c++
ExclusiveArch:  %{ix86} x86_64 ppc

%description
SML/NJ is an interactive compiler for the Standard ML Programming
Language (1997 Revision).

%prep
%setup -q
tar -xzf config.tgz
# place urlgetter
cp %{SOURCE2} .
%patch2 -p1

mkdir base
cd base
tar -xzf ../runtime.tgz
tar -xzf ../MLRISC.tgz
%patch1

%build
# remove reference to remote d/l
echo "SRCARCHIVEURL=/" > ./config/srcarchiveurl
export BUILDDIR="%{_builddir}/%{name}-%{version}"
export URLGETTER="%{_sourcedir}/urlgetter.sh"

CFLAGS="%{optflags}" config/install.sh -default 64

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

# ship required env var
# todo: move this to the build, if possible
# especially as there is a conflict
# if you installed both 32-bit and 64-bit archs
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export SMLNJ_HOME=%{_libdir}/smlnj" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

%files
%doc %{version}-*
%{_bindir}/ml-antlr
%{_bindir}/ml-build
%{_bindir}/ml-burg
%{_bindir}/ml-lex
%{_bindir}/ml-makedepend
%ifarch %{ix86}
%{_bindir}/ml-nlffigen
%endif
%{_bindir}/ml-ulex
%{_bindir}/ml-yacc
%{_bindir}/sml
%{_libdir}/smlnj
# todo: cook it into the build, if possible
%config %{_sysconfdir}/profile.d/%{name}.sh

%changelog
