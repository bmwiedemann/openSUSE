#
# spec file for package installation-images-extras
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           installation-images-extras
Version:        20130703
Release:        0
Summary:        Install all debuginfos for install
License:        MIT
Group:          System/Filesystems
BuildRequires:  installation-images
BuildRequires:  installation-images-debuginfodeps
BuildRequires:  squashfs
AutoReqProv:    off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep

%build

%install
mkdir -p usr/lib
cp -a /usr/lib/debug usr/lib
find usr/lib/debug -type l | while read link; do
  t=$(readlink -m /$link)
  echo $link $t
  rm $link
  ln -s $t $link
done
basefile=$(ls -1 /CD1/boot/*/root)
mkdir -p %{buildroot}/$(dirname $basefile)
mksquashfs . %{buildroot}/$basefile-debuginfos -comp xz 

%files
%defattr(-,root,root)
/CD1

%changelog
