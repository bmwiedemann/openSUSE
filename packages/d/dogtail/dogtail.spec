#
# spec file for package dogtail
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


%define pythons python3
Name:           dogtail
Version:        0.9.11
Release:        0
Summary:        GUI test tool and automation framework
License:        GPL-2.0-only
URL:            https://gitlab.com/dogtail/dogtail/
Source0:        https://gitlab.com/dogtail/dogtail/raw/released/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
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
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}/%{_docdir}/dogtail
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
%{python3_sitelib}/dogtail-%{version}.dist-info
%{_datadir}/applications/*
%{_datadir}/dogtail/
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%license COPYING
%doc README
%doc NEWS
%doc %{_datadir}/doc/dogtail

%changelog
