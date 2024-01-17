#
# spec file for package dogtail
#
# Copyright (c) 2020 SUSE LLC
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


Name:           dogtail
Version:        0.9.11
Release:        0
Summary:        GUI test tool and automation framework
License:        GPL-2.0-only
URL:            https://gitlab.com/dogtail/dogtail/
Source0:        https://gitlab.com/dogtail/dogtail/raw/released/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       hicolor-icon-theme
Requires:       python3-atspi
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-imaging
Requires:       python3-rpm
Requires:       xinit
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
Requires:       python3-gobject-Gdk
%endif

%description
GUI test tool and automation framework that uses assistive technologies to
communicate with desktop applications.

%prep
%setup -q

%build
python3 ./setup.py build

%install
python3 ./setup.py install -O2 --root=%{buildroot} --record=%{name}.files
rm -rf %{buildroot}/%{_docdir}/dogtail
rm -rf %{buildroot}/%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
find examples -type f -exec chmod 0644 \{\} \;
desktop-file-install %{buildroot}/%{_datadir}/applications/sniff.desktop \
  --dir=%{buildroot}/%{_datadir}/applications \
%suse_update_desktop_file -G "UI test application" -r %{buildroot}/%{_datadir}/applications/sniff.desktop Development Profiling

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%{_bindir}/*
%{python3_sitelib}/dogtail/
%{_datadir}/applications/*
%{_datadir}/dogtail/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%license COPYING
%doc README
%doc NEWS
%doc %{_datadir}/doc/dogtail

%changelog
