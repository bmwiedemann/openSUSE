#
# spec file for package ipadic
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


Name:           ipadic
Version:        2.7.0
Release:        0
Summary:        Standard Japanese Dictionary for ChaSen
License:        SUSE-Permissive
Group:          System/I18n/Japanese
URL:            https://osdn.net/projects/ipadic/
Source0:        https://osdn.net/projects/ipadic/downloads/24435/ipadic-2.7.0.tar.gz
Patch0:         ipadic.patch
BuildRequires:  automake
BuildRequires:  chasen-devel
BuildRequires:  perl-Text-ChaSen
#!BuildIgnore:  ipadic
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
BuildArch:      noarch

%description
Standard Japanese dictionary for ChaSen.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
  --with-dicdir=%{_datadir}/chasen/dic/ \
  --with-chasenrc-path=%{_sysconfdir}/chasenrc
# single thread, broken with parallel build
make

%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS* README*
%doc doc/*.pdf
%dir %{_datadir}/chasen/
%{_datadir}/chasen/*
%config %{_sysconfdir}/chasenrc

%changelog
