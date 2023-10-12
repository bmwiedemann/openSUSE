#
# spec file for package tuxguitar
#
# Copyright (c) 2023 SUSE LLC
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
%ifarch riscv64
%global bit riscv64
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
Version:        1.6.0
Release:        0
Summary:        A multitrack tablature editor and player written in Java-SWT
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/helge17/tuxguitar
Source0:        https://github.com/helge17/tuxguitar/archive/refs/tags/%{version}.tar.gz
Patch0:         0001-tuxguitar-aarch64.patch
Patch1:         0002-tuxguitar-armv6hl.patch
Patch2:         0003-tuxguitar-armv7hl.patch
Patch3:         0004-tuxguitar-ppc64.patch
Patch4:         0005-tuxguitar-ppc64le.patch
Patch5:         0006-tuxguitar-riscv64.patch
Patch6:         0007-tuxguitar-s390x.patch
Patch7:         0008-tuxguitar-x86.patch
Patch10:        0009-no-vst.patch
Patch11:        0010-no-lv2.patch
Patch12:        0011-no-fluidsynth.patch
Patch20:        0012-default-soundfont.patch
Patch21:        0013-startscript.patch
Patch22:        0014-desktop.patch
Patch30:        tuxguitar-CVE-2020-13940.patch
BuildRequires:  alsa-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  maven-local
BuildRequires:  update-desktop-files
BuildRequires:  mvn(com.itextpdf:itextpdf)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.eclipse.swt:org.eclipse.swt)
Requires:       apache-commons-compress
Requires:       eclipse-swt >= 4.13
Recommends:     snd_sf2
Recommends:     timidity
Suggests:       fluid-soundfont-gm
%if 0%{?suse_version} >= 1500
BuildRequires:  fluidsynth-devel
BuildRequires:  liblilv-0-devel
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  suil-devel
%endif

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management,
tempo management, gp3/gp4/gp5/gpx import and export.

%prep
%setup -q
find . -name "*.exe" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.sf2" -print -delete
find . -name "*.jar" -print -delete
find . -name "*.so" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# In source archive, all modules have an attribute "VERSION" set to "SNAPSHOT"
# this attribute is set during build/delivery
# Refer to application delivery process :
#   https://github.com/helge17/tuxguitar/blob/9d40a35ffc906fd0479b4c47aff00e048daac220/misc/build_tuxguitar_from_source.sh#L118
find . \( -name "*.xml" -or -name "*.gradle"  -or -name "*.properties" -or -name control -or -name Info.plist \) -and -type f -exec sed -i "s/SNAPSHOT/%{version}/" '{}' \;
sed -i "s/static final String RELEASE_NAME =.*/static final String RELEASE_NAME = (TGApplication.NAME + \" %{version}\");/" TuxGuitar/src/org/herac/tuxguitar/app/view/dialog/about/TGAboutDialog.java

%patch10 -p1
%if 0%{?suse_version} <= 1500
%patch11 -p1
%endif
%if 0%{?suse_version} < 1500
%patch12 -p1
%endif

%patch20 -p1
%patch21 -p1
%patch22 -p1

%patch30 -p1

%pom_xpath_remove "pom:profile[pom:id[text()='platform-windows-swt-all']]"
%pom_xpath_remove "pom:profile[pom:id[text()='platform-macos-swt-cocoa-64']]"
%pom_xpath_remove "pom:profile[pom:id[text()='platform-freebsd-swt-x86_64']]"
%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt
%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt build-scripts/%{name}-linux-swt-%{bit}
%pom_xpath_remove "pom:artifactItem[pom:destFileName[text()='swt.jar']]" build-scripts/%{name}-linux-swt-%{bit}
%pom_remove_dep :org.eclipse.swt.gtk.linux.x86_64
%pom_remove_dep :org.eclipse.swt.win32.win32.x86_64
%pom_remove_dep :org.eclipse.swt.cocoa.macosx.x86_64
%pom_xpath_inject pom:modules "<module>../../TuxGuitar-viewer</module>" build-scripts/%{name}-linux-swt-%{bit}

%build
%{mvn_build} -j -f -- \
    -e -f build-scripts/%{name}-linux-swt-%{bit}/pom.xml \
    -Dproject.build.sourceEncoding=UTF-8 -Dnative-modules=true

%install
%mvn_install

# install jnis we built
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a build-scripts/native-modules/*/target/build/lib/*.so %{buildroot}%{_libdir}/%{name}/

# Launch script
mkdir -p %{buildroot}/%{_bindir}
cat build-scripts/common-resources/common-linux/tuxguitar.sh | sed 's#@LIBDIR@#%{_libdir}#g' > %{buildroot}/%{_bindir}/%{name}

# Fix permissions
chmod 755 %{buildroot}/%{_bindir}/%{name}
chmod 755 %{buildroot}%{_libdir}/%{name}/*.so

# mime types
mkdir -p %{buildroot}/%{_datadir}/mime/packages/
cp -a build-scripts/common-resources/common-linux/share/mime/packages/tuxguitar.xml %{buildroot}/%{_datadir}/mime/packages/

# data files
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a TuxGuitar/share/* %{buildroot}/%{_datadir}/%{name}
cp -a misc/tuxguitar.tg %{buildroot}/%{_datadir}/%{name}
cp -a build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/dist/* %{buildroot}/%{_datadir}/%{name}

# desktop files
install -dm 755 %{buildroot}/%{_datadir}/applications
install -pm 644 build-scripts/common-resources/common-linux/share/applications/tuxguitar.desktop %{buildroot}/%{_datadir}/applications/

# icon
install -D -m 644 build-scripts/common-resources/common-linux/share/pixmaps/tuxguitar.xpm %{buildroot}%{_datadir}/pixmaps/tuxguitar.xpm
%suse_update_desktop_file -n -i tuxguitar AudioVideo Music Java

# man page
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a build-scripts/common-resources/common-linux/share/man/man1/%{name}.1 %{buildroot}/%{_mandir}/man1/

%fdupes -s %{buildroot}

ln -sf %{_jnidir}/%{name}/%{name}-alsa.jar %{buildroot}%{_javadir}/%{name}/
ln -sf %{_jnidir}/%{name}/%{name}-jack.jar %{buildroot}%{_javadir}/%{name}/
%if 0%{?suse_version} >= 1500
ln -sf %{_jnidir}/%{name}/%{name}-fluidsynth.jar %{buildroot}%{_javadir}/%{name}/
%endif
%if 0%{?suse_version} > 1500
ln -sf %{_jnidir}/%{name}/%{name}-synth-lv2.jar %{buildroot}%{_javadir}/%{name}/
%endif

%files -f .mfiles
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/mime/packages/%{name}.xml
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_javadir}/%{name}/tuxguitar-alsa.jar
%{_javadir}/%{name}/tuxguitar-jack.jar
%if 0%{?suse_version} >= 1500
%{_javadir}/%{name}/tuxguitar-fluidsynth.jar
%endif
%if 0%{?suse_version} > 1500
%{_javadir}/%{name}/tuxguitar-synth-lv2.jar
%endif

%changelog
