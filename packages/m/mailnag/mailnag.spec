#
# spec file for package mailnag
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


Name:           mailnag
Version:        1.2.1
Release:        0
Summary:        Mail notification daemon
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
Url:            https://github.com/pulb/mailnag
Source:         https://github.com/pulb/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  python
BuildRequires:  update-desktop-files
Requires:       dbus-1-python
Requires:       gnome-keyring
Requires:       python
Requires:       python-gobject
Requires:       python-pyxdg
Recommends:     %{name}-lang
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
Requires:       python-gobject-Gdk
%endif

%description
Mailnag checks POP3 and IMAP servers for new mail and when it finds
one creates a proper GNOME 3 notification that mentions sender and
subject.

%lang_package

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install \
  --root=%{buildroot}    \
  --prefix=%{_prefix}

%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE NEWS README.md
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{python_sitelib}/Mailnag/
%{python_sitelib}/%{name}-*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
