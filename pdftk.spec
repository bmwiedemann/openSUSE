#
# spec file for package pdftk
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.3.3
Release:        0
Summary:        A handy tool for manipulating PDF
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PDF
URL:            https://www.pdflabs.com/
Source0:        https://gitlab.com/pdftk-java/pdftk/-/archive/v%{version}/pdftk-v%{version}.tar.bz2
Patch0:         %{name}-bc175.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk18on)
Requires:       apache-commons-lang3
Requires:       bouncycastle
# needed for the startscript
Requires:       javapackages-tools
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

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%pom_remove_plugin :jacoco-maven-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# startscript
%jpackage_script com.gitlab.pdftk_java.pdftk "" "" %{name}:bcprov:commons-lang3 %{name} true
# manpage
install -dm 0755 %{buildroot}%{_mandir}/man1
install -pm 0644 pdftk.1 -t %{buildroot}%{_mandir}/man1

%files -f .mfiles
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
