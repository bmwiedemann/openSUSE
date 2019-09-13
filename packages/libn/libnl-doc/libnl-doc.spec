#
# spec file for package libnl-doc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libnl-doc
Version:        3.2.27
Release:        0
Summary:        Documentation for libnl, a library for working with Netlink sockets
License:        GPL-3.0
Group:          Documentation/HTML
Url:            http://www.carisma.slowglass.com/~tgr/libnl/

#Git-Clone:	git://git.infradead.org/users/tgr/libnl
#Git-Clone:	git://github.com/thom311/libnl/
#Mailing-List:	http://lists.infradead.org/mailman/listinfo/libnl
Source:         https://github.com/thom311/libnl/releases/download/libnl3_2_27/%name-%version.tar.gz
Source2:        https://github.com/thom311/libnl/releases/download/libnl3_2_27/%name-%version.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
The libnl suite is a collection of libraries providing APIs to
Netlink protocol based Linux kernel interfaces.

%prep
%setup -qn libnl-doc-%version

%build

%install
b="%buildroot"
rm -Rf build-aux configure.ac
find . -name .gitignore -delete
mkdir -p "$b/%_docdir"
cp -a . "$b/%_docdir/%name"
%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%files
%defattr(-,root,root)
%_docdir/%name

%changelog
