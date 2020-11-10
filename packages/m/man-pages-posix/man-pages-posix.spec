#
# spec file for package man-pages-posix
#
# Copyright (c) 2020 SUSE LLC
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


%define year 2017
Name:           man-pages-posix
Version:        2017a
Release:        0
Summary:        POSIX Manual Pages
License:        SUSE-IEEE
Group:          Documentation/Man
URL:            https://www.kernel.org/doc/man-pages/
Source:         https://www.kernel.org/pub/linux/docs/man-pages/%{name}/%{name}-%{year}-a.tar.xz
BuildRequires:  fdupes
BuildRequires:  xz
Supplements:    man-pages
BuildArch:      noarch

%description
A large collection of man pages (reference material) from

This release contains a copy of the POSIX 1003.1-2017 man pages.
The directories man0p, man1p, man3p contain descriptions of the
headers, the utilities, and the functions documented in that standard.
For the copyright notice, see the file POSIX-COPYRIGHT.

The man pages are organized into the following sections:
* 0p: POSIX headers
* 1p: POSIX utilities
* 3p: POSIX functions

%prep
%setup -q -n %{name}-%{year}

%build

%install
for i in man?p ; do
  mkdir -p "%{buildroot}/%{_mandir}/$i"
  cp -p "$i"/* "%{buildroot}/%{_mandir}/$i/"
done
cd "%{buildroot}/%{_mandir}"
RETVAL=0
ARE_MISSING=""
for i in */* ; do
    FOUND=0
    grep "^.so man" "$i" && FOUND=1
    if [ "$FOUND" = 1 ] ; then
      if [ ! -f `grep "^.so man" "$i" | awk '{print $2}'` ]; then
	ARE_MISSING="$i $ARE_MISSING"
        RETVAL=1
      fi
    fi
done
echo ""
echo "The following manual pages are now missing (for .so reference):"
echo "$ARE_MISSING"
echo ""
if [ "$RETVAL" -ne 0 ] ; then
  exit "$RETVAL"
fi
%fdupes -s %{buildroot}/%{_prefix}

%files
%dir %{_mandir}/man?p
%{_mandir}/man*/*.gz
%doc README
%doc POSIX-COPYRIGHT
%doc man-pages-*.Announce

%changelog
