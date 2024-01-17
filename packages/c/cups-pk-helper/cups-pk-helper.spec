#
# spec file for package cups-pk-helper
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cups-pk-helper
Version:        0.2.7
Release:        0
Summary:        PolicyKit helper to configure cups with fine-grained privileges
License:        GPL-2.0-or-later
Group:          Hardware/Printing
URL:            https://www.freedesktop.org/wiki/Software/cups-pk-helper/
Source0:        https://www.freedesktop.org/software/cups-pk-helper/releases/%{name}-%{version}.tar.xz
BuildRequires:  cups-devel
BuildRequires:  meson
# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  glib2-devel
BuildRequires:  polkit-devel
# Without cups installed, the cups-pk-helper-mechanism gives error: CRITICAL **: Failed to connect to cupsd
Requires:       cups >= 1.6

%description
This package provides a PolicyKit helper to configure cups with
fine-grained privileges. For example, it's possible to let users
enable/disable printers without requiring a password, while still
requiring a password for editing printer settings.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%{_libexecdir}/cups-pk-helper-mechanism
%{_datadir}/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%{_datadir}/locale/en/
%{_datadir}/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy

%files lang -f %{name}.lang
# english locale should be in the main package
%exclude %{_datadir}/locale/en

%changelog
