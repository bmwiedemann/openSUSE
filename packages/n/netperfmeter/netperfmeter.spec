#
# spec file for package netperfmeter
#
# Copyright (c) 2023 SUSE LLC
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


Name:           netperfmeter
Version:        1.9.4
Release:        0
Summary:        Network performance meter for the UDP, TCP, SCTP and DCCP protocols
License:        GPL-3.0-or-later
URL:            https://www.uni-due.de/~be0001/netperfmeter/
#Git-Clone:     https://github.com/dreibh/netperfmeter.git
Source:         https://www.uni-due.de/~be0001/netperfmeter/download/%{name}-%{version}.tar.xz
Source1:        https://www.uni-due.de/~be0001/netperfmeter/download/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)

%description
NetPerfMeter is a network performance meter for the UDP, TCP, SCTP
and DCCP transport protocols over IPv4 and IPv6. It simultaneously
transmits bidirectional flows to an endpoint and measures the
resulting flow bandwidths and QoS. The results are written as
vector and scalar files.
The vector files can e.g. be used to create plots of the results.

%prep
%autosetup

%build
# FIXME: you should use the %%cmake macros
mkdir build && cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_NEAT=0 \
    -DBUILD_TEST_PROGRAMS=1 \
    -DBUILD_PLOT_PROGRAMS=1
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}/%{_bindir}/*

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/combinesummaries
%{_bindir}/createsummary
%{_bindir}/extractvectors
%{_bindir}/getabstime
%{_bindir}/netperfmeter
%{_bindir}/runtimeestimator
%{_mandir}/man1/combinesummaries.1%{?ext_man}
%{_mandir}/man1/createsummary.1%{?ext_man}
%{_mandir}/man1/extractvectors.1%{?ext_man}
%{_mandir}/man1/getabstime.1%{?ext_man}
%{_mandir}/man1/netperfmeter.1%{?ext_man}
%{_mandir}/man1/runtimeestimator.1%{?ext_man}

%package pdfproctools
Summary:        PDF Processing Tools
Group:          Productivity/Networking/Diagnostic
Requires:       ghostscript
Requires:       perl >= 5.8.0
Requires:       perl-PDF-API2
Requires:       qpdf
BuildArch:      noarch

%description pdfproctools
SetPDFMetadata updates the metadata of a PDF file. In particular,
it can be used to add outlines (bookmarks) to a document.
Furthermore, it can set the document properties (e.g. author,
title, keywords, creator, producer).  PDFEmbedFonts embeds all
referenced fonts into a PDF file. Optionally, it can also linearize
the PDF file for online publication ("fast web view", "optimized").

This package contains tools for PDF file processing.

%files pdfproctools
%{_bindir}/pdfembedfonts
%{_bindir}/setpdfmetadata
%{_mandir}/man1/pdfembedfonts.1%{?ext_man}
%{_mandir}/man1/setpdfmetadata.1%{?ext_man}

%package plotting
Summary:        Network Performance Meter (plotting program)
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       %{name}-pdfproctools = %{version}
Requires:       R-core
BuildArch:      noarch

%description plotting
NetPerfMeter is a network performance meter for the UDP,
TCP, MPTCP, SCTP and DCCP transport protocols over IPv4 and IPv6.
It simultaneously transmits bidirectional flows to an endpoint
and measures the resulting flow bandwidths and QoS. The
results are written as vector and scalar files. The vector
files can e.g. be used to create plots of the results.

This package contains a plotting program for the results.

%files plotting
%{_bindir}/plot-netperfmeter-results
%dir %{_datadir}/netperfmeter
%{_datadir}/netperfmeter/plot-netperfmeter-results.R
%{_datadir}/netperfmeter/plotter.R
%{_mandir}/man1/plot-netperfmeter-results.1%{?ext_man}

%changelog
