#
# spec file for package dbgl
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2024, Martin Hauke <mardnh@gmx.de>
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


%define realver 098
%define java_version 21
Name:           dbgl
Version:        0.98
Release:        0
Summary:        DOSBox Game Launcher
License:        GPL-2.0-only
Group:          System/Emulators/Other
URL:            https://dbgl.org
Source0:        https://dbgl.org/download/src%{realver}.zip
Source1:        %{name}-wrapper.sh
Source2:        %{name}.appdata.xml
Patch0:         fix-swt-color.patch
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-text
BuildRequires:  eclipse-swt
BuildRequires:  java-devel >= %{java_version}
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       apache-commons-io
Requires:       apache-commons-lang3
Requires:       apache-commons-text
Requires:       dosbox >= 0.70
Requires:       eclipse-swt
Requires:       java >= %{java_version}
Requires:       javapackages-tools
BuildArch:      noarch

%description
DBGL is a Java front-end for DOSBox, based largely upon the
proven interface of D-Fend.

%prep
%setup -q -c
%autopatch -p1
# unbundle libs
rm ./src/dist/shared/lib/commons-lang3-*.jar
rm ./src/dist/shared/lib/commons-io-*.jar
rm ./src/dist/shared/lib/commons-text-*.jar

%build
mkdir -p lib
build-jar-repository -s -p libtest commons-io commons-lang3 apache-commons-text swt
ant distlinux

%install
install -D -m0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
install -d %{buildroot}%{_javadir}/dbgl
tar xvf dist/dbgl%{realver}.tar.gz -C %{buildroot}%{_javadir}/dbgl/
# Use symbol links to system libraries
build-jar-repository -s -p %{buildroot}/%{_javadir}/%{name}/lib commons-io commons-lang3 apache-commons-text swt
#
install -d %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_javadir}/%{name}/dbgl.png %{buildroot}%{_datadir}/pixmaps/
install -D -pm0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/dbgl.appdata.xml
%suse_update_desktop_file -c %{name} %{name} "DOSBox Game Launcher" %{name} %{name} Game Emulator
# Remove not needed files
rm %{buildroot}%{_javadir}/dbgl/lib/swtlin64.jar
rm %{buildroot}%{_javadir}/dbgl/dbgl

%files
%license src/dist/shared/COPYING
%{_bindir}/dbgl
%{_javadir}/dbgl
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
