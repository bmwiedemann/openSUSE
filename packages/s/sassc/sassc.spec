#
# spec file for package sassc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sassc
Version:        3.5.0
Release:        0
Summary:        Libsass command line driver
License:        MIT
Group:          Development/Tools/Other
Url:            https://github.com/sass/sassc/
Source:         https://github.com/sass/sassc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel
BuildRequires:  libtool
BuildRequires:  make

%description
SassC is a C/C++ port of the Sass engine. The point is to be
simple, fast, and easy to integrate.

Sass is a pre-processing language for CSS. It allows you to write
cleaner stylesheets and makes collaboration on your CSS a breeze.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc LICENSE Readme.md
%{_bindir}/%{name}

%changelog
