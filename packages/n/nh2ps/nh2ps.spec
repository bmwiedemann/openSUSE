#
# spec file for package nh2ps
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


Name:           nh2ps
Summary:        Hangul Text to Postscript Converter
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/PS
Version:        2.3.1
Release:        0
Source:         ftp://jazz.snu.ac.kr/pub/unix/util/nh2ps/nh2ps-2.3.1.tar.gz
Patch:          nh2ps-2.3.1-cflags.patch
Patch1:         nh2ps-2.3.1-perlpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Convert plain hangul text into postscript form. By Choi Jun Ho, the
Junker <junker@jazz.snu.ac.kr>.



Authors:
--------
    Choi Jun Ho <junker@jazz.snu.ac.kr>

%prep
%setup -q
%patch
%patch1 -p1

%build
export RPM_OPT_FLAGS
# parallel build fails
make -j1

%install
install -d %{buildroot}%{_prefix}/bin
make PREFIX=%{buildroot}%{_prefix} install

%files
%defattr(-,root,root)
%doc ksc5601-char-list README.a2ps
%doc README.filtering_with_gs README.nh2ps README.font
%{_prefix}/bin/nh2ps*

%changelog
