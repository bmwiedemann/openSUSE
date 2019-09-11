#
# spec file for package solaar
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           solaar
Version:        0.9.2
Release:        0
Summary:        Linux devices manager for the Logitech Unifying Receiver
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://pwr.github.io/Solaar/
Source0:        https://github.com/pwr/Solaar/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE solaar-fix-desktop-categories.patch malcolmlewis@opensuse.org -- Fix desktop categories as per openSUSE desktop file specification.
Patch0:         solaar-fix-desktop-categories.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-devel
BuildRequires:  python-distutils-extra
BuildRequires:  update-desktop-files
BuildRequires:  udev
Requires:       typelib-1_0-Gtk-3_0
Requires:       %{name}-cli = %{version}
Recommends:     %{name}-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Solaar will detect all devices paired with your Unifying Receiver, and
at the very least display some basic information about them.

For some devices, extra settings (usually not available through the
standard Linux system configuration) are supported. For a full list of
supported devices and their features, see docs/devices.md.

%package        cli
Summary:        Command line devices manager for the Logitech Unifying Receiver
Group:          Hardware/Other
Requires:       python-gobject
Requires:       python-pyudev

%description    cli
Solaar will detect all devices paired with your Unifying Receiver, and
at the very least display some basic information about them.

For some devices, extra settings (usually not available through the
standard Linux system configuration) are supported. For a full list of
supported devices and their features, see docs/devices.md.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other

%description    doc
Solaar will detect all devices paired with your Unifying Receiver, and
at the very least display some basic information about them.

For some devices, extra settings (usually not available through the
standard Linux system configuration) are supported. For a full list of
supported devices and their features, see docs/devices.md.

%if %( echo `rpm -q --queryformat %%{version} udev` ) > 190
%define _udevprefix /usr/lib
%else
%define _udevprefix /lib
%endif

%prep
%setup -q -n Solaar-%{version}
%patch0 -p1
sed -i '/yield autostart_path/d' setup.py

%build
python setup.py build

%install
python setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
install -Dm0644 rules.d/42-logitech-unify-permissions.rules %{buildroot}%{_udevprefix}/udev/rules.d/42-logitech-unify-permissions.rules
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes -s %{buildroot}%{_datadir}/

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc ChangeLog COPYING COPYRIGHT README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/solaar.svg
%{_datadir}/%{name}/
%{python_sitelib}/solaar/ui/
%{python_sitelib}/solaar/gtk.*

%files cli
%defattr(-,root,root)
%{_bindir}/%{name}-cli
%{_udevprefix}/udev/rules.d/*.rules
%{python_sitelib}/*
%exclude %{python_sitelib}/solaar/ui/
%exclude %{python_sitelib}/solaar/gtk.*

%files doc
%defattr(-,root,root)
%doc docs/*

%changelog
