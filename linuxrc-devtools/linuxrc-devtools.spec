#
# spec file for package linuxrc-devtools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           linuxrc-devtools
Version:        0.16
Release:        0
Source:         %{name}-%{version}.tar.xz

BuildRequires:  make

Url:            http://github.com/openSUSE/linuxrc-devtools
Summary:        Tools to submit from Git to OBS via Jenkins
License:        MIT
Group:          Development/Tools

BuildArch:      noarch

%description
This is a collection of scripts used to connect github via jenkins to the
open build service.

%prep
%setup -q

%build

%install
make install DESTDIR="${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root)
%{_bindir}/build_it
%{_bindir}/git2log
%{_bindir}/git2tags
%{_bindir}/make_package
%{_bindir}/submit_it
%{_bindir}/tobs

%changelog
