#
# spec file for package qdl
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


Name:           qdl
Version:        1.0+git49.20210507
Release:        0
Summary:        A tool for flash images to Qualcomm based systems
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/andersson/qdl
#Source          https://github.com/andersson/qdl/archive/master.tar.gz
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libudev-devel
BuildRequires:  libxml2-devel

%description
This tool communicates with USB devices of id 05c6:9008 to upload a flash
loader and use this to flash images. Mostly Qualcomm based systems.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} %(xml2-config --cflags) -fpie -g" \
            LDFLAGS="%{optflags} %(xml2-config --libs) -ludev -pie"

%install
%make_install prefix="%{_prefix}"

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
