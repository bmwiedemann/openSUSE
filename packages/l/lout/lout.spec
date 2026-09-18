#
# spec file for package lout
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.43.4
Release:        0
Summary:        A document formatting system
License:        GPL-3.0-or-later
URL:            https://github.com/william8000/lout
Source0:        https://github.com/william8000/lout/archive/refs/tags/%{version}.tar.gz#/lout-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  ghostscript

%description
Lout is a document formatting system. The system reads a high-level
description of a document similar in style to LaTeX and produces a
PostScript file. Plain text output is also available, PDF output is
limited but working (e.g. no graphics). Either of these may be
fed to a printer. Lout is offered in multiple languages.

%prep
%autosetup

find . -name README -exec chmod 0644 '{}' \;

%build
# NOTE: CFLAGS must come via the environment, not the make command
# line: command-line variables are immune to the makefile's
# CFLAGS += config defines (-DLIB_DIR etc.) and the build then fails.
# %%{optflags} reach the makefile through ?= honoring the environment.
export CFLAGS="%{optflags}"
%make_build \
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
# Upstream installdoc leaves executable bits on doc files
# (rpmlint E: script-without-shebang); nothing under doc/ is runnable
find %{buildroot}%{_datadir}/%{name}/doc -type f -perm -111 -exec chmod a-x '{}' +
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
