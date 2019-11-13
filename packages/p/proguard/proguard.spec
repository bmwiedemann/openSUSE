#
# spec file for package proguard
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           proguard
Version:        5.3.3
Release:        0
Summary:        Java class file shrinker, optimizer, obfuscator and preverifier
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://www.guardsquare.com/en/proguard
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        README.dist
BuildRequires:  ant
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-tools
Requires:       java >= 1.6
Requires:       javapackages-tools
BuildArch:      noarch

%description
ProGuard is a free Java class file shrinker, optimizer, obfuscator and
preverifier. It detects and removes unused classes, fields, methods, and
attributes. It optimizes bytecode and removes unused instructions. It
renames the remaining classes, fields, and methods using short meaningless
names. Finally, it preverifies the processed code for Java 6 or for Java
Micro Edition.

%package manual
Summary:        Manual for %{name}
Group:          Documentation/HTML
Requires:       javapackages-tools

%description manual
The manual for %{name}.

%package gui
Summary:        GUI for %{name}
Group:          Development/Libraries/Java
# we convert the favicon.ico to png files of different sizes, so we require
# ImageMagick
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       %{name} = %{version}-%{release}
Requires:       javapackages-tools

%description gui
A GUI for %{name}.

%prep
%setup -q -n %{name}%{version}

# remove all jar and class files, the snippet from Packaging:Java does
# not work
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

# remove the Class-Path from MANIFESTs
sed -i '/class-path/I d' src/%{name}/gui/MANIFEST.MF
sed -i '/class-path/I d' src/%{name}/retrace/MANIFEST.MF

# this will create three png files from the favicon that contains multiple size
# icons: 0: 48x48, 1: 32x32, 2: 16x16
convert docs/favicon.ico %{name}.png
cp -p %{name}-0.png %{name}48.png
cp -p %{name}-1.png %{name}32.png
cp -p %{name}-2.png %{name}16.png

# add README.dist
cp -p %{SOURCE2} .

%build
cd buildscripts/
# build ProGuard, ProGuardGUI, retrace and anttask
ant -Dant.build.javac.target=1.6 -Dant.build.javac.source=1.6 -Dant.jar=%{_javadir}/ant.jar basic anttask

%install
mkdir -p %{buildroot}%{_javadir}/%{name}/
cp -p lib/%{name}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
cp -p lib/%{name}gui.jar %{buildroot}%{_javadir}/%{name}/%{name}gui.jar
cp -p lib/retrace.jar %{buildroot}%{_javadir}/%{name}/retrace.jar

mkdir -p %{buildroot}%{_bindir}
%jpackage_script proguard.ProGuard "" "" proguard proguard true
%jpackage_script proguard.gui.ProGuardGUI "" "" proguard proguard-gui true
%jpackage_script proguard.retrace.ReTrace "" "" proguard proguard-retrace true

#install the desktop file for proguard-gui
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

#copy icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp -p %{name}48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
cp -p %{name}32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
cp -p %{name}16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/proguard.jar
%{_javadir}/%{name}/retrace.jar
%{_bindir}/proguard
%{_bindir}/proguard-retrace
%doc README examples/ README.dist

%files manual
%doc docs/*

%files gui
%{_bindir}/%{name}-gui
%{_javadir}/%{name}/proguardgui.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/*

%changelog
