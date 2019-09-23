#
# spec file for package nf3d
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nf3d
Version:        0.8
Release:        0
Summary:        GANTT-style visualization for Netfilter connections and logged packets
License:        GPL-3.0
Group:          Productivity/Networking/Security
Url:            https://home.regit.org/software/nf3d/

#Git-Clone:	git://github.com/regit/nf3d
Source:         https://home.regit.org/wp-content/uploads/2013/02/nf3d-0.8.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-setuptools

%description
nf3d is a Netfilter visualization tool. It displays connections and
logged packets in a GANTT diagram fashion.

%prep
%setup -q

%build
export CFLAGS="%optflags"
python setup.py build

%install
python setup.py install --root="%buildroot" --prefix="%_prefix"

%files
%defattr(-,root,root)
%_bindir/nf3d
%python_sitelib/nf3d*

%changelog
