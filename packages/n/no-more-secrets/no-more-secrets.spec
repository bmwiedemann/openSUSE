#
# spec file for package no-more-secrets
#
# Copyright (c) 2021 SUSE LLC
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


Name:           no-more-secrets
Version:        1.0.1
Release:        0
Summary:        A recreation of the "decrypting text" effect from the 1992 movie Sneakers
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://github.com/bartobri/%{name}
Source0:        https://github.com/bartobri/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A tool to recreate the famous "decrypting text" effect as seen in the 1992 movie Sneakers.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" nms sneakers-ncurses

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} install

%files
%defattr(-,root,root)
%doc README.md
# Fix for openSUSE == 42.1 (42.2 works)
%if 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/nms
%{_bindir}/sneakers
%{_mandir}/man6/nms.6%{ext_man}
%{_mandir}/man6/sneakers.6%{ext_man}

%changelog
