#
# spec file for package icedtea-web
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%bcond_without pack200
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
Patch3:         standalone-pack200.patch
Patch4:         remove-pack200-support.patch
Patch5:         java17.patch
Patch6:         java21.patch
Patch7:         javaws-policy.patch
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
BuildRequires:  rhino
BuildRequires:  tagsoup
BuildRequires:  zip
BuildConflicts: java >= 22
BuildConflicts: java-devel >= 22
BuildConflicts: java-headless >= 22
Requires:       java >= 1.8
Requires:       pack200
Requires:       rhino
Requires:       tagsoup
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
BuildArch:      noarch
%if %{with pack200}
BuildRequires:  pack200
%endif

%description
The IcedTea-Web project provides a Free Software web browser plugin running
applets written in the Java programming language and an implementation of Java
Web Start, originally based on the NetX project.

%package javadoc
Summary:        Java Web Start and plugin implementation (API documentation)
Group:          Documentation/Other

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
%if %{with pack200}
%patch -P 3 -p1
%else
%patch -P 4 -p1
%endif
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1

rm -rf netx/net/sourceforge/jnlp/NetxPanel.java netx/sun

rm -f netx/net/sourceforge/jnlp/util/WindowsDesktopEntry.java

%build
autoreconf -fiv
export bashcompdir=%{_datadir}/bash-completion/completions
%configure \
%if %{with pack200}
    --with-pack200=%{_bindir}/pack200 \
%endif
    --bindir=%{_datadir}/%{name} \
    --disable-native-plugin \
    --disable-pluginjar \
    --docdir=%{_javadocdir}/%{name} \
    --enable-docs \
    --enable-shell-launchers \
    --with-itw-libs=BUNDLED \
    --with-modularjdk-file=%{_datadir}/%{name}

%make_build

%install
%make_install

# Install desktop files.
install -dm 0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications itweb-settings.desktop
desktop-file-install --vendor ''\
  --dir %{buildroot}%{_datadir}/applications policyeditor.desktop

# Symlink the scripts to bin directory
install -dm 0755 %{buildroot}%{_bindir}
for i in javaws itweb-settings policyeditor; do
  ln -sf %{_datadir}/%{name}/${i}.sh %{buildroot}%{_bindir}/${i}
done

# Default security policy file
install -dm 0755 %{buildroot}%{_sysconfdir}/%{name}
install -pm 0644 javaws.policy %{buildroot}%{_sysconfdir}/%{name}/

%fdupes %{buildroot}%{_javadocdir}/%{name}

rm -rf %{buildroot}%{_mandir}/*/man1

%posttrans
update-desktop-database &> /dev/null || :
exit 0

%postun
update-desktop-database &> /dev/null || :
exit 0

%files
%{_bindir}/itweb-settings*
%{_bindir}/javaws*
%{_bindir}/policyeditor*
%{_mandir}/man1/*
%{_datadir}/applications/itweb-settings.desktop
%{_datadir}/applications/javaws.desktop
%{_datadir}/applications/policyeditor.desktop
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/javaws.png
%{_datadir}/bash-completion/completions

%files javadoc
%license COPYING
%doc NEWS README
%{_javadocdir}/%{name}

%changelog
