#
# spec file for package barbie_seahorse_adventures
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


Name:           barbie_seahorse_adventures
Version:        1.1
Release:        0
Summary:        You are a seahorse and you want to go to the moon!
License:        GPL-2.0
Group:          Amusements/Games/Action/Arcade
Url:            http://www.imitationpickles.org/barbie/
Source0:        http://www.imitationpickles.org/barbie/files/barbie-1.1.tgz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
Requires:       python
Requires:       python-pygame
BuildArch:      noarch

%description
You are a seahorse and you want to go to the moon!

When you play - make sure to check out all 3 phases - Jungle, Volcano, and Moon!

%prep
%setup -q -n barbie-%{version}

# Remove not needed files
rm -f data/REMOVE_ME.txt data/sample.txt lib/pgu/LICENSE.txt

# Adjust python version
sed -i 's|/usr/bin/python|/usr/bin/python2|' leveledit.py tileedit.py

# Convert to unix line end
find . -name "*.py" -exec dos2unix "{}" "+"

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{data,lib}
for d in data lib ; do
    cp -a $d %{buildroot}%{_datadir}/%{name}
done

# install files
install -Dm 0644 *.ini %{buildroot}%{_datadir}/%{name}

for f in create-upload leveledit run_game tileedit ; do
    install -Dm 0555 ${f}.py %{buildroot}%{_datadir}/%{name}
done

for f in preview pyweek-upload ; do
    install -Dm 0644 ${f}.py %{buildroot}%{_datadir}/%{name}
done

# install icons
for i in 32 64 128 ; do
    install -Dm 0644 icon${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
install -Dm 0644 icon64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

# install app store metadata
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
