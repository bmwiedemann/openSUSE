#
# spec file for package thunar-sendto-clamtk
#
# Copyright (c) 2024 SUSE LLC
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


Name:           thunar-sendto-clamtk
Version:        0.08
Release:        0
Summary:        Adds a right-click, context menu to scan files or folders in Thunar
License:        GPL-1.0-or-later
Group:          Productivity/File utilities
URL:            https://gitlab.com/dave_m/thunar-sendto-clamtk/
Source:         https://gitlab.com/dave_m/thunar-sendto-clamtk/-/archive/v%{version}/thunar-sendto-clamtk-v%{version}.tar.gz
BuildRequires:  gzip
Requires:       clamtk >= 5.00
Requires:       thunar
BuildArch:      noarch

%description
All this plugin does is copy a desktop file to Thunar's send-to
directory.  If this seems redundant, that's because it is:
this plugin depends on clamtk, which already has this directory
file. So, it stands to reason we should be able to just find that
file and copy it, rather than having our own copy.

%prep
%setup -qn %name-v%version

%build
gunzip thunar-sendto-clamtk.1.gz

%install
install -Dm 644 thunar-sendto-clamtk.desktop %{buildroot}%{_usr}/share/Thunar/sendto/thunar-sendto-clamtk.desktop
install -Dm 644 thunar-sendto-clamtk.1 %{buildroot}%{_mandir}/man1/thunar-sendto-clamtk.1

%files
%doc CHANGES DISCLAIMER README.md
%license LICENSE
%dir %{_usr}/share/Thunar/
%dir %{_usr}/share/Thunar/sendto/
%{_usr}/share/Thunar/sendto/thunar-sendto-clamtk.desktop
%{_mandir}/man1/thunar-sendto-clamtk.1%{?ext_man}

%changelog
