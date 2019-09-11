#
# spec file for package vacuum-im-plugins-gmailnotify
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
%define rtime 1518929179
%define rhash 2d687c8
Name:           %{app_name}-plugins-gmailnotify
Version:        1.0.5+git%{rtime}.%{rhash}
Release:        0
Summary:        GMailNotify plugin for Vacuum-IM
License:        GPL-3.0
Group:          Productivity/Networking/Instant Messenger
URL:            http://www.vacuum-im.org/
Source:         %{name}-git%{rtime}.%{rhash}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  openssl-devel
BuildRequires:  vacuum-im-devel
BuildRequires:  xz

%description
Vacuum-IM plugin for gmail notifications.

%prep
%setup -q -n %{name}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DINSTALL_LIB_DIR=%{_lib} \
    -DINSTALL_APP_DIR=%{app_name} \
    -DINSTALL_DOC_DIR=%{_defaultdocdir} \
    -DVACUUM_LIB_PATH=%{_libdir} \
    -DVACUUM_SDK_PATH=%{_includedir}/%{app_name}
make %{?_smp_mflags} V=1

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

%files
%dir %{_libdir}/%{app_name}
%{_libdir}/%{app_name}/plugins/
%{_datadir}/%{app_name}

%changelog
