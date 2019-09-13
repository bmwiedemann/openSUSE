#
# spec file for package pkipplib (Version 0.07)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           pkipplib
BuildRequires:  python python-devel
Url:            http://www.pykota.com/software/pkipplib/
License:        GPL-2.0+
Group:          Development/Languages/Python
AutoReqProv:    on
Summary:        IPP and CUPS support for Python
Version:        0.07
Release:        183
# URL for Source0: http://www.pykota.com/software/pkipplib/download/tarballs/pkipplib-0.07.tar.gz/download
Source0:        %{name}-%{version}.tar.bz2
Requires:       python
# Skip testing devel dependencies required by libtool .la files by the following comment:
# skip-check-libtool-deps
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%prep
# Be quiet when unpacking:
%setup -q

%build
# There is nothing to build because the sources contain readymade Python scripts.

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record-rpm=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README COPYING
%doc notifiers/samplenotifier

%description
This software is a Python library which can prepare IPP requests with
the help of a somewhat high level API. These requests can then be sent
to an IPP printer or print server (e.g. CUPS).

This library can also parse IPP answers received, and create high level
Python objects from them.

Both of these actions can be done through an IPPRequest class and its
instance methods.

Finally, a CUPS class can be leveraged to easily deal with CUPS print
servers.

All of this library being written in the Python language, there is no
need to link the code with the CUPS' API, which makes it independant of
the CUPS version being installed.

Nevertheless some features require an appropriate CUPS version which
supports the functionality (e.g. IPP subscriptions require CUPS 1.2.x).



Authors:
--------
    Jerome Alet

%changelog
* Thu Jun 29 2006 jsmeix@suse.de
- Initial version 0.07
