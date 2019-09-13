#
# spec file for package skinlf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version2  20060722
Name:           skinlf
Version:        6.7
Release:        0
Summary:        Allows developers to write skinnable application using the Swing toolkit
# Included software nanoxml is licensed under zlib, while skinlf is itself Apache-1.1
License:        Apache-1.1 AND Zlib
Group:          Development/Libraries/Java
URL:            http://skinlf.l2fprod.com/index.html
# Upstream download link https://skinlf.dev.java.net/files/documents/66/37801/skinlf-6.7-20060722.zip seems dead
Source0:        %{name}-%{version}-%{_version2}.tar.bz2
Source1:        imageconversion.jar
Source2:        %{name}-build.xml
Source3:        %{name}-resources.tar.bz2
Patch0:         skinlf-no-jimi.patch
Patch1:         skinlf-6.7-getpeer.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.5
BuildRequires:  jpackage-utils
BuildRequires:  laf-plugin
BuildRequires:  xalan-j2
Requires:       java >= 1.5
Requires:       jpackage-utils
Requires:       laf-plugin
Requires:       xalan-j2
BuildArch:      noarch

%description
Skin Look And Feel allows Java developers to write skinnable application using
the Swing toolkit. Skin Look And Feel is able to read GTK (The Gimp Toolkit)
and KDE (The K Desktop Environment) skins to enhance your application GUI
controls such as Buttons, Checks, Radios, Scrollbars, Progress Bar, Lists,
Tables, Internal Frames, Colors, Background Textures, Regular Windows. Skin
Look And Feel (aka SkinLF) also includes NativeSkin to create irregular
windows.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Recommends:     %{name} = %{version}

%description javadoc
Skin Look And Feel allows Java developers to write skinnable application using
the Swing toolkit. Skin Look And Feel is able to read GTK (The Gimp Toolkit)
and KDE (The K Desktop Environment) skins to enhance your application GUI
controls such as Buttons, Checks, Radios, Scrollbars, Progress Bar, Lists,
Tables, Internal Frames, Colors, Background Textures, Regular Windows. Skin
Look And Feel (aka SkinLF) also includes NativeSkin to create irregular
windows.

This package provides the HTML-Documentation for %{name}.

%package demo
Summary:        Examples for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description demo
Skin Look And Feel allows Java developers to write skinnable application using
the Swing toolkit. Skin Look And Feel is able to read GTK (The Gimp Toolkit)
and KDE (The K Desktop Environment) skins to enhance your application GUI
controls such as Buttons, Checks, Radios, Scrollbars, Progress Bar, Lists,
Tables, Internal Frames, Colors, Background Textures, Regular Windows. Skin
Look And Feel (aka SkinLF) also includes NativeSkin to create irregular
windows.

This package provides a few demo examples for %{name}.

%prep
%setup -q -a3
cp %{SOURCE1} .
cp %{SOURCE2} build.xml
for i in AUTHORS CHANGES INSTALL LICENSE LICENSE_nanoxml README THANKS; do
	dos2unix -o $i
	chmod 644 $i
done
%patch0
%patch1 -p1

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar javadocs

%install
# jars
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 lib/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# demo
install -dm 755 %{buildroot}%{_datadir}/%{name}
install -m 644 lib/%{name}_demo.jar \
	%{buildroot}%{_datadir}/%{name}
install -m 644 lib/themepack.zip \
	%{buildroot}%{_datadir}/%{name}

cat > bin/alwaysontop.sh << EOF
#!/bin/bash
java -cp %{_javadir}/%{name}.jar:%{_datadir}/%{name}/%{name}_demo.jar examples.alwaysontop
EOF

cat > bin/demo.sh << EOF
#!/bin/bash
THEMEPACK=\$1
if [ "\$THEMEPACK" == "" ]; then
	THEMEPACK=%{_datadir}/%{name}/themepack.zip
else
	shift
fi
java -cp %{_javadir}/%{name}.jar:%{_javadir}/laf-plugin.jar:%{_datadir}/%{name}/%{name}_demo.jar examples.demo \$THEMEPACK \$@
EOF

# install startscripts for demo-apps
install -m 755 bin/*.sh \
	%{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc AUTHORS CHANGES LICENSE_nanoxml README THANKS
%{_javadir}/%{name}*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.jar
%{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/themepack.zip

%changelog
