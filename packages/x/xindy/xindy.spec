#
# spec file for package xindy
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


Name:           xindy
Version:        2.5.1
Release:        0
Summary:        Index generator for structured documents like LaTeX or SGML
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://xindy.org/
#DL-URL:	http://ctan.org/tex-archive/indexing/xindy/
Source:         ftp://ctan.org/tex-archive/indexing/xindy/base/xindy-2.5.1.tar.gz
Patch1:         fix-FHS.dpatch.diff
Patch2:         help-option.dpatch.diff
Patch3:         1000_Unescaped-left-brace-deprecated-in-regexps.diff
BuildRequires:  automake
BuildRequires:  clisp
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-latex
BuildRequires:  texlive-lh
BuildRequires:  texlive-metafont
BuildRequires:  tex(pdftex.map)
BuildRequires:  tex(t2aenc.def)
%if %suse_version > 1230
BuildRequires:  tex(lgrcmr.fd)
BuildRequires:  tex(lgrenc.def)
%endif
# Need this at runtime for indexing to work correctly:
%requires_eq clisp
Requires:       xindy-rules = %version
# clisp is not present
ExcludeArch:    armv4l ppc64 ppc64le
Obsoletes:      xindy-doc < %version-%release
Provides:       xindy-doc = %version-%release

%description
xindy is an index processor that can be used to generate book-like
indexes for arbitrary document-preparation systems. This includes
systems such as TeX and LaTeX, the roff-family, SGML/XML-based
systems (e.g. HTML) that process some kind of text and generate
indexing information. The kernel system is not fixed to any specific
system, but can be configured to work together with such systems.

In comparison to other index processors xindy has several powerful
features that make it an ideal framework for describing and
generating complex indices, addressing especially international
indexing.

%package rules
Summary:        Rule files for Xindy
Group:          Productivity/Publishing/TeX
BuildArch:      noarch

%description rules
xindy is an index processor that can be used to generate book-like
indexes for arbitrary document-preparation systems.

This package contains the rule files (the knowledge base) of xindy.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --docdir=%_docdir/%name
# not safe for -j
%make_build -j1

%install
%make_install
rm -f "%buildroot/%_prefix/VERSION"

%files
%license COPYING
%_bindir/*
%_libdir/%name
%doc %_mandir/man*/*

%files rules
%_datadir/%name

%changelog
