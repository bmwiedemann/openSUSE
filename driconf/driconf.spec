#
# spec file for package driconf
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


Name:           driconf
Version:        0.9.1
Release:        0
Summary:        A configuration applet for the Direct Rendering Infrastructure
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://dri.freedesktop.org/wiki/DriConf
Source:         driconf-%{version}.tar.gz
Patch1:         driconf-0.9.1-setup.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/driconf/patches/1/
Patch2:         driconf-0.9.1-glxinfo-unicode.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/driconf/patches/2/
Patch3:         driconf-0.9.1-update-toolbar-methods.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/driconf/bugs/3/
Patch4:         driconf_simpleui.patch
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
Requires:       Mesa
Requires:       python-gtk
Requires:       xdriinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
DRIconf is a configuration applet for the Direct Rendering Infrastructure.
It allows customizing performance and visual quality settings of OpenGL
drivers on a per-driver, per-screen and/or per-application level.

The settings are stored in system wide and per-user XML configuration files,
which are parsed by the OpenGL drivers on startup.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%find_lang driconf

desktop-file-install --vendor suse \
  --dir %{buildroot}/%{_datadir}/applications/ \
  --set-icon=%{_datadir}/driconf/driconf-icon.png --remove-category=AdvancedSettings \
  --add-category=System --add-category=Utility --add-category=DesktopSettings \
  --set-generic-name="Direct Rendering Infrastucture Configurator" \
  %{name}.desktop

%files -f driconf.lang
%defattr(-,root,root,-)
%doc COPYING CHANGELOG README TODO
%{_bindir}/driconf
%{python_sitelib}/*
%{_datadir}/driconf
%{_datadir}/applications/*.desktop

%changelog
