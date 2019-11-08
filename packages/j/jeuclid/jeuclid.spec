#
# spec file for package jeuclid
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


Name:           jeuclid
Version:        3.1.3
Release:        0
Summary:        MathML rendering solution
# LGPL-2.1 is for the FreeHEP component only (see LICENSE.FreeHEP)
License:        Apache-2.0 AND LGPL-2.1-only
Group:          Development/Libraries/Java
URL:            http://jeuclid.sourceforge.net/index.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-parent-%{version}-src.zip
#fedora specific build script based on debian
Source1:        build.xml
Source2:        jeuclid-mathviewer.desktop
Source3:        jeuclid-mathviewer.sh
Source4:        jeuclid-cli.sh
#removes FreeHep support as per the build README, optional feature (not upstream)
Patch0:         jeuclid-core-FreeHep.patch
#Allows for compiling code that uses Apple EAWT without the lib
Patch1:         AppleJavaExtensions.patch
#removes OSX dep for the viewer
Patch2:         MacOSX.patch
Patch3:         jeuclid-commons-lang3.patch
Patch4:         jeuclid-batik_1_10.patch
BuildRequires:  ant
BuildRequires:  apache-commons-cli >= 1.1
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-logging
BuildRequires:  batik >= 1.10
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jcip-annotations
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xml-commons-apis
BuildRequires:  xmlgraphics-commons >= 1.3
BuildRequires:  xmlgraphics-fop >= 0.95
Requires:       apache-commons-logging
Requires:       batik >= 1.10
Requires:       java
Requires:       javapackages-tools
Requires:       jcip-annotations
Requires:       xmlgraphics-commons >= 1.3
BuildArch:      noarch

%description
JEuclid is a complete MathML rendering solution, consisting of:

    A MathViewer application
    Command line converters from MathML to other formats
    An ant task for automated conversion
    Display components for AWT, Swing, and SWT

JEuclid features:

    Almost complete support for presentation MathML 2.0
    Basic support for content MathML 2.0
    Initial support for the upcoming MathML 3.0

This pacakges contains the core module containing basic JEuclid
rendering and document handling classes.

%package mathviewer
Summary:        Viewer for MathML files
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Requires:       hicolor-icon-theme

%description mathviewer
JEuclid is a complete MathML rendering solution, consisting of:

    A MathViewer application
    Command line converters from MathML to other formats
    An ant task for automated conversion
    Display components for AWT, Swing, and SWT

JEuclid features:

    Almost complete support for presentation MathML 2.0
    Basic support for content MathML 2.0
    Initial support for the upcoming MathML 3.0

This pacakges contains the Swing MathViewer application.

%package fop
Summary:        JEuclid plug-in for FOP
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Requires:       xmlgraphics-fop >= 0.95

%description fop
JEuclid is a complete MathML rendering solution, consisting of:

    A MathViewer application
    Command line converters from MathML to other formats
    An ant task for automated conversion
    Display components for AWT, Swing, and SWT

JEuclid features:

    Almost complete support for presentation MathML 2.0
    Basic support for content MathML 2.0
    Initial support for the upcoming MathML 3.0

This pacakges contains a JEuclid plug-in for
FOP (Formatting Objects Processor).

%package	cli
Summary:        Command line interface for JEuclid
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Requires:       apache-commons-cli >= 1.1
Requires:       apache-commons-io
Requires:       apache-commons-lang3

%description cli
JEuclid is a complete MathML rendering solution, consisting of:

    A MathViewer application
    Command line converters from MathML to other formats
    An ant task for automated conversion
    Display components for AWT, Swing, and SWT

JEuclid features:

    Almost complete support for presentation MathML 2.0
    Basic support for content MathML 2.0
    Initial support for the upcoming MathML 3.0

This pacakges provides a command line interface for JEuclid.

%prep
%setup -q -n %{name}-parent-%{version}
cp %{SOURCE1} %{_builddir}/%{name}-parent-%{version}/
#fix line endings
sed 's/\r//' NOTICE > NOTICE.unix
touch -r NOTICE NOTICE.unix;
mv NOTICE.unix NOTICE

mkdir lib
build-jar-repository -s -p lib jcip-annotations commons-logging xmlgraphics-commons batik-all xmlgraphics-fop.jar commons-cli commons-lang3 xml-apis

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

#removes the FreeHep support from the build per the build README
rm -f %{name}-core/src/main/java/net/sourceforge/jeuclid/converter/FreeHep*;

%build
ant compile-core compile-mathviewer compile-cli compile-fop -verbose

%install
mkdir -p %{buildroot}%{_javadir}
cp -p target/%{name}-core.jar \
%{buildroot}%{_javadir}/%{name}-core.jar
cp -p target/%{name}-fop.jar \
%{buildroot}%{_javadir}/%{name}-fop.jar
cp -p target/%{name}-mathviewer.jar \
%{buildroot}%{_javadir}/%{name}-mathviewer.jar
cp -p target/%{name}-cli.jar \
%{buildroot}%{_javadir}/%{name}-cli.jar

install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE3} %{buildroot}%{_bindir}/jeuclid-mathviewer
install -pm 755 %{SOURCE4} %{buildroot}%{_bindir}/jeuclid-cli

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
cp -p src/icons/jeuclid_48x48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications \
%{SOURCE2}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license LICENSE.txt jeuclid/LICENSE.FreeHEP
%doc NOTICE README.Release
%{_javadir}/%{name}-core.jar

%files mathviewer
%{_javadir}/%{name}-mathviewer.jar
%{_bindir}/jeuclid-mathviewer
%{_datadir}/icons/hicolor/48x48/apps/jeuclid_48x48.png
%{_datadir}/applications/jeuclid-mathviewer.desktop

%files fop
%{_javadir}/%{name}-fop.jar

%files cli
%{_javadir}/%{name}-cli.jar
%{_bindir}/jeuclid-cli

%changelog
