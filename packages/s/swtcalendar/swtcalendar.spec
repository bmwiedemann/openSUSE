#
# spec file for package swtcalendar
#
# Copyright (c) 2025 SUSE LLC
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


Name:           swtcalendar
Version:        0.5
Release:        0
Summary:        GUI date picker for Java using SWT
License:        MIT
Group:          Development/Languages/Java
URL:            http://swtcalendar.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}/%{name}-src-%{version}.zip
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  eclipse-swt
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  unzip
BuildArch:      noarch

%description
SWTCalendar is a port of Kai Toedter's JCalendar to Eclipse's SWT.
It is a GUI date picker for Java using SWT as the GUI toolkit.
SWTCalendar was designed to be a flexible component so developer
can embed a date picker in their application or create their own
standalone date picker dialog.

%prep
%setup -q -n %{name}
dos2unix *.txt

%build
export CLASSPATH=$(find-jar swt)
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

%install
mkdir -p %{buildroot}%{_javadir}
install swtcalendar.jar %{buildroot}%{_javadir}

%files
%doc MIT.txt README.txt
%{_javadir}/*

%changelog
