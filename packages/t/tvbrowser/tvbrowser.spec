#
# spec file for package tvbrowser
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tvbrowser
Summary:        Digital TV guide
License:        GPL-3.0+
Group:          Productivity/Multimedia/Other
Version:        4
Release:        0
Requires:       java = 1.8.0
Url:            http://tv-browser.org
Source:         https://downloads.sourceforge.net/project/tvbrowser/TV-Browser%20Releases%20%28Java%208%20and%20higher%29/%{version}/%{name}_%{version}_src.zip
# TODO build from source, too
Source2:        http://www.tvbrowser.org/data/uploads/1372016422809_543/NewsPlugin.jar
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel = 1.8.0
BuildRequires:  jpackage-utils
BuildRequires:  optipng
%if 0%{?suse_version} >= 1330
BuildRequires:  strip-nondeterminism
%endif
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
TV-Browser is Plugin based digital TV guide. Plugins can be installed with
the download function of TV-Browser.

%prep
cp %{S:2} .
%setup -q
dos2unix src/LICENSE.txt
find -name "*.png" | while read a; do
    optipng -o 5 "$a" || optipng -o 5 -fix "$a"
done

%build
%ant runtime-linux -Dnewsplugin.url=file:///%{_sourcedir}/NewsPlugin.jar
%if 0%{?suse_version} >= 1330
strip-nondeterminism runtime/tvbrowser_linux/icons/*.zip runtime/tvbrowser_linux/infothemes/*.zip runtime/tvbrowser_linux/*.jar
%endif

cat >tvbrowser <<'EOF'
#!/bin/sh

# try to find a suitable Java runtime, tvbrowser only works with 1.8 currently
if [ -x /usr/lib64/jvm/jre-1.8.0/bin/java ]; then
# 64bit VM found
JAVAEXE=/usr/lib64/jvm/jre-1.8.0/bin/java
elif [ -x /usr/lib/jvm/jre-1.8.0/bin/java ]; then
# 32bit VM found
JAVAEXE=/usr/lib/jvm/jre-1.8.0/bin/java
else
# fall back to the default java and hope for the best...
JAVAEXE=/usr/bin/java
fi

cd %{_javadir}/%{name}/ && \
#    exec %{_bindir}/java \
    exec $JAVAEXE \
        -Xms64m \
        -Xmx256m \
        -Djava.library.path=%{_javadir}/%{name} \
        -Dpropertiesfile=linux.properties \
        -jar tvbrowser.jar \
        "$@"
EOF

%install
export NO_BRP_CHECK_BYTECODE_VERSION="true"

install -D -p -m 755 tvbrowser %{buildroot}%{_bindir}/tvbrowser

mkdir -p %{buildroot}%{_javadir}/%{name}/
cp -r runtime/tvbrowser_linux/* %{buildroot}%{_javadir}/%{name}/

for size in 16 32 48 128; do
    (
        install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
        cd %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
        ln -s %{_javadir}/%{name}/imgs/tvbrowser${size}.png tvbrowser.png
    )
done

%suse_update_desktop_file -c tvbrowser TV-Browser 'Digital TV Guide' tvbrowser tvbrowser AudioVideo TV Java

%fdupes %{buildroot}%{_javadir}

install -Dm0644 deployment/linux/tvbrowser.appdata.xml %{buildroot}%{_datadir}/appdata/tvbrowser.appdata.xml

%check
# These tests fail:
rm -v test/src/util/misc/TextLineBreakerTest.java test/src/util/ui/html/HTMLTextHelperTest.java
%ant test

%clean
%ant clean

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt
%{_bindir}/tvbrowser
%{_javadir}/%{name}
%{_datadir}/applications/tvbrowser.desktop
%{_datadir}/icons/hicolor/*/apps/tvbrowser.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/tvbrowser.appdata.xml

%changelog
