#
# spec file for package man-pages-zh_CN
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


Name:           man-pages-zh_CN
Version:        1.6.3.6
Release:        0
Summary:        Simplified Chinese Linux man pages
License:        GFDL-1.3-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/man-pages-zh/manpages-zh
Source:         %{URL}/archive/v%{version}/manpages-zh-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  opencc
BuildRequires:  python3
Provides:       locale(man:zh)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Modern Linux man pages localization project for Chinese language.

It's based on manpages-zh project, a successor for CMPP linux man
pages translation project (discontinued), and Linux CN linux man
pages translation project, with some new addons from openSUSE
maintainers.

%prep
%setup -q -n manpages-zh-%{version}

%build
autoreconf -fiv
%configure --disable-zhtw

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_datadir}/doc/manpages-zh

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog AUTHORS
%{_mandir}/zh_CN

%changelog
