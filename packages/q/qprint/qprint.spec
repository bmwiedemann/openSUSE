#
# spec file for package qprint
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           qprint
Version:        1.1
Release:        0
Summary:        Command line utility which encodes and decodes files in this format
License:        SUSE-Public-Domain
Group:          Productivity/Security
Url:            http://www.fourmilab.ch/webtools/qprint/
Source:         http://www.fourmilab.ch/webtools/qprint/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
qprint is a command line utility which encodes and decodes files in this format. It can be used within a pipeline as an encoding or decoding filter, and is most commonly used in this manner as part of an automated mail processing system. With appropriate options, qprint can encode pure binary files, but it's a poor choice since it may inflate the size of the file by as much as a factor of three. The base64 MIME encoding is a better choice for such data.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root)
%{_bindir}/qprint
%{_mandir}/man1/qprint.1.*

%changelog
