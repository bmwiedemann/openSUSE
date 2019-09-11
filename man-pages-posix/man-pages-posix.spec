#
# spec file for package man-pages-posix
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           man-pages-posix
Version:        2013a
Release:        0
Summary:        POSIX Manual Pages
License:        SUSE-IEEE
Group:          Documentation/Man
Url:            https://www.kernel.org/doc/man-pages/
Source:         https://www.kernel.org/pub/linux/docs/man-pages/%name/%name-2013-a.tar.xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  xz
Supplements:    man-pages

%description
A large collection of man pages (reference material) from

	IEEE Std 1003.1, 2013 Edition, Standard for Information 
	Technology--Portable Operating System Interface (POSIX), 
	The Open Group Base Specifications Issue 7, 
	Copyright (C) 2013 by the Institute of Electrical and 
	Electronics Engineers, Inc and The Open Group.

The man pages are organized into the following sections:
* 0p: POSIX headers
* 1p: POSIX utilities
* 3p: POSIX functions

%prep
%setup -qn %name-2013-a
#find -name "*.orig" -print -delete

%build

%install
for i in man?p ; do
  mkdir -p "%buildroot/%_mandir/$i"
  cp -p "$i"/* "%buildroot/%_mandir/$i/"
done
cd "%buildroot/%_mandir"
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
%fdupes -s %buildroot/%_prefix

%files
%defattr(-,root,root)
%dir %_mandir/man?p
%doc %_mandir/man*/*.gz
%doc README
%doc POSIX-COPYRIGHT
%doc man-pages-*.Announce
%doc man-pages-*.lsm

%changelog
