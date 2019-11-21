#
# spec file for package scilab
#
# Copyright (c) 2019 SUSE LLC
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


%define sover 6
%define soname lib%{name}%{sover}
#%%define beta_version 5.5.0-beta-1

Name:           scilab
Summary:        High Level Programming Language/Numerical Analysis Software
License:        GPL-2.0-only AND BSD-3-Clause
Group:          Productivity/Scientific/Math
Version:        6.0.2
Release:        0
URL:            http://www.scilab.org
# FOR STABLE RELEASE
Source0:        http://www.scilab.org/download/%{version}/%{name}-%{version}-src.tar.gz
# FOR BETA RELEASE
#Source0:        http://www.scilab.org/download/%%{beta_version}/%%{name}-%%{beta_version}-src.tar.gz
Source1:        %{name}-rpmlintrc

Patch0:         scilab-ocaml.patch
# Bug 767102 - help() should suggest scilab-doc
Patch1:         %{name}-0001-Use-pkcon-to-install-doc-package.patch
# PATCH-FIX-UPSTREAM scilab-fix-64bit-portability-issue.patch badshah400@gmail.com -- Fix compiler warnings w.r.t 64bit portability
Patch3:         scilab-fix-64bit-portability-issue.patch
# PATCH-FIX-OPENSUSE scilab-special-jarnames.patch badshah400@gmail.com -- Adapt configure script for a few java library names peculiar to openSUSE
Patch5:         scilab-special-jarnames.patch
# PATCH-FIX-UPSTREAM scilab-build-with-jogl-gluegen-2.3.patch badshah400@gmail.com -- Make scilab build with jogl and gluegen >= 2.3.0
Patch8:         scilab-build-with-jogl-2.3.patch
# PATCH-FIX-OPENSUSE scilab-timestamp.patch olaf@aepfle.de -- Remove timestamps from binaries
Patch9:         scilab-timestamp.patch
# PATCH-FIX-UPSTREAM scilab-no-return-in-non-void.patch badshah400@gmail.com -- Fix non-void functions that do not return
Patch17:        scilab-no-return-in-non-void.patch
# PATCH-FIX-UPSTREAM scilab-openjdk9-no-javah.patch badshah400@opensuse.org -- Ignore missing javah for openjdk 9+: set it to javac -h directly
Patch21:        scilab-openjdk9-no-javah.patch
# PATCH-FIX-UPSTREAM scilab-bin-correct-java9-path.patch badshah400@gmail.com -- Fix scilab binary to look for libjava.so in the correct location according to java >=9 specifications
Patch23:        scilab-bin-correct-java9-path.patch
# PATCH-FIX-UPSTREAM scilab-xcos-java9.patch badshah400@gmail.com -- Fix compilation of xcos against openjdk-java 9; patch sent upstream
Patch24:        scilab-xcos-java9.patch
# PATCH-FIX-UPSTREAM scilab-java9-ClassLoader.patch badshah400@gmail.com -- Hack frontloading of all necessary jar classpaths by passing them to _JAVA_OPTIONS since dynamic classpath loading doesn not work any more; see http://mailinglists.scilab.org/Scilab-GUI-and-adv-cli-fail-to-launch-with-java-9-td4037645.html
Patch25:        scilab-java9-ClassLoader.patch
# PATCH-FIX-OPENSUSE  scilab-java_source_target.patch fridrich.strba@suse.com -- Build with source and target 6 in order to avoid runtime errors of unrecognized bytecode 
Patch26:        scilab-java_source_target.patch
# PATCH-FIX-UPSTREAM scilab-drop-javax-annotation.patch badshah400@gmail.com -- Remove references to javax.annotation as it is unavailable with java >= 11 and the code referencing this doesn't do anything anyway
Patch27:        scilab-drop-javax-annotation.patch
# PATCH-FIX-OPENSUSE scilab-fix-build-with-modern-lucene.patch - Build against lucene 7
Patch28:        scilab-fix-build-with-modern-lucene.patch
ExcludeArch:    i586 ppc64

# SECTION Dependency to rebuild configure after patching autotools files
BuildRequires:  libtool
# /SECTION

# Dependencies are extracted from :
# "http://wiki.scilab.org/Dependencies of Scilab 5.X"
# Mandatory
%if 0%{?suse_version} > 1500
BuildRequires:  asm5
%else
BuildRequires:  asm2
%endif
BuildRequires:  eigen3-devel >= 3.3.2
BuildRequires:  f2c
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  time

## for dynamic link features
Requires:       gcc
Requires:       gcc-c++
Requires:       gcc-fortran
# Core
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel

# Numerical libraries
# see "http://wiki.scilab.org/Linalg performances"
BuildRequires:  arpack-ng-devel
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
BuildRequires:  libarpack2

# GUI/Console
BuildRequires:  ant
BuildRequires:  ecj
BuildRequires:  java-devel >= 11
BuildRequires:  jpackage-utils
BuildRequires:  lucene >= 6.0
BuildRequires:  lucene-analyzers-common >= 6.0
BuildRequires:  lucene-queryparser >= 6.0

Requires:       ecj
Requires:       java >= 11
Requires:       lucene >= 6.0
Requires:       lucene-analyzers-common >= 6.0
Requires:       lucene-queryparser >= 6.0

BuildRequires:  Mesa-devel
BuildRequires:  flexdock
BuildRequires:  jogl2 >= 2.2.4

Requires:       flexdock
Requires:       jogl2 >= 2.2.4

BuildRequires:  jrosetta
Requires:       jrosetta

BuildRequires:  apache-commons-logging
BuildRequires:  batik
BuildRequires:  fop
BuildRequires:  javahelp2
BuildRequires:  jeuclid
BuildRequires:  jgraphx >= 2.0.0.1
BuildRequires:  jlatexmath
BuildRequires:  jlatexmath-fop
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xmlgraphics-commons
BuildRequires:  xmlgraphics-fop

Requires:       apache-commons-logging
Requires:       batik
Requires:       fop
Requires:       javahelp2
Requires:       jeuclid
Requires:       jgraphx >= 2.0.0.1
Requires:       jlatexmath
Requires:       jlatexmath-fop
Requires:       xmlgraphics-commons
Requires:       xmlgraphics-fop

# TCL/TK features
BuildRequires:  tcl-devel
BuildRequires:  tk-devel

Requires:       bwidget
Requires:       tcl
Requires:       tk

# Modelica
BuildRequires:  ocaml
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(num)

# Documentation
BuildRequires:  saxon9
Requires:       saxon9
#BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  liberation-fonts
# make doc now requires access to display
BuildRequires:  Mesa-libGL-devel
BuildRequires:  xorg-x11-server
%define         X_display         ":98"

# QA tests and validation
BuildRequires:  ant-junit
# FIXME: Disable until cobertura and checkstyle builds for >= openSUSE 13.1 are fixed
%if 0%{?suse_version} <= 1230
BuildRequires:  checkstyle
BuildRequires:  cobertura
BuildRequires:  objectweb-asm
%endif
BuildRequires:  junit4

# All optional dependencies are needed to provide a full-featured Scilab
BuildRequires:  fftw-devel
BuildRequires:  gettext-devel
BuildRequires:  hdf5-devel
BuildRequires:  libmatio-devel
BuildRequires:  suitesparse-devel

# hdf5 does not bump soname but check at runtime
Requires:       hdf5 = %{_hdf5_version}

# Specific dependencies for packaging purpose
BuildRequires:  fdupes
BuildRequires:  update-desktop-files

# scilab parts
Requires:       scilab-devel = %{version}
Requires:       scilab-modules = %{version}

Recommends:     scilab-lang = %{version}

Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme

%description
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

%package -n     %{soname}
Summary:        Scientific software package for numerical computations (shared libraries)
Group:          Development/Libraries/Other

%description -n %{soname}
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

This package provides the shared libraries required by scilab and scilab-devel.


%package        devel
Summary:        Scientific software package for numerical computations (include files)
Group:          Development/Languages/C and C++
Requires:       %{soname} = %{version}
Requires:       libSM-devel
Requires:       libxml2-devel
Requires:       ncurses-devel
Requires:       pcre-devel
Requires:       pkg-config
Requires:       tcl-devel
Requires:       tk-devel

%description    devel
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

This package provides files for coding in C/C++ with Scilab.

%package        modules
Summary:        Scilab modules
Group:          Productivity/Scientific/Other
BuildArch:      noarch
Requires:       scilab = %{version}
Recommends:     scilab-modules-doc = %{version}

%description    modules
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

This package provides Scilab modules.

%package        modules-doc
Summary:        Documentation for Scilab modules
Group:          Documentation/Other
BuildArch:      noarch
Requires:       %{name} = %{version}
Recommends:     %{name}-modules-doc-lang = %{version}

%description    modules-doc
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

This package provides documentation files for Scilab modules.

%package        tests
Summary:        Provides test files for Scilab
Group:          Development/Tools/Other
BuildArch:      noarch
Requires:       %{name} = %{version}
# Requires:       testng

%description    tests
Scilab is the free software for numerical computation providing a powerful
computing environment for engineering and scientific applications. It
includes hundreds of mathematical functions. It has a high level programming
language allowing access to advanced data structures, 2-D and 3-D graphical
functions.

This package provides test files for Scilab.

%lang_package
%lang_package -n %{name}-modules-doc

%prep
%autosetup -p1

%build
# Remove a bad merge remnant (.orig file) to prevent trigerring rpmlint's suse-filelist-forbidden
rm ./modules/cacsd/tests/unit_tests/dscr.tst.orig

# Fix Class-Path in manifest
sed -i '/name="Class-Path"/d' build.incl.xml
sed -i '/name="Class-Path"/d' modules/javasci/build.xml
sed -i '/name="Class-Path"/d' modules/scirenderer/build.xml

autoreconf -fvi
%configure \
    --disable-static-system-lib \
    --without-umfpack \
    --without-emf \
    --with-xcos

make -C modules/scicos modelicac modelicat XML2Modelica
make %{?_smp_mflags}

# SECTION SED HACK TO FRONTLOAD ALL NECESSARY JARS WHEN STARTING SCILAB
# See discussion http://mailinglists.scilab.org/Scilab-GUI-and-adv-cli-fail-to-launch-with-java-9-td4037645.html
export SCI_ALL_JAR_CLASSPATHS=`grep -Eo "\".*.jar" etc/classpath.xml | sed 's/$SCILAB/$SCI/' | tr -d "\"" | tr "\n" ":"`
sed -i "s|@SPEC_ALL_JAR_CLASSPATHS@|${SCI_ALL_JAR_CLASSPATHS}|" bin/scilab
export SCI_LIB_PATH=%{_libdir}/scilab
sed -i "s|@SPEC_SCI_LIB_PATH@|${SCI_LIB_PATH}|" bin/scilab
# /SECTION

export DISPLAY=%%{X_display}
Xvfb %%{X_display} >& Xvfb.log &
sleep 5
export SCI_ALL_JAR_CLASSPATHS=`grep -Eo "\".*.jar" etc/classpath.xml | sed 's/$SCILAB/./' | tr -d "\"" | tr "\n" ":"`
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:./modules/*/.libs:./modules/.libs
export _JAVA_OPTIONS="--add-modules=java.xml.bind,java.activation -Djava.awt.headless=true -Djava.class.path=${SCI_ALL_JAR_CLASSPATHS}"
make doc SCIVERBOSE=1

%install
make install DESTDIR=%{buildroot}

# Install .conf file so that ldconfig can find shared libs in non-std location
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf

# remove docs packaged using %%doc
rm -rf %{buildroot}%{_datadir}/scilab/ACK*
rm -rf %{buildroot}%{_datadir}/scilab/CHANGES*
rm -rf %{buildroot}%{_datadir}/scilab/COPYING*
rm -rf %{buildroot}%{_datadir}/scilab/README*
rm -rf %{buildroot}%{_datadir}/scilab/RELEASE*
rm -rf %{buildroot}%{_datadir}/scilab/Readme_Visual.txt
rm -rf %{buildroot}%{_datadir}/scilab/license.txt

# Remove more advanced repl, user should use CLI options instead
rm -fr %{buildroot}%{_datadir}/applications/%{name}-*.desktop

%suse_update_desktop_file -i scilab
%suse_update_desktop_file -i scinotes
%suse_update_desktop_file -i -r xcos Education Math Physics

%find_lang %{name} %{?no_lang_C}

# Remove la files
rm -fr %{buildroot}%{_libdir}/%{name}/*.la

# Add localized help files to scilab-doc.lang
# adapted from find-lang.sh
# always provide the english help to handle missing localized help pages
find %{buildroot}%{_datadir}/%{name}/modules/helptools/jar -type f -o -type l|sed '
s:'"%{buildroot}"'::
s:\(.*/'"%{name}"'_\)\([^\._]\+\)\(.*\.jar$\):%lang(\2) \1\2\3:
s:^\([^%].*\)::
s:%lang(en) ::
s:%lang(C) ::
/^$/d' |tee %{name}-modules-doc.lang
## Remove en localization doc files from lang package; bundle these in %%{name}-modules-doc directly
sed -i '/scilab_en_US_help.jar/d' %{name}-modules-doc.lang
sed -i '/scilab_images.jar/d' %{name}-modules-doc.lang

%fdupes %{buildroot}%{_datadir}/%{name}/contrib/
%fdupes %{buildroot}%{_datadir}/%{name}/modules/
%fdupes %{buildroot}%{_datadir}/icons/hicolor/24x24/mimetypes/
# All scilab binaries in %%{_bindir} are essentially the same bash script, (hard) link them
%fdupes %{buildroot}%{_bindir}/

# FIXME: Disable tests until checkstyle and cobertura builds are fixed for openSUSE >= 13.1
# FIXME: Weird jvm crashes causes a test to fail, disable for openSUSE 12.3 also for now
%if 0%{?suse_version} < 1230
%check
echo $MALLOC_CHECK_
echo $MALLOC_PERTURB_
make check
%endif

%post -n %{soname} -p /sbin/ldconfig

%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.*

%files
%doc ACKNOWLEDGEMENTS
%doc README.md CHANGES.md
%license COPYING COPYING-BSD
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/etc/
%{_datadir}/%{name}/Version.incl
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}/contrib
%{_datadir}/%{name}/tools
%dir %{_datadir}/appdata
%{_datadir}/appdata/scilab.appdata.xml

%files lang -f %{name}.lang

%files modules
%{_datadir}/%{name}/modules/
# part of scilab-doc
%exclude %{_datadir}/%{name}/modules/helptools/jar/%{name}_*.jar
%exclude %{_datadir}/%{name}/modules/*/examples
%exclude %{_datadir}/%{name}/modules/*/help
# part of scilab-tests
%exclude %{_datadir}/%{name}/modules/*/tests

%files modules-doc
%{_datadir}/%{name}/modules/*/examples
%{_datadir}/%{name}/modules/*/help
%{_datadir}/%{name}/modules/helptools/jar/%{name}_images.jar
%{_datadir}/%{name}/modules/helptools/jar/%{name}_en_US_help.jar

%files modules-doc-lang -f %{name}-modules-doc.lang

%files devel
%license COPYING COPYING-BSD
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf

%files tests
%{_datadir}/%{name}/modules/*/tests

%changelog
