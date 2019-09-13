#
# spec file for package java-1_7_0-bootstrap
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global debug_package %{nil}
%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
%global jit_arches %{ix86} x86_64 ppc64 ppc64le %{arm} %{aarch64}
# Standard JPackage naming and versioning defines.
%global priority        0
%global javaver         1.7.0
%global buildver        151
# Standard JPackage directories and symbolic links.
%global sdklnk          java-%{javaver}-bootstrap
%global archname        %{sdklnk}
%global jrelnk          jre-%{javaver}-bootstrap
%global sdkdir          %{sdklnk}-%{javaver}
%global jredir          %{sdkdir}/jre
%global sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%global jrebindir       %{_jvmdir}/%{jrelnk}/bin
%global jvmjardir       %{_jvmjardir}/%{sdkdir}
%global jvmjarlink      %{_jvmjardir}/%{sdklnk}
# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0
# cacert symlink
%global cacerts  %{_jvmdir}/%{jredir}/lib/security/cacerts
# real file made by update-ca-certificates
%global javacacerts %{_var}/lib/ca-certificates/java-cacerts
%global arch %{_arch}
%ifnarch %{jit_arches}
%global archinstall %{_arch}
%endif
%ifarch %{ix86}
%global arch i586
%global archinstall i386
%endif
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch %{arm}
%global archinstall arm
%endif
%ifarch %{aarch64}
%global arch aarch64
%global archinstall aarch64
%endif
%ifarch ppc64
%global archinstall ppc64
%endif
%ifarch ppc64le
%global archinstall ppc64le
%endif
# bnc#542545
# 32-bit versus 64-bit specific provides:
%ifarch %{ix86} ppc s390
%global bits 32
%endif
%ifarch x86_64 ia64 s390x
%global bits 64
%endif
%if 0%{?__isa_bits}
%global bits %{__isa_bits}
%endif
%define _unpackaged_files_terminate_build 0
Name:           java-1_7_0-bootstrap
Version:        %{javaver}
Release:        0
Summary:        A bootstrap version of openJDK
License:        GPL-2.0-with-classpath-exception
Group:          Development/Languages/Java
Url:            http://icedtea.classpath.org
Source0:        java-1_7_0-openjdk.i586.rpm
Source1:        java-1_7_0-openjdk-devel.i586.rpm
Source2:        java-1_7_0-openjdk-headless.i586.rpm
Source3:        java-1_7_0-openjdk.x86_64.rpm
Source4:        java-1_7_0-openjdk-devel.x86_64.rpm
Source5:        java-1_7_0-openjdk-headless.x86_64.rpm
Source6:        java-1_7_0-openjdk.s390.rpm
Source7:        java-1_7_0-openjdk-devel.s390.rpm
Source8:        java-1_7_0-openjdk-headless.s390.rpm
Source9:        java-1_7_0-openjdk.s390x.rpm
Source10:       java-1_7_0-openjdk-devel.s390x.rpm
Source11:       java-1_7_0-openjdk-headless.s390x.rpm
Source12:       java-1_7_0-openjdk.ppc.rpm
Source13:       java-1_7_0-openjdk-devel.ppc.rpm
Source14:       java-1_7_0-openjdk-headless.ppc.rpm
Source15:       java-1_7_0-openjdk.ppc64.rpm
Source16:       java-1_7_0-openjdk-devel.ppc64.rpm
Source17:       java-1_7_0-openjdk-headless.ppc64.rpm
Source18:       java-1_7_0-openjdk.ppc64le.rpm
Source19:       java-1_7_0-openjdk-devel.ppc64le.rpm
Source20:       java-1_7_0-openjdk-headless.ppc64le.rpm
Source21:       java-1_7_0-openjdk.aarch64.rpm
Source22:       java-1_7_0-openjdk-devel.aarch64.rpm
Source23:       java-1_7_0-openjdk-headless.aarch64.rpm
Source24:       java-1_7_0-openjdk.arm.rpm
Source25:       java-1_7_0-openjdk-devel.arm.rpm
Source26:       java-1_7_0-openjdk-headless.arm.rpm
NoSource:       0
NoSource:       1
NoSource:       2
NoSource:       3
NoSource:       4
NoSource:       5
NoSource:       6
NoSource:       7
NoSource:       8
NoSource:       9
NoSource:       10
NoSource:       11
NoSource:       12
NoSource:       13
NoSource:       14
NoSource:       15
NoSource:       16
NoSource:       17
NoSource:       18
NoSource:       19
NoSource:       20
NoSource:       21
NoSource:       22
NoSource:       23
NoSource:       24
NoSource:       25
NoSource:       26
BuildRequires:  hicolor-icon-theme
BuildRequires:  jpackage-utils >= 1.7.5
# mozilla-nss has to be installed to prevent
# java.security.ProviderException: Could not initialize NSS
# ...
# java.io.FileNotFoundException: /usr/lib64/libnss3.so
#was bnc#634793
Requires:       mozilla-nss
#require headless subvariant
Requires(pre):  %{name}-headless = %{version}-%{release}
Requires(pre):  update-alternatives
# Standard JPackage base provides.
Provides:       java = %{javaver}
Provides:       java-%{javaver} = %{version}-%{release}
Provides:       java-%{javaver}-openjdk = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{javaver}
Provides:       jre-%{javaver} = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk = %{version}-%{release}
Provides:       jre-openjdk = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       jaas = %{version}
Provides:       java-sasl = %{version}
Provides:       jce = %{version}
Provides:       jdbc-stdext = %{version}
Provides:       jdbc-stdext = 4.1
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}
# Required at least by fop
Provides:       java-%{bits} = %{javaver}
Provides:       java-%{javaver}-%{bits}
Provides:       java-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-%{bits} = %{javaver}
Provides:       jre-%{javaver}-%{bits}
Provides:       jre-%{javaver}-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-openjdk-%{bits} = %{version}-%{release}
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
# runtime certificates generation available in 11.3+ - bnc#596177
%if 0%{?suse_version} >= 1130
Requires(post): file
Requires(post): java-ca-certificates
%else
# the certificates will converted in a prep to standard keystore file - cacerts
# The openssl requirment seems to be necessary for build only.
Requires:       openssl
%endif

%description
A bootstrap version of openJDK

This package is a binary repackaging of existing binaries
for openJDK.  It's used only for bootstrapping new openJDK
versions.

%package headless
Summary:        OpenJDK 7 runtime environment without X, audio and video support
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       java-headless = %{version}-%{release}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-%{javaver}-headless = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{version}-%{release}
Provides:       jre-openjdk-headless = %{version}-%{release}
#FIXME: add extensions provides? Would not it be better to require full JRE?
# from http://en.opensuse.org/openSUSE:Package_dependencies#Splitting_off_a_sub-package
# provides a libjvm.so to ensure update is working well
Provides:       %{name}:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjvm.so

%description headless
SUSE's implementation of the OpenJDK 7 runtime environment.
This build is without X, audio and video support. If you need it,
please install %{name}.

It contains a Java virtual machine, runtime class libraries, and an
Java application launcher that are necessary to run programs written in
the Java programming language. It is not a development environment and
does not contain development tools such as compilers and debuggers. For
development tools, see the %{name}-devel package.

%package devel
Summary:        SUSE's implementation of the OpenJDK 7 Development Environment
Group:          Development/Languages/Java
Requires(pre):  %{_sbindir}/update-alternatives
Requires(pre):  %{name} = %{version}-%{release}
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-%{javaver}-openjdk-devel = %{version}-%{release}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openjdk = %{version}

%description devel
SUSE's implementation of the OpenJDK 7 Development Environment.

It is a development environment for building applications, applets,
and components using the Java programming language.

It includes tools useful for developing and testing programs written
in the Java programming language and running on the Java platform.
These tools are designed to be used from the command line. Except
for the appletviewer, these tools do not provide a graphical user
interface.

%prep

%build
srcdir=`dirname %{SOURCE0}`
cd %{buildroot}
for f in ${srcdir}/java*.%{arch}.rpm; do
  rpm2cpio $f | cpio --extract --unconditional --preserve-modification-time --make-directories
done
for i in `find .%{_datadir}/icons/hicolor/ -name java*.png | xargs`; do
  pushd `dirname $i`
  mv java*.png java-%{javaver}-bootstrap.png
  popd
done
for i in `find . -name \*.desktop | xargs`; do
  sed -i 's#^Icon=java.*$#Icon=java-%{javaver}-bootstrap#g' $i
done
find . -name *openjdk* | sed -e "p;s/openjdk/bootstrap/" | xargs -n2 mv
for i in `find . -type l | xargs`; do
  pushd `dirname $i`
  link=`basename $i`
  target=`readlink $link | sed 's#openjdk#bootstrap#g'`
  rm -f $link
  ln -sf $target $link
  popd
done

%install
export LANG=en_US.UTF-8
#bnc#530046
export STRIP_KEEP_SYMTAB=libjvm*
# skip /usr/lib/rpm/brp-check-bytecode-version:
export NO_BRP_CHECK_BYTECODE_VERSION=true
# and skip pointless debug info stripping
export NO_BRP_STRIP_DEBUG=true

%post headless
ext=.gz
update-alternatives \
  --install %{_bindir}/java java %{jrebindir}/java %{priority} \
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{jrelnk} \
  --slave %{_jvmjardir}/jre jre_exports %{_jvmjardir}/%{jrelnk} \
  --slave %{_bindir}/keytool keytool %{jrebindir}/keytool \
  --slave %{_bindir}/orbd orbd %{jrebindir}/orbd \
  --slave %{_bindir}/policytool policytool %{jrebindir}/policytool \
  --slave %{_bindir}/rmid rmid %{jrebindir}/rmid \
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir}/rmiregistry \
  --slave %{_bindir}/servertool servertool %{jrebindir}/servertool \
  --slave %{_bindir}/tnameserv tnameserv %{jrebindir}/tnameservSuSE/ \
  --slave %{_mandir}/man1/java.1$ext java.1$ext \
  %{_mandir}/man1/java-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \
  %{_mandir}/man1/keytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/orbd.1$ext orbd.1$ext \
  %{_mandir}/man1/orbd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/policytool.1$ext policytool.1$ext \
  %{_mandir}/man1/policytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmid.1$ext rmid.1$ext \
  %{_mandir}/man1/rmid-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \
  %{_mandir}/man1/rmiregistry-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/servertool.1$ext servertool.1$ext \
  %{_mandir}/man1/servertool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/tnameserv.1$ext tnameserv.1$ext \
  %{_mandir}/man1/tnameserv-%{sdklnk}.1$ext  \
  --slave %{_datadir}/applications/policytool.desktop policytool.desktop \
  %{_jvmdir}/%{sdkdir}/jre/lib/desktop/policytool.desktop

update-alternatives \
  --install %{_jvmdir}/jre-openjdk \
  jre_openjdk %{_jvmdir}/%{jrelnk} %{priority} \
  --slave %{_jvmjardir}/jre-openjdk \
  jre_openjdk_exports %{_jvmjardir}/%{jrelnk}
update-alternatives \
  --install %{_jvmdir}/jre-%{javaver} \
  jre_%{javaver} %{_jvmdir}/%{jrelnk} %{priority} \
  --slave %{_jvmjardir}/jre-%{javaver} \
  jre_%{javaver}_exports %{_jvmjardir}/%{jrelnk}

%postun headless
if [ $1 -eq 0 ]
then
  if test -f /proc/sys/fs/binfmt_misc/jarexec
  then
    echo '-1' > /proc/sys/fs/binfmt_misc/jarexec
  fi
  update-alternatives --remove java %{jrebindir}/java
  update-alternatives --remove jre_openjdk %{_jvmdir}/%{jrelnk}
  update-alternatives --remove jre_%{javaver} %{_jvmdir}/%{jrelnk}
fi

%if 0%{?suse_version} >= 1130
%posttrans headless
# bnc#781690#c11: don't trust user defined JAVA_HOME and use the current VM
# XXX: this might conflict between various versions of openjdk
export JAVA_HOME=%{_jvmdir}/%{jrelnk}

# check if the java-cacerts is a valid keystore (bnc#781690)
if [ X"`%{_bindir}/file --mime-type -b %{javacacerts}`" \
    != "Xapplication/x-java-keystore;" ]; then
%if 0%{?suse_version} <= 1310
    # workaround for bnc#847952 - pre 13.1 keyring.jar attempts to load invalid keystore and fail on it
    rm -f "%{javacacerts}"
%endif
    %{_sbindir}/update-ca-certificates
fi

# remove the default empty cacert file, if it's installed
if [ 0`stat -c "%{s}" %{cacerts} 2>/dev/null` = "032" ] ; then
    rm -f %{cacerts}
fi

# if cacerts does exists, neither does not contain/point to a
# valid keystore (bnc#781690) ...
if [ X"`%{_bindir}/file --mime-type -b -L %{cacerts}`" \
    != "Xapplication/x-java-keystore;" ]; then
    # bnc#727223
    rm -f %{cacerts}
    ln -s %{javacacerts} %{cacerts}
fi
%endif

%post devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority} \
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdklnk} \
  --slave %{_jvmjardir}/java java_sdk_exports %{jvmjarlink} \
  --slave %{_bindir}/appletviewer appletviewer %{sdkbindir}/appletviewer \
  --slave %{_bindir}/apt apt %{sdkbindir}/apt \
  --slave %{_bindir}/extcheck extcheck %{sdkbindir}/extcheck \
  --slave %{_bindir}/jar jar %{sdkbindir}/jar \
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir}/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{sdkbindir}/javadoc \
  --slave %{_bindir}/javah javah %{sdkbindir}/javah \
  --slave %{_bindir}/javap javap %{sdkbindir}/javap \
  --slave %{_bindir}/jconsole jconsole %{sdkbindir}/jconsole \
  --slave %{_bindir}/pack200                  pack200                     %{sdkbindir}/pack200 \
  --slave %{_bindir}/unpack200                unpack200                   %{sdkbindir}/unpack200 \
  --slave %{_bindir}/jdb jdb %{sdkbindir}/jdb \
  --slave %{_bindir}/jhat jhat %{sdkbindir}/jhat \
  --slave %{_bindir}/jinfo jinfo %{sdkbindir}/jinfo \
  --slave %{_bindir}/jmap jmap %{sdkbindir}/jmap \
  --slave %{_bindir}/jps jps %{sdkbindir}/jps \
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir}/jrunscript \
  --slave %{_bindir}/jsadebugd jsadebugd %{sdkbindir}/jsadebugd \
  --slave %{_bindir}/jstack jstack %{sdkbindir}/jstack \
  --slave %{_bindir}/jstat jstat %{sdkbindir}/jstat \
  --slave %{_bindir}/jstatd jstatd %{sdkbindir}/jstatd \
  --slave %{_bindir}/native2ascii native2ascii %{sdkbindir}/native2ascii \
  --slave %{_bindir}/rmic rmic %{sdkbindir}/rmic \
  --slave %{_bindir}/schemagen schemagen %{sdkbindir}/schemagen \
  --slave %{_bindir}/serialver serialver %{sdkbindir}/serialver \
  --slave %{_bindir}/wsgen wsgen %{sdkbindir}/wsgen \
  --slave %{_bindir}/wsimport wsimport %{sdkbindir}/wsimport \
  --slave %{_bindir}/xjc xjc %{sdkbindir}/xjc \
  --slave %{_mandir}/man1/appletviewer.1$ext appletviewer.1$ext \
  %{_mandir}/man1/appletviewer-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/apt.1$ext apt.1$ext \
  %{_mandir}/man1/apt-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/extcheck.1$ext extcheck.1$ext \
  %{_mandir}/man1/extcheck-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jar.1$ext jar.1$ext \
  %{_mandir}/man1/jar-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jarsigner.1$ext jarsigner.1$ext \
  %{_mandir}/man1/jarsigner-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javac.1$ext javac.1$ext \
  %{_mandir}/man1/javac-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javadoc.1$ext javadoc.1$ext \
  %{_mandir}/man1/javadoc-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javah.1$ext javah.1$ext \
  %{_mandir}/man1/javah-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javap.1$ext javap.1$ext \
  %{_mandir}/man1/javap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \
  %{_mandir}/man1/jconsole-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \
  %{_mandir}/man1/jcmd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \
  %{_mandir}/man1/jdb-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/pack200.1$ext pack200.1$ext \
  %{_mandir}/man1/pack200-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/unpack200.1$ext unpack200.1$ext \
  %{_mandir}/man1/unpack200-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jhat.1$ext jhat.1$ext \
  %{_mandir}/man1/jhat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \
  %{_mandir}/man1/jinfo-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \
  %{_mandir}/man1/jmap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \
  %{_mandir}/man1/jps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jsadebugd.1$ext jsadebugd.1$ext \
  %{_mandir}/man1/jsadebugd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \
  %{_mandir}/man1/jstack-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \
  %{_mandir}/man1/jstat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \
  %{_mandir}/man1/jstatd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/native2ascii.1$ext native2ascii.1$ext \
  %{_mandir}/man1/native2ascii-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmic.1$ext rmic.1$ext \
  %{_mandir}/man1/rmic-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/schemagen.1$ext schemagen.1$ext \
  %{_mandir}/man1/schemagen-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \
  %{_mandir}/man1/serialver-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/wsgen.1$ext wsgen.1$ext \
  %{_mandir}/man1/wsgen-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/wsimport.1$ext wsimport.1$ext \
  %{_mandir}/man1/wsimport-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/xjc.1$ext xjc.1$ext \
  %{_mandir}/man1/xjc-%{sdklnk}.1$ext \
  --slave %{_datadir}/applications/jconsole.desktop jconsole.desktop \
  %{_jvmdir}/%{sdkdir}/jre/lib/desktop/jconsole.desktop

update-alternatives \
  --install %{_jvmdir}/java-openjdk \
  java_sdk_openjdk %{_jvmdir}/%{sdklnk} %{priority} \
  --slave %{_jvmjardir}/java-openjdk \
  java_sdk_openjdk_exports %{jvmjarlink}
update-alternatives \
  --install %{_jvmdir}/java-%{javaver} \
  java_sdk_%{javaver} %{_jvmdir}/%{sdklnk} %{priority} \
  --slave %{_jvmjardir}/java-%{javaver} \
  java_sdk_%{javaver}_exports %{jvmjarlink}

%postun devel
if [ $1 -eq 0 ]
then
  update-alternatives --remove javac %{sdkbindir}/javac
  update-alternatives --remove java_sdk_openjdk %{_jvmdir}/%{sdklnk}
  update-alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdklnk}
fi

%files
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/xawt
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjsoundalsa.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libsplashscreen.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/xawt/libmawt.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjavagtk.so

%files headless
%dir %{_docdir}/%{name}-headless
%doc %{_docdir}/%{name}-headless/ASSEMBLY_EXCEPTION
%doc %{_docdir}/%{name}-headless/LICENSE
%doc %{_docdir}/%{name}-headless/THIRD_PARTY_README
%dir %{_libdir}/jvm-exports

%dir %{_jvmdir}/%{sdkdir}/jre/lib/desktop/
%{_jvmdir}/%{sdkdir}/jre/lib/desktop/policytool.desktop
%{_datadir}/icons/hicolor/*/apps/java-%{javaver}-bootstrap.png

%{_jvmdir}/java-%{javaver}-bootstrap
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}

%{jvmjarlink}
%{_jvmjardir}/%{sdkdir}
%{_jvmjardir}/%{jrelnk}

%dir %{_jvmdir}/%{sdkdir}/jre/
%dir %{_jvmdir}/%{sdkdir}/jre/bin
%dir %{_jvmdir}/%{sdkdir}/jre/lib
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}
%ifarch %{ix86}
%{_jvmdir}/%{sdkdir}/jre/lib/i386/client/Xusage.txt
%endif
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/headless
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/jli
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/xawt

%attr(775,root,root) %{_jvmdir}/%{sdkdir}/jre/bin/*
# jre/lib
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/*.so

#belongs to full package
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjsoundalsa.so
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libsplashscreen.so
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/xawt/libmawt.so
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjavagtk.so
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libicedtea-sound.so
%exclude %{_jvmdir}/%{sdkdir}/jre/lib/pulseaudio.properties

%ifarch %{ix86}
%dir %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/libjsig.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/libjvm.so
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/Xusage.txt
%endif
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/jli/libjli.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/headless/libmawt.so
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjvm.*
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjsig.so

%config(noreplace) %{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/jvm.cfg

%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/Xusage.txt
%{_jvmdir}/%{sdkdir}/jre/lib/applet/
%{_jvmdir}/%{sdkdir}/jre/lib/cmm/
%{_jvmdir}/%{sdkdir}/jre/lib/ext/
%{_jvmdir}/%{sdkdir}/jre/lib/images/
%dir %{_jvmdir}/%{jredir}/lib/management/
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{sdkdir}/jre/lib/zi/
%{_jvmdir}/%{sdkdir}/jre/lib/*jar
%{_jvmdir}/%{sdkdir}/jre/lib/classlist
%{_jvmdir}/%{sdkdir}/jre/lib/currency.data
%attr(755,root,root) %{_jvmdir}/%{sdkdir}/jre/lib/jexec
%{_jvmdir}/%{sdkdir}/jre/lib/jvm.hprof.txt
%{_jvmdir}/%{sdkdir}/jre/lib/meta-index
%{_jvmdir}/%{sdkdir}/jre/lib/mime.types

%if 0%{?suse_version} <= 1130
%config(noreplace) %{cacerts}
%endif
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.cfg
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/local_policy.jar
#bnc#637224
%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig*bfc
%config(noreplace) %{_jvmdir}/%{jredir}/lib/fontconfig*src
%config(noreplace) %{_jvmdir}/%{jredir}/lib/*.properties
%config(noreplace) %{_jvmdir}/%{jredir}/lib/psfont.properties.ja
%config(noreplace) %{_jvmdir}/%{jredir}/lib/management/*

%{_mandir}/man1/java-%{sdklnk}.1*
%{_mandir}/man1/keytool-%{sdklnk}.1*
%{_mandir}/man1/orbd-%{sdklnk}.1*
%{_mandir}/man1/policytool-%{sdklnk}.1*
%{_mandir}/man1/rmid-%{sdklnk}.1*
%{_mandir}/man1/rmiregistry-%{sdklnk}.1*
%{_mandir}/man1/servertool-%{sdklnk}.1*
%{_mandir}/man1/tnameserv-%{sdklnk}.1*

%files devel

%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib

%attr(755,root,root) %{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*

%{_jvmdir}/%{sdkdir}/jre/lib/desktop/jconsole.desktop

%{_mandir}/man1/appletviewer-%{sdklnk}.1*
%{_mandir}/man1/apt-%{sdklnk}.1*
%{_mandir}/man1/extcheck-%{sdklnk}.1*
%{_mandir}/man1/idlj-%{sdklnk}.1*
%{_mandir}/man1/jar-%{sdklnk}.1*
%{_mandir}/man1/jarsigner-%{sdklnk}.1*
%{_mandir}/man1/javac-%{sdklnk}.1*
%{_mandir}/man1/javadoc-%{sdklnk}.1*
%{_mandir}/man1/javah-%{sdklnk}.1*
%{_mandir}/man1/javap-%{sdklnk}.1*
%{_mandir}/man1/jconsole-%{sdklnk}.1*
%{_mandir}/man1/jcmd-%{sdklnk}.1*
%{_mandir}/man1/pack200-%{sdklnk}.1*
%{_mandir}/man1/unpack200-%{sdklnk}.1*
%{_mandir}/man1/jdb-%{sdklnk}.1*
%{_mandir}/man1/jhat-%{sdklnk}.1*
%{_mandir}/man1/jinfo-%{sdklnk}.1*
%{_mandir}/man1/jmap-%{sdklnk}.1*
%{_mandir}/man1/jps-%{sdklnk}.1*
%{_mandir}/man1/jrunscript-%{sdklnk}.1*
%{_mandir}/man1/jsadebugd-%{sdklnk}.1*
%{_mandir}/man1/jstack-%{sdklnk}.1*
%{_mandir}/man1/jstat-%{sdklnk}.1*
%{_mandir}/man1/jstatd-%{sdklnk}.1*
%{_mandir}/man1/native2ascii-%{sdklnk}.1*
%{_mandir}/man1/rmic-%{sdklnk}.1*
%{_mandir}/man1/schemagen-%{sdklnk}.1*
%{_mandir}/man1/serialver-%{sdklnk}.1*
%{_mandir}/man1/wsgen-%{sdklnk}.1*
%{_mandir}/man1/wsimport-%{sdklnk}.1*
%{_mandir}/man1/xjc-%{sdklnk}.1*

%changelog
