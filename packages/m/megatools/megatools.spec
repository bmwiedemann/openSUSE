#
# spec file for package megatools
#
# Copyright (c) 2023 SUSE LLC
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

%global snapshot 20230212

Name:           megatools
Version:        1.11.1
Release:        0
Summary:        CLI client for mega.co.nz
License:        GPL-2.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            http://megatools.megous.com
Source0:        %{name}-%{version}.%{snapshot}.tar.gz
Source1:        %{name}-%{version}.%{snapshot}.tar.gz.asc
# Keyring obtained from https://xff.cz/key.txt
Source2:        %{name}.keyring
BuildRequires:  asciidoc
BuildRequires:  docbook2X
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  libcurl-devel >= 7.85.0
BuildRequires:  libopenssl-devel
BuildRequires:  meson
Requires:       curl >= 7.85.0
Requires:       fuse
Requires:       glib-networking >= 2.32.0
Requires:       openssl

%description	-n %{name}
Megatools allow you to copy individual files as well as entire directory trees
to and from the cloud. You can also perform streaming downloads for example to
preview videos and audio files, without needing to download the entire file.
 
You can register an account using a "megareg" tool, with the benefit of having
true control of your encryption keys.
 
Megatools are robust and optimized for fast operation - as fast as Mega servers
allow. Memory requirements and CPU utilization are kept at minimum.

%prep
%autosetup -n %{name}-%{version}.%{snapshot}
 
%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
%ldconfig_scriptlets

%files
%license LICENSE
%doc NEWS README
%{_bindir}/mega*
%{_mandir}/man1/mega*.1.*
%{_mandir}/man5/mega*.5.*
%exclude %{_datadir}/doc/%{name}/*

%changelog
