#
# spec file for package cosmic-icons
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


Name:           cosmic-icons
Version:        1.0.0~alpha3
Release:        0
Summary:        System76 Cosmic icon theme for Linux
License:        CC-BY-SA-4.0 AND GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-icons
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  fdupes
BuildRequires:  just
BuildRequires:  zstd
BuildArch:      noarch
Requires:       pop-icon-theme

%description
These are the icons used by the COSMIC DE, created by System76

%prep
%autosetup

%build
#nothing to do here

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%fdupes %{buildroot}

%files
%license LICENSE COPYING
%doc README.md
%{_datadir}/icons/Cosmic

%changelog
