#
# spec file for package yodl
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yodl
Version:        4.02.01
Release:        0
Summary:        Yet One-other Document Language
License:        GPL-3.0-only
Group:          Development/Tools/Doc Generators
Url:            https://fbb-git.gitlab.io/yodl/
Source:         https://gitlab.com/fbb-git/yodl/-/archive/%{version}/yodl-%{version}.tar.gz
Patch0:         %{name}-doc-packages.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  grep
BuildRequires:  icmake
BuildRequires:  sed
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  tex(a4.sty)
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(makecell.sty)

%description
YODL is a package that consists of programs, some shell scripts, and
auxiliary "lib" files for which hold macro files. The whole purpose of
the package is to provide a simple-to-use and extensible document
language that can be used to convert documents in the YODL format to a
variety of other formats. In this purpose, YODL somewhat resembles
generic markup languages.

%prep
%setup -q
%patch0

sed -i s/"#define COPT.*"/"#define COPT \"%{optflags}\""/ ./yodl/build
# remove clearing of display during build, since it breaks OBS builds for s390x
%ifarch s390x
sed -i '/.*CLS.*/d' yodl/verbinsert/icmconf
%endif

%build
pushd yodl
./build programs
./build macros
./build manual
./build man
popd

%install
pushd yodl
cp -a tmp/install/* %{buildroot}
chmod +x %{buildroot}%{_bindir}/yodl2whatever
(cd %{buildroot}%{_bindir}; for i in html latex man ms sgml txt xml; do ln -s yodl2whatever yodl2$i; done)
popd

rm %{buildroot}%{_docdir}/%{name}/yodl.dvi
rm %{buildroot}%{_docdir}/%{name}/yodl.latex
rm %{buildroot}%{_docdir}/%{name}/yodl.ps
rm %{buildroot}%{_docdir}/%{name}/yodl.txt

%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc yodl/AUTHORS.txt yodl/changelog yodl/README.* yodl/CHANGES
%doc %{_docdir}/%{name}/
%{_bindir}/yodl
%{_bindir}/yodl2html
%{_bindir}/yodl2latex
%{_bindir}/yodl2man
%{_bindir}/yodl2ms
%{_bindir}/yodl2sgml
%{_bindir}/yodl2txt
%{_bindir}/yodl2whatever
%{_bindir}/yodl2xml
%{_bindir}/yodlpost
%{_bindir}/yodlstriproff
%{_bindir}/yodlverbinsert
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/yodl.1%{ext_man}
%{_mandir}/man1/yodlconverters.1%{ext_man}
%{_mandir}/man1/yodlpost.1%{ext_man}
%{_mandir}/man1/yodlstriproff.1%{ext_man}
%{_mandir}/man1/yodlverbinsert.1%{ext_man}
%{_mandir}/man7/yodlbuiltins.7%{ext_man}
%{_mandir}/man7/yodlletter.7%{ext_man}
%{_mandir}/man7/yodlmacros.7%{ext_man}
%{_mandir}/man7/yodlmanpage.7%{ext_man}
%{_mandir}/man7/yodltables.7%{ext_man}

%changelog
