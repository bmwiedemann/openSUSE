#
# spec file for package makewhat
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


Name:           makewhat
Version:        2009.6.17
Release:        0
URL:            https://build.opensuse.org/package/show/Base:System/makewhat
Summary:        Utilities to create a whatis database
License:        GPL-2.0-or-later
Group:          System/Base
BuildRequires:  update-alternatives
Requires:       man
Requires(post): update-alternatives
Requires(preun): update-alternatives
Source:         makewhat.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The man system in SUSE Linux (package man) does not need a whatis
database. Nevertheless, some manual browsers, such as tkman, still need
such a database.

%prep
%setup -n makewhat

%build
echo Build section is empty

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
install -m755 makewhatis %{buildroot}%{_sbindir}/makewhatis.mw
ln -sf %{_sbindir}/makewhatis.mw %{buildroot}%{_sysconfdir}/alternatives/makewhatis
ln -sf %{_sysconfdir}/alternatives/makewhatis %{buildroot}%{_sbindir}/makewhatis

%post
%{_sbindir}/update-alternatives --quiet --force \
        --install %{_sbindir}/makewhatis makewhatis %{_sbindir}/makewhatis.mw 900

%preun
if test $1 -eq 0
then
	%{_sbindir}/update-alternatives --quiet --remove makewhatis %{_sbindir}/makewhatis
fi

%files
%defattr(-,root,root)
%ghost %config %{_sysconfdir}/alternatives/makewhatis
%{_sbindir}/makewhatis.mw
%{_sbindir}/makewhatis

%changelog
