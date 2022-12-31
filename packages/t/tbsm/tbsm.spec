#
# spec file for package tbsm
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tbsm
Version:        0.7
Release:        0
Summary:        A pure bash session or application launcher
License:        GPL-2.0-only
BuildArch:      noarch
Group:          System/X11/Utilities
URL:            https://loh-tar.github.io/tbsm
Source:         https://github.com/loh-tar/tbsm/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  pcre-devel

%description
tbsm is an application or session launcher, written in pure bash with no ncurses or dialog dependencies. It is inspired by cdm, tdm, in some way by krunner and related.

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{makeinstall}
mkdir -p %{buildroot}%{_datadir}/licenses/tbsm/
mv %{buildroot}%{_datadir}/doc/tbsm/99_License.txt %{buildroot}%{_datadir}/licenses/tbsm/99_License.txt

%files
%defattr(-, root, root)
%{_bindir}/*
%config %{_sysconfdir}/xdg/tbsm/
%doc %{_datadir}/doc/tbsm/
%license %{_datadir}/licenses/tbsm/

%changelog
