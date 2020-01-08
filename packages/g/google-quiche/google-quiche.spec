#
# spec file for package google-quiche
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define src_install_dir /usr/src/%{name}

Name:           google-quiche
Version:        20190815
Release:        0
Summary:        Google's implementation of QUIC and related protocols
License:        BSD-3-Clause AND LGPL-2.1-or-later      
Url:            https://quiche.googlesource.com/quiche 
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes

%description
QUICHE (QUIC, Http/2, Etc) is Google‘s implementation of QUIC and related 
protocols. It powers Chromium as well as Google’s QUIC servers and some
other projects.

%package source
Summary:        Source code of %{name}
Group:          Development/Sources
BuildArch:      noarch

%description source
QUICHE (QUIC, Http/2, Etc) is Google‘s implementation of QUIC and related 
protocols. It powers Chromium as well as Google’s QUIC servers and some
other projects.

This package contains source code of %{name}.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

