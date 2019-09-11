#
# spec file for package fIcy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           fIcy
Version:        1.0.21
Release:        0
Summary:        Icecast/Shoutcast Stream Grabber
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Other
URL:            https://www.thregr.org/~wavexx/software/fIcy/
Source:         https://www.thregr.org/~wavexx/software/fIcy/releases/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fIcy-use_getaddrinfo.patch
Patch0:         fIcy-use_getaddrinfo.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
fIcy is a command line icecast/shoutcast stream grabber. It will work
with any ICY-compatible stream and allows to either save the stream to
user-customizable files or pipe the output to a media player, or both.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} \
    CXX="g++" \
    CXXFLAGS="%{optflags}"

%install
install -d "%{buildroot}%{_bindir}"
install -m0755 fIcy fPls fResync "%{buildroot}%{_bindir}/"

%files
%doc COPYING.txt FAQ.rst NEWS.rst README.rst TODO.rst
%{_bindir}/fIcy
%{_bindir}/fPls
%{_bindir}/fResync

%changelog
