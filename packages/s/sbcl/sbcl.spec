#
# spec file for package sbcl
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


# Use --with-bootstrap to build sbcl using the upstream binaries
%bcond_with bootstrap

Name:           sbcl
#!BuildIgnore:  gcc-PIE
Version:        2.5.6
Release:        0
Summary:        Steel Bank Common Lisp
License:        BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Languages/Other
URL:            http://www.sbcl.org/
Source:         http://downloads.sourceforge.net/project/sbcl/sbcl/%version/%{name}-%{version}-source.tar.bz2
Source1:        README.openSUSE
Source2:        sbclrc.sample
Source3:        customize-target-features.lisp
%if %{with bootstrap}
Source20:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.3-x86-linux-binary.tar.bz2
Source21:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.7-x86-64-linux-binary.tar.bz2
Source22:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.7-powerpc-linux-binary.tar.bz2
Source23:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.7-armel-linux-binary.tar.bz2
Source24:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.11-armhf-linux-binary.tar.bz2
Source25:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.2-arm64-linux-binary.tar.bz2
Source26:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.5.8-ppc64le-linux-binary.tar.bz2
%ifarch %{ix86}
%define sbcl_arch x86
%define sbcl_bootstrap_src 20
%endif
%ifarch x86_64
%define sbcl_arch x86-64
%define sbcl_bootstrap_src 21
%endif
%ifarch ppc
%define sbcl_arch ppc
%define sbcl_bootstrap_src 22
%endif
%ifarch armv5tel
%define sbcl_arch arm
%define sbcl_bootstrap_src 23
%endif
%ifarch armv6hl armv7hl
%define sbcl_arch arm
%define sbcl_bootstrap_src 24
%endif
%ifarch aarch64
%define sbcl_arch arm64
%define sbcl_bootstrap_src 25
%endif
%ifarch ppc64le
%define sbcl_arch ppc64
%define sbcl_bootstrap_src 26
%endif
%ifarch ppc64
%define sbcl_arch ppc64
%define with_clisp 1
%endif
%ifarch riscv64
%define sbcl_arch riscv64
%define with_clisp 1
%endif
%if 0%{?with_clisp}
BuildRequires:  clisp
%endif
%else
BuildRequires:  sbcl
%endif
BuildRequires:  ctags
BuildRequires:  ghostscript
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version:1}
BuildRequires:  netcfg
BuildRequires:  texinfo
%else
BuildRequires:  texinfo-tex
%endif
%if 0%{?suse_version:1} && 0%{?suse_version} <= 1220
BuildRequires:  texlive
%else
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
%endif
# PATCH-FIX-OPENSUSE install README.openSUSE and sbclrc.sample
Patch0:         sbcl-1.1.2-install.patch
# PATCH-FIX-UPSTREAM Remove obsolete qemu workarounds
Patch1:         remove-qemu-workarounds.patch
ExcludeArch:    s390x
Requires:       sbcl-bin

%description
Steel Bank Common Lisp (SBCL) is a high performance Common Lisp
compiler.
In addition to the compiler and runtime system for ANSI Common Lisp, it
provides an interactive environment including a debugger, a statistical
profiler, a code coverage tool, and many other extensions.

%package bin
Summary:        The Steel Bank Common Lisp loader program

%description bin
This package contains just the SBCL loader stub.

%prep
%if %{with bootstrap}
%if !0%{?with_clisp}
tar -xf %{S:%{sbcl_bootstrap_src}}
ln -s "$(basename -- %{S:%{sbcl_bootstrap_src}} -binary.tar.bz2)" BOOTSTRAP
%endif
%endif

%autosetup -p1
cp %{S:1} .
cp %{S:2} .
cp %{S:3} .

sed -i -e "s|\"%version\"|\"%version-%release-%_vendor\"|" version.lisp-expr

%build
export CFLAGS="%optflags -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%if %{with bootstrap}
%{?sbcl_arch:export SBCL_ARCH=%{sbcl_arch}}
%if 0%{?with_clisp}
 %_buildshell make.sh --xc-host='env LC_ALL=C.utf8 clisp -q -norc' --prefix=%{_prefix}
%else
 %_buildshell ./make.sh \
  --prefix=%{_prefix} \
  --xc-host="$(readlink -f ../BOOTSTRAP/run-sbcl.sh)"
%endif
%else
%_buildshell make.sh --xc-host="sbcl --disable-debugger --no-sysinit --no-userinit"  --prefix=%{_prefix}
%endif
cd doc/manual && make

%install
INSTALL_ROOT=%{buildroot}/%{_prefix} %_buildshell install.sh
if test %{_docdir} != %{_prefix}/share/doc ;then
    mkdir -p %{buildroot}/%{_docdir}
    mv %{buildroot}/%{_prefix}/share/doc/sbcl %{buildroot}/%{_docdir}/
fi
## Unpackaged files
rm -f  %{buildroot}%{_infodir}/dir
# SCM crud, test files from %%check, dangling texinfo files
find %{buildroot} "(" \
	-name CVS -o -name .cvsignore -o \
	-name .gitignore -o -name a.out -o \
	-name test-passed -o -name test-output -o \
	-name "*.texinfo" -o -name makefile ")" \
	-exec rm -Rf {} +

# How to make that info stuff portable?
%if 0%{?install_info:1} > 0

%post
%install_info --info-dir=%{_infodir} %{_infodir}/asdf.info.*
%install_info --info-dir=%{_infodir} %{_infodir}/sbcl.info.*

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/asdf.info.*
%install_info_delete --info-dir=%{_infodir} %{_infodir}/sbcl.info.*
%endif

%files
%doc %{_docdir}/%{name}
%doc %{_mandir}/man1/sbcl.1*
%doc %{_infodir}/asdf.info*
%doc %{_infodir}/sbcl.info*
%dir %{_prefix}/lib/sbcl/
%{_prefix}/lib/sbcl/sbcl.core
%{_prefix}/lib/sbcl/sbcl.mk
%{_prefix}/lib/sbcl/contrib/

%files bin
%{_bindir}/sbcl

%changelog
