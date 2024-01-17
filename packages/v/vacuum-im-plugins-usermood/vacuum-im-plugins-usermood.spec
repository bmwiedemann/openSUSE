#
# spec file for package vacuum-im-plugins-usermood
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


%define app_name vacuum-im
Name:           vacuum-im-plugins-usermood
Version:        0.0.1
Release:        0
Summary:        Vacuum-IM user mood plugin
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
Url:            http://www.vacuum-im.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.2.0
BuildRequires:  fdupes
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libvacuumutils37
BuildRequires:  vacuum-im-devel
BuildRequires:  xz

%description
Vacuum-IM plugin to send and receive information about user moods.

%prep
%setup -q -n %{name}

%build
%cmake \
	-DINSTALL_LIB_DIR=%{_lib} \
	-DINSTALL_APP_DIR=%{app_name} \
	-DINSTALL_DOC_DIR=%{_defaultdocdir} \
        -DVACUUM_LIB_PATH=%{_prefix}/%{_lib} \
        -DVACUUM_SDK_PATH=%{_includedir}/%{app_name}
make %{?_smp_mflags} V=1

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

%files
%{_libdir}/%{app_name}
%dir %{_libdir}/%{app_name}/plugins
%{_datadir}/%{app_name}

%changelog
