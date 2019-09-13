#
# spec file for package lifecycle-data
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


Name:           lifecycle-data
Version:        1
Release:        0
Summary:        End of life dates for specific packages
License:        MIT
Group:          System/Management
Url:            http://www.suse.com/lifecycle
Source:         openSUSE.lifecycle
BuildArch:      noarch

%description
Package lifecycle data.  This is the source of zypper lifecycle information.

%package openSUSE
Summary:        End of life dates for specific packages
Group:          System/Management
Supplements:    packageand(openSUSE-release:zypper-lifecycle-plugin)

%description openSUSE
Package lifecycle data.  This is the source of zypper lifecycle information.

%prep

%build

%install
install -d %{buildroot}%{_datadir}/lifecycle/data
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/lifecycle/data/openSUSE.lifecycle

%files openSUSE
%dir %{_datadir}/lifecycle
%dir %{_datadir}/lifecycle/data
%{_datadir}/lifecycle/data/openSUSE.lifecycle

%changelog
