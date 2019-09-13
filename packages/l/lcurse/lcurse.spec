#
# spec file for package lcurse
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


Name:           lcurse
Version:        1.0.0
Release:        0
Summary:        Python script to have a "curse" compatible client for linux
License:        Unlicense
Group:          Amusements/Games/Other
Url:            https://github.com/ephraim/lcurse
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       python3-beautifulsoup4
Requires:       python3-lxml
Requires:       python3-qt5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Python script to have a "curse" compatible client for linux.

In this context curse refers to the curse.com addon database for World of
Warcraft.

%prep
%setup -q

%build

%install
# install desktop file and icon
install -D -m 0644 media/lcurse.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 media/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove media/ directory so it is not copied to datadir
rm -r media/

# install source
install -d -m 0755 . %{buildroot}%{_datadir}/%{name}
cp -r * %{buildroot}%{_datadir}/%{name}

# link to executable in bindir
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?suse_version} >= 1310
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
