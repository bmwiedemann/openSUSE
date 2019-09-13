# Specification for package metamath
#
# Copyright (c) 2016-2019 by Aaron Puchert
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Do not build LaTeX docs on SLES.
%if 0%{?is_opensuse}
%bcond_without  latex_doc
%else
%bcond_with     latex_doc
%endif

%define book_version 20190407

# Global definitions
Name:           metamath
Version:        0.177
Release:        0
Summary:        Formal proof verifier and proof assistant
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://us.metamath.org/
# Source links aren't stable. (They always points to the latest version.)
# http://us.metamath.org/downloads/metamath.tar.bz2
Source0:        %{name}.tar.bz2
# http://us.metamath.org/latex/metamath.tex
Source1:        %{name}.tex
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
%if %{with latex_doc}
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-anysize
BuildRequires:  texlive-bibtex-bin
BuildRequires:  texlive-breqn
BuildRequires:  texlive-hyperref
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makecell
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-microtype
BuildRequires:  texlive-needspace
BuildRequires:  texlive-tabu
Recommends:     %{name}-book = %{book_version}-%{release}
%endif
Recommends:     %{name}-data = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Metamath language is a language to write theorems and formal proofs for
them. The Metamath program can parse files in the Metamath language and verify
the proofs. You can find examples of theories developed in Metamath on the
website.

%package book
Summary:        The Metamath book
Version:        %{book_version}
License:        CC0-1.0
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{VERSION}-%{release}
BuildArch:      noarch

%description book
The Metamath book, written by Norman Megill with extensive revisions by
David A. Wheeler, provides an in-depth understanding of the Metamath language
and program. The first part of the book also includes an easy-to-read informal
discussion of abstract mathematics and computers, with references to other
proof verifiers and automated theorem provers.

%package data
Summary:        Data base files for %{name}
License:        CC0-1.0 AND GPL-2.0-or-later
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{VERSION}-%{release}
BuildArch:      noarch

%description data
This package contains Metamath data base files for several formal theories.
* set.mm – Logic and set theory database (see Ch. 3 of the Metamath book).
* nf.mm – Logic and set theory database for Quine's New Foundations set theory.
* hol.mm – Higher order logic (simple type theory) database.
* iset.mm – Intuitionistic logic database.
* ql.mm – Quantum logic database.
* demo0.mm – Demo of simple formal system (see Ch. 2 of the Metamath book).
* miu.mm – Hofstadter's MIU-system (see Appendix D of the Metamath book).
* big-unifier.mm – A unification stress test (see comments in the file).
* peano.mm – A presentation of Peano arithmetic by Robert Solovay.

%prep
%setup -q -n %{name}

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

# Build documentation as outlined in the LaTeX file.
%if %{with latex_doc}
touch metamath.ind
touch special-settings.sty
pdflatex %{SOURCE1}
pdflatex %{SOURCE1}
bibtex metamath
makeindex metamath.ind
pdflatex %{SOURCE1}
pdflatex %{SOURCE1}
%endif

%install
%make_install
%if %{with latex_doc}
install -Dm0644 metamath.pdf %{buildroot}%{_datadir}/%{name}/%{name}.pdf
%endif

%files
%license LICENSE.TXT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%if %{with latex_doc}
%files book
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.pdf
%endif

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.mm

%changelog
