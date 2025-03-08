#
# spec file for package setroubleshoot-plugins
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


Name:           setroubleshoot-plugins
Version:        3.3.14
Release:        0
Summary:        Helps troubleshoot SELinux problems
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://gitlab.com/setroubleshoot/plugins/
Source:         https://releases.pagure.org/setroubleshoot/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM regenerate to fix build with python 3.13
Patch0:         https://gitlab.com/setroubleshoot/plugins/-/commit/9e54f6a661330070ad25a0e86f197b3530bfc5c7.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  python3-devel
# Introduction of get_package_nvr functions
Requires:       setroubleshoot-server >= 3.3.23
BuildArch:      noarch

%description
This package provides a set of analysis plugins for use with
setroubleshoot. Each plugin has the capacity to analyze SELinux AVC
data and system data to provide user friendly reports describing how
to interpret SELinux AVC denials.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/locale
%fdupes %{buildroot}%{_datadir}/setroubleshoot/plugins

%files
%license COPYING
%doc AUTHORS ChangeLog README
%dir %{_datadir}/setroubleshoot
%{_datadir}/setroubleshoot/plugins

%files lang -f %{name}.lang

%changelog
