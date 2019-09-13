#
# spec file for package yast2-slide-show
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


%define version_unconverted 84.87.20190314.3f822a8
# xml2po uses temporary files that do not like being called twice
# xml2po probably is not thread-safe.
%define jobs 1
Name:           yast2-slide-show
Version:        84.87.20190314.3f822a8
Release:        0
Summary:        Slide show displayed during package installation with YaST
License:        GPL-2.0-only
Group:          Metapackages
Url:            https://github.com/openSUSE/yast-slide-show/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  xml2po
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The slide show displayed during package installation with YaST.

%prep
%setup -q

%build
# put the distro version in the text so the same package can be
# reused for TW and Leap
if [ "%{vendor}" = 'openSUSE' ]; then
	version="%{distribution}"
	version="${version#openSUSE }"
	sed -i -e "/ENTITY suse-version/s/\".*\"/\"$version\"/" slideshow.xml
fi
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
# don't do that for now. we also need to include CHECKSUMS etc
# create missing directory.yast entries, looks like noone else
# does that for us (boo#1048145)
#for d in %buildroot/CD1/suse/setup/slide/{txt/*,pic}; do
#	find "$d" -mindepth 1 -maxdepth 1 -not -name directory.yast -printf "%%P\n" | sort > "$d/directory.yast"
#done
%fdupes %{buildroot}

%files
%defattr(-,root,root)
/CD1

%changelog
