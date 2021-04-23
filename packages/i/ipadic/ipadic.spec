#
# spec file for package ipadic
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ipadic
BuildRequires:  chasen-devel
BuildRequires:  perl-Text-ChaSen
#!BuildIgnore:  ipadic
PreReq:         %install_info_prereq
Version:        2.6.3
Release:        0
Url:            http://chasen.aist-nara.ac.jp/
# Original Source is gzipped.
Source0:        http://chasen.aist-nara.ac.jp/stable/ipadic/ipadic-2.6.3.tar.bz2
Patch0:         ipadic.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Standard Japanese Dictionary for ChaSen
License:        SUSE-Permissive
Group:          System/I18n/Japanese

%description
Standard Japanese dictionary for ChaSen.


%prep
%setup
%patch0 -p 1

%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
            --with-dicdir=%{_prefix}/share/chasen/dic/ \
            --with-chasenrc-path=/etc/chasenrc \
            --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
make

%install
mkdir -p $RPM_BUILD_ROOT/etc
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS* README*
%doc doc/*.pdf
%dir %{_prefix}/share/chasen/
%{_prefix}/share/chasen/*
%config /etc/chasenrc

%changelog
