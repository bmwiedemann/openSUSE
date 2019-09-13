#
# spec file for package compiz-manager
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           compiz-manager
Version:        0.7.0
Release:        0
Summary:        Wrapper script to launch Compiz with proper options
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            https://github.com/raveit65/compiz-manager
Source:         https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source2:        Compiz.desktop
Source3:        config.skel
# PATCH-FEATURE-OPENSUSE compiz-manager-setup.patch dimstar@opensuse.org -- Configure compiz-manager to fit the openSUSE.
Patch0:         compiz-manager-setup.patch
BuildRequires:  update-desktop-files
Requires:       compiz < 0.9
Requires:       util-linux
BuildArch:      noarch

%description
This script detects what options to pass to Compiz to get it
started, and start a default plugin and possibly window decorator.

%prep
%setup -q
%patch0 -p1
cp -f %{SOURCE2} Compiz.desktop
cp -f %{SOURCE3} config.skel

%build
# Nothing to build.

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0644 COPYING %{buildroot}%{_docdir}/%{name}/COPYING
install -Dm 0644 Compiz.desktop %{buildroot}%{_datadir}/compiz-manager/Compiz.desktop
install -Dm 0644 config.skel %{buildroot}%{_datadir}/compiz-manager/config.skel

%suse_update_desktop_file %{buildroot}%{_datadir}/compiz-manager/Compiz.desktop

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
