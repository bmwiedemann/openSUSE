#
# spec file for package restool
#
# Copyright (c) 2021 SUSE LLC
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

Name:           restool
Version:        2.3.1
Release:        0
Summary:        Tool to create and manage DPAA2 
License:        GPL-2.0-or-later
URL:            https://source.codeaurora.org/external/qoriq/qoriq-components/restool/about/
Source0:        %{name}-%{version}.tar.xz
Group:          Hardware/Other
ExclusiveArch:  aarch64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pandoc
     
%description
restool is a user space application providing the ability to dynamically create and manage DPAA2 containers and objects from Linux.

%prep
%autosetup -p1

%build
%{make_build}

%install
%{make_install} prefix=%{_usr}

%files
%license COPYING
%{_bindir}/restool
%{_bindir}/ls-*
%{_datadir}/bash-completion/completions/restool
%{_mandir}/man1/restool*

%changelog
