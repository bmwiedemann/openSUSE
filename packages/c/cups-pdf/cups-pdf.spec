#
# spec file for package cups-pdf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cups-pdf
Version:        3.0.1
Release:        0
Summary:        Virtual PDF printer for CUPS
License:        GPL-2.0
Group:          Productivity/Publishing/PDF
Url:            http://www.cups-pdf.de/
Source0:        http://www.cups-pdf.de/src/cups-pdf_%{version}.tar.gz
BuildRequires:  cups-devel
Requires:       cups-client
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CUPS-PDF is a PDF writer backend for CUPS.
It provides a virtual CUPS-PDF printer which produces PDF files
so that application programs which have no built-in support
to "Save as PDF" could print to CUPS-PDF to get a PDF file.
For details see %{_docdir}/cups-pdf/README
and http://en.opensuse.org/SDB:Printing_to_PDF

%prep
%setup -q

%build
cd src
gcc %{optflags} -o cups-pdf cups-pdf.c -lcups

%install
install -Dm644 extra/CUPS-PDF_noopt.ppd %{buildroot}%{_datadir}/cups/model/CUPS-PDF_noopt.ppd
install -Dm644 extra/CUPS-PDF_opt.ppd %{buildroot}%{_datadir}/cups/model/CUPS-PDF_opt.ppd
install -Dm644 extra/cups-pdf.conf %{buildroot}%{_sysconfdir}/cups/cups-pdf.conf
install -Dm700 src/cups-pdf %{buildroot}%{_prefix}/lib/cups/backend/cups-pdf
install -dm755 %{buildroot}%{_localstatedir}/spool/cups-pdf
pushd %{buildroot}%{_datadir}/cups/model
ln -s CUPS-PDF_opt.ppd CUPS-PDF.ppd
popd

%post
# Add a symbolic link if /usr/lib64/cups/backend/ exists:
if test -d %{_libdir}/cups/backend
then ln -s %{_prefix}/lib/cups/backend/cups-pdf %{_libdir}/cups/backend/cups-pdf || :
fi
# Add a "CUPS-PDF" queue if the package is installed (but not when the package is updated):
if test "$1" -eq "1"
then %{_sbindir}/lpadmin -h localhost -p CUPS-PDF -v cups-pdf:/ -m CUPS-PDF.ppd -E || :
fi
# Exit successfully in any case:
exit 0

%postun
# Only if the package is erased (but not when it is replaced with an update package):
if test "$1" -eq "0"
then # Remove the "CUPS-PDF" queue (be silent if it does not exist):
     %{_sbindir}/lpadmin -h localhost -x CUPS-PDF 2>/dev/null || :
     # Remove the symbolic link (ignore if it does not exist):
     rm -f %{_libdir}/cups/backend/cups-pdf || :
fi
# Exit successfully in any case:
exit 0

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%config(noreplace) %{_sysconfdir}/cups/cups-pdf.conf
%dir %{_prefix}/lib/cups
%dir %{_prefix}/lib/cups/backend
%attr(700, root, root) %{_prefix}/lib/cups/backend/cups-pdf
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%{_datadir}/cups/model/CUPS-PDF.ppd
%{_datadir}/cups/model/CUPS-PDF_noopt.ppd
%{_datadir}/cups/model/CUPS-PDF_opt.ppd
%dir %{_localstatedir}/spool/cups-pdf

%changelog
