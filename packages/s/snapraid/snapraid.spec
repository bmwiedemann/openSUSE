#
# spec file for package snapraid
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           snapraid
Version:        13.0
Release:        0
Summary:        Disk array backup for many large rarely-changed files
License:        GPL-3.0-or-later
URL:            https://github.com/amadvance/snapraid
Source:         https://github.com/amadvance/snapraid/releases/download/v%{version}/snapraid-%{version}.tar.gz
BuildRequires:  gcc

%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build check

%install
%make_install
sed -i '/^#/! s/^/#/' snapraid.conf.example
install -Dm 0644 snapraid.conf.example %{buildroot}%{_sysconfdir}/snapraid.conf

%files
%license COPYING
%doc HISTORY README AUTHORS %{name}.txt
%config %{_sysconfdir}/snapraid.conf
%{_bindir}/snapraid
%{_mandir}/man1/snapraid.1%{?ext_man}

%changelog
