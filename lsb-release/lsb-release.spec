#
# spec file for package lsb-release
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


Name:           lsb-release
Version:        3.0
Release:        0
Summary:        Linux Standard Base Release Tools
License:        GPL-2.0+
Group:          System/Fhs
Url:            https://github.com/thkukuk/lsb-release_os-release
Source:         lsb-release-3.0.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Tools from the Linux Standard Base project to determine the used distribution

%prep
%setup -q

%build
# for openSUSE, the distributor is the openSUSE project
%if 0%{?is_opensuse}
sed -e 's/^MSG_DISTRIBUTOR=".*"/MSG_DISTRIBUTOR="openSUSE"/' -i lsb_release
%endif
make

%install
make install INSTALL_ROOT=%{buildroot}%{_prefix}

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/lsb?release
%{_mandir}/man1/lsb?release.1%{ext_man}

%changelog
