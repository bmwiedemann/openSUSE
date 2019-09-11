#
# spec file for package kubic-locale-archive
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define glibc_version %(rpm -q --queryformat '%%{VERSION}' glibc)
Name:           kubic-locale-archive
Version:        %{glibc_version}
Release:        0
Summary:        Minimal locale archive for very small systems
License:        GPL-2.0+ AND MIT AND LGPL-2.1+
Group:          System/Libraries
BuildRequires:  glibc-i18ndata
Requires:       glibc = %{glibc_version}
BuildArch:      noarch

%description
This package contains a glibc locale archive with the C.UTF-8 and
en_US.UTF-8 locale for very minimal systems only supporting
english as locale.

%prep
if [ -f %{_defaultlicensedir}/glibc/LICENSES ]; then
  cp %{_defaultlicensedir}/glibc/LICENSES .
else
  cp %{_docdir}/glibc/LICENSES .
fi

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/locale
localedef -i en_US -f UTF-8 en_US.UTF-8 --archive --prefix=%{buildroot}
localedef -i C -f UTF-8 C.UTF-8 --archive --prefix=%{buildroot}

%files
%license LICENSES
%{_prefix}/lib/locale/locale-archive

%changelog
