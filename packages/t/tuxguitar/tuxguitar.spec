#
# spec file for package tuxguitar
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Summary:        A multitrack tablature editor and player written in Java-SWT
License:        LGPL-2.1+
Group:          Applications/Multimedia
Name:           tuxguitar
Version:        1.4
Release:        0
Url:            http://www.tuxguitar.pw
# Source file cleaned of potentially proprietary SF2, DLL, EXE files:
#   wget -N http://downloads.sourceforge.net/tuxguitar/tuxguitar-1.4-src.tar.gz
#   tar zxf tuxguitar-1.4-src.tar.gz
#   find tuxguitar-1.4-src -name "*.exe" -exec rm {} \;
#   find tuxguitar-1.4-src -name "*.dll" -exec rm {} \;
#   find tuxguitar-1.4-src -name "*.sf2" -exec rm {} \;
#   tar zcf tuxguitar-1.4-src-clean.tar.gz tuxguitar-1.4-src
Source0:        %{name}-%{version}-src-clean.tar.gz
Patch0:         tuxguitar-startscript.patch
Patch1:         tuxguitar-default-soundfont.patch
Patch2:         tuxguitar-jsa-build.patch
Patch3:         tuxguitar-tray-build.patch
Patch4:         tuxguitar-do-not-force-java-1.5.patch

Requires:       eclipse-swt
Requires:       java >= 1.7
Requires:       javapackages-tools
# use FluidR3_GM.sf2 (from fluid-soundfont-gm) as default sound font
%if 0%{?suse_version} <= 1320
Requires:       fluid-soundfont-gm
%else
Suggests:       fluid-soundfont-gm
%endif
Recommends:     timidity
Recommends:     snd_sf2
# export to PDF feature requires itext
#Requires:         itext
#BuildRequires:    itext
BuildRequires:  alsa-devel
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  desktop-file-utils
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1320
BuildRequires:  fluidsynth-devel
%endif
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-tools
BuildRequires:  update-desktop-files

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management, 
tempo management, gp3/gp4/gp5 import and export.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Set debug="true" on javac part of the build scripts.
for file in $(find . -name build.xml); do
   sed -i 's|debug="false"|debug="true"|' $file
done

# Don't force compiling with JAVA 1.5
find . -wholename "./*/build.properties" -exec sed -re "s/^ant.build.javac.source=1.5/#ant.build.javac.source=1.5/" -i {} \;
find . -wholename "./*/build.properties" -exec sed -re "s/^ant.build.javac.target=1.5/#ant.build.javac.target=1.5/" -i {} \;
# Fix build.properties files by providing paths to required jar files
sed "s/TuxGuitar-ui-toolkit\/tuxguitar-ui-toolkit-swt.jar/TuxGuitar-ui-toolkit-swt\/tuxguitar-ui-toolkit-swt.jar/" \
 -i TuxGuitar-image/build.properties
sed "s/TuxGuitar-ui-toolkit\/tuxguitar-ui-toolkit-swt.jar/TuxGuitar-ui-toolkit-swt\/tuxguitar-ui-toolkit-swt.jar/" \
 -i TuxGuitar-tray/build.properties
echo "path.tuxguitar-editor-utils=../TuxGuitar-editor-utils/tuxguitar-editor-utils.jar" \
 >> TuxGuitar-tray/build.properties
echo -e "\npath.tuxguitar-editor-utils=../TuxGuitar-editor-utils/tuxguitar-editor-utils.jar" \
 >> TuxGuitar-tray/build.properties
echo "path.tuxguitar-editor-utils=../TuxGuitar-editor-utils/tuxguitar-editor-utils.jar" \
 >> TuxGuitar-jsa/build.properties
# Use fluidsynth by default
%if 0%{?suse_version} <= 1320
sed "s/tuxguitar-fluidsynth.enabled=false/tuxguitar-fluidsynth.enabled=true/" \
 -i build-scripts/common-resources/common-linux/dist/tuxguitar-plugin-settings.cfg
sed -re "s/midi.port=.*$/midi.port=tuxguitar-fluidsynth_\/usr\/share\/sounds\/sf2\/FluidR3_GM.sf2/" \
 -i build-scripts/common-resources/common-linux/dist/tuxguitar.cfg
%endif
# Update URL
sed "s/www.tuxguitar.com.ar/www.tuxguitar.pw/" -i TuxGuitar/dist/about_description.dist
# Remove duplicated files
rm -fr TuxGuitar/doc
rm -f TuxGuitar/dist/tuxguitar.cfg
# Remove not needed file
rm -f TuxGuitar/share/lang/toutf.pl

%build
# Plugins to build:
%if 0%{?suse_version} <= 1320
PLUGINS="alsa ascii browser-ftp compat converter fluidsynth gervill gm-settings gpx gtp \
         image jack jsa lilypond midi musicxml oss ptb svg tef tray tuner viewer"
%else
#remove "fluidsynth"
PLUGINS="alsa ascii browser-ftp compat converter gervill gm-settings gpx gtp \
         image jack jsa lilypond midi musicxml oss ptb svg tef tray tuner viewer"
%endif
# FIXME: "pdf" plugin requires itext, but even after adding itext 1.4 from Education repo:
# error: package com.itextpdf.text does not exist

# JNI's to build
%if 0%{?suse_version} <= 1320
JNIS="alsa fluidsynth jack oss"
%else
JNIS="alsa jack oss"
%endif
LIBSUFFIX=$(echo %{_lib}|sed 's|lib||')

# to pass to ant:
ANT_FLAGS=" \
   -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
   -Dpath.tuxguitar=$PWD/TuxGuitar/%{name}.jar \
   -Dpath.swt=%{_libdir}/java/swt.jar \
   -Dlib.swt.jar=%{_libdir}/java/swt.jar \
   -Ddist.lib.path=%{_libdir}/%{name}/ \
   -Ddist.jar.path=%{_datadir}/%{name}/ \
   -Ddist.share.path=%{_datadir}/%{name}/ \
   -Dos.bin.dir=%{_bindir} \
   -Dos.lib.suffix=$LIBSUFFIX \
   -Dos.data.dir=%{_datadir}/ \
   -Ddist.default.style=Oxygen \
   -Ddist.default.song=%{_datadir}/%{name}/%{name}.tg"
#   -Dpath.itext=% {_javadir}/itext.jar \

# build jars
ant -f TuxGuitar-lib/build.xml -v -d $ANT_FLAGS all
ant -f TuxGuitar-editor-utils/build.xml -v -d $ANT_FLAGS all
ant -f TuxGuitar-ui-toolkit/build.xml -v -d $ANT_FLAGS all
ant -f TuxGuitar-ui-toolkit-swt/build.xml -v -d $ANT_FLAGS all
ant -f TuxGuitar/build.xml -v -d $ANT_FLAGS all
ant -f TuxGuitar-gm-utils -v -d $ANT_FLAGS all
for jarname in $PLUGINS; do
   ant -f TuxGuitar-$jarname/build.xml  -v -d $ANT_FLAGS \
      -Dbuild.jar=../TuxGuitar/share/plugins/tuxguitar-$jarname.jar all
done

# build jnis
for jni in $JNIS; do
   make -C TuxGuitar-$jni/jni %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS} \
              -I%{_jvmdir}/java-openjdk/include \
              -I%{_jvmdir}/java-openjdk/include/linux \
              -fPIC"
done

%install
# install main content
install -dm 755 $RPM_BUILD_ROOT/%{_bindir}
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -pm 644 TuxGuitar/dist/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r TuxGuitar/share/* $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -pm 755 misc/%{name}.sh $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -pm 644 misc/%{name}.tg $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{name}.tg
install -pm 644 build-scripts/common-resources/common-linux/dist/*.cfg $RPM_BUILD_ROOT/%{_datadir}/%{name}/
for jardir in TuxGuitar* ; do
 if [ -e $jardir/*jar ]
 then 
  install -m 644 $jardir/*jar  $RPM_BUILD_ROOT/%{_datadir}/%{name}/
 fi
done

# install jnis we built
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a TuxGuitar-*/jni/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/

# mime-type file
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/mime/packages
install -pm 644 misc/%{name}.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages/

# man
install -dm 755 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -pm 644 misc/%{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

# desktop files
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/applications
install -pm 644 misc/tuxguitar.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/

# mime-type icons
for sz in 16 24 32 48 64 96 ; do
  install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes
  install -pm 644 TuxGuitar/share/skins/Lavender/icon-${sz}x${sz}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/audio-x-tuxguitar.png
  install -pm 644 TuxGuitar/share/skins/Lavender/icon-${sz}x${sz}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/audio-x-gtp.png
  install -pm 644 TuxGuitar/share/skins/Lavender/icon-${sz}x${sz}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/audio-x-ptb.png
done

#install also big icon
install -D -m 644 TuxGuitar/share/skins/Lavender/icon-48x48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/tuxguitar.png
%suse_update_desktop_file -n -i tuxguitar AudioVideo Music Java

%fdupes $RPM_BUILD_ROOT

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-desktop-database &> /dev/null

%postun
if [ $1 -eq 0 ] ; then
   touch --no-create %{_datadir}/icons/hicolor &>/dev/null
   gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
   update-mime-database %{_datadir}/mime >& /dev/null ||:
fi
update-desktop-database &> /dev/null

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%files
%defattr(-,root,root,-)
%doc README
%{_mandir}/*/*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml

%changelog
