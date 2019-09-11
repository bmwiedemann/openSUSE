#
# spec file for package psutils
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           psutils
Version:        p17
Release:        0
Summary:        Tools for Manipulating PostScript Files
License:        GPL-2.0+
Group:          Productivity/Publishing/PS
Source:         http://mirrors.ctan.org/support/psutils/psutils-p17.tar.gz
Patch0:         psutils-p17.dif
Patch1:         psutils-flip.dif
Patch2:         psutils-pserror.dif
Requires:       perl
Provides:       psutils-p17
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

You will find a README in /usr/share/doc/packages/psutils/ which also
describes several Perl scripts for importing PostScript files. A manual
page for each ps utility is also included.

%prep
%setup -q -n psutils
%patch1 -p1 -b .flip
%patch2 -p0 -b .sec
%patch0

%build
make %{?_smp_mflags} -f Makefile.unix RPM_OPT_FLAGS="%{optflags}"

%install
    mkdir -p %{buildroot}%{_mandir}/man1 %{buildroot}%{_prefix}/bin
    make -f Makefile.unix BINDIR=%{buildroot}%{_bindir} \
                          MANDIR=%{buildroot}%{_mandir}/man1 \
                          INCLUDEDIR=%{buildroot}%{_datadir}/psutils install

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/epsffit
%{_bindir}/extractres
%{_bindir}/fixdlsrps
%{_bindir}/fixfmps
%{_bindir}/fixmacps
%{_bindir}/fixpsditps
%{_bindir}/fixpspps
%{_bindir}/fixscribeps
%{_bindir}/fixtpps
%{_bindir}/fixwfwps
%{_bindir}/fixwpps
%{_bindir}/fixwwps
%{_bindir}/getafm
%{_bindir}/includeres
%{_bindir}/psbook
%{_bindir}/psmerge
%{_bindir}/psnup
%{_bindir}/psresize
%{_bindir}/psselect
%{_bindir}/pstops
%{_bindir}/showchar
%{_mandir}/man1/epsffit.1.gz
%{_mandir}/man1/extractres.1.gz
%{_mandir}/man1/fixdlsrps.1.gz
%{_mandir}/man1/fixfmps.1.gz
%{_mandir}/man1/fixmacps.1.gz
%{_mandir}/man1/fixpsditps.1.gz
%{_mandir}/man1/fixpspps.1.gz
%{_mandir}/man1/fixscribeps.1.gz
%{_mandir}/man1/fixtpps.1.gz
%{_mandir}/man1/fixwfwps.1.gz
%{_mandir}/man1/fixwpps.1.gz
%{_mandir}/man1/fixwwps.1.gz
%{_mandir}/man1/getafm.1.gz
%{_mandir}/man1/includeres.1.gz
%{_mandir}/man1/psbook.1.gz
%{_mandir}/man1/psmerge.1.gz
%{_mandir}/man1/psnup.1.gz
%{_mandir}/man1/psresize.1.gz
%{_mandir}/man1/psselect.1.gz
%{_mandir}/man1/pstops.1.gz
%dir %{_datadir}/psutils/
%{_datadir}/psutils/md68_0.ps
%{_datadir}/psutils/md71_0.ps

%changelog
