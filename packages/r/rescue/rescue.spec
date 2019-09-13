#
# spec file for package rescue
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rescue
Version:        1.0.0.3
Release:        0
Summary:        Action Adventure in Space
License:        GPL-3.0+
Group:          Amusements/Games/Strategy/Other
Url:            http://rescue.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Rescue_%{version}.zip
Source1:        %{name}.sh
Source2:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  unzip
Requires:       jre >= 1.6.0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rescue! Max is an Action Adventure in Space written in java.
It is based on an old mac game called Rescue! by Tom Spreen.

A 2D space real-time, action/strategy game. You are in control of a ship that
you fly around space fighting enemies and making friends on your way.
The main objective is to rescue people from planets and take them to star bases.

%prep
%setup -q -n Rescue

# extract icon
unzip -j Rescue.jar rescue/gui/logo.png

# Convert to unix line end
find -name "*.txt" -print0 -or -name "*.htm" -print0 -or -name "*.css" -print0 \
    -or -name "*.ini" -print0 -or -name "*.xml" -print0 | xargs -0 dos2unix

# Some docs have the DOS line ends
dos2unix ChangeLog.txt gpl.txt todo.txt

%build

%install
# install wrappers
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p  %{buildroot}%{_libexecdir}/%{name}/{help,lib,missions}
for d in help lib missions ; do
    cp -a $d %{buildroot}%{_libexecdir}/%{name}
done

# install Jar files
install -Dm 0644 *.jar %{buildroot}%{_libexecdir}/%{name}

# install icon
install -Dm 0644 logo.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt gpl.txt todo.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_libexecdir}/%{name}

%changelog
