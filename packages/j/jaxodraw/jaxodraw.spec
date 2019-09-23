#
# spec file for package jaxodraw
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


%define major 2.1
%define minor 0
Name:           jaxodraw
Version:        %{major}.%{minor}
Release:        0
Summary:        A Java-based GUI for drawing Feynman diagrams
# The xslt files in the manual are Apache-2.0 licensed, GPL-2.0+ for everything else
License:        GPL-2.0-or-later AND Apache-2.0
Group:          Productivity/Scientific/Physics
URL:            http://jaxodraw.sourceforge.net
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{major}-%{minor}-src.tar.gz
Source1:        http://sourceforge.net/projects/jaxodraw/files/installer_files/installer-2.0-1.tar.gz
Source2:        http://downloads.sourceforge.net/%{name}/axodraw4j_2008_11_19.tar.gz
Source3:        %{name}.appdata.xml
# ANT BUILD SCRIPTS IMPORTED FROM UPSTREAM SVN
# http://sourceforge.net/p/jaxodraw/code/HEAD/tree/branches/2.1-x/
Source4:        build.properties
Source5:        build.xml
# PATCH-FEATURE-OPENSUSE jaxodraw-set-default-viewers.patch badshah400@gmail.com -- Set xdg-open as the default HTML and postscript viewers (can be changed by user)
Patch0:         jaxodraw-set-default-viewers.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.7.0
BuildRequires:  javapackages-tools
BuildRequires:  update-desktop-files
BuildRequires:  tex(latex)
Requires:       java >= 1.7.0
Requires:       javapackages-tools
Recommends:     %{name}-javadoc = %{version}
Recommends:     %{name}-latex
BuildArch:      noarch

%description
JaxoDraw is a Java program for drawing Feynman diagrams. It has a
complete graphical user interface that allows to carry out all actions
in a mouse click-and-drag fashion. Fine-tuning of the diagrams is
possible through keyboard short-cuts. Graphs may be exported to a
variety of image formats, including (encapsulated) postscript, and can
be saved in XML files to be used in later sessions.

The main feature of JaxoDraw is the possibility of generating
LaTeX code that makes use of J. Vermaseren's axodraw package to
compile. In fact the main motivation for writing JaxoDraw was to
create a graphical user interface for the axodraw package. In that
way, we combine the power of LaTeX with the easiness of a
what-you-see-is-what-you-get interface.

%package javadoc
Summary:        Javadocs for %{name}
License:        GPL-2.0-or-later
Group:          Documentation/Other
Requires:       %{name} = %{version}
Requires:       javapackages-tools

%description javadoc
This package contains the API documentation for %{name}.

%package latex
Summary:        LaTeX style file axodraw4j.sty for documents generated with jaxodraw
# In order to compile documents one needs a LaTeX compiler
License:        LPPL-1.3c
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}
Requires:       texlive-pst-tools
Requires:       tex(latex)
Requires(post): coreutils
Requires(posttrans): texlive
Requires(postun): coreutils
Requires(postun): texlive
Requires(pre):  texlive

%description latex
This package contains the LaTeX style file that is needed for EPS export
functionality in jaxodraw.

You need this if you want the export to EPS function to work or if you want to
compile LaTeX files generated with jaxodraw.

%prep
%setup -q -n %{name}-%{major}-%{minor} -a 1 -a 2
%patch0 -p1
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# REMOVE UNNECESSARY-FOR-BUILD DIR WITH POTENTIAL LICENSING ISSUES
test -d src/site && rm -r src/site

%build
cp %{SOURCE4} ./
cp %{SOURCE5} ./
sed -i "s/jaxodraw.release=SNAPSHOT/jaxodraw.release=0/" build.properties

# FIX EOF ENCODINGS
for f in src/doc/{TODO,CHANGELOG,README,BUGS} src/doc/legal/{GNU-,}LICENSE
do
  sed -i 's/\r$//' ${f}
done

ant jar javadoc

%install
install -D -m 0644 build/%{name}-%{major}-%{minor}.jar %{buildroot}%{_javadir}/%{name}.jar

# startscript
cat > %{name} << 'EOF'
#!/bin/sh
#
# jaxodraw startscript
#
java -jar %{_javadir}/%{name}.jar
EOF

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

# INSTALL .desktop file and appstream file [taken from FEDORA]
install -D -m 644 installer-2.0-1/OS/Linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -r %{name} Graphics 2DGraphics VectorGraphics Education Science DataVisualization

install -D -p -m 644 installer-2.0-1/OS/Linux/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
# Man page
install -D -p -m 644 installer-2.0-1/OS/Linux/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# LaTeX style
install -D -p -m 644 axodraw4j.sty %{buildroot}%{_datadir}/texmf/tex/latex/axodraw4j/axodraw4j.sty

# Register as an application to be visible in the software center
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# POST SCRIPTS IMPORTED FROM texlive-specs-a SPECFILE
%post latex
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr
> %{_localstatedir}/run/texlive/run-update

%postun latex
if test $1 = 0; then
    %{_bindir}/mktexlsr 2> /dev/null || :
    exit 0
fi
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr
> %{_localstatedir}/run/texlive/run-update

%posttrans latex
test -f %{_localstatedir}/run/texlive/run-update || exit 0
test -z "$ZYPP_IS_RUNNING" || exit 0
VERBOSE=false %{_datadir}/texmf/texconfig/update || :
rm -f %{_localstatedir}/run/texlive/run-update

%files
%doc src/doc/* axodraw4j-summary.txt
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
# OWN THE APPDATA DIR FOR openSUSE < 13.2 (NEEDED FOR SLE 12, openSUSE 13.1)
%if 0%{?suse_version} < 1320
%dir %{_datadir}/appdata
%endif
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%files javadoc
%{_javadocdir}/%{name}/

%files latex
%{_datadir}/texmf/tex/latex/axodraw4j/

%changelog
