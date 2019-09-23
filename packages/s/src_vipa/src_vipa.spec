#
# spec file for package src_vipa
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           src_vipa
Url:            http://www.ibm.com/developerworks/linux/linux390/useful_add-ons_vipa.html
Version:        2.1.0
Release:        0
Summary:        Virtual Source IP address support for HA solutions
License:        CPL-1.0
Group:          Productivity/Clustering/HA
Source:         http://public.dhe.ibm.com/software/dw/linux390/ht_src/%name-%version.tar.gz
Source1:        http://www.ibm.com/developerworks/linux/linux390/MD5/src/%name-%version.md5
Patch1:         src_vipa-ldlibrarypath.patch
Patch2:         src_vipa-ignore_ldconfig.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides very flexible means of source IP address
selection to arbitrary applications. This is particularly useful for
high availability setups, where the dummy device holds a "VIPA"
(virtual IP address). Please read the
/usr/share/doc/packages/src_vipa/README and the manpage of src_vipa for
further information.



%prep
pushd `dirname %{S:0}`
md5sum -c %{S:1}
popd
%setup -q
%patch1 -p1
%patch2

%build
make SRC_VIPA_PATH=%_libdir
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
make INSTROOT=%buildroot SRC_VIPA_PATH=%buildroot%_libdir install
#mkdir -p $RPM_BUILD_ROOT/{%{_sbindir},%{_mandir}/man8/}
#install vconfig $RPM_BUILD_ROOT/%{_sbindir}
#cp -p vconfig.8 $RPM_BUILD_ROOT%{_mandir}/man8/
#cp %SOURCE2 .

%files
%defattr(444,root,root,755)
%doc README LICENSE
%doc %{_mandir}/man8/*.8.gz
%attr(555,root,root) %_sbindir/*
%attr(555,root,root) %_libdir/src_vipa*

%changelog
