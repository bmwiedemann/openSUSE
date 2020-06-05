#
# spec file for package wxEDID
#
# Copyright (c) 2020 SUSE LLC
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


Name:           wxEDID
Version:        0.0.20
Release:        0
Summary:        Extended Display Identification Data editor
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/wxedid/
Source0:        https://sourceforge.net/projects/wxedid/files/wxedid-%{version}.tar.gz
# PATCH-FIX-OPENSUSE our wx packages do not enable implicit string type conversion, breaking the build
Patch0:         wxedid-no-implicit-string-conversion.patch
BuildRequires:  c++_compiler
BuildRequires:  wxWidgets-devel

%description
wxEDID is a wxWidgets - based EDID (Extended Display Identification Data) editor.
This is an early stage of development, allowing to modify the base EDID v1.3+
structure and CEA-861 (as first extension block).
Besides normal editor functionality, the app has been equipped with a DTD
constructor, which aims to ease timings selection/editing. It's also possible to
export and import EDID data to/from text files (hex ASCII format) and also to
save the structures as a human-readable text.

%prep
%setup -q -n wxedid-%{version}
%autopatch -p1
sed -i 's:.*__DATE__.*::g' src/wxEDID_Main.cpp
sed -i 's:.*__TIME__.*::g' src/wxEDID_Main.cpp

%build
# missing whitespace
CXXFLAGS="%{optflags} " CFLAGS="%{optflags} " %configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/wxedid

%changelog
