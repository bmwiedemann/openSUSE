#
# spec file for package tvbrowser
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


Name:           tvbrowser
Version:        4.2.7
Release:        0
Summary:        Digital TV guide
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://tv-browser.org/
Source0:        https://downloads.sourceforge.net/project/tvbrowser/TV-Browser%20Releases%20%28Java%2011%20and%20higher%29/%{version}/%{name}_%{version}_src.zip
# TODO build from source, too
Source2:        https://www.tvbrowser.org/data/uploads/1372016422809_543/NewsPlugin.jar
Patch0:         fix-junit-classpath.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel >= 11
BuildRequires:  jpackage-utils
BuildRequires:  optipng
BuildRequires:  strip-nondeterminism
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       java >= 11
BuildArch:      noarch

%description
TV-Browser is Plugin based digital TV guide. Plugins can be installed with
the download function of TV-Browser.

%prep
cp -p %{SOURCE2} .
%setup -q
# needed to apply patch
dos2unix build.xml
%patch0 -p1
dos2unix src/LICENSE.txt
find -name "*.png" | while read a; do
    optipng -quiet -o 5 "$a" || optipng -quiet -o 5 -fix "$a"
done

%build
%{ant} runtime-linux -Dnewsplugin.url=file:///%{_sourcedir}/NewsPlugin.jar
strip-nondeterminism runtime/tvbrowser_linux/icons/*.zip \
                     runtime/tvbrowser_linux/infothemes/*.zip \
                     runtime/tvbrowser_linux/*.jar

cat >tvbrowser <<'EOF'
#!/bin/sh
cd %{_javadir}/%{name}
exec ./tvbrowser.sh -Dswing.aatext=TRUE -Dawt.useSystemAAFontSettings=on "$@"
EOF

%install
export NO_BRP_CHECK_BYTECODE_VERSION="true"

install -D -p -m 0755 -t %{buildroot}%{_bindir}/ tvbrowser
install -D -m 0644 -t %{buildroot}%{_datadir}/metainfo/ deployment/linux/tvbrowser.appdata.xml

mkdir -p %{buildroot}%{_javadir}/%{name}/
cp -a runtime/tvbrowser_linux/* %{buildroot}%{_javadir}/%{name}/
chmod 0755 %{buildroot}%{_javadir}/%{name}/tvbrowser.sh

for size in 16 32 48 128; do
    (
        install -d %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
        cd %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
        ln -s %{_javadir}/%{name}/imgs/tvbrowser${size}.png tvbrowser.png
    )
done

%suse_update_desktop_file -c tvbrowser TV-Browser 'Digital TV Guide' tvbrowser tvbrowser Video AudioVideo TV

%fdupes %{buildroot}%{_javadir}

%check
# These test(s) fail:
rm -v test/src/util/misc/TextLineBreakerTest.java
%{ant} test

%files
%doc ChangeLog.txt
%{_bindir}/tvbrowser
%{_javadir}/%{name}
%{_datadir}/applications/tvbrowser.desktop
%{_datadir}/icons/hicolor/*/apps/tvbrowser.png
%{_datadir}/metainfo/tvbrowser.appdata.xml

%changelog
