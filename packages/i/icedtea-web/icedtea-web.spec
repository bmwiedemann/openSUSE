#
# spec file for package icedtea-web
#
# Copyright (c) 2024 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags} V=1}
%define javadir     %{_jvmdir}/java
%define jredir      %{_jvmdir}/jre
%define javaplugin  libjavaplugin.so.%{_arch}
%define binsuffix      .itweb
# Alternatives priority
%define priority 18000
Name:           icedtea-web
Version:        1.8.8
Release:        0
Summary:        Java Web Start implementation
License:        GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Languages/Java
URL:            https://github.com/AdoptOpenJDK/IcedTea-Web
Source0:        %{name}-%{version}.tar.xz
Patch0:         icedtea-web-suse-desktop-files.patch
Patch1:         more-java-versions.patch
Patch2:         reproducible-timestamps.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hamcrest
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  procps
BuildRequires:  strip-nondeterminism
BuildRequires:  rhino
BuildRequires:  tagsoup
BuildRequires:  zip
BuildConflicts: java >= 14
BuildConflicts: java-devel >= 14
BuildConflicts: java-headless >= 14
Requires:       java >= 1.8
Requires:       rhino
Requires:       tagsoup
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       %{name}-javadoc
Obsoletes:      java-1_6_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_7_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_8_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_9_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-plugin < 1.8.0
Provides:       java-1_6_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_7_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_8_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_9_0-openjdk-plugin = %{version}-%{release}
Provides:       java-plugin = 1.8.0

%description
The IcedTea-Web project provides a Free Software web browser plugin running
applets written in the Java programming language and an implementation of Java
Web Start, originally based on the NetX project.

%package javadoc
Summary:        Java Web Start and plugin implementation (API documentation)
Group:          Documentation/Other
BuildArch:      noarch

%description javadoc
The IcedTea-Web project provides a Free Software web browser plugin running
applets written in the Java programming language and an implementation of Java
Web Start, originally based on the NetX project.
This package contains API documentation for the %{name} Java Web Start
and plugin implementation.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

rm -rf netx/net/sourceforge/jnlp/NetxPanel.java netx/sun

rm -f netx/net/sourceforge/jnlp/util/WindowsDesktopEntry.java

%build
autoreconf -fiv
export bashcompdir=%{_datadir}/bash-completion/completions
%configure \
    --with-jdk-home=%{javadir} \
    --with-jre-home=%{jredir} \
    --docdir=%{_javadocdir}/%{name} \
    --disable-native-plugin \
    --disable-pluginjar \
    --enable-shell-launchers \
	--with-itw-libs=BUNDLED \
    --enable-docs \
    --with-modularjdk-file=%{_datadir}/%{name} \
    --program-suffix=%{binsuffix} \
    --with-pkgversion=suse-%{release}-%{_arch}

%make_build

%install
%make_install

# Move man pages to a more specific name
mv %{buildroot}/%{_mandir}/man1/javaws.1 %{buildroot}/%{_mandir}/man1/javaws%{binsuffix}.1
mv %{buildroot}/%{_mandir}/man1/itweb-settings.1 %{buildroot}/%{_mandir}/man1/itweb-settings%{binsuffix}.1
mv %{buildroot}/%{_mandir}/man1/policyeditor.1 %{buildroot}/%{_mandir}/man1/policyeditor%{binsuffix}.1

# Install desktop files.
install -d -m 755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications itweb-settings.desktop
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications policyeditor.desktop

# Symlink *.itweb.sh to *.itweb
for i in javaws itweb-settings policyeditor; do
  ln -sf ${i}.itweb.sh %{buildroot}%{_bindir}/${i}.itweb
done

strip-nondeterminism %{buildroot}%{_datadir}/icedtea-web/javaws.jar
%fdupes %{buildroot}

rm -rf %{buildroot}%{_mandir}/*/man1

%posttrans
update-desktop-database &> /dev/null || :
exit 0

%postun
update-desktop-database &> /dev/null || :
exit 0

%files
%{_bindir}/itweb-settings%{binsuffix}*
%{_bindir}/javaws%{binsuffix}*
%{_bindir}/policyeditor%{binsuffix}*
%{_mandir}/man1/*
%{_datadir}/applications/itweb-settings.desktop
%{_datadir}/applications/javaws.desktop
%{_datadir}/applications/policyeditor.desktop
%dir %{_datadir}/icedtea-web
%{_datadir}/icedtea-web/*
%{_datadir}/pixmaps/javaws.png
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/itweb-settings.bash
%{_datadir}/bash-completion/completions/javaws.bash
%{_datadir}/bash-completion/completions/policyeditor.bash
%if %{with plugin}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/IcedTeaPlugin.so
%endif

%files javadoc
%license COPYING
%doc NEWS README
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
