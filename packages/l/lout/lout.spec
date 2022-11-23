#
# spec file for package lout
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


Name:           lout
Version:        3.42.2
Release:        0
Summary:        A document formatting system
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PS
URL:            https://savannah.nongnu.org/projects/lout/
Source0:        https://github.com/william8000/lout/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  ghostscript

%description
Lout is a document formatting system. The system reads a high-level
description of a document similar in style to LaTeX and produces a
PostScript file. Plain text output is also available, PDF output is
limited but working (e.g. no graphics). Either of these may be
fed to a printer. Lout is offered in multiple languages.

%prep
%setup -q
find . -name README -exec chmod 0644 '{}' \;

%build
make COPTS="%{optflags}" \
     BINDIR=%{_bindir} \
     LOUTLIBDIR=%{_datadir}/%{name} \
     LOUTDOCDIR=%{_datadir}/%{name}/doc \
     MANDIR=%{_mandir}/man1 \
     prg2lout lout

function render_docs {
    subdir=$1
    pdf_file=$2
    passes=$3

    curdir=$(pwd)
    pushd doc/$subdir

    # We need to set the PATH variable here, because lout eventually exec's
    #   prg2lout.  In order for lout to find the latter, we have to set the
    #   PATH.
    # We also need to tell lout where to find its files, since we haven't
    #   installed them in their final location under %%{_datadir}/lout/ yet.
    PATH=$curdir lout \
       -I $curdir/include \
       -D $curdir/data \
       -F $curdir/font \
       -H $curdir/hyph \
       -C $curdir/maps \
       -r${passes} all > outfile.ps
    # Note that the above clobbers the prebuilt file outfile.ps that is
    # included in Lout's source tarball.
    ps2pdf outfile.ps ../${pdf_file}
    rm *.li *.ld outfile.ps
    popd
}

render_docs design design.pdf       3
render_docs expert expert-guide.pdf 4
render_docs slides slides.pdf       2
render_docs user   user-guide.pdf   6

%install
mkdir -p %{buildroot}%{_bindir}
make BINDIR=%{buildroot}%{_bindir} \
     LOUTLIBDIR=%{buildroot}%{_datadir}/%{name} \
     LOUTDOCDIR=%{buildroot}%{_datadir}/%{name}/doc \
     MANDIR=%{buildroot}%{_mandir}/man1 \
     install installman installdoc
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc README READMEPDF
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*.1%{?ext_man}

%changelog
