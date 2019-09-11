#
# spec file for package wammu
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           wammu
Version:        0.44
Release:        0
Summary:        Mobile Phone Manager
License:        GPL-3.0+
Group:          Productivity/Telephony/Utilities
Url:            http://wammu.eu/wammu/
Source:         https://dl.cihar.com/wammu/v0/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Python location
%{!?__python: %define __python python}
%define wammu_python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:  desktop-file-utils
%endif
BuildRequires:  python-devel
BuildRequires:  python-gammu >= 2.7
BuildRequires:  python-pybluez
BuildRequires:  python-setuptools
%if 0%{?suse_version} > 1130
BuildRequires:  python-wxWidgets >= 2.6
%else
BuildRequires:  wxPython >= 2.6
%endif
BuildRequires:  python-xml
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       python-base = %py_ver
Requires:       python-gammu >= 2.7
Requires:       python-pybluez
Requires:       python-xml
%if 0%{?suse_version} > 1130
Requires:       python-wxWidgets >= 2.6
%else
Requires:       wxPython >= 2.6
%endif
Recommends:     python-dbus
Recommends:     python-pybluez
Recommends:     %{name}-lang = %{version}
# These distributions use /usr/lib for python on all architectures
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel} || 0%{?mandriva_version} || 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description
It works with any phone that Gammu supports, including many models from
Nokia, Siemens, and Alcatel. It has complete support (read, edit,
delete, copy) for contacts, todo, and calendar. It can read, save, and
send SMS. It includes an SMS composer for multi-part SMS messages, and
it can display SMS messages that include pictures. Currently, only text
and predefined bitmaps or sounds can be edited in the SMS composer. It
can export messages to an IMAP4 server (or other email storage).

This program does not support browsing files in phone, use gMobileMedia
instead.

%lang_package
%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%{__python} setup.py install -O1 --root=%{buildroot} --prefix=%{_prefix}
%else
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif

%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} GTK Utility Telephony
%endif
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    --mode 0644 \
    --remove-category=Application \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

# Remove unneeded locales
%if 0%{?suse_version} && 0%{?suse_version} < 1140
rm -rf %{buildroot}%{_datadir}/locale/sw/
%endif

%find_lang %{name} --with-man --all-name

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog PKG-INFO README*
%{_bindir}/wammu
%{_bindir}/wammu-configure
%{wammu_python_sitelib}/Wammu/
%{wammu_python_sitelib}/wammu-*.egg-info
%{_datadir}/Wammu/
%{_datadir}/applications/wammu.desktop
%doc %{_mandir}/man1/wammu.1%{ext_man}
%doc %{_mandir}/man1/wammu-configure.1%{ext_man}
%{_datadir}/pixmaps/wammu.*
%{_datadir}/appdata/

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%lang(cs) %doc %dir %{_mandir}/cs
%lang(nl) %doc %dir %{_mandir}/nl
%if 0%{?suse_version} < 1130
%lang(ru) %doc %dir %{_mandir}/ru
%endif
%lang(sk) %doc %dir %{_mandir}/sk
%lang(en_GB) %doc %dir %{_mandir}/en_GB
%lang(et) %doc %dir %{_mandir}/et
%lang(id) %doc %dir %{_mandir}/id
%lang(tr) %doc %dir %{_mandir}/tr
%lang(uk) %doc %dir %{_mandir}/uk

%changelog
