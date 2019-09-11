#
# spec file for package awesome-freedesktop
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


%define _version 0.0~git20170109
Name:           awesome-freedesktop
Version:        git201701091085
Release:        0
Summary:        Desktop entries and menu for awesome
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://github.com/copycat-killer/awesome-freedesktop
Source:         %{name}-%{_version}.tar.gz
BuildRequires:  awesome >= 4.0
Requires:       awesome >= 4.0
BuildArch:      noarch

%description
This project aims to add support for freedesktop.org compliant
desktop entries and menu.

Main features:
 * a freedesktop.org-compliant (or almost) applications menu.
 * a freedesktop.org-compliant (or almost) desktop.
 * a (yet limited) icon lookup function.

You can choose any icon theme that's installed in %{_datadir}/icons/.

%prep
%setup -q -n %{name}-%{_version}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/awesome/lib/freedesktop/
install -pm 0644 *.lua %{buildroot}%{_datadir}/awesome/lib/freedesktop/

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%dir %{_datadir}/awesome/
%dir %{_datadir}/awesome/lib/
%{_datadir}/awesome/lib/freedesktop/

%changelog
