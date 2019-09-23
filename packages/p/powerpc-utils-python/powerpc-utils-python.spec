#
# spec file for package powerpc-utils-python
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


Summary:        Python utilities for PowerPC platforms
License:        IPL-1.0
Group:          System/Management 
%define version_unconverted 1.2.1+git20150311.f7bdc5c

Name:           powerpc-utils-python	
Version:        1.2.1+git20150311.f7bdc5c
Release:        0
Source0:        %{name}-%{version}.tar.gz
Patch0:         no-buildroot-reference.patch
Url:            https://github.com/nfont/powerpc-utils-python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Requires:       python-gtk => 2.0
ExclusiveArch:  ppc ppc64 ppc64le

%description
Python based utilities for maintaining and servicing PowerPC systems.

%prep
%setup -q
%patch0 -p1

%build
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} FILES=""

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/amsvis
%dir %{python_sitelib}/powerpcAMS
%{python_sitelib}/powerpcAMS/*.py
%{python_sitelib}/powerpcAMS/*.py[co]
%{python_sitelib}/powerpcAMS-*-py*.egg-info
%{_mandir}/man1/amsvis.1*
%doc README COPYRIGHT

%changelog
