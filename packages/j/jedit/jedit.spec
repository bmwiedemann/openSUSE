#
# spec file for package jedit
#
# Copyright (c) 2021 SUSE LLC
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


%define _buildshell /bin/bash
%define section	free
Name:           jedit
Version:        5.5.0
Release:        0
Summary:        Programmer's Text Editor Written in Java
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            http://www.jedit.org/
Source0:        http://download.sourceforge.net/jedit/jedit%{version}source.tar.bz2
Source1:        icons.tar
Source2:        %{name}.desktop
Source3:        %{name}.in
Source4:        http://prdownloads.sourceforge.net/jedit-plugins/QuickNotepad-5.0.tgz
#svn co https://jedit.svn.sourceforge.net/svnroot/jedit/build-support/trunk build-support
Source5:        build-support-r22713.tar.gz
Patch0:         jedit-jdk9+.patch
Patch1:         jedit-doclet.patch
BuildRequires:  ant >= 1.8.2
BuildRequires:  ant-apache-bsf
BuildRequires:  ant-contrib
BuildRequires:  ant-junit
BuildRequires:  apache-commons-logging
BuildRequires:  apache-ivy
BuildRequires:  bouncycastle
BuildRequires:  bsh2
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  hamcrest
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel >= 1.8
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  rhino
BuildArch:      noarch

%description
jEdit is a cross-platform programmer's text editor written in Java.
Some of jEdit's features include:

* Built-in macro language (BeanShell).
* Extensible plug-in architecture with more than 80 plug-ins
   available.
* Plug-ins can be downloaded and installed from within jEdit using
   the plug-in manager feature.
* Syntax highlighting for more than 80 languages.
* Supports a large number of character encodings including UTF8 and
   Unicode.
* Auto-indenting of source code.
* Folding (indent and marker based).
* Word wrap.
* Unlimited undo and redo.
* Highly configurable and customizable.
* Every other feature, both basic and advanced, that you would expect
to find in a text editor.

%package javadoc
Summary:        Programmer's text editor written in Java (Documentation)
Group:          Productivity/Text/Editors

%description javadoc
Javadoc for %{summary}.

%prep
%setup -q -D -n jEdit -b 1 -a 4 -a 5
%patch0 -p1
%patch1 -p1

find . -name '*jar' -delete

rm -f doclet/GenerateTocXML.java

%build

DOCBOOK=%{_datadir}/xml/docbook/stylesheet/nwalsh/current

# Specify some properties
cat <<EOF > build.properties
xsltproc.executable=%{_bindir}/xsltproc
docbook.xsl=${DOCBOOK}
docbook.catalog=${DOCBOOK}/catalog.xml
build.support=$(pwd)/build-support/
EOF

# link dependencies
link_dependencies () {
    mkdir -p "$2"
    IFS=':' read -a jars <<< $(build-classpath $1)
    for jar in "${jars[@]}"; do ln -sf "${jar}" "$2/$1-$(basename "${jar}")"; done
}

link_dependencies jsr-305 lib/compile
link_dependencies junit lib/test
link_dependencies hamcrest lib/test
link_dependencies ant lib/ant-contrib
link_dependencies bsh2-bsf lib/scripting

mkdir -p lib/ivy
ln -sf $(build-classpath ivy) lib/ivy/ivy-2.2.0.jar

# we have to break a dependency where build target expects plugins are in place,
# where they are built separatelly and need jEdit.jar for a build
mkdir -p lib/default-plugins/
touch lib/default-plugins/HACK

export CLASSPATH=$(build-classpath apache-commons-logging)
# Run the build
# XXX: there's NPE on build-docs, but who care about html docs those times, right?
%ant -Divy.done=true build docs-javadoc

# plugins-build hardcodes the jedit.jar path - so to make it happy
ln -s build/jedit.jar

pushd QuickNotepad
%ant
popd
mv QuickNotepad.jar build/jars
rm build/jars/HACK

%install
# dirs
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 0755 %{buildroot}%{_mandir}/man1/

install -d -m 0755 %{buildroot}%{_javadir}
install build/%{name}.jar %{buildroot}%{_datadir}/%{name}/%{name}.jar
# link /usr/share/jedit/jedit.jar to /usr/share/java
(cd %{buildroot}%{_javadir} && ln -s %{_datadir}/%{name}/%{name}.jar %{name}.jar)

# Install the /usr/share/jedit subdirectories
cp -ar build/{doc,jars,keymaps,macros,modes,properties,startup} %{buildroot}%{_datadir}/%{name}

# Symlink the javadoc into /usr/share/jedit
(cd %{buildroot}%{_datadir}/%{name}/doc && ln -s %{_javadocdir}/%{name} api)

# Man page
install -m 0644 package-files/linux/%{name}.1 %{buildroot}%{_mandir}/man1/

# Icons
for size in 16 32 48 64 128 256; do
    dims="${size}x${size}"
    install -D -m 644 ../icons/icon_${dims}.png %{buildroot}%{_datadir}/icons/hicolor/${dims}/apps/%{name}.png
done

# Desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

# Launcher script
cat %{SOURCE3} | sed 's|@data|%{_datadir}/%{name}|g' > %{name}
install %{name} %{buildroot}%{_bindir}

%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/
%exclude %{_datadir}/%{name}/doc/api

%files javadoc
%doc %{_javadocdir}/%{name}
%{_datadir}/%{name}/doc/api

%changelog
