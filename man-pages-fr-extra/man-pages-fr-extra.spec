#
# spec file for package man-pages-fr-extra
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           man-pages-fr-extra
Version:        20151231
Release:        0
License:        GPL-2.0 and GPL-2.0+ and BSD-3-Clause and GFDL-1.1 and GFDL-1.2
Summary:        LDP man Pages (French)
Url:            https://packages.debian.org/fr/sid/manpages-fr-extra
Group:          Documentation/Man
Source:         http://ftp.de.debian.org/debian/pool/main/m/manpages-fr-extra/manpages-fr-extra_%{version}.tar.xz
BuildRequires:  po4a
BuildRequires:  fdupes
Recommends:     man-pages-fr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains translations which are neither shipped by man-pages-fr nor
along with original manual pages.

As these translations come from Debian maintainers, they may contain Debian-specific
information. Most of them are applicable to SUSE though.

%prep
%setup -q -n manpages-fr-extra

%build
make

%install
make install INSTDIR=%{buildroot}%{_mandir}/fr
# Do not include nscd.conf.5 and nscd.conf.8, more recent versions are included in man-pages-fr
rm %{buildroot}%{_mandir}/fr/man5/nscd.conf.5
rm %{buildroot}%{_mandir}/fr/man8/nscd.8
%fdupes -s %{buildroot}/%{_mandir}
%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%defattr(-,root,root)
%doc debian/copyright debian/changelog
