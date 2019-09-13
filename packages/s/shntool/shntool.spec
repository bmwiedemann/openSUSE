#
# spec file for package shntool
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


Name:           shntool
Version:        3.0.10        
Release:        0
Summary:        Multi-purpose WAVE data processing and reporting utility
License:        GPL-2.0
Group:          Multimedia/Sound/Editors and Convertors
Url:            http://www.etree.org/shnutils/shntool/
Source:         http://www.etree.org/shnutils/shntool/dist/src/shntool-%{version}.tar.gz
Patch0:         fix-fails-to-determine-correct-size.patch
Recommends:     flac
Recommends:     wavpack
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
shntool is a multi-purpose WAVE data processing and reporting
utility. File formats are abstracted from its core, so it can process
any file that contains WAVE data, compressed or not - provided there
exists a format module to handle that particular file type.

shntool has native support for .wav files. Working with other
lossless audio formats requires appropriate helper programs.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README doc/BUGS doc/CREDITS
%{_bindir}/shn*
%{_mandir}/man1/shntool.1%{ext_man}

%changelog

