#
# spec file for package pdftk
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Franz Sirl (fsirl)
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


Name:           pdftk
Version:        3.2.1
Release:        0
Summary:        A handy tool for manipulating PDF
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PDF
URL:            https://www.pdflabs.com/
Source0:        https://gitlab.com/pdftk-java/pdftk/-/archive/v%{version}/pdftk-v%{version}.tar.bz2
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  bouncycastle
Requires:       apache-commons-lang3
Requires:       bouncycastle
Requires:       jre >= 11
BuildArch:      noarch

%description
If PDF is electronic paper, then pdftk is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses.
Pdftk is a simple tool for doing everyday things with PDF documents.

Use it to:
  * Merge PDF Documents
  * Split PDF Pages into a New Document
  * Rotate PDF Documents or Pages
  * Decrypt Input as Necessary (Password Required)
  * Encrypt Output as Desired
  * Fill PDF Forms with X/FDF Data and/or Flatten Forms
  * Generate FDF Data Stencil from PDF Forms
  * Apply a Background Watermark or a Foreground Stamp
  * Report PDF Metrics such as Metadata and Bookmarks
  * Update PDF Metadata
  * Attach Files to PDF Pages or the PDF Document
  * Unpack PDF Attachments
  * Burst a PDF Document into Single Pages
  * Uncompress and Re-Compress Page Streams
  * Repair Corrupted PDF (Where Possible)

%prep
%setup -q -n %{name}-v%{version}
mkdir lib
ln -s %{_javadir}/bcprov.jar %{_javadir}/commons-lang3.jar -t lib

%build
%{ant} jar

%install
install -dm0755 %{buildroot}%{_bindir} %{buildroot}%{_javadir} %{buildroot}%{_mandir}/man1
install -m0644 build/jar/pdftk.jar %{buildroot}%{_javadir}
install -m0644 pdftk.1 -t %{buildroot}%{_mandir}/man1
# startscript
cat >%{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
exec %{_bindir}/java -cp %{_javadir}/%{name}.jar:%{_javadir}/bcprov.jar:%{_javadir}/commons-lang3.jar com.gitlab.pdftk_java.pdftk \$*
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%license license_gpl_pdftk/*.txt license_gpl_pdftk/*/*.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_javadir}/%{name}.jar

%changelog
