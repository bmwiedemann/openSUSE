#
# spec file for package unclutter-xfixes
#
# Copyright (c) 2023 SUSE LLC
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


Name:           unclutter-xfixes
Version:        1.6
Release:        0
Summary:        A rewrite of unclutter using the x11-xfixes extension
License:        MIT
Url:            https://github.com/Airblader/unclutter-xfixes
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  libev-devel
BuildRequires:  asciidoc
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
Conflicts:      unclutter

%description
This is a rewrite of the popular tool unclutter, but using the x11-xfixes
extension. This means that this rewrite doesn't use fake windows or pointer
grabbing and hence causes less problems with window managers and/or applications.

%prep
%autosetup

%build
%make_build

%install
install -Dm 0755 unclutter %{buildroot}%{_bindir}/unclutter
install -Dm 0644 man/unclutter-xfixes.1 %{buildroot}%{_mandir}/man1/unclutter.1

%files
%license LICENSE
%doc README.md
%{_bindir}/unclutter
%{_mandir}/man1/unclutter.1%{?ext_man}

%changelog
