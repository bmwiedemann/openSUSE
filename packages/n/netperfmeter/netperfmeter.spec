#
# spec file for package netperfmeter
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


%define services netperfmeter.service netperfmeter-module-loader.service
Name:           netperfmeter
Version:        2.0.9
Release:        0
Summary:        Network performance meter for the UDP, TCP, SCTP and DCCP protocols
License:        GPL-3.0-or-later
URL:            https://www.uni-due.de/~be0001/netperfmeter/
#Git-Clone:     https://github.com/dreibh/netperfmeter.git
Source:         https://www.uni-due.de/~be0001/netperfmeter/download/%{name}-%{version}.tar.xz
Source1:        https://www.uni-due.de/~be0001/netperfmeter/download/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  GraphicsMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  hicolor-icon-theme
BuildRequires:  lksctp-tools-devel
BuildRequires:  mupdf
BuildRequires:  pdf2svg
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
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
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
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

# don't package non-standard size icons
for i in 150 20 310 40 42 44 8; do
  rm -rf %{buildroot}/%{_datadir}/icons/hicolor/"$i"x"$i"
done

%pre
%service_add_pre %{services}

%post
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%license COPYING
%doc AUTHORS ChangeLog
%config %{_sysconfdir}/netperfmeter.conf
%{_bindir}/combinesummaries
%{_bindir}/createsummary
%{_bindir}/extractvectors
%{_bindir}/getabstime
%{_bindir}/netperfmeter
%{_bindir}/netperfmeter-module-loader
%{_bindir}/runtimeestimator
%{_mandir}/man1/combinesummaries.1%{?ext_man}
%{_mandir}/man1/createsummary.1%{?ext_man}
%{_mandir}/man1/extractvectors.1%{?ext_man}
%{_mandir}/man1/getabstime.1%{?ext_man}
%{_mandir}/man1/netperfmeter.1%{?ext_man}
%{_mandir}/man1/netperfmeter-module-loader.1%{?ext_man}
%{_mandir}/man1/runtimeestimator.1%{?ext_man}
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/combinesummaries
%{_datadir}/bash-completion/completions/createsummary
%{_datadir}/bash-completion/completions/extractvectors
%{_datadir}/bash-completion/completions/netperfmeter
%{_datadir}/icons/hicolor/*/*/%{name}.*??g
%{_datadir}/mime/packages/netperfmeter.xml
%{_unitdir}/netperfmeter.service
%{_unitdir}/netperfmeter-module-loader.service

%package pdfproctools
Summary:        PDF Processing Tools
Group:          Productivity/Networking/Diagnostic
Requires:       ghostscript
Requires:       mupdf
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
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/pdfembedfonts
%{_datadir}/bash-completion/completions/setpdfmetadata

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
%{_datadir}/netperfmeter/
%{_mandir}/man1/plot-netperfmeter-results.1%{?ext_man}
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/plot-netperfmeter-results

%changelog
