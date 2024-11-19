#
# spec file for package pantheon-sound-theme
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


Name:           pantheon-sound-theme
Version:        1.1.0
Release:        0
Summary:        The elementary.io sound theme
License:        Unlicense
URL:            https://github.com/elementary/sound-theme
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  vala
BuildArch:      noarch
Provides:       elementary-sound-theme = %{version}
Obsoletes:      elementary-sound-theme < %{version}

%description
A set of system sounds for the Pantheon Desktop.

%prep
%autosetup -n sound-theme-%{version}

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md
%{_datadir}/sounds/elementary

%changelog
