#
# spec file for package epymc
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


Name:           epymc
Version:        1.2.0
Release:        0
Summary:        A Media Center designed to run on a large number of devices
License:        GPL-3.0+
Group:          Productivity/Multimedia/Video/Players
Url:            https://github.com/DaveMDS/epymc
Source0:        v%{version}.tar.gz
Patch0:         fix-desktop-file.patch
BuildArch:      noarch
BuildRequires:  efl-devel
BuildRequires:  intltool
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-efl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
Requires:       python3-efl
ExcludeArch:    %ix86

%description

EpyMC is a Media Center application written in python that use the Enlightenment Foundation Library as
the living base. 

%lang_package

%prep
%setup -q -n  %{name}-%{version}
%patch0 -p1

%build
python3 setup.py build

%install
python3 setup.py install --root "%{buildroot}"
%if 0%{?suse_version}
%fdupes %{buildroot}/%{_datadir}
%suse_update_desktop_file epymc "Video;Player"
%endif
%find_lang %{name}

%files
%defattr(-,root,root,-)
%doc README.md COPYING TODO
%doc README.md COPYING TODO
%{_bindir}/epymc
%{_bindir}/epymc_standalone
%{_bindir}/epymc_thumbnailer
%{_bindir}/epymc_watchdog

%{python3_sitelib}/epymc*
%exclude %{python3_sitelib}/epymc/locale/*/LC_MESSAGES/epymc.mo
%{python3_sitelib}/EpyMC*
%{_datadir}/icons/*
%{_datadir}/applications/epymc.desktop
%{_datadir}/xsessions/epymc_xsession.desktop

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
