#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}

%if "%flavor" == "base"
%define bootstrap  1
%define base       -%{flavor}%nil
%else
%define bootstrap  0
%define base       %nil
%endif
%define scshcommit 114432435e4eadd54334df6b37fcae505079b49f
%define scshshort  1144324
%define scshver    0.7
%define rxcommit   dd9037f6f9ea01019390614f6b126b7dd293798d
%define rxshort    dd9037f
%define scheme     1.9.2

Name:           scsh%{base}
Version:        %{scshver}+git%{scshcommit}
Release:        0
Summary:        A Unix shell embedded within Scheme
License:        BSD-3-Clause
Group:          System/Shells
URL:            https://scsh.net
Source0:        https://github.com/scheme/scsh/archive/%{scshcommit}/scsh-%{scshshort}.tar.gz
Source1:        https://github.com/scheme/rx/archive/%{rxcommit}/rx-%{rxshort}.tar.gz
Source2:        scsh-install-lib-1.3.0.tar.gz
Patch0:         declaration.patch
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?bootstrap} == 0
BuildRequires:  ca-certificates
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-latexconfig
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(article.cls)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(hyphenat.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(mathabx.map)
BuildRequires:  tex(mathabx.sty)
BuildRequires:  tex(newtxmath.sty)
BuildRequires:  tex(pdftex.map)
BuildRequires:  tex(ptmr8t.tfm)
BuildRequires:  tex(relsize.sty)
BuildRequires:  tex(t1ptm.fd)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(txfonts.sty)
BuildRequires:  tex(wasyb10.tfm)
BuildRequires:  tex(wasysym.sty)
Requires:       scsh-base = %version
BuildRequires:  scsh-base = %version
%endif
BuildRequires:  racket
BuildRequires:  scheme48 = %{scheme}
BuildRequires:  scheme48-devel = %{scheme}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description
Scsh is a Unix shell embedded in Scheme. It allows the user to write
commands in a language within Scheme that follows the Unix way, but
also allows to specify more complex commands with the elegance of
Scheme.

%prep
%setup -q -n scsh-%{scshcommit}
rm -rvf rx/
tar xf %{S:1}
ln -sf rx-%{rxcommit} rx
%patch0 -p0

%build
autoreconf
%add_optflags -Wall -Wno-return-type -fPIC -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=500

%configure --with-scheme48=%{_libdir}/scheme48-%{scheme}
%make_build   SCHEME48VM=%{_libdir}/scheme48-%{scheme}/scheme48vm

%if 0%{?bootstrap} == 0
cp -p rx/README README.rx
cp -p README.md README

pushd doc
    scribble --latex scsh.scribble
    pdflatex scsh.tex
    pdflatex scsh.tex
    pdflatex scsh.tex
popd
%endif

%install
PATH=%{buildroot}%{_bindir}:$PATH
export PATH
%if 0%{?bootstrap} > 0
make DESTDIR=%{buildroot} SCHEME48VM=%{_libdir}/scheme48-%{scheme}/scheme48vm enough dirs install-scsh
rm -rf %{buildroot}%{_bindir}
%else
make DESTDIR=%{buildroot} SCHEME48VM=%{_libdir}/scheme48-%{scheme}/scheme48vm install
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin
ln -sf %{_bindir}/scsh %{buildroot}/bin/scsh
%endif
rm -rf %{buildroot}%{_libdir}/scsh-%{scshver}/*.so
rm -rf %{buildroot}%{_datadir}/scsh-%{scshver}
%endif

%check
make test

%files
%defattr(-,root,root)
%if 0%{?bootstrap} > 0
%dir %{_libdir}/scsh-%{scshver}/
%{_libdir}/scsh-%{scshver}/*.so
%dir %{_datadir}/scsh-%{scshver}/
%{_datadir}/scsh-%{scshver}/*.scm
%else
%license COPYING
%doc README README.rx doc/scsh.pdf
%if 0%{?suse_version} < 1550
/bin/scsh
%endif
%{_bindir}/scsh
%{_libdir}/scsh-%{scshver}/*.image
%endif

%changelog
