#
# spec file for package smlnj
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2026.2
Release:        0
Summary:        Standard ML of New Jersey
License:        BSD-3-Clause
URL:            https://www.smlnj.org/
# Upstream ships one source tarball per Unix arch; contents are identical
# except for the bundled boot.ARCH-unix.tgz bootstrap heap
Source0:        https://smlnj.org/dist/working/%{version}/smlnj-amd64-unix-%{version}.tgz
Source1:        https://smlnj.org/dist/working/%{version}/smlnj-arm64-unix-%{version}.tgz
Source2:        smlnj-rpmlintrc
# keep package names: --perl explodes autoconf/automake into perl(...) providers
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
# development line supports 64-bit AMD64/AArch64 Unix only
ExclusiveArch:  x86_64 aarch64

%description
SML/NJ is an interactive compiler for the Standard ML Programming
Language (1997 Revision).

%prep
%ifarch x86_64
%setup -q -T -b 0 -n smlnj
%endif
%ifarch aarch64
%setup -q -T -b 1 -n smlnj
%endif

%build
# build.sh builds and installs in one go (bundled LLVM, runtime, heap,
# libraries); stage under BUILD, rpm wipes BUILDROOT before the install phase
bash build.sh -install $PWD/stage-smlnj

%install
mkdir -p %{buildroot}%{_libdir}
cp -a stage-smlnj %{buildroot}%{_libdir}/smlnj
# LLVM static libs/headers are linked into run.* already; drop the rest,
# keeping libHeap2Obj.a (heap2exec input)
rm -f %{buildroot}%{_libdir}/smlnj/bin/{llvm-config,llvm-tblgen,llc,llvm-libtool-darwin}
rm -f %{buildroot}%{_libdir}/smlnj/lib/libLLVM*.a %{buildroot}%{_libdir}/smlnj/lib/libCFGCodeGen.a
rm -rf %{buildroot}%{_libdir}/smlnj/include %{buildroot}%{_libdir}/smlnj/lib/cmake
# driver scripts bake the staging path; rewrite it to the final libdir path
for f in %{buildroot}%{_libdir}/smlnj/bin/* %{buildroot}%{_libdir}/smlnj/bin/.*-sml; do
  [ -f "$f" ] && sed -i -e "s,$PWD/stage-smlnj,%{_libdir}/smlnj," "$f"
done
mkdir -p %{buildroot}%{_bindir}
for f in %{buildroot}%{_libdir}/smlnj/bin/*; do
  # llvm-config is a build-time tool only; keep it out of PATH
  [ "${f##*/}" = "llvm-config" ] && continue
  [ -f "$f" ] && ln -sf %{_libdir}/smlnj/bin/${f##*/} %{buildroot}%{_bindir}/${f##*/}
done

# ship required env var
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export SMLNJ_HOME=%{_libdir}/smlnj" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

%check
export SMLNJ_HOME=%{buildroot}%{_libdir}/smlnj
export CM_PATHCONFIG=%{buildroot}%{_libdir}/smlnj/lib/pathconfig
# @SMLversion is answered by the driver script itself; evaluate through the
# heap instead so the check exercises heap load, CM and the Basis library
HEAP=$(echo %{buildroot}%{_libdir}/smlnj/bin/.heap/sml.*-linux)
RUN=$(echo %{buildroot}%{_libdir}/smlnj/bin/.run/run.*-linux)
echo 'val _ = print (Int.toString (foldl (op+) 0 (List.tabulate (100, fn x => x * x))) ^ "\n");' | \
  $RUN @SMLcmdname=sml @SMLload=$HEAP @SMLalloc=1M | grep -q 328350

%files
%license LICENSE
%doc README.md NOTES.md CONTRIBUTING.md
%{_bindir}/asdlgen
%{_bindir}/heap2exec
%{_bindir}/heap2obj
%{_bindir}/ml-antlr
%{_bindir}/ml-build
%{_bindir}/ml-burg
%{_bindir}/ml-makedepend
%{_bindir}/ml-ulex
%{_bindir}/ml-yacc
%{_bindir}/print-cfg
%{_bindir}/sml
%{_libdir}/smlnj
%config %{_sysconfdir}/profile.d/%{name}.sh

%changelog
