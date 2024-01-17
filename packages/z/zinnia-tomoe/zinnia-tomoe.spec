#
# spec file for package zinnia-tomoe
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           zinnia-tomoe
Version:        0.6.0
Release:        0
%define date 20080911
Summary:        Zinnia model files trained with data provided by Tomoe
License:        LGPL-2.1
Group:          System/I18n/Japanese
Url:            http://zinnia.sourceforge.net/
Source0:        %{name}-%{version}-%{date}.tar.bz2
# PATCH-FIX-OPENSUSE zinnia-0.6.0-install-dir.patch
Patch0:         zinnia-tomoe-0.6.0-install-dir.patch
BuildArch:      noarch
BuildRequires:  zinnia
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
zinnia provides hand recognization model to Zinnia. This model
supports Japanese and simplified Chinese.

%prep
%setup -q -n zinnia-tomoe-%{version}-%{date}
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog
%dir %{_datadir}/zinnia
%dir %{_datadir}/zinnia/model
%dir %{_datadir}/zinnia/model/tomoe
%{_datadir}/zinnia/model/tomoe/handwriting-ja.model
%{_datadir}/zinnia/model/tomoe/handwriting-zh_CN.model

%changelog
