#
# spec file for package engdic
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           engdic
License:        SUSE-Public-Domain
Group:          Productivity/Office/Dictionary
BuildRequires:  dos2unix
Summary:        Little Korean <-> English Dictionary
Version:        0.2
Release:        123
Url:            http://www.freshports.org/korean/engdic/
Source0:        ftp://ftp.holywar.net/pub/engdic/engdic-0.2.tar.bz2
Source1:        edic
Patch0:         encoding-bugs.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Little Korean <-> English dictionary.

%prep
%setup
gunzip data/*.gz
%patch0 -p 1

%build
for i in data/*.dic
do
    echo $i
    dos2unix $i
    iconv -f euc-kr -t utf-8 < $i > $i.tmp
    mv $i.tmp $i
done

%install
mkdir -p %{buildroot}%{_prefix}/{bin,share/engdic}
install -m 644 data/*.dic %{buildroot}%{_prefix}/share/engdic
install -m 755 $RPM_SOURCE_DIR/edic  %{buildroot}%{_prefix}/bin
ln -s edic %{buildroot}%{_prefix}/bin/engdic

%files
%defattr(-,root,root)
%{_prefix}/share/engdic
%{_prefix}/bin/edic
%{_prefix}/bin/engdic

%changelog
