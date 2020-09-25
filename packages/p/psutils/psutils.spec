#
# spec file for package psutils
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


Name:           psutils
Version:        2.03
Release:        0
Summary:        Tools for Manipulating PostScript Files
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/PS
URL:            https://github.com/rrthomas/psutils
Source:         https://github.com/rrthomas/psutils/releases/download/v%{version}/psutils-%{version}.tar.gz
Requires:       paper
Requires:       perl
Requires:       perl(IPC::Run3)

%description
This archive contains utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement
into signatures for booklet printing, and page merging for n-up
printing.

psbook      rearranges pages into signatures

psselect    selects pages and page ranges

pstops      performs general page rearrangement and selection

psnup       put multiple pages per physical sheet of paper

psresize    alter document paper size

epsffit     fits an EPSF file to a given bounding box

You will find a README in %{_docdir}/psutils/ which also
describes several Perl scripts for importing PostScript files. A manual
page for each ps utility is also included.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/epsffit
%{_bindir}/psbook
%{_bindir}/psnup
%{_bindir}/psresize
%{_bindir}/psselect
%{_bindir}/pstops
%{_bindir}/extractres
%{_bindir}/includeres
%{_bindir}/psjoin
%{_datadir}/psutils
%{_datadir}/psutils/PSUtils.pm
%{_mandir}/man1/epsffit.1*
%{_mandir}/man1/psbook.1*
%{_mandir}/man1/psnup.1*
%{_mandir}/man1/psresize.1*
%{_mandir}/man1/psselect.1*
%{_mandir}/man1/pstops.1*
%{_mandir}/man1/psutils.1*
%{_mandir}/man1/extractres.1*
%{_mandir}/man1/includeres.1*
%{_mandir}/man1/psjoin.1*

%changelog
