#
# spec file for package metamath
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Aaron Puchert
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


# Do not build LaTeX docs on SLES.
# Also don't build on Tumbleweed. Seems that tabu broke with TeXlive 2022.
# https://github.com/metamath/metamath-book/issues/235.
%if 0%{?is_opensuse} && 0%{?suse_version} <= 1500
%bcond_without  latex_doc
%else
%bcond_with     latex_doc
%endif

%define book_version 20190602
%define book_tag second_edition

# Global definitions
Name:           metamath
Version:        0.198
Release:        0
Summary:        Formal proof verifier and proof assistant
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://us.metamath.org/
Source0:        https://github.com/metamath/metamath-exe/archive/refs/tags/v%{version}.tar.gz#/metamath-%{version}.tar.gz
Source1:        https://github.com/metamath/metamath-book/archive/refs/tags/%{book_tag}.tar.gz#/metamath-book-%{book_version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
%if %{with latex_doc}
BuildRequires:  texlive-bibtex-bin
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(anysize.sty)
BuildRequires:  tex(breqn.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(longtable.sty)
BuildRequires:  tex(makecell.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabu.sty)
Suggests:       %{name}-book = %{book_version}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Metamath language is a language to write theorems and formal proofs for
them. The Metamath program can parse files in the Metamath language and verify
the proofs. You can find examples of theories developed in Metamath on the
website.

%package book
Summary:        The Metamath book
License:        CC0-1.0
Group:          Documentation/Other
Version:        %{book_version}
Release:        0
Recommends:     %{name} = %{VERSION}
BuildArch:      noarch

%description book
The Metamath book, written by Norman Megill with extensive revisions by
David A. Wheeler, provides an in-depth understanding of the Metamath language
and program. The first part of the book also includes an easy-to-read informal
discussion of abstract mathematics and computers, with references to other
proof verifiers and automated theorem provers.

%prep
%setup -q -a 1 -n metamath-exe-%{VERSION}/

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

# Build documentation as outlined in the LaTeX file.
%if %{with latex_doc}
pushd metamath-book-%{book_tag}
echo "Package amsmath Warning: Foreign command \\atop;
LaTeX Font Warning: Font shape \`TS1/cmtt/bx/n' undefined" >>allowed-errors
./generate-pdf
popd
%endif

%install
%make_install
%if %{with latex_doc}
install -Dm0644 metamath-book-%{book_tag}/metamath.pdf \
    %{buildroot}%{_datadir}/%{name}/%{name}.pdf
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

%changelog
