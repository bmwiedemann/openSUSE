#
# spec file for package hibiscus
#
# Copyright (c) 2025 SUSE LLC
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


%define _major 2
%define _minor 10
%define _micro 24
%define _build 388
%define _version %{_major}.%{_minor}.%{_micro}
%define _tag V_%{_major}_%{_minor}_%{_micro}_BUILD_%{_build}

Name:           hibiscus
Version:        %{_version}
Release:        0
Summary:        Java online banking client using the HBCI standard
License:        Apache-2.0 AND GPL-2.0-only AND LGPL-2.0-only AND CPL-1.0 AND Zlib AND MPL-1.0 AND EPL-1.0
Group:          Productivity/Office/Finance
URL:            https://www.willuhn.de/products/hibiscus/
Source:         https://github.com/willuhn/hibiscus/archive/refs/tags/%{_tag}.tar.gz
Source2:        hibiscus-rpmlintrc
BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jameica-devel >= 2.10.4
BuildRequires:  java-devel >= 11
BuildRequires:  jpackage-utils
BuildRequires:  xml-commons-apis
Requires:       jameica >= 2.10.4

# Don't offer libraries linked in here to other packages:
AutoReqProv:    off

%description
A free Java homebanking application that uses the HBCI4Java implementation
and runs as a plugin inside the Jameica framework. Support chipcards
key files and PIN/TAN including chipTAN and smsTAN for authentification.
Supported file formats include MT940, DTAUS, CSV, Moneyplex and PDF/HTML.

%prep
%setup -q -n %{name}-%{_tag}

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc build/ChangeLog
%license LICENSE COPYING
%{_prefix}/lib/jameica/plugins/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
