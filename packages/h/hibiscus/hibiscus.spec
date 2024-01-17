#
# spec file for package hibiscus
#
# Copyright (c) 2022 SUSE LLC
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


%define _build 370
%define tag V_2_10_8_BUILD_%{_build}
Name:           hibiscus
Version:        2.10.8
Release:        0
Summary:        Java online banking client using the HBCI standard
License:        Apache-2.0 AND GPL-2.0-only AND LGPL-2.0-only AND CPL-1.0 AND Zlib AND MPL-1.0 AND EPL-1.0
Group:          Productivity/Office/Finance
URL:            https://www.willuhn.de/products/hibiscus/
Source:         https://github.com/willuhn/hibiscus/archive/refs/tags/%{tag}.tar.gz
Source2:        hibiscus-rpmlintrc
BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hbci4java >= 3.1.55
BuildRequires:  hicolor-icon-theme
BuildRequires:  itextpdf >= 5.5.2
BuildRequires:  jameica-devel >= 2.10.1
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  pcsc-towitoko-devel
BuildRequires:  super-csv >= 2.4.0
BuildRequires:  xml-commons-apis
Requires:       hbci4java
Requires:       itextpdf
Requires:       jameica >= 2.10.0
Requires:       pcsc-towitoko-devel
Requires:       super-csv
%ifnarch s390 %{arm} %{ix86}
BuildRequires:  eclipse-swtchart >= 0.13.0
%requires_eq    eclipse-swtchart
%endif
# Don't offer libraries linked in here to other packages:

%description
A free Java homebanking application that uses the HBCI4Java implementation
and runs as a plugin inside the Jameica framework. Support chipcards
key files and PIN/TAN including chipTAN and smsTAN for authentification.
Supported file formats include MT940, DTAUS, CSV, Moneyplex and PDF/HTML.

%prep
%setup -q -n %{name}-%{tag}

# Remove Windows and Mac libraries
rm -rf lib/hbci4java-card-*

# older version of the CTAPI driver from Kobil
# can't be build from source
# questionable redistribution rights
rm lib/libct.so

# required for reading older key files in SIZ-RDH formats
# implemented under NDA with no chances of source code release
rm -rf lib/libhbci4java-sizrdh*

%build
# TODO: solve this better
cp -r %{_prefix}/lib/jameica/src .
cp -r %{_prefix}/lib/jameica/lib .

export CLASSPATH="$(build-classpath xml-commons-apis)"
ant -f build/build.xml -Ddefine.java.version=1.8 init compile jar zip src

%install
mkdir -p %{buildroot}%{_prefix}/lib/jameica/plugins
cp -r releases/%{version}-%{_build}/%{name} %{buildroot}%{_prefix}/lib/jameica/plugins

# unbundle HBCI4Java
rm  %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/hbci4j-core-3.1.62.jar
ln -sf %{_jnidir}/hbci4java/hbci4j-core.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/hbci4j-core-3.1.62.jar
rm %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libhbci4java-card-*.so
%ifarch x86_64
ln -sf %{_jnidir}/hbci4java/libhbci4java-card-linux.so %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libhbci4java-card-linux-64.so
%else
ln -sf  %{_jnidir}/hbci4java/libhbci4java-card-linux.so %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libhbci4java-card-linux-32.so
%endif

%ifnarch s390 %{arm} %{ix86}
# unbundle SWT Chart
rm %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/swtchart/*.jar
ln -sf %{_datadir}/eclipse/droplets/swtchart/plugins/org.eclipse.swtchart_0.13.0.*.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/swtchart/org.eclipse.swtchart_0.13.0.202009151159.jar
ln -sf %{_datadir}/eclipse/droplets/swtchart/plugins/org.eclipse.swtchart.extensions_0.13.0.*.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/swtchart/org.eclipse.swtchart.extensions_0.13.0.202009151159.jar
%endif

# unbundle iText PDF
rm %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/itext-*.jar
ln -sf %{_javadir}/itextpdf/itext-pdfa.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/itext-pdfa-5.5.2.jar
ln -sf %{_javadir}/itextpdf/itextpdf.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/itextpdf-5.5.2.jar

# unbundle libtowitoko
rm %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libtowitoko*
%ifarch x86_64
ln -sf  %{_libdir}/libtowitoko.so %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libtowitoko-2.0.7-amd64.so
%else
ln -sf  %{_libdir}/libtowitoko.so %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/libtowitoko-2.0.7.so
%endif

# unbundle Super CSV
rm %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/super-csv-2.4.0.jar
ln -sf %{_javadir}/super-csv/super-csv.jar %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/lib/super-csv-2.4.0.jar

# icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mv %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/icons/%{name}-icon-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
mv %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/icons/%{name}-icon-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
mv %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/icons/%{name}-icon-64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
rm -rf %{buildroot}%{_prefix}/lib/jameica/plugins/%{name}/icons

install -D -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%fdupes %{buildroot}

%files
%doc build/ChangeLog
%license LICENSE COPYING
%{_prefix}/lib/jameica/plugins/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
