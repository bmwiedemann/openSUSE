#
# spec file for package steamtricks-data
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           steamtricks-data
Version:        20180128.f77bb8e
Release:        0
Summary:        Steamtricks companion data repository
License:        GPL-2.0
Group:          Amusements/Games/Other
Url:            https://github.com/steamtricks/steamtricks-data
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  steamtricks
Requires:       steamtricks
# https://github.com/steamtricks/steamtricks-data/commit/e263295
Requires:       bsdiff

%description
steamtricks companion data repository

While steamtricks is the client/daemon that triggers and applies fixes,
steamtricks-data is the repository that provides the instructions for making the
fixes.

%prep
%setup -q

%build

%install
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/steamtricks/data

%changelog
