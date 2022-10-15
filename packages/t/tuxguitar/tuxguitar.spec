#
# spec file for package tuxguitar
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2008-2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>
# Copyright (c) 2008-2017 Fedora project
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


%bcond_without itext
%ifarch x86_64
%global bit x86_64
%endif
%ifarch armv7hl
%global bit armv7hl
%endif
%ifarch armv6hl
%global bit armv6hl
%endif
%ifarch ppc64
%global bit ppc64
%endif
%ifarch ppc64le
%global bit ppc64le
%endif
%ifarch s390x
%global bit s390x
%endif
%ifarch aarch64
%global bit aarch64
%endif
%ifarch %{ix86}
%global bit x86
%endif
Name:           tuxguitar
Version:        1.5.4
Release:        0
Summary:        A multitrack tablature editor and player written in Java-SWT
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://www.tuxguitar.pw
Source0:        https://sourceforge.net/projects/%{name}/files/TuxGuitar/TuxGuitar-%{version}/%{name}-%{version}-src.tar.gz
Patch0:         tuxguitar-default-soundfont.patch
Patch1:         no-vst.patch
Patch2:         tuxguitar-additional-arch.patch
Patch3:         tuxguitar-startscript.patch
Patch4:         no-fluidsynth.patch
Patch5:         tuxguitar-startscript-itext.patch
BuildRequires:  alsa-devel
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  desktop-file-utils
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  java-devel >= 1.7
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  maven-local
BuildRequires:  update-desktop-files
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.eclipse.swt:org.eclipse.swt)
Requires:       apache-commons-compress
Requires:       eclipse-swt
Recommends:     snd_sf2
Recommends:     timidity
%ifarch %{ix86}
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  fluidsynth-devel
%endif
%if %{with itext}
BuildRequires:  mvn(com.itextpdf.tool:xmlworker)
BuildRequires:  mvn(com.itextpdf:itextpdf)
%endif
# use FluidR3_GM.sf2 (from fluid-soundfont-gm) as default sound font
%if 0%{?suse_version} <= 1320
Requires:       fluid-soundfont-gm
%else
Suggests:       fluid-soundfont-gm
%endif

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management,
tempo management, gp3/gp4/gp5 import and export.

%prep
%setup -q -n %{name}-%{version}-src
find . -name "*.exe" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.sf2" -print -delete
find . -name "*.jar" -print -delete
find . -name "*.so" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?suse_version} < 1500
%patch4 -p1
%endif
%if %{with itext}
%patch5 -p1
%else
%pom_remove_dep -r com.itextpdf:itextpdf
%pom_remove_dep -r com.itextpdf.tool:xmlworker
%pom_remove_dep -r com.itextpdf:itextpdf build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r com.itextpdf.tool:xmlworker build-scripts/%{name}-linux-%{bit}
%pom_disable_module ../../TuxGuitar-pdf build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r :tuxguitar-pdf
%pom_disable_module ../../TuxGuitar-pdf-ui build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r :tuxguitar-pdf-ui
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='itextpdf']]" build-scripts/%{name}-linux-%{bit}
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='xmlworker']]" build-scripts/%{name}-linux-%{bit}
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='tuxguitar-pdf']]" build-scripts/%{name}-linux-%{bit}
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='tuxguitar-pdf-ui']]" build-scripts/%{name}-linux-%{bit}
%endif

%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt
%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt build-scripts/%{name}-linux-%{bit}
%pom_change_dep :org.eclipse.swt.gtk.linux.x86 :org.eclipse.swt
%pom_remove_dep :org.eclipse.swt.gtk.linux.x86_64
%pom_remove_dep :org.eclipse.swt.gtk.linux.ppc
%pom_remove_dep :org.eclipse.swt.win32.win32.x86
%pom_remove_dep :org.eclipse.swt.cocoa.macosx
%pom_remove_dep :org.eclipse.swt.cocoa.macosx.x86_64
%pom_remove_dep :org.eclipse.swt.carbon.macosx

%pom_xpath_inject pom:modules "<module>../../TuxGuitar-tray</module>
 <module>../../TuxGuitar-viewer</module>"  build-scripts/%{name}-linux-%{bit}

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8" . TuxGuitar-lib
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8" . TuxGuitar-lib

%build
%{mvn_build} -j -f -- \
    -e -f build-scripts/%{name}-linux-%{bit}/pom.xml \
    -Dproject.build.sourceEncoding=UTF-8 -Dnative-modules=true

%install
%mvn_install
# install jnis we built
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a TuxGuitar-*/jni/*.so %{buildroot}%{_libdir}/%{name}/

# Launch script
mkdir -p %{buildroot}/%{_bindir}
cp -a misc/tuxguitar.sh %{buildroot}/%{_bindir}/%{name}
perl -pi -e 's#/usr/lib64/%{name}#%{_libdir}/%{name}#g' %{buildroot}/%{_bindir}/%{name}

# Fix permissions
chmod 755 %{buildroot}/%{_bindir}/%{name}
chmod 755 %{buildroot}%{_libdir}/%{name}/*.so

# mime types
mkdir -p %{buildroot}/%{_datadir}/mime/packages/
cp -a misc/tuxguitar.xml %{buildroot}/%{_datadir}/mime/packages/

# data files
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a TuxGuitar/share/* %{buildroot}/%{_datadir}/%{name}
cp -a misc/tuxguitar.tg %{buildroot}/%{_datadir}/%{name}
cp -a build-scripts/%{name}-linux-%{bit}/target/%{name}-%{version}-linux-%{bit}/dist/* %{buildroot}/%{_datadir}/%{name}

STYLE=Oxygen

for dim in 16 24 32 48 64 96; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/apps/
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/apps/%{name}.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-%{name}.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-gtp.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-ptb.png
done

# desktop files
install -dm 755 %{buildroot}/%{_datadir}/applications
install -pm 644 misc/tuxguitar.desktop %{buildroot}/%{_datadir}/applications/

#install also big icon
install -D -m 644 TuxGuitar/share/skins/Lavender/icon-48x48.png %{buildroot}%{_datadir}/pixmaps/tuxguitar.png
%suse_update_desktop_file -n -i tuxguitar AudioVideo Music Java

# man page
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a misc/%{name}.1 %{buildroot}/%{_mandir}/man1/

%fdupes -s %{buildroot}

ln -sf %{_jnidir}/%{name}/%{name}-alsa.jar %{buildroot}%{_javadir}/%{name}/
%if 0%{?suse_version} >= 1500
ln -sf %{_jnidir}/%{name}/%{name}-fluidsynth.jar %{buildroot}%{_javadir}/%{name}/
%endif
ln -sf %{_jnidir}/%{name}/%{name}-jack.jar %{buildroot}%{_javadir}/%{name}/
ln -sf %{_jnidir}/%{name}/%{name}-oss.jar %{buildroot}%{_javadir}/%{name}/

%files -f .mfiles
%license LICENSE
%doc AUTHORS CHANGES README
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%{_javadir}/%{name}/tuxguitar-alsa.jar
%if 0%{?suse_version} >= 1500
%{_javadir}/%{name}/tuxguitar-fluidsynth.jar
%endif
%{_javadir}/%{name}/tuxguitar-jack.jar
%{_javadir}/%{name}/tuxguitar-oss.jar

%changelog
