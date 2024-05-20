#
# spec file for package lout
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


%define tarver  3.41
%define tardate 2023_06_19
Name:           lout
Version:        3.41.0
Release:        0
Summary:        A document formatting system
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PS
URL:            http://jeffreykingston.id.au/lout/
Source0:        http://jeffreykingston.id.au/lout/lout-%{tarver}.tar.gz
# PATCH-FIX-UPSTREAM opensuse-build.patch mcepl@suse.com
# Make package building in OpenSUSE OBS
Patch0:         opensuse-build.patch
# PATCH-FIX-UPSTREAM Fix-for-CVE-2019-19917-and-CVE-2019-19918.patch mcepl@suse.com
# Fix for CVE-2019-19918 and CVE-2019-19918
# Patch from https://lists.nongnu.org/archive/html/lout-users/2020-10/msg00013.html
Patch1:         fix-for-CVE-2019-19917-and-CVE-2019-19918.patch
# PATCH-FIX-UPSTREAM tblf-fix-typo-in-PaintBox-PDF-backend.patch mcepl@suse.com
# Patch from https://github.com/william8000/lout/commit/a8833f63f2b7.patch
# fix typo in @PaintBox PDF backend
Patch2:         tblf-fix-typo-in-PaintBox-PDF-backend.patch
# PATCH-FIX-UPSTREAM avoid-calling-catclose-with-an-invalid-argument.patch mcepl@suse.com
# Patch from https://github.com/william8000/lout/commit/5e7b8f9e7d44.patch
# avoid calling catclose with an invalid argument
Patch3:         avoid-calling-catclose-with-an-invalid-argument.patch
BuildRequires:  fdupes
BuildRequires:  ghostscript

%description
Lout is a document formatting system. The system reads a high-level
description of a document similar in style to LaTeX and produces a
PostScript file. Plain text output is also available, PDF output is
limited but working (e.g. no graphics). Either of these may be
fed to a printer. Lout is offered in multiple languages.

%prep
%autosetup -p1 -n lout-%{tardate}

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

%check
# Program doesn't have specific test suite, but
# building of complete documentation represents
# rather thorough test of complete functionality of
# the program.

%files
%doc README READMEPDF
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*.1%{?ext_man}

%changelog
