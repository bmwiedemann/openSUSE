#
# spec file for package catcodec
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


Name:           catcodec
Version:        1.0.5
Release:        1%{?dist}
Summary:        En-/decode OpenTTD sound replacement files
License:        GPL-2.0
Group:          Development/Tools/Building

Url:            http://www.openttd.org/download-catcodec
Source0:        http://binaries.openttd.org/extra/catcodec/%{version}/catcodec-%{version}-source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++

%description
catcodec decodes and encodes sample catalogues for OpenTTD. These sample
catalogues are not much more than some meta-data (description and file name)
and raw PCM data.

catcodec is licensed under the GNU General Public License version 2.0. For
more information, see the file 'COPYING'.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} PACKAGE_NAME=catcodec

%files
%defattr(-,root,root)
%{_mandir}/man1/catcodec.1*
%{_bindir}/catcodec
%doc %{_datadir}/doc/catcodec

%changelog
