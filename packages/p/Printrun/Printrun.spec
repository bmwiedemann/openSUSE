#
# spec file for package Printrun
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1

Name:           Printrun
Version:        2.0.0~rc5.1522069560.e0ee40a
Release:        0
Summary:        RepRap printer interface and tools
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Convertors
Url:            https://github.com/kliment/Printrun
Source0:        Printrun-%{version}.tar.xz

# Desktop files
Source1:        pronsole.desktop
Source2:        pronterface.desktop
Source3:        plater.desktop

BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module setuptools}
BuildRequires:  gettext
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
%if 0%{?fedora_version}
BuildRequires:  desktop-file-utils
%endif

Requires:       plater = %{version}-%{release}
Requires:       pronsole = %{version}-%{release}
Requires:       pronterface = %{version}-%{release}

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts. Together with skeinforge
they form a pretty powerful softwarecombo. This package installs whole Printrun.

###############################################

%package        common
Summary:        Common files for Printrun
Group:          Productivity/Graphics/Convertors
Requires:       %{python_module numpy}
Requires:       %{python_module pyglet}
Requires:       %{python_module pyserial}

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

###############################################

%package     -n pronsole
Summary:        CLI interface for RepRap
Group:          Productivity/Graphics/Convertors
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n pronterface
Summary:        GUI interface for RepRap
Group:          Productivity/Graphics/Convertors
Requires:       %{python_module wxPython}
Requires:       pronsole = %{version}-%{release}
BuildArch:      noarch

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n plater
Summary:        RepRap STL plater
Group:          Productivity/Graphics/Convertors
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{python_module wxPython}
BuildArch:      noarch

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

###############################################


%prep
%setup -q

# use launchers for skeinforge
sed -i 's|python skeinforge/skeinforge_application/skeinforge.py|skeinforge|' pronsole.py
sed -i 's|python skeinforge/skeinforge_application/skeinforge_utilities/skeinforge_craft.py|skeinforge-craft|' pronsole.py

# fixup shebangs, /usr/bin/env python3 -> python3, and executable bits
sed -s -i -e '1 s@/usr/bin/env python3@/usr/bin/python3@' printrun/*py

%build
%python_build

# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || echo plater not there
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || echo pronterface not there
done
cd ..

%install
%python_install

# fixup executable bits
for f in %{buildroot}%{python3_sitearch}/printrun/*py; do
  sed -e '/\/usr\/bin\/python3/ Q 1 ; Q 0' $f || chmod 0755 $f
done

# desktop files
%if 0%{?suse_version}
mkdir -p "%buildroot/%_docdir/%name"
mkdir -p %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/pronsole.desktop
install -Dm644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/pronterface.desktop
install -Dm644 %{SOURCE3} %{buildroot}/%{_datadir}/applications/plater.desktop

%suse_update_desktop_file -i %{buildroot}/%{_datadir}/applications/pronsole.desktop
%suse_update_desktop_file -i %{buildroot}/%{_datadir}/applications/pronterface.desktop
%suse_update_desktop_file -i %{buildroot}/%{_datadir}/applications/plater.desktop
%fdupes -s %{buildroot}%{python3_sitearch}/
%endif

%if 0%{?fedora_version}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
%endif

# locales
mkdir -p %{buildroot}%{_datadir}/locale
cp -ar %{buildroot}%{_datadir}/pronterface/locale/* %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/pronterface/locale
ln -s -f %{_datadir}/locale/ %{buildroot}%{_datadir}/pronterface/ # the app expects the locale folder in here

%{find_lang} pronterface
%{find_lang} plater

%files
%doc README*
%license COPYING

%files common
%doc README*
%license COPYING
%{python3_sitearch}/*
%{_bindir}/printcore.*

%files -n pronsole
%{_bindir}/pronsole.*
%{_datadir}/pixmaps/pronsole.png
%{_datadir}/applications/pronsole.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/pronsole.appdata.xml

%files -n pronterface -f pronterface.lang
%{_bindir}/pronterface.*
%{_datadir}/pronterface
%{_datadir}/pixmaps/pronterface.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/pronterface.appdata.xml
%{_datadir}/applications/pronterface.desktop

%files -n plater -f plater.lang
%{_bindir}/plater.*
%{_datadir}/pixmaps/plater.png
%{_datadir}/applications/plater.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/plater.appdata.xml

%changelog
