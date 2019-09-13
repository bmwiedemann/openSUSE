#
# spec file for package sbcl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Use --without-bootstrap to build sbcl with an existing sbcl package
%bcond_without bootstrap

Name:           sbcl
#!BuildIgnore:  gcc-PIE
Version:        1.5.4
Release:        0
Summary:        Steel Bank Common Lisp
License:        SUSE-Public-Domain AND BSD-3-Clause
Group:          Development/Languages/Other
Url:            http://www.sbcl.org/
Source:         http://downloads.sourceforge.net/project/sbcl/sbcl/%version/%{name}-%{version}-source.tar.bz2
Source1:        README.openSUSE
Source2:        sbclrc.sample
Source3:        customize-target-features.lisp
%if %{with bootstrap}
Source20:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.3-x86-linux-binary.tar.bz2
Source21:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.7-x86-64-linux-binary.tar.bz2
Source22:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.7-powerpc-linux-binary.tar.bz2
Source23:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.7-armel-linux-binary.tar.bz2
Source24:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.3.12-armhf-linux-binary.tar.bz2
Source25:       http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.2-arm64-linux-binary.tar.bz2
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
###BuildRequires:  clisp
%else
BuildRequires:  sbcl
%endif
BuildRequires:  ctags
BuildRequires:  ghostscript
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
# PATCH-FIX-OPENSUSE  disable localport bsd sockets tests broken in kvm builds for some toganm@opensuse.org
Patch1:         disable-localport-bsd-sockets-test.patch
# PATCH-FIX-OPENSUSE  fix some unsafe tests for our build hosts
Patch2:         fix-tests.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    ppc64 ppc64le

%description
Steel Bank Common Lisp (SBCL) is a high performance Common Lisp
compiler. It is open source / free software, with a permissive license.
In addition to the compiler and runtime system for ANSI Common Lisp, it
provides an interactive environment including a debugger, a statistical
profiler, a code coverage tool, and many other extensions.

%prep
%if %{with bootstrap}
tar -xf %{S:%{sbcl_bootstrap_src}}
ln -s "$(basename -- %{S:%{sbcl_bootstrap_src}} -binary.tar.bz2)" BOOTSTRAP
%endif
%setup -q
%patch0 -p1 -b install
%patch1 -p1 -b sockets
%patch2

cp %{S:1} .
cp %{S:2} .
cp %{S:3} .

sed -i -e "s|\"%version\"|\"%version-%release-%_vendor\"|" version.lisp-expr

%build
CFLAGS="%optflags"
%if %{with bootstrap}
%{?sbcl_arch:export SBCL_ARCH=%{sbcl_arch}}
 %_buildshell ./make.sh \
  --prefix=%{_prefix} \
  --xc-host="$(readlink -f ../BOOTSTRAP/run-sbcl.sh)"
###%_buildshell make.sh --xc-host='clisp -q -norc' --prefix=%{_prefix} 
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
# CVS crud
find %{buildroot} -name CVS -type d | xargs rm -rf
find %{buildroot} -name .cvsignore | xargs rm -f
find %{buildroot} -name .gitignore | xargs rm -f
# remove the a.out files
find %{buildroot} -name a\.out | xargs rm -f
# 'test-passed' files from %%check
find %{buildroot} -name 'test-passed' | xargs rm -vf
find %{buildroot} -name 'test-output' -type d | xargs rm -rf

# remove dangling texinfo files
find %{buildroot} -name *\.texinfo | xargs rm -f
# remove Makefiles
find %{buildroot} -name Makefile | xargs rm -f

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
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}
%doc %{_mandir}/man1/sbcl.1*
%doc %{_infodir}/asdf.info*
%doc %{_infodir}/sbcl.info*
%{_bindir}/sbcl
%dir %{_prefix}/lib/sbcl/
%{_prefix}/lib/sbcl/sbcl.core
%{_prefix}/lib/sbcl/sbcl.mk
%{_prefix}/lib/sbcl/contrib/

%changelog
