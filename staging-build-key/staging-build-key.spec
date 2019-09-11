#
# spec file for package staging-build-key
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


%define keyname staging-build-key

Name:           %keyname
BuildRequires:  gpg
Provides:       build-key
AutoReqProv:    off
Summary:        The public gpg key for rpm package signature verification
License:        MIT
Group:          System/Packages
Version:        12.0
Release:        0
Source0:        %keyname.asc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define keydir  %{_prefix}/lib/rpm/gnupg/keys

%description
GPG key used in staging projects


%prep
%setup -qcT

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 %{SOURCE0} $RPM_BUILD_ROOT%keydir/%keyname.asc

%files
%defattr(644,root,root)
%attr(755,root,root) %dir /usr/lib/rpm/gnupg
/usr/lib/rpm/gnupg/keys

%changelog
