#
# spec file for package fontweak
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fontweak
Version:        1.3.1
Release:        0
Summary:        GUI front-end of fontconfig
License:        GPL-3.0+
Group:          System/X11/Utilities
Url:            https://github.com/guoyunhe/fontweak
Source:         %{name}-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  java-devel >= 1.7.0
Requires:       java >= 1.7.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A front-end for fontconfig. Setup perfect font effects, fast and easily.

* Choose fonts by font family and language
* Combine English font and Chinese font
* Setup font render options, including hinting, antialias, subpixel rendering
* Font replacement. Use installed fonts render missing fonts.
* Scheme management, 1-click setup and Reset system default functions.

%prep
%setup -q

%build
%{ant} jar

%install
# jars
install -dm 0755 "%{buildroot}/%{_datadir}/%{name}"
install -m 0644 "dist/fontweak.jar" "%{buildroot}/%{_datadir}/%{name}/"

# startscript
install -dm 0755 "%{buildroot}/%{_bindir}"
cat >"%{buildroot}/%{_bindir}/%{name}" << EOF
#!/bin/sh
exec java -jar "%{_datadir}/%{name}/%{name}.jar"
EOF
chmod 0755 "%{buildroot}/%{_bindir}/%{name}"

# .desktop
install -dm 0755 "%{buildroot}/%{_datadir}/applications"
install -m 0644 "%{name}.desktop" "%{buildroot}/%{_datadir}/applications/"

# icon
install -dm 0755 "%{buildroot}/%{_datadir}/pixmaps"
install -m 0644 "icon.svg" "%{buildroot}/%{_datadir}/pixmaps/%{name}.svg"

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
