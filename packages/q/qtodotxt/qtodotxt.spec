#
# spec file for package qtodotxt
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


%define _name   QTodoTxt
Name:           qtodotxt
Version:        1.9.0
Release:        0
Summary:        User interface client for todo.txt files
License:        GPL-3.0+
Group:          Productivity/Office/Organizers
Url:            https://github.com/mNantern/QTodoTxt
Source:         https://github.com/mNantern/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       python3-dateutil
Requires:       python3-qt5
BuildArch:      noarch

%description
QTodoTxt is a graphical interface for the todo.txt format.

Todo.txt is a TODO list format in which the data is stored in a text
file. Since todo.txt is both machine and human-readable, tasks can be
checked out with alternative editors, and be synchronised with cloud
sync tools such as Nextcloud, etc.

%prep
%setup -q -n %{_name}-%{version}
sed -e 's/^Icon=.*$/Icon=%{name}/;/^Keywords/d' packaging/Debian/%{name}.desktop > %{name}.desktop

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} \
  --prefix=%{_prefix}

# A tricky way to get all available icon sizes.
convert -strip %{name}/ui/resources/%{name}.ico packaging/%{name}.png
iter=0
for size in 48 32 16; do
    install -Dpm 0644 packaging/%{name}-$iter.png \
      %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
    iter=$(( iter + 1 ))
done
install -Dpm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file -r -G %{_name} %{name} Utility DesktopUtility
%fdupes %{buildroot}%{python3_sitelib}/

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS gpl.txt
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
