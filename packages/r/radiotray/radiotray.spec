#
# spec file for package radiotray
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           radiotray
Version:        0.7.3
Release:        0
Summary:        A streaming player for listening to online radios
License:        GPL-1.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            http://radiotray.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/radiotray/releases/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM radiotray-0.7.3-fix-wrong-mutex-unlock.patch boo#904322
Patch0:         radiotray-0.7.3-fix-wrong-mutex-unlock.patch
# PATCH-FIX-UPSTREAM radiotray-port-gst1-gtk3.patch zaitor@opensuse.org -- Port to gtk3 and gstreamer-1.0.
Patch1:         radiotray-port-gst1-gtk3.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python
BuildRequires:  python-xdg
BuildRequires:  update-desktop-files
Requires:       python-dbus-python
Requires:       python-gobject-Gdk
Requires:       python-gst
Requires:       python-gtk
Requires:       python-lxml
Requires:       python-notify
Requires:       python-xdg
Recommends:     gstreamer-plugins-ugly
BuildArch:      noarch

%description
Radio Tray is an online radio streaming player that runs on a Linux system
tray. Its goal is to have the minimum interface possible, making it very
straightforward to use.

Radio Tray is not a full featured music player, there are plenty of
excellent music players already. However, there was a need for a simple
application with minimal interface just to listen to online radios.
And that's the sole purpose of Radio Tray.

%lang_package

%prep
%setup -q
%patch0
%patch1

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
%find_lang %{name} %{?no_lang_C}
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{version}
%fdupes %{buildroot}%{python_sitelib}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc AUTHORS CONTRIBUTORS NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info

%files lang -f %{name}.lang

%changelog
