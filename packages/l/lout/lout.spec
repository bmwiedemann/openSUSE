#
# spec file for package lout
#
# Copyright (c) 2020 SUSE LLC
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


%global makedocs 0
Name:           lout
Version:        3.40
Release:        1%{?dist}
Summary:        A document formatting system
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PS
URL:            http://savannah.nongnu.org/projects/lout/
Source0:        http://download.savannah.gnu.org/releases/lout/lout-%{version}.tar.gz
Patch0:         makefile.patch
# PATCH-FIX-UPSTREAM lout-3.40-cve.patch mcepl@suse.com
# from https://lists.nongnu.org/archive/html/lout-users/2020-10/msg00013.html
# Fix for bsc#1159713 and bsc#1159714 (CVE-2019-19918 and CVE-2019-19917)
Patch1:         lout-3.40-cve.patch
BuildRequires:  fdupes
BuildRequires:  ghostscript
%if !%{makedocs}
Source1:        design.pdf
Source2:        expert-guide.pdf
Source3:        user-guide.pdf
Source4:        slides.pdf
%endif

%description
Lout is a document formatting system. The system reads a high-level
description of a document similar in style to LaTeX and produces a
PostScript file. Plain text output is also available, PDF output is
limited but working (e.g. no graphics). Either of these may be
fed to a printer. Lout is offered in multiple languages.

%prep
%setup -q
%autopatch -p1

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

# For some reason, ps2pdf segfaults in koji.
%if %{makedocs}
render_docs design design.pdf       3
render_docs expert expert-guide.pdf 4
render_docs slides slides.pdf       2
render_docs user   user-guide.pdf   6
%else
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} doc/
%endif

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/doc
mkdir -p %{buildroot}/%{_mandir}/man1
make BINDIR=%{buildroot}%{_bindir} \
     LOUTLIBDIR=%{buildroot}%{_datadir}/%{name} \
     LOUTDOCDIR=%{buildroot}%{_datadir}/%{name}/doc \
     MANDIR=%{buildroot}%{_mandir}/man1 \
     install installman installdoc

# Looks like vim dump?
rm -rf %{buildroot}%{_datadir}/%{name}/doc/user/.pie_intr.swp

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc %attr(0644,-,-) README READMEPDF
%license COPYING
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
